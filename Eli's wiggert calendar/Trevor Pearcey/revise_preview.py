#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "pearcey-T-build-wegert.mp4"
FULL_OUT = HERE / "pearcey-T-build-wegert-v2.mp4"
SMALL_OUT = HERE / "pearcey-T-build-wegert-v2-small.mp4"

X_MIN, X_MAX = -6.0, 6.0
Y_MIN, Y_MAX = -6.0, 3.0
T_MAX = 3.0
DT = 0.003
BUILD_SECONDS = 10.0
UNIQUE_FPS = 15

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
    """Match the cutoff used by the 15-unique-frame/s base renderer."""
    if seconds >= BUILD_SECONDS:
        return T_MAX
    count = int(BUILD_SECONDS * UNIQUE_FPS)
    index = min(count - 1, max(0, int(seconds * UNIQUE_FPS)))
    target = t_for_build_frame(index, count)
    step = min(int(round(T_MAX / DT)), max(1, int(round(target / DT))))
    return step * DT


def display_t(value: float) -> float:
    # This is an explanatory animation, not a numerical-results table.
    return round(float(value) + 1.0e-9, 1)


def displayed_bounds(value: float) -> tuple[str, str]:
    shown = display_t(value)
    return f"−{shown:.1f}", f"{shown:.1f}"


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
                    (x0 + ux * pos, y0 + uy * pos,
                     x0 + ux * (pos + step), y0 + uy * (pos + step)),
                    fill=fill,
                    width=width,
                )
            pos += step
            remain -= step
            if remain <= 1.0e-6:
                drawing = not drawing
                remain = float(dash if drawing else gap)


def draw_definition(draw: ImageDraw.ImageDraw, width: int, scale: float) -> None:
    """Typeset P(x,y)=lim(T→∞) integral rather than showing ASCII interval notation."""
    main = font(STIX_ITALIC, round(40 * scale))
    roman = font(STIX, round(35 * scale))
    limit = font(STIX, round(29 * scale))
    limit_sub = font(STIX_ITALIC, round(18 * scale))
    integral = font(STIX, round(66 * scale))
    bound = font(STIX_ITALIC, round(22 * scale))
    exponent = font(STIX_ITALIC, round(22 * scale))
    differential = font(STIX_ITALIC, round(30 * scale))

    p_width = text_width(draw, "P", main)
    xy_width = text_width(draw, "(x, y) =", roman)
    lim_width = max(text_width(draw, "lim", limit), text_width(draw, "T → ∞", limit_sub))
    e_width = text_width(draw, "e", main)
    exponent_width = text_width(draw, "i(t⁴ + yt² + xt)", exponent)
    dt_width = text_width(draw, "dt", differential)
    integral_width = 52 * scale
    gaps = (13 + 16 + 15 + 8 + 8) * scale
    total = p_width + xy_width + lim_width + integral_width + e_width + exponent_width + dt_width + gaps
    x = (width - total) / 2
    y = 132 * scale

    draw.text((x, y + 3 * scale), "P", font=main, fill="white")
    x += p_width + 13 * scale
    draw.text((x, y + 7 * scale), "(x, y) =", font=roman, fill="white")
    x += xy_width + 16 * scale

    lim_x = x
    lim_text_width = text_width(draw, "lim", limit)
    lim_sub_width = text_width(draw, "T → ∞", limit_sub)
    draw.text((lim_x + (lim_width - lim_text_width) / 2, y + 2 * scale), "lim", font=limit, fill="white")
    draw.text((lim_x + (lim_width - lim_sub_width) / 2, y + 39 * scale), "T → ∞", font=limit_sub, fill="white")
    x += lim_width + 15 * scale

    integral_x = x
    draw.text((integral_x, y - 14 * scale), "∫", font=integral, fill="white")
    draw.text((integral_x + 31 * scale, y - 18 * scale), "T", font=bound, fill="white")
    draw.text((integral_x + 26 * scale, y + 47 * scale), "−T", font=bound, fill="white")
    x += integral_width + 8 * scale

    draw.text((x, y + 4 * scale), "e", font=main, fill="white")
    x += e_width - 2 * scale
    draw.text((x, y - 7 * scale), "i(t⁴ + yt² + xt)", font=exponent, fill="white")
    x += exponent_width + 8 * scale
    draw.text((x, y + 10 * scale), "dt", font=differential, fill="white")


def draw_cutoff_overlay(image: Image.Image, value: float, width: int, scale: float) -> None:
    draw = ImageDraw.Draw(image)
    axis_y = 960 * scale
    axis_l = 95 * scale
    axis_r = width - 95 * scale
    draw.line((axis_l, axis_y, axis_r, axis_y), fill=(150, 150, 150, 255), width=max(1, round(2 * scale)))
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

    integral = font(STIX, round(58 * scale))
    bound = font(STIX, round(21 * scale))
    t_face = font(STIX_ITALIC, round(24 * scale))
    lower, upper = displayed_bounds(value)

    integral_w = text_width(draw, "∫", integral)
    bound_w = max(text_width(draw, lower, bound), text_width(draw, upper, bound))
    group_w = integral_w + bound_w + 5 * scale
    integral_x = (width - group_w) / 2
    integral_y = 989 * scale
    draw.text((integral_x, integral_y), "∫", font=integral, fill="white")
    draw.text((integral_x + integral_w - 2 * scale, integral_y - 3 * scale), upper, font=bound, fill="white")
    draw.text((integral_x + integral_w - 2 * scale, integral_y + 42 * scale), lower, font=bound, fill="white")

    t_text = f"T = {display_t(value):.1f}"
    t_width = text_width(draw, t_text, t_face)
    draw.text(((width - t_width) / 2, 1091 * scale), t_text, font=t_face, fill=(225, 225, 225, 255))


