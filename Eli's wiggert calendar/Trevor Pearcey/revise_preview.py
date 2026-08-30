#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import subprocess
import tempfile
from functools import lru_cache
from io import BytesIO
from pathlib import Path

import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import math_to_image
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "pearcey-T-build-wegert.mp4"
FULL_OUT = HERE / "pearcey-T-build-wegert-v2.mp4"
SMALL_OUT = HERE / "pearcey-T-build-wegert-v2-small.mp4"

X_MIN, X_MAX = -6.0, 6.0
Y_MIN, Y_MAX = -6.0, 3.0
T_MAX = 3.0
DT = 0.003
BUILD_SECONDS = 6.0
UNIQUE_FPS = 15
ZOOM_SECONDS = 5.5
CAUSTIC_LABEL_SECONDS = 18.0
CAUSTIC_CURVE_SECONDS = 19.0
PRESENTATION_SECONDS = 23.0

DEFINITION = r"$P(x,y)=\lim_{T\to\infty}\int_{-T}^{T} e^{i(t^4+y t^2+x t)}\,dt$"

STIX = "/usr/share/fonts/opentype/stix-word/STIX-Regular.otf"
STIX_ITALIC = "/usr/share/fonts/opentype/stix-word/STIX-Italic.otf"
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path: str, size: int):
    return ImageFont.truetype(path, size)


def text_width(draw: ImageDraw.ImageDraw, text: str, face) -> int:
    box = draw.textbbox((0, 0), text, font=face)
    return box[2] - box[0]


def ease(s: float) -> float:
    s = min(max(s, 0.0), 1.0)
    return s * s * (3.0 - 2.0 * s)


def t_for_build_frame(index: int, count: int) -> float:
    s = index / max(count - 1, 1)
    e = ease(s)
    return 0.06 + (T_MAX - 0.06) * (e ** 0.82)


def cutoff_for_time(seconds: float) -> float:
    """Match the cutoff used by the base renderer's 15 unique frames/s."""
    if seconds >= BUILD_SECONDS:
        return T_MAX
    count = int(BUILD_SECONDS * UNIQUE_FPS)
    index = min(count - 1, max(0, int(seconds * UNIQUE_FPS)))
    target = t_for_build_frame(index, count)
    step = min(int(round(T_MAX / DT)), max(1, int(round(target / DT))))
    return step * DT


def display_t(value: float) -> float:
    """The moving explanatory readout intentionally uses only tenths."""
    return round(float(value) + 1.0e-9, 1)


def displayed_bounds(value: float) -> tuple[str, str]:
    shown = display_t(value)
    return f"−{shown:.1f}", f"{shown:.1f}"


def integral_expression(value: float) -> str:
    shown = display_t(value)
    # MathText renders '-' as a mathematical minus, not a text hyphen.
    return rf"$\int_{{-{shown:.1f}}}^{{{shown:.1f}}}$"


@lru_cache(maxsize=96)
def math_rgba(expression: str, font_size: int) -> Image.Image:
    """Render a small LaTeX-style MathText expression onto transparency."""
    buf = BytesIO()
    math_to_image(
        expression,
        buf,
        prop=FontProperties(size=font_size),
        dpi=120,
        format="png",
        color="black",
    )
    buf.seek(0)
    source = Image.open(buf).convert("L")
    alpha = Image.fromarray(255 - np.asarray(source, dtype=np.uint8), "L")
    bbox = alpha.getbbox()
    rgba = Image.new("RGBA", source.size, (245, 245, 245, 0))
    rgba.putalpha(alpha)
    return rgba.crop(bbox) if bbox else rgba


def paste_math_centered(
    image: Image.Image,
    expression: str,
    font_size: int,
    center_y: float,
) -> None:
    formula = math_rgba(expression, font_size)
    x = round((image.width - formula.width) / 2)
    y = round(center_y - formula.height / 2)
    image.alpha_composite(formula, (x, y))


def draw_dashed_polyline(draw, points, fill, width, dash=12, gap=9):
    drawing = True
    remain = float(dash)
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        dx, dy = x1 - x0, y1 - y0
        length = math.hypot(dx, dy)
        if not length:
            continue
        ux, uy = dx / length, dy / length
        pos = 0.0
        while pos < length:
            step = min(remain, length - pos)
            if drawing:
                draw.line(
                    (
                        x0 + ux * pos,
                        y0 + uy * pos,
                        x0 + ux * (pos + step),
                        y0 + uy * (pos + step),
                    ),
                    fill=fill,
                    width=width,
                )
            pos += step
            remain -= step
            if remain <= 1.0e-6:
                drawing = not drawing
                remain = float(dash if drawing else gap)


