#!/usr/bin/env python3
from __future__ import annotations

import ctypes as C
import math
import os
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[2]
WEGERT_COLOR_CORE = (
    ROOT / "third_party" / "wegert" / "app" / "src" / "main" / "assets" / "wegert_color.glsl"
)
OUT = HERE / "pearcey-T-build-wegert.mp4"
POSTER = HERE / "pearcey-final-frame.png"

# The mathematical field is 4:3 because x spans 12 units and y spans 9.
FIELD_W = 540
FIELD_H = 405
VIDEO_W = 720
VIDEO_H = 1280
FIELD_OUT_W = 720
FIELD_OUT_H = 540
FIELD_TOP = 300
FPS = 30
UNIQUE_FPS = 15
# Finish the cutoff as the camera settles, then keep an unmarked natural field
# available to the presentation compositor until its delayed overlay.
BUILD_SECONDS = 6
HOLD_SECONDS = 6
CUSP_SECONDS = 3
T_MAX = 3.0
DT = 0.003
X_MIN, X_MAX = -6.0, 6.0
Y_MIN, Y_MAX = -6.0, 3.0

color_core = WEGERT_COLOR_CORE.read_text()
if "vec3 wegert_color_complex(vec2 value)" not in color_core:
    raise SystemExit(f"Wegert coloring core not found at {WEGERT_COLOR_CORE}")

VERTEX = r"""#version 330 core
layout(location = 0) in vec2 a_position;
out vec2 v_ndc;
void main() {
    v_ndc = a_position;
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

FRAGMENT = (
    r"""#version 330 core
in vec2 v_ndc;
out vec4 frag_color;
uniform sampler2D u_values;
"""
    + color_core
    + r"""
