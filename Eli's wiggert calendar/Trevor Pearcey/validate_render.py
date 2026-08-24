#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import tempfile
import types
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
RENDERER_PATH = HERE / "render_pearcey.py"
REVISION_PATH = HERE / ".revision-2"
VIDEO_PATH = HERE / "pearcey-T-build-wegert.mp4"
POSTER_PATH = HERE / "pearcey-final-frame.png"

failures: list[str] = []


def expect(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def load_renderer():
    spec = importlib.util.spec_from_file_location("pearcey_renderer_under_test", RENDERER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load render_pearcey.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_revision() -> dict[str, str]:
    revision: dict[str, str] = {}
    for raw in REVISION_PATH.read_text().splitlines():
        raw = raw.strip()
        if raw and not raw.startswith("#") and "=" in raw:
            key, value = raw.split("=", 1)
            revision[key.strip()] = value.strip()
    return revision


def reference_pearcey(x: float, y: float, cutoff: float) -> complex:
    # Independent fine-grid quadrature of the definition, over [-T,T].
    h = 0.0001
    count = int(round((2.0 * cutoff) / h))
    t = np.linspace(-cutoff, cutoff, count + 1, dtype=np.float64)
    values = np.exp(1j * (t**4 + y * t**2 + x * t))
    weights = np.ones(count + 1, dtype=np.float64)
    weights[0] = weights[-1] = 0.5
    return complex(h * np.sum(weights * values))


def check_math(renderer) -> None:
    captured: list[np.ndarray] = []

    class FakeWegert:
        def __init__(self, _w: int, _h: int):
            pass

        def color(self, field: np.ndarray) -> np.ndarray:
            captured.append(field.copy())
            return np.zeros((renderer.FIELD_H, renderer.FIELD_W, 3), dtype=np.uint8)

        def close(self) -> None:
            pass

    class Sink:
        def write(self, _data: bytes) -> None:
            pass

        def close(self) -> None:
            pass

    class FakePopen:
        def __init__(self, *_args, **_kwargs):
            self.stdin = Sink()

        def wait(self) -> int:
            return 0

    names = [
        "WegertGL", "subprocess", "compose", "OUT", "POSTER",
        "FIELD_W", "FIELD_H", "VIDEO_W", "VIDEO_H",
        "FPS", "UNIQUE_FPS", "BUILD_SECONDS", "HOLD_SECONDS", "CUSP_SECONDS",
    ]
    saved = {name: getattr(renderer, name) for name in names}

    try:
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            renderer.WegertGL = FakeWegert
            renderer.subprocess = types.SimpleNamespace(Popen=FakePopen, PIPE=-1)
            renderer.compose = lambda *_args, **_kwargs: bytes(renderer.VIDEO_W * renderer.VIDEO_H * 3)
            renderer.OUT = tmp / "ignored.mp4"
            renderer.POSTER = tmp / "mini.png"
            renderer.FIELD_W = 7
            renderer.FIELD_H = 7
            renderer.VIDEO_W = 2
            renderer.VIDEO_H = 2
            renderer.FPS = 1
            renderer.UNIQUE_FPS = 1
            renderer.BUILD_SECONDS = 4
            renderer.HOLD_SECONDS = 0
            renderer.CUSP_SECONDS = 0
            renderer.main()
    finally:
        for name, value in saved.items():
            setattr(renderer, name, value)

    expect(bool(captured), "math check did not capture a computed Pearcey field")
    if not captured:
        return

    field = captured[-1]
    xs = np.linspace(renderer.X_MIN, renderer.X_MAX, 7, dtype=np.float32)
    ys = np.linspace(renderer.Y_MIN, renderer.Y_MAX, 7, dtype=np.float32)
    representative = [(4, 3), (1, 1), (3, 4), (5, 5), (2, 2)]
    max_error = 0.0
    for iy, ix in representative:
        x = float(xs[ix])
        y = float(ys[iy])
        reference = reference_pearcey(x, y, renderer.T_MAX)
        error = abs(complex(field[iy, ix]) - reference)
        max_error = max(max_error, error)
    expect(
        max_error <= 3.0e-4,
        f"Pearcey T={renderer.T_MAX:g} representative-point error {max_error:.3g} exceeds 3e-4",
    )
    print(f"math: max representative-point error {max_error:.3g}")


def probe_video() -> tuple[float, int, int, float]:
    proc = subprocess.run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height,r_frame_rate:format=duration",
            "-of", "json", str(VIDEO_PATH),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)
    stream = data["streams"][0]
    numerator, denominator = stream["r_frame_rate"].split("/", 1)
    fps = float(numerator) / float(denominator)
    return float(data["format"]["duration"]), int(stream["width"]), int(stream["height"]), fps


def frame_at(seconds: float) -> np.ndarray:
    proc = subprocess.run(
        [
            "ffmpeg", "-v", "error", "-ss", f"{seconds:.3f}", "-i", str(VIDEO_PATH),
            "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-",
        ],
        check=True,
        capture_output=True,
    )
    if not proc.stdout:
        raise RuntimeError(f"no frame available at {seconds:.2f}s")
    return np.asarray(Image.open(io.BytesIO(proc.stdout)).convert("RGB"), dtype=np.uint8)


def mean_abs_difference(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean(np.abs(a.astype(np.int16) - b.astype(np.int16))))


def check_render(renderer, revision: dict[str, str]) -> None:
    expect(VIDEO_PATH.is_file(), "render did not produce the MP4")
    expect(POSTER_PATH.is_file(), "render did not produce the final-frame PNG")
    if not VIDEO_PATH.is_file() or not POSTER_PATH.is_file():
        return

    duration, width, height, fps = probe_video()
    expected_hold = float(revision["natural_hold_seconds"])
    expected_overlay = float(revision["overlay_seconds"])
    expected_duration = float(renderer.BUILD_SECONDS) + expected_hold + expected_overlay

    expect((width, height) == (renderer.VIDEO_W, renderer.VIDEO_H),
           f"video is {width}x{height}, expected {renderer.VIDEO_W}x{renderer.VIDEO_H}")
    expect(abs(fps - renderer.FPS) < 0.01, f"video is {fps:g} fps, expected {renderer.FPS}")
    expect(abs(duration - expected_duration) <= 0.25,
           f"video is {duration:.2f}s; revision-2 sequence requires about {expected_duration:.2f}s")

    poster = np.asarray(Image.open(POSTER_PATH).convert("RGB"), dtype=np.uint8)
    expect(poster.shape[:2] == (renderer.VIDEO_H, renderer.VIDEO_W),
           f"poster is {poster.shape[1]}x{poster.shape[0]}, expected {renderer.VIDEO_W}x{renderer.VIDEO_H}")

    field_slice = slice(renderer.FIELD_TOP, renderer.FIELD_TOP + renderer.FIELD_OUT_H)
    poster_field = poster[field_slice, :, :]
    expect(float(np.std(poster_field)) > 12.0, "final field is nearly flat/blank")
    quantized = (poster_field // 32).reshape(-1, 3)
    expect(len(np.unique(quantized, axis=0)) >= 32, "final field has too little color structure")

    early_t = min(1.0, renderer.BUILD_SECONDS * 0.2)
    clean_a_t = renderer.BUILD_SECONDS + 0.5
    clean_b_t = renderer.BUILD_SECONDS + expected_hold - 1.0

    try:
        early = frame_at(early_t)
        clean_a = frame_at(clean_a_t)
        change = mean_abs_difference(early[field_slice, :, :], clean_a[field_slice, :, :])
        expect(change >= 2.0, f"field barely changes while T builds (mean pixel change {change:.2f})")
    except Exception as exc:
        failures.append(f"could not inspect build/hold frames: {exc}")
        clean_a = None

    clean_b = None
    if duration > clean_b_t + 0.1:
        try:
            clean_b = frame_at(clean_b_t)
            if clean_a is not None:
                drift = mean_abs_difference(clean_a, clean_b)
                expect(drift <= 2.0, f"supposed clean hold is still changing (mean pixel drift {drift:.2f})")
        except Exception as exc:
            failures.append(f"could not inspect end of clean hold: {exc}")
    else:
        failures.append(
            f"video ends before the required {expected_hold:g}s clean final hold can complete"
        )

    if clean_a is not None and revision.get("show_interval_bar", "true").lower() == "false":
        bottom_top = min(renderer.VIDEO_H, renderer.FIELD_TOP + renderer.FIELD_OUT_H + 40)
        bottom_bottom = min(renderer.VIDEO_H, bottom_top + 240)
        region = clean_a[bottom_top:bottom_bottom, :, :]
        luminance = region.mean(axis=2)
        bright_fraction = float(np.mean(luminance > 80.0)) if region.size else 0.0
        expect(
            bright_fraction < 0.01,
            f"clean hold still has a bright bottom control/annotation region ({100*bright_fraction:.2f}% bright pixels)",
        )

    if clean_b is not None:
        overlay_change = mean_abs_difference(clean_b, poster)
        expect(overlay_change >= 0.15,
               f"final overlay phase is not visibly distinct (mean pixel change {overlay_change:.3f})")

    if revision.get("cusp_overlay") == "dashed_labeled":
        source = RENDERER_PATH.read_text()
        expect("caustic overlay" in source, "revision-2 requires an explicit visible 'caustic overlay' cue")
        expect("draw.line(pts" not in source,
               "cusp overlay is still drawn as one continuous solid polyline instead of a dashed annotation")

    print(f"video: {duration:.2f}s, {width}x{height}, {fps:g} fps")


def main() -> None:
    renderer = load_renderer()
    revision = parse_revision()
    check_math(renderer)
    check_render(renderer, revision)
    if failures:
        for message in failures:
            print(f"FAIL: {message}")
        raise SystemExit(1)
    print("Pearcey numerical and render assertions passed")


if __name__ == "__main__":
    main()