def draw_cutoff_overlay(
    image: Image.Image,
    value: float,
    width: int,
    scale: float,
    y_offset: float,
) -> None:
    draw = ImageDraw.Draw(image)
    axis_y = 960 * scale - y_offset
    axis_l = 95 * scale
    axis_r = width - 95 * scale
    draw.line(
        (axis_l, axis_y, axis_r, axis_y),
        fill=(150, 150, 150, 255),
        width=max(1, round(2 * scale)),
    )
    center_x = (axis_l + axis_r) / 2
    half = (axis_r - axis_l) * 0.5 * min(value / T_MAX, 1.0)
    draw.line(
        (center_x - half, axis_y, center_x + half, axis_y),
        fill=(245, 245, 245, 255),
        width=max(2, round(7 * scale)),
    )
    for x in (center_x - half, center_x + half):
        draw.line(
            (x, axis_y - 15 * scale, x, axis_y + 15 * scale),
            fill=(255, 255, 255, 255),
            width=max(1, round(3 * scale)),
        )

    paste_math_centered(
        image,
        integral_expression(value),
        max(14, round(28 * scale)),
        1030 * scale - y_offset,
    )
    paste_math_centered(
        image,
        rf"$T={display_t(value):.1f}$",
        max(11, round(18 * scale)),
        1105 * scale - y_offset,
    )


def draw_caustic_label(
    image: Image.Image,
    width: int,
    scale: float,
    y_offset: float,
) -> None:
    draw = ImageDraw.Draw(image)
    label_font = font(DEJAVU, max(11, round(22 * scale)))
    equation_font = font(STIX_ITALIC, max(17, round(34 * scale)))
    title = "CAUSTIC OVERLAY"
    equation = "27x² + 8y³ = 0"
    title_width = text_width(draw, title, label_font)
    equation_width = text_width(draw, equation, equation_font)
    box_width = max(title_width, equation_width) + 44 * scale
    box_height = 92 * scale
    box_x = (width - box_width) / 2
    box_y = 1140 * scale - y_offset
    draw.rounded_rectangle(
        (box_x, box_y, box_x + box_width, box_y + box_height),
        radius=max(7, round(14 * scale)),
        fill=(0, 0, 0, 255),
        outline=(255, 255, 255, 120),
        width=max(1, round(scale)),
    )
    draw.text(
        ((width - title_width) / 2, box_y + 12 * scale),
        title,
        font=label_font,
        fill="white",
    )
    draw.text(
        ((width - equation_width) / 2, box_y + 42 * scale),
        equation,
        font=equation_font,
        fill="white",
    )


def make_formula(directory: Path, width: int, height: int, scale: float):
    top, bottom = 40, 245
    y0 = round(top * scale)
    y1 = round(bottom * scale)
    formula = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(formula)
    kicker = font(STIX, max(14, round(28 * scale)))
    heading = "Pearcey integral"
    draw.text(
        ((width - text_width(draw, heading, kicker)) / 2, 54 * scale),
        heading,
        font=kicker,
        fill=(190, 190, 190, 255),
    )
    paste_math_centered(
        formula,
        DEFINITION,
        max(14, round(27 * scale)),
        165 * scale,
    )
    path = directory / "formula.png"
    formula.crop((0, y0, width, y1)).save(path)
    return path, y0


def make_lower_video(directory: Path, width: int, scale: float):
    # The bar, moving integral, T readout, and late label all live on black.
    # Encode that narrow strip once instead of blending hundreds of PNGs.
    top, bottom = 930, 1246
    y0 = round(top * scale)
    y1 = round(bottom * scale)
    band_height = y1 - y0
    path = directory / "lower.mp4"
    command = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{width}x{band_height}",
        "-r",
        str(UNIQUE_FPS),
        "-i",
        "-",
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "ultrafast",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        str(path),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert process.stdin is not None
    try:
        for frame_number in range(round(PRESENTATION_SECONDS * UNIQUE_FPS)):
            seconds = frame_number / UNIQUE_FPS
            frame = Image.new("RGBA", (width, band_height), (0, 0, 0, 255))
            draw_cutoff_overlay(frame, cutoff_for_time(seconds), width, scale, y0)
            if seconds >= CAUSTIC_LABEL_SECONDS:
                draw_caustic_label(frame, width, scale, y0)
            process.stdin.write(frame.convert("RGB").tobytes())
    finally:
        process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError("ffmpeg failed while encoding lower presentation strip")
    return path, y0