void main() {
    vec2 uv = 0.5 * (v_ndc + vec2(1.0));
    vec2 value = texture(u_values, uv).rg;
    frag_color = vec4(wegert_color_complex(value), 1.0);
}
"""
)

EGL_DEFAULT_DISPLAY = C.c_void_p(0)
EGL_NO_SURFACE = C.c_void_p(0)
EGL_NO_CONTEXT = C.c_void_p(0)
EGL_NONE = 0x3038
EGL_SURFACE_TYPE = 0x3033
EGL_PBUFFER_BIT = 0x0001
EGL_RENDERABLE_TYPE = 0x3040
EGL_OPENGL_BIT = 0x0008
EGL_RED_SIZE = 0x3024
EGL_GREEN_SIZE = 0x3023
EGL_BLUE_SIZE = 0x3022
EGL_ALPHA_SIZE = 0x3021
EGL_WIDTH = 0x3057
EGL_HEIGHT = 0x3056
EGL_OPENGL_API = 0x30A2

GL_VERTEX_SHADER = 0x8B31
GL_FRAGMENT_SHADER = 0x8B30
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_INFO_LOG_LENGTH = 0x8B84
GL_ARRAY_BUFFER = 0x8892
GL_STATIC_DRAW = 0x88E4
GL_FLOAT = 0x1406
GL_FALSE = 0
GL_TRIANGLE_STRIP = 0x0005
GL_RGBA = 0x1908
GL_UNSIGNED_BYTE = 0x1401
GL_TEXTURE_2D = 0x0DE1
GL_TEXTURE0 = 0x84C0
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_NEAREST = 0x2600
GL_CLAMP_TO_EDGE = 0x812F
GL_RG32F = 0x8230
GL_RG = 0x8227

os.environ.setdefault("EGL_PLATFORM", "surfaceless")
os.environ.setdefault("LIBGL_ALWAYS_SOFTWARE", "1")
egl = C.CDLL("libEGL.so.1")
gl = C.CDLL("libGL.so.1")


def proto(lib, name, restype, *args):
    f = getattr(lib, name)
    f.restype = restype
    f.argtypes = list(args)
    return f


eglGetDisplay = proto(egl, "eglGetDisplay", C.c_void_p, C.c_void_p)
eglInitialize = proto(egl, "eglInitialize", C.c_uint, C.c_void_p, C.POINTER(C.c_int), C.POINTER(C.c_int))
eglChooseConfig = proto(egl, "eglChooseConfig", C.c_uint, C.c_void_p, C.POINTER(C.c_int), C.POINTER(C.c_void_p), C.c_int, C.POINTER(C.c_int))
eglCreatePbufferSurface = proto(egl, "eglCreatePbufferSurface", C.c_void_p, C.c_void_p, C.c_void_p, C.POINTER(C.c_int))
eglBindAPI = proto(egl, "eglBindAPI", C.c_uint, C.c_uint)
eglCreateContext = proto(egl, "eglCreateContext", C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p, C.POINTER(C.c_int))
eglMakeCurrent = proto(egl, "eglMakeCurrent", C.c_uint, C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p)
eglDestroySurface = proto(egl, "eglDestroySurface", C.c_uint, C.c_void_p, C.c_void_p)
eglDestroyContext = proto(egl, "eglDestroyContext", C.c_uint, C.c_void_p, C.c_void_p)
eglTerminate = proto(egl, "eglTerminate", C.c_uint, C.c_void_p)

glCreateShader = proto(gl, "glCreateShader", C.c_uint, C.c_uint)
glShaderSource = proto(gl, "glShaderSource", None, C.c_uint, C.c_int, C.POINTER(C.c_char_p), C.POINTER(C.c_int))
glCompileShader = proto(gl, "glCompileShader", None, C.c_uint)
glGetShaderiv = proto(gl, "glGetShaderiv", None, C.c_uint, C.c_uint, C.POINTER(C.c_int))
glGetShaderInfoLog = proto(gl, "glGetShaderInfoLog", None, C.c_uint, C.c_int, C.POINTER(C.c_int), C.c_char_p)
glCreateProgram = proto(gl, "glCreateProgram", C.c_uint)
glAttachShader = proto(gl, "glAttachShader", None, C.c_uint, C.c_uint)
glLinkProgram = proto(gl, "glLinkProgram", None, C.c_uint)
glGetProgramiv = proto(gl, "glGetProgramiv", None, C.c_uint, C.c_uint, C.POINTER(C.c_int))
glGetProgramInfoLog = proto(gl, "glGetProgramInfoLog", None, C.c_uint, C.c_int, C.POINTER(C.c_int), C.c_char_p)
glUseProgram = proto(gl, "glUseProgram", None, C.c_uint)
glGenVertexArrays = proto(gl, "glGenVertexArrays", None, C.c_int, C.POINTER(C.c_uint))
glBindVertexArray = proto(gl, "glBindVertexArray", None, C.c_uint)
glGenBuffers = proto(gl, "glGenBuffers", None, C.c_int, C.POINTER(C.c_uint))
glBindBuffer = proto(gl, "glBindBuffer", None, C.c_uint, C.c_uint)
glBufferData = proto(gl, "glBufferData", None, C.c_uint, C.c_ssize_t, C.c_void_p, C.c_uint)
glEnableVertexAttribArray = proto(gl, "glEnableVertexAttribArray", None, C.c_uint)
glVertexAttribPointer = proto(gl, "glVertexAttribPointer", None, C.c_uint, C.c_int, C.c_uint, C.c_uint, C.c_int, C.c_void_p)
glGetUniformLocation = proto(gl, "glGetUniformLocation", C.c_int, C.c_uint, C.c_char_p)
glUniform1i = proto(gl, "glUniform1i", None, C.c_int, C.c_int)
glViewport = proto(gl, "glViewport", None, C.c_int, C.c_int, C.c_int, C.c_int)
glDrawArrays = proto(gl, "glDrawArrays", None, C.c_uint, C.c_int, C.c_int)
glReadPixels = proto(gl, "glReadPixels", None, C.c_int, C.c_int, C.c_int, C.c_int, C.c_uint, C.c_uint, C.c_void_p)
glFinish = proto(gl, "glFinish", None)
glGenTextures = proto(gl, "glGenTextures", None, C.c_int, C.POINTER(C.c_uint))
glActiveTexture = proto(gl, "glActiveTexture", None, C.c_uint)
glBindTexture = proto(gl, "glBindTexture", None, C.c_uint, C.c_uint)
glTexParameteri = proto(gl, "glTexParameteri", None, C.c_uint, C.c_uint, C.c_int)
glTexImage2D = proto(gl, "glTexImage2D", None, C.c_uint, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_uint, C.c_uint, C.c_void_p)
glTexSubImage2D = proto(gl, "glTexSubImage2D", None, C.c_uint, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_uint, C.c_uint, C.c_void_p)


def compile_shader(kind, text):
    shader = glCreateShader(kind)
    encoded = text.encode()
    pointer = C.c_char_p(encoded)
    glShaderSource(shader, 1, C.byref(pointer), None)
    glCompileShader(shader)
    ok = C.c_int()
    glGetShaderiv(shader, GL_COMPILE_STATUS, C.byref(ok))
    if not ok.value:
        length = C.c_int()
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, C.byref(length))
        message = C.create_string_buffer(max(length.value, 1))
        glGetShaderInfoLog(shader, len(message), None, message)
        raise RuntimeError(message.value.decode(errors="replace"))
    return shader


class WegertGL:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
        self.display = eglGetDisplay(EGL_DEFAULT_DISPLAY)
        major = C.c_int(); minor = C.c_int()
        if not self.display or not eglInitialize(self.display, C.byref(major), C.byref(minor)):
            raise RuntimeError("EGL initialization failed")
        attrs = (C.c_int * 13)(
            EGL_SURFACE_TYPE, EGL_PBUFFER_BIT,
            EGL_RENDERABLE_TYPE, EGL_OPENGL_BIT,
            EGL_RED_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_BLUE_SIZE, 8, EGL_ALPHA_SIZE, 8,
            EGL_NONE,
        )
        config = C.c_void_p(); count = C.c_int()
        if not eglChooseConfig(self.display, attrs, C.byref(config), 1, C.byref(count)) or count.value < 1:
            raise RuntimeError("No OpenGL pbuffer config")
        pbuffer_attrs = (C.c_int * 5)(EGL_WIDTH, w, EGL_HEIGHT, h, EGL_NONE)
        self.surface = eglCreatePbufferSurface(self.display, config, pbuffer_attrs)
        if not self.surface or not eglBindAPI(EGL_OPENGL_API):
            raise RuntimeError("OpenGL pbuffer creation failed")
        context_attrs = (C.c_int * 1)(EGL_NONE)
        self.context = eglCreateContext(self.display, config, EGL_NO_CONTEXT, context_attrs)
        if not self.context or not eglMakeCurrent(self.display, self.surface, self.surface, self.context):
            raise RuntimeError("OpenGL context creation failed")

        vs = compile_shader(GL_VERTEX_SHADER, VERTEX)
        fs = compile_shader(GL_FRAGMENT_SHADER, FRAGMENT)
        self.program = glCreateProgram()
        glAttachShader(self.program, vs); glAttachShader(self.program, fs); glLinkProgram(self.program)
        ok = C.c_int(); glGetProgramiv(self.program, GL_LINK_STATUS, C.byref(ok))
        if not ok.value:
            length = C.c_int(); glGetProgramiv(self.program, GL_INFO_LOG_LENGTH, C.byref(length))
            msg = C.create_string_buffer(max(length.value, 1)); glGetProgramInfoLog(self.program, len(msg), None, msg)
            raise RuntimeError(msg.value.decode(errors="replace"))
        glUseProgram(self.program)

        vertices = (C.c_float * 8)(-1, -1, 1, -1, -1, 1, 1, 1)
        vao = C.c_uint(); vbo = C.c_uint()
        glGenVertexArrays(1, C.byref(vao)); glBindVertexArray(vao)
        glGenBuffers(1, C.byref(vbo)); glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, C.sizeof(vertices), C.cast(vertices, C.c_void_p), GL_STATIC_DRAW)
        glEnableVertexAttribArray(0); glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)

        self.texture = C.c_uint(); glGenTextures(1, C.byref(self.texture))
        glActiveTexture(GL_TEXTURE0); glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RG32F, w, h, 0, GL_RG, GL_FLOAT, None)
        loc = glGetUniformLocation(self.program, b"u_values")
        if loc < 0:
            raise RuntimeError("u_values uniform missing")
        glUniform1i(loc, 0)
        glViewport(0, 0, w, h)
        self.pixels = (C.c_ubyte * (w * h * 4))()

    def color(self, field: np.ndarray) -> np.ndarray:
        packed = np.empty((self.h, self.w, 2), dtype=np.float32)
        packed[..., 0] = field.real
        packed[..., 1] = field.imag
        glActiveTexture(GL_TEXTURE0); glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, self.w, self.h, GL_RG, GL_FLOAT, packed.ctypes.data_as(C.c_void_p))
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4); glFinish()
        glReadPixels(0, 0, self.w, self.h, GL_RGBA, GL_UNSIGNED_BYTE, self.pixels)
        rgba = np.frombuffer(self.pixels, dtype=np.uint8).reshape(self.h, self.w, 4)
        return rgba[::-1, :, :3].copy()

    def close(self):
        eglMakeCurrent(self.display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT)
        eglDestroySurface(self.display, self.surface)
        eglDestroyContext(self.display, self.context)
        eglTerminate(self.display)


def ease(s: float) -> float:
    s = min(max(s, 0.0), 1.0)
    return s * s * (3.0 - 2.0 * s)


def t_for_build_frame(index: int, count: int) -> float:
    s = index / max(count - 1, 1)
    e = ease(s)
    return 0.06 + (T_MAX - 0.06) * (e ** 0.82)


def load_font(size: int, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size)


FONT_TITLE = load_font(48, True)
FONT_EQ = load_font(30)
FONT_SMALL = load_font(25)
FONT_T = load_font(34, True)


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, font, fill=(240, 240, 240)):
    box = draw.textbbox((0, 0), text, font=font)
    x = (VIDEO_W - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def cusp_overlay(alpha: float):
    overlay = Image.new("RGBA", (VIDEO_W, VIDEO_H), (0, 0, 0, 0))
    if alpha <= 0:
        return overlay
    draw = ImageDraw.Draw(overlay)
    color = (255, 255, 255, int(255 * alpha))
    for sign in (-1.0, 1.0):
        pts = []
        for y in np.linspace(-4.95, 0.0, 260):
            x = sign * math.sqrt(max(0.0, -8.0 * y**3 / 27.0))
            px = (x - X_MIN) / (X_MAX - X_MIN) * FIELD_OUT_W
            py = FIELD_TOP + (Y_MAX - y) / (Y_MAX - Y_MIN) * FIELD_OUT_H
            pts.append((px, py))
        draw.line(pts, fill=color, width=3)
    return overlay


def compose(field_rgb: np.ndarray, T: float, cusp_alpha: float = 0.0) -> bytes:
    image = Image.new("RGB", (VIDEO_W, VIDEO_H), (10, 10, 12))
    field = Image.fromarray(field_rgb, "RGB").resize((FIELD_OUT_W, FIELD_OUT_H), Image.Resampling.BICUBIC)
    image.paste(field, (0, FIELD_TOP))
    draw = ImageDraw.Draw(image)
    centered(draw, 62, "Pearcey integral", FONT_TITLE)
    centered(draw, 142, "P_T(x,y) = ∫[-T,T] exp i(t⁴ + y t² + x t) dt", FONT_EQ)

    axis_y = 970
    axis_l, axis_r = 95, VIDEO_W - 95
    draw.line((axis_l, axis_y, axis_r, axis_y), fill=(150, 150, 150), width=2)
    center_x = (axis_l + axis_r) / 2
    half = (axis_r - axis_l) * 0.5 * min(T / T_MAX, 1.0)
    draw.line((center_x - half, axis_y, center_x + half, axis_y), fill=(245, 245, 245), width=7)
    for x in (center_x - half, center_x + half):
        draw.line((x, axis_y - 15, x, axis_y + 15), fill=(255, 255, 255), width=3)
    centered(draw, 1010, f"integration interval   [−{T:.2f}, {T:.2f}]", FONT_SMALL)
    centered(draw, 1080, f"T = {T:.2f}", FONT_T)

    if cusp_alpha > 0:
        image = Image.alpha_composite(image.convert("RGBA"), cusp_overlay(cusp_alpha)).convert("RGB")
        draw = ImageDraw.Draw(image)
        centered(draw, 1162, "27x² + 8y³ = 0", FONT_SMALL, fill=(255, 255, 255))
    return np.asarray(image, dtype=np.uint8).tobytes()


def add_block(accum, y_phase, scalar, cos_xt, start_j, end_j, dt):
    if end_j <= start_j:
        return accum
    idx = np.arange(start_j if start_j else 0, end_j + 1)
    weights = np.ones(len(idx), np.float32)
    weights[0] = 0.5
    weights[-1] = 0.5
    coeff = (dt * weights * scalar[idx]).astype(np.complex64)
    accum += (y_phase[:, idx] * coeff[None, :]) @ cos_xt[idx, :]
    return accum


def main():
    x = np.linspace(X_MIN, X_MAX, FIELD_W, dtype=np.float32)
    y = np.linspace(Y_MIN, Y_MAX, FIELD_H, dtype=np.float32)
    n_steps = int(round(T_MAX / DT))
    t = np.arange(n_steps + 1, dtype=np.float32) * np.float32(DT)
    t2 = t * t
    scalar = (2.0 * np.exp(1j * (t2 * t2))).astype(np.complex64)
    y_phase = np.exp(1j * y[:, None] * t2[None, :]).astype(np.complex64)
    cos_xt = np.cos(t[:, None] * x[None, :]).astype(np.float32)

    build_unique = BUILD_SECONDS * UNIQUE_FPS
    target_T = [t_for_build_frame(i, build_unique) for i in range(build_unique)]
    target_j = [min(n_steps, max(1, int(round(v / DT)))) for v in target_T]

    wegert = WegertGL(FIELD_W, FIELD_H)
    ffmpeg = subprocess.Popen([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pixel_format", "rgb24",
        "-video_size", f"{VIDEO_W}x{VIDEO_H}", "-framerate", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUT)
    ], stdin=subprocess.PIPE)

    accum = np.zeros((FIELD_H, FIELD_W), dtype=np.complex64)
    prev_j = 0
    last_rgb = None
    last_T = 0.0

    for i, j in enumerate(target_j):
        if j > prev_j:
            accum = add_block(accum, y_phase, scalar, cos_xt, prev_j, j, DT)
            prev_j = j
        last_rgb = wegert.color(accum)
        last_T = j * DT
        frame = compose(last_rgb, last_T, 0.0)
        for _ in range(FPS // UNIQUE_FPS):
            ffmpeg.stdin.write(frame)
        if i % 30 == 0:
            print(f"build {i:03d}/{build_unique}: T={last_T:.3f}", flush=True)

    hold_frame = compose(last_rgb, last_T, 0.0)
    for _ in range(HOLD_SECONDS * FPS):
        ffmpeg.stdin.write(hold_frame)

    for k in range(CUSP_SECONDS * FPS):
        alpha = ease(min(1.0, k / max(FPS - 1, 1)))
        ffmpeg.stdin.write(compose(last_rgb, last_T, alpha))

    ffmpeg.stdin.close()
    if ffmpeg.wait():
        raise RuntimeError("ffmpeg failed")
    wegert.close()

    Image.fromarray(
        np.frombuffer(compose(last_rgb, last_T, 1.0), dtype=np.uint8).reshape(VIDEO_H, VIDEO_W, 3)
    ).save(POSTER)
    print(OUT)
    print(POSTER)


if __name__ == "__main__":
    main()
