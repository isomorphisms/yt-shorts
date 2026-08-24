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

STIX = "/usr/share/fonts/opentype/stix-word/STIX-Regular.otf"
STIX_ITALIC = "/usr/share/fonts/opentype/stix-word/STIX-Italic.otf"
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path: str, size: int):
    return ImageFont.truetype(path, size)


def text_width(draw: ImageDraw.ImageDraw, text: str, face) -> int:
    box = draw.textbbox((0, 0), text, font=face)
    return box[2] - box[0]


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


def make_overlays(directory: Path, width: int, height: int):
    scale = width / 720.0
    field_top = int(round(300 * scale))
    field_width = width
    field_height = int(round(540 * scale))

    formula = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(formula)

    kicker = font(STIX, round(28 * scale))
    main = font(STIX_ITALIC, round(42 * scale))
    roman = font(STIX, round(40 * scale))
    sub = font(STIX_ITALIC, round(25 * scale))
    integral = font(STIX, round(68 * scale))
    exponent = font(STIX_ITALIC, round(25 * scale))
    differential = font(STIX_ITALIC, round(34 * scale))

    heading = "Pearcey integral"
    draw.text(
        ((width - text_width(draw, heading, kicker)) / 2, 54 * scale),
        heading,
        font=kicker,
        fill=(190, 190, 190, 255),
    )

    # Draw P_T and the integral limits by baseline placement.  Visible math
    # therefore uses actual sub/superscript positioning rather than `_`/`^`.
    p_width = text_width(draw, "P", main)
    sub_width = text_width(draw, "T", sub)
    xy_width = text_width(draw, "(x, y) =", roman)
    e_width = text_width(draw, "e", main)
    exponent_width = text_width(draw, "i(t⁴ + yt² + xt)", exponent)
    dt_width = text_width(draw, "dt", differential)
    integral_width = 54 * scale
    total = (
        p_width + sub_width + xy_width + integral_width + e_width
        + exponent_width + dt_width + (18 + 18 + 14 + 10 + 10) * scale
    )
    x = (width - total) / 2
    y = 132 * scale

    draw.text((x, y), "P", font=main, fill="white")
    x += p_width - 3 * scale
    draw.text((x, y + 28 * scale), "T", font=sub, fill="white")
    x += sub_width + 18 * scale
    draw.text((x, y + 4 * scale), "(x, y) =", font=roman, fill="white")
    x += xy_width + 14 * scale

    integral_x = x
    draw.text((integral_x, y - 13 * scale), "∫", font=integral, fill="white")
    draw.text((integral_x + 33 * scale, y - 18 * scale), "T", font=sub, fill="white")
    draw.text((integral_x + 28 * scale, y + 49 * scale), "−T", font=sub, fill="white")
    x += integral_width + 10 * scale

    draw.text((x, y + 4 * scale), "e", font=main, fill="white")
    x += e_width - 2 * scale
    draw.text((x, y - 7 * scale), "i(t⁴ + yt² + xt)", font=exponent, fill="white")
    x += exponent_width + 10 * scale
    draw.text((x, y + 10 * scale), "dt", font=differential, fill="white")

    formula_path = directory / "formula.png"
    formula.save(formula_path)

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

    return formula_path, label_path, curve_path


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
        formula, label, curve = make_overlays(temporary_path, width, height)
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
            "[2:v]format=rgba[label];"
            "[v1][label]overlay=0:0:enable='gte(t,18)'[v2];"
            "[3:v]format=rgba[curve];"
            "[v2][curve]overlay=0:0:enable='gte(t,19)'[v]"
        )
        subprocess.run(
            [
                "ffmpeg", "-y", "-loglevel", "error",
                "-i", str(SOURCE),
                "-loop", "1", "-i", str(formula),
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
