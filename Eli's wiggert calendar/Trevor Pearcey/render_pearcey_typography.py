#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from functools import lru_cache
from io import BytesIO
from pathlib import Path

import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import math_to_image
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "render_pearcey.py"


def load_base():
    spec = importlib.util.spec_from_file_location("pearcey_base_renderer", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load render_pearcey.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_base()

# Keep visible mathematical notation as mathematics, not ASCII approximations.
STATIC_FORMULA = r"$P(x,y)=\lim_{T\to\infty}\int_{−T}^{T} e^{i(t^4+y t^2+x t)}\,dt$"
MATH_COLOR = (245, 245, 245)


def display_t(value: float) -> float:
    """The animation is qualitative: one decimal is enough for the moving readout."""
    return round(float(value) + 1.0e-9, 1)


def displayed_bounds(value: float) -> tuple[str, str]:
    shown = display_t(value)
    return f"−{shown:.1f}", f"{shown:.1f}"


def integral_formula(value: float) -> str:
    lower, upper = displayed_bounds(value)
    return rf"$\int_{{{lower}}}^{{{upper}}}$"


@lru_cache(maxsize=64)
def math_rgba(expression: str, font_size: int) -> Image.Image:
    """Render MathText to a tightly cropped transparent image."""
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
    gray = np.asarray(source, dtype=np.uint8)
    alpha = Image.fromarray(255 - gray, "L")
    bbox = alpha.getbbox()
    rgba = Image.new("RGBA", source.size, (*MATH_COLOR, 0))
    rgba.putalpha(alpha)
    return rgba.crop(bbox) if bbox else rgba


def paste_math_centered(image: Image.Image, expression: str, font_size: int, center_y: int) -> None:
    formula = math_rgba(expression, font_size)
    x = (base.VIDEO_W - formula.width) // 2
    y = center_y - formula.height // 2
    image.paste(formula, (x, y), formula)


def compose(field_rgb: np.ndarray, T: float, cusp_alpha: float = 0.0) -> bytes:
    image = Image.new("RGB", (base.VIDEO_W, base.VIDEO_H), (10, 10, 12))
    field = Image.fromarray(field_rgb, "RGB").resize(
        (base.FIELD_OUT_W, base.FIELD_OUT_H), Image.Resampling.BICUBIC
    )
    image.paste(field, (0, base.FIELD_TOP))

    draw = ImageDraw.Draw(image)
    base.centered(draw, 56, "Pearcey integral", base.FONT_TITLE)
    paste_math_centered(image, STATIC_FORMULA, 27, 194)

    # Keep the interval bar.  The numeric integral underneath makes clear that the
    # bar is the truncation interval, not a playback/pinch control.
    axis_y = 960
    axis_l, axis_r = 95, base.VIDEO_W - 95
    draw = ImageDraw.Draw(image)
    draw.line((axis_l, axis_y, axis_r, axis_y), fill=(150, 150, 150), width=2)
    center_x = (axis_l + axis_r) / 2
    half = (axis_r - axis_l) * 0.5 * min(T / base.T_MAX, 1.0)
    draw.line((center_x - half, axis_y, center_x + half, axis_y), fill=(245, 245, 245), width=7)
    for x in (center_x - half, center_x + half):
        draw.line((x, axis_y - 15, x, axis_y + 15), fill=(255, 255, 255), width=3)

    paste_math_centered(image, integral_formula(T), 34, 1033)
    paste_math_centered(image, rf"$T={display_t(T):.1f}$", 24, 1110)

    if cusp_alpha > 0:
        image = Image.alpha_composite(
            image.convert("RGBA"), base.cusp_overlay(cusp_alpha)
        ).convert("RGB")
        draw = ImageDraw.Draw(image)
        base.centered(
            draw,
            1162,
            "27x² + 8y³ = 0",
            base.FONT_SMALL,
            fill=(255, 255, 255),
        )

    return np.asarray(image, dtype=np.uint8).tobytes()


def main() -> None:
    base.compose = compose
    base.main()


if __name__ == "__main__":
    main()