def make_curve(directory: Path, width: int, height: int, scale: float):
    top, bottom = 300, 840
    y0 = round(top * scale)
    y1 = round(bottom * scale)
    field_top = y0
    field_width = width
    field_height = round(540 * scale)
    curve = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(curve)
    for sign in (-1.0, 1.0):
        points = []
        for y_value in np.linspace(-4.95, 0.0, 450):
            x_value = sign * math.sqrt(max(0.0, -8.0 * y_value**3 / 27.0))
            pixel_x = (x_value - X_MIN) / (X_MAX - X_MIN) * field_width
            pixel_y = field_top + (Y_MAX - y_value) / (Y_MAX - Y_MIN) * field_height
            points.append((pixel_x, pixel_y))
        draw_dashed_polyline(
            draw,
            points,
            (0, 0, 0, 220),
            max(2, round(7 * scale)),
            dash=12 * scale,
            gap=9 * scale,
        )
        draw_dashed_polyline(
            draw,
            points,
            (255, 255, 255, 255),
            max(1, round(3 * scale)),
            dash=12 * scale,
            gap=9 * scale,
        )
    path = directory / "curve.png"
    curve.crop((0, y0, width, y1)).save(path)
    return path, y0


def render(small: bool):
    if not SOURCE.exists():
        raise SystemExit(f"base render missing: {SOURCE}")

    if small:
        width, height, fps = 360, 640, 15
        output = SMALL_OUT
        source_scale = "scale=360:640,"
        crop = "crop=360:270:0:150"
        zoom_size = "360x270"
        pad = "pad=360:640:0:150:black"
        crf = "24"
    else:
        width, height, fps = 720, 1280, 30
        output = FULL_OUT
        source_scale = ""
        crop = "crop=720:540:0:300"
        zoom_size = "720x540"
        pad = "pad=720:1280:0:300:black"
        crf = "20"

    scale = width / 720.0
    zoom_frames = round(ZOOM_SECONDS * fps)
    with tempfile.TemporaryDirectory(prefix="pearcey-v2-") as temporary:
        temporary_path = Path(temporary)
        formula, formula_y = make_formula(temporary_path, width, height, scale)
        lower, lower_y = make_lower_video(temporary_path, width, scale)
        curve, curve_y = make_curve(temporary_path, width, height, scale)

        zoom = (
            f"zoompan=z='if(lte(on,{zoom_frames}),"
            f"1+1.1*(1-on/{zoom_frames})*(1-on/{zoom_frames}),1)'"
            ":x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*0.60'"
            f":d=1:s={zoom_size}:fps={fps}"
        )
        # Normalize to the target frame rate before padding. This preserves the
        # source clock for both 30-fps full output and 15-fps preview output;
        # padding after zoompan previously made the full render stop at 12 s and
        # made the small preview run at half-speed.
        filter_graph = (
            f"[0:v]{source_scale}trim=start=0:end=11.9667,setpts=PTS-STARTPTS,"
            f"fps={fps},tpad=stop_mode=clone:stop_duration=11.0333,"
            f"{crop},{zoom},{pad}[base];"
            "[1:v]format=rgba[formula];"
            f"[base][formula]overlay=0:{formula_y}:eof_action=repeat[v1];"
            f"[v1][2:v]overlay=0:{lower_y}:eof_action=repeat[v2];"
            "[3:v]format=rgba[curve];"
            f"[v2][curve]overlay=0:{curve_y}:enable='gte(t,{CAUSTIC_CURVE_SECONDS:g})':eof_action=repeat[v]"
        )
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(SOURCE),
                "-framerate",
                str(fps),
                "-i",
                str(formula),
                "-i",
                str(lower),
                "-framerate",
                str(fps),
                "-i",
                str(curve),
                "-filter_complex",
                filter_graph,
                "-map",
                "[v]",
                "-t",
                f"{PRESENTATION_SECONDS:g}",
                "-an",
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                crf,
                "-pix_fmt",
                "yuv420p",
                "-movflags",
                "+faststart",
                str(output),
            ],
            check=True,
        )
    print(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--small",
        action="store_true",
        help="make the 360x640 15 fps repository-preview draft",
    )
    args = parser.parse_args()
    render(args.small)


if __name__ == "__main__":
    main()
