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
    # The moving display is deliberately qualitative: tenths, symmetric bounds,
    # and a real mathematical minus rather than text/programming notation.
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
        revision.integral_expression(1.14) == r"$\int_{-1.1}^{1.1}$",
        "moving integral is not typeset with the current symmetric cutoff",
    )
    expect(
        r"\lim_{T\to\infty}" in revision.DEFINITION,
        "Pearcey definition is missing the T→∞ limit",
    )
    expect(
        r"\int_{-T}^{T}" in revision.DEFINITION,
        "Pearcey definition is missing symmetric -T,T integral limits",
    )
    expect("t^4" in revision.DEFINITION and "y t^2" in revision.DEFINITION,
           "Pearcey definition is missing exponent powers")

    # Render the actual MathText rather than merely accepting a syntactically
    # plausible string. This catches unsupported/missing-glyph regressions in
    # the presentation path that the old hand-selected italic font allowed.
    definition_image = revision.math_rgba(revision.DEFINITION, 27)
    integral_image = revision.math_rgba(revision.integral_expression(1.1), 28)
    expect(definition_image.width >= 550 and definition_image.height >= 70,
           f"typeset definition has implausible extent {definition_image.size}")
    expect(integral_image.width >= 80 and integral_image.height >= 70,
           f"typeset moving integral has implausible extent {integral_image.size}")

    expect(
        revision.cutoff_for_time(0.0)
        < revision.cutoff_for_time(5.0)
        < revision.cutoff_for_time(10.0),
        "displayed truncation cutoff does not grow through the build",
    )

    source = REVISION_RENDERER.read_text()
    for required in (
        "math_to_image",
        "27x² + 8y³ = 0",
        "CAUSTIC OVERLAY",
        "draw_dashed_polyline",
        "draw_cutoff_overlay",
        "make_lower_video",
        "fps={fps},tpad=stop_mode=clone",
    ):
        expect(required in source, f"revised compositor is missing presentation marker {required!r}")
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


def check_timeline(path: Path, scale: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    build_early = frame_at(path, 2.0)
    build_late = frame_at(path, 8.0)
    clean_early = frame_at(path, 12.5)
    clean_late = frame_at(path, 17.0)

    field = slice(round(300 * scale), round(840 * scale))
    indicator = slice(round(930 * scale), round(1130 * scale))
    build_field_change = mean_difference(build_early[field], build_late[field])
    indicator_change = changed_pixels(build_early[indicator], build_late[indicator])
    clean_field_drift = mean_difference(clean_early[field], clean_late[field])

    expect(build_field_change >= 1.0,
           f"{path.name}: Pearcey field barely changes while T grows ({build_field_change:.3f})")
    expect(indicator_change >= round(300 * scale * scale),
           f"{path.name}: interval/integral indicator does not visibly change ({indicator_change} pixels)")
    expect(clean_field_drift <= 0.75,
           f"{path.name}: final field is still changing during the hold ({clean_field_drift:.3f})")

    print(
        f"timeline {path.name}: build {build_field_change:.3f}; "
        f"interval pixels {indicator_change}; hold drift {clean_field_drift:.3f}"
    )
    return clean_late, field, indicator


def check_revision_sequence() -> None:
    check_video_shape(FULL_VIDEO, 720, 1280, 30.0)
    check_video_shape(SMALL_VIDEO, 360, 640, 15.0)
    if not FULL_VIDEO.is_file() or not SMALL_VIDEO.is_file():
        return

    # Check both outputs. The old preview accidentally stretched 30-fps source
    # frames onto a 15-fps clock, so its field and T readout disagreed even while
    # the full version looked temporally plausible.
    clean_late, field, _ = check_timeline(FULL_VIDEO, 1.0)
    check_timeline(SMALL_VIDEO, 0.5)

    label_only = frame_at(FULL_VIDEO, 18.5)
    with_curve = frame_at(FULL_VIDEO, 19.5)

    # At 18.5 s the explanatory label is present but the field itself is clean.
    label_field_change = mean_difference(clean_late[field], label_only[field])
    expect(label_field_change <= 0.75,
           f"curve appears before its label has established itself ({label_field_change:.3f})")
    label_region_change = changed_pixels(clean_late[1120:1260], label_only[1120:1260])
    expect(label_region_change >= 300,
           f"CAUSTIC OVERLAY label is not visibly present before the curve ({label_region_change} pixels)")

    # A second, later change occurs inside the field when the dashed curve appears.
    curve_change = changed_pixels(label_only[field], with_curve[field])
    expect(curve_change >= 300,
           f"dashed caustic curve is not visibly added after the label ({curve_change} pixels)")

    print(f"overlay: label pixels {label_region_change}; curve pixels {curve_change}")


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