def make_overlays(directory: Path, width: int, height: int, fps: int):
    scale = width / 720.0
    field_top = int(round(300 * scale))
    field_width = width
    field_height = int(round(540 * scale))

    formula = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(formula)
    kicker = font(STIX, round(28 * scale))
    heading = "Pearcey integral"
    draw.text(
        ((width - text_width(draw, heading, kicker)) / 2, 54 * scale),
        heading,
        font=kicker,
        fill=(190, 190, 190, 255),
    )
    draw_definition(draw, width, scale)
    formula_path = directory / "formula.png"
    formula.save(formula_path)

    dynamic_dir = directory / "cutoff"
    dynamic_dir.mkdir()
    frame_count = 23 * fps
    for frame_number in range(frame_count):
        seconds = frame_number / fps
        dynamic = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw_cutoff_overlay(dynamic, cutoff_for_time(seconds), width, scale)
        dynamic.save(dynamic_dir / f"{frame_number:05d}.png", optimize=True)

    label = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(label)
    label_font = font(DEJAVU, round(22 * scale))
    equation_font = font(STIX_ITALIC, round(34 * scale))
    title = "CAUSTIC OVERLAY"
    equation = "27x² + 8y³ = 0"
    title_width = text_width(draw, title, label_font)
    equation_width = text_width(draw, equation, equation_font)
    box_width = max(title_width, equation_width) + 44 * scale
    box_height = 92 * scale
    box_x = (width - box_width) / 2
    box_y = 940 * scale
    draw.rounded_rectangle(
        (box_x, box_y, box_x + box_width, box_y + box_height),
        radius=round(14 * scale),
        fill=(0, 0, 0, 190),
        outline=(255, 255, 255, 100),
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
    label_path = directory / "label.png"
    label.save(label_path)

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
            draw, points, (0, 0, 0, 220), max(2, round(7 * scale)),
            dash=12 * scale, gap=9 * scale,
        )
        draw_dashed_polyline(
            draw, points, (255, 255, 255, 255), max(1, round(3 * scale)),
            dash=12 * scale, gap=9 * scale,
        )
    curve_path = directory / "curve.png"
    curve.save(curve_path)

    return formula_path, dynamic_dir, label_path, curve_path


def render(small: bool):
    if not SOURCE.exists():
        raise SystemExit(f"base render missing: {SOURCE}")

    if small:
        width, height, fps = 360, 640, 15
        output = SMALL_OUT
        source_scale = "scale=360:640,"
        crop = "crop=360:270:0:150"
        zoom_frames = 82
        zoom_size = "360x270"
        pad = "pad=360:640:0:150:black"
        crf = "24"
    else:
        width, height, fps = 720, 1280, 30
        output = FULL_OUT
        source_scale = ""
        crop = "crop=720:540:0:300"
        zoom_frames = 165
        zoom_size = "720x540"
        pad = "pad=720:1280:0:300:black"
        crf = "20"

    # The mathematical field keeps building through 10 s.  The camera reaches
    # the full view by about 5.5 s.  We then keep the clean final field visible
    # until 18 s.  The overlay label appears at 18 s and the dashed curve at
    # 19 s, so the curve cannot be mistaken for a feature generated by Wegert.
    with tempfile.TemporaryDirectory(prefix="pearcey-v2-") as temporary:
        temporary_path = Path(temporary)
        formula, dynamic_dir, label, curve = make_overlays(temporary_path, width, height, fps)
        zoom = (
            f"zoompan=z='if(lte(on,{zoom_frames}),"
            f"1+1.1*(1-on/{zoom_frames})*(1-on/{zoom_frames}),1)'"
            ":x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*0.60'"
            f":d=1:s={zoom_size}:fps={fps}"
        )
        filter_graph = (
            f"[0:v]{source_scale}trim=start=0:end=11.9667,setpts=PTS-STARTPTS,"
            f"{crop},{zoom},tpad=stop_mode=clone:stop_duration=11.0333,{pad}[base];"
            "[1:v]format=rgba[formula];"
            "[base][formula]overlay=0:0[v1];"
            "[2:v]format=rgba[cutoff];"
            "[v1][cutoff]overlay=0:0[v2];"
            "[3:v]format=rgba[label];"
            "[v2][label]overlay=0:0:enable='gte(t,18)'[v3];"
            "[4:v]format=rgba[curve];"
            "[v3][curve]overlay=0:0:enable='gte(t,19)'[v]"
        )
        subprocess.run(
            [
                "ffmpeg", "-y", "-loglevel", "error",
                "-i", str(SOURCE),
                "-loop", "1", "-i", str(formula),
                "-framerate", str(fps), "-i", str(dynamic_dir / "%05d.png"),
                "-loop", "1", "-i", str(label),
                "-loop", "1", "-i", str(curve),
                "-filter_complex", filter_graph,
                "-map", "[v]", "-t", "23", "-an",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", crf,
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output),
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
