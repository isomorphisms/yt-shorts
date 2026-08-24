#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
BASE_RENDERER = HERE / "render_pearcey.py"
REVISION_RENDERER = HERE / "revise_preview.py"
FULL_VIDEO = HERE / "pearcey-T-build-wegert-v2.mp4"
SMALL_VIDEO = HERE / "pearcey-T-build-wegert-v2-small.mp4"

failures: list[str] = []


def expect(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reference_pearcey(x: float, y: float, cutoff: float) -> complex:
    h = 0.0001
    count = int(round((2.0 * cutoff) / h))
    t = np.linspace(-cutoff, cutoff, count + 1, dtype=np.float64)
    values = np.exp(1j * (t**4 + y * t**2 + x * t))
    weights = np.ones(count + 1, dtype=np.float64)
    weights[0] = weights[-1] = 0.5
    return complex(h * np.sum(weights * values))


def check_math(base) -> None:
    xs = np.linspace(base.X_MIN, base.X_MAX, 7, dtype=np.float32)
    ys = np.linspace(base.Y_MIN, base.Y_MAX, 7, dtype=np.float32)
    n_steps = int(round(base.T_MAX / base.DT))
    t = np.arange(n_steps + 1, dtype=np.float32) * np.float32(base.DT)
    t2 = t * t
    scalar = (2.0 * np.exp(1j * (t2 * t2))).astype(np.complex64)
    y_phase = np.exp(1j * ys[:, None] * t2[None, :]).astype(np.complex64)
    cos_xt = np.cos(t[:, None] * xs[None, :]).astype(np.float32)
    field = np.zeros((len(ys), len(xs)), dtype=np.complex64)
    base.add_block(field, y_phase, scalar, cos_xt, 0, n_steps, base.DT)

    max_error = 0.0
    for iy, ix in [(4, 3), (1, 1), (3, 4), (5, 5), (2, 2)]:
        reference = reference_pearcey(float(xs[ix]), float(ys[iy]), base.T_MAX)
        max_error = max(max_error, abs(complex(field[iy, ix]) - reference))
    expect(
        max_error <= 3.0e-4,
        f"Pearcey T={base.T_MAX:g} representative-point error {max_error:.3g} exceeds 3e-4",
    )
    print(f"math: max representative-point error {max_error:.3g}")


def check_typography(revision) -> None:
    # The presentation should expose only the precision that is useful to a
    # viewer, while keeping the mathematical sign and symmetry explicit.
    expect(revision.display_t(1.14) == 1.1, "moving T readout is not rounded to one decimal")
    expect(revision.display_t(1.16) == 1.2, "moving T readout does not advance by tenths")
    expect(
        revision.displayed_bounds(1.14) == ("−1.1", "1.1"),
        "symmetric bounds must use U+2212 and one decimal: −1.1 to 1.1",
    )
    expect(
        revision.displayed_bounds(1.16) == ("−1.2", "1.2"),
        "symmetric bounds must advance with T: −1.2 to 1.2",
    )
    expect(
        revision.cutoff_for_time(0.0) < revision.cutoff_for_time(5.0) < revision.cutoff_for_time(10.0),
        "displayed truncation cutoff does not grow through the build",
    )

    source = REVISION_RENDERER.read_text()
    for required in (
        "T → ∞",
        "−T",
        "∫",
        "t⁴",
        "yt²",
        "27x² + 8y³ = 0",
        "CAUSTIC OVERLAY",
        "draw_dashed_polyline",
        "draw_cutoff_overlay",
        "axis_y",
    ):
        expect(required in source, f"revised compositor is missing typography/overlay marker {required!r}")
    expect("integration interval" not in source.lower(),
           "interval indicator should be mathematical notation, not a prose control label")


def probe(path: Path) -> tuple[float, int, int, float]:
    proc = subprocess.run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height,r_frame_rate:format=duration",
            "-of", "json", str(path),
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


def frame_at(path: Path, seconds: float) -> np.ndarray:
    proc = subprocess.run(
        [
            "ffmpeg", "-v", "error", "-ss", f"{seconds:.3f}", "-i", str(path),
            "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-",
        ],
        check=True,
        capture_output=True,
    )
    if not proc.stdout:
        raise RuntimeError(f"no frame at {seconds:.2f}s in {path.name}")
    return np.asarray(Image.open(io.BytesIO(proc.stdout)).convert("RGB"), dtype=np.uint8)


def mean_difference(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.mean(np.abs(left.astype(np.int16) - right.astype(np.int16))))


def changed_pixels(left: np.ndarray, right: np.ndarray, threshold: int = 25) -> int:
    delta = np.max(np.abs(left.astype(np.int16) - right.astype(np.int16)), axis=2)
    return int(np.count_nonzero(delta > threshold))


def check_video_shape(path: Path, expected_width: int, expected_height: int, expected_fps: float) -> None:
    expect(path.is_file(), f"missing {path.name}")
    if not path.is_file():
        return
    duration, width, height, fps = probe(path)
    expect(abs(duration - 23.0) <= 0.25, f"{path.name} duration is {duration:.2f}s, expected about 23s")
    expect((width, height) == (expected_width, expected_height),
           f"{path.name} is {width}x{height}, expected {expected_width}x{expected_height}")
    expect(abs(fps - expected_fps) < 0.01,
           f"{path.name} is {fps:g} fps, expected {expected_fps:g}")


def check_revision_sequence() -> None:
    check_video_shape(FULL_VIDEO, 720, 1280, 30.0)
    check_video_shape(SMALL_VIDEO, 360, 640, 15.0)
    if not FULL_VIDEO.is_file():
        return

    build_early = frame_at(FULL_VIDEO, 2.0)
    build_late = frame_at(FULL_VIDEO, 8.0)
    clean_early = frame_at(FULL_VIDEO, 12.5)
    clean_late = frame_at(FULL_VIDEO, 17.0)
    label_only = frame_at(FULL_VIDEO, 18.5)
    with_curve = frame_at(FULL_VIDEO, 19.5)

    # The field and the interval indicator should both move while T grows.
    field = slice(300, 840)
    build_field_change = mean_difference(build_early[field, :, :], build_late[field, :, :])
    expect(build_field_change >= 1.0,
           f"Pearcey field barely changes while T grows ({build_field_change:.3f})")
    indicator = slice(930, 1140)
    indicator_change = changed_pixels(build_early[indicator], build_late[indicator])
    expect(indicator_change >= 300,
           f"moving interval/integral indicator does not visibly change ({indicator_change} pixels)")

    # The final natural field should sit still for several seconds even though
    # the final T=3.0 notation remains visible below it.
    clean_field_drift = mean_difference(clean_early[field, :, :], clean_late[field, :, :])
    expect(clean_field_drift <= 0.75,
           f"natural final field is still changing (mean drift {clean_field_drift:.3f})")

    # At 18.5 s the label has appeared but the field itself must still be clean.
    label_field_change = mean_difference(clean_late[field, :, :], label_only[field, :, :])
    expect(label_field_change <= 0.75,
           f"curve appears before its overlay label has had time to establish itself ({label_field_change:.3f})")
    label_region_change = changed_pixels(clean_late[1120:1260], label_only[1120:1260])
    expect(label_region_change >= 300,
           f"CAUSTIC OVERLAY label is not visibly present before the curve ({label_region_change} changed pixels)")

    # A second, later change must occur inside the field when the dashed curve is added.
    curve_change = changed_pixels(label_only[field, :, :], with_curve[field, :, :])
    expect(curve_change >= 300,
           f"dashed caustic curve is not visibly added after the label ({curve_change} changed field pixels)")

    print(
        f"sequence: build field {build_field_change:.3f}; interval pixels {indicator_change}; "
        f"clean field drift {clean_field_drift:.3f}; label pixels {label_region_change}; curve pixels {curve_change}"
    )


def main() -> None:
    base = load_module(BASE_RENDERER, "pearcey_base")
    revision = load_module(REVISION_RENDERER, "pearcey_revision")
    check_math(base)
    check_typography(revision)
    check_revision_sequence()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print("Pearcey revision validation passed")


if __name__ == "__main__":
    main()
