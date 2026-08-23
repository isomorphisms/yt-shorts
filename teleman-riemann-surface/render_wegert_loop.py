#!/usr/bin/env python3
from __future__ import annotations

import ctypes as C
import math
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEGERT_SHADER = ROOT / "third_party" / "wegert" / "app" / "src" / "main" / "assets" / "wegert.frag"
OUT = Path(__file__).resolve().parent / "wegert-k-loop.mp4"
W = H = 720
FPS = 30
SECONDS = 7
FRAMES = FPS * SECONDS

# Load Wegert's production shader. For the headless renderer only, translate
# the GLES prologue to desktop GLSL; the shader body remains Wegert's.
source = WEGERT_SHADER.read_text()
source = source.replace("#version 300 es", "#version 330 core")
source = source.replace("precision highp float;\n", "")
source = source.replace("precision highp int;\n", "")

# sqrt((z^2-1)(z^2-k^2)) gives every factor exponent 1/2. Apply that
# exponent to the phase and log-modulus which Wegert has already accumulated,
# immediately before Wegert's existing colour computation.
needle = "    float hue_degrees = 360.0 * positive_fract(phase / TAU);"
if needle not in source:
    raise SystemExit("Wegert shader changed: square-root injection point not found")
source = source.replace(
    needle,
    "    phase *= 0.5;\n    log_modulus *= 0.5;\n\n" + needle,
    1,
)

VERTEX = r"""#version 330 core
layout(location = 0) in vec2 a_position;
out vec2 v_ndc;
void main() {
    v_ndc = a_position;
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

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

os.environ.setdefault("EGL_PLATFORM", "surfaceless")
egl = C.CDLL("libEGL.so.1")
gl = C.CDLL("libGL.so.1")


def proto(lib, name, restype, *args):
    function = getattr(lib, name)
    function.restype = restype
    function.argtypes = list(args)
    return function


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
glUniform2f = proto(gl, "glUniform2f", None, C.c_int, C.c_float, C.c_float)
glUniform1f = proto(gl, "glUniform1f", None, C.c_int, C.c_float)
glUniform1i = proto(gl, "glUniform1i", None, C.c_int, C.c_int)
glUniform2fv = proto(gl, "glUniform2fv", None, C.c_int, C.c_int, C.POINTER(C.c_float))
glViewport = proto(gl, "glViewport", None, C.c_int, C.c_int, C.c_int, C.c_int)
glDrawArrays = proto(gl, "glDrawArrays", None, C.c_uint, C.c_int, C.c_int)
glReadPixels = proto(gl, "glReadPixels", None, C.c_int, C.c_int, C.c_int, C.c_int, C.c_uint, C.c_uint, C.c_void_p)
glFinish = proto(gl, "glFinish", None)


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


display = eglGetDisplay(EGL_DEFAULT_DISPLAY)
major = C.c_int()
minor = C.c_int()
if not display or not eglInitialize(display, C.byref(major), C.byref(minor)):
    raise SystemExit("EGL initialization failed")

attributes = (C.c_int * 15)(
    EGL_SURFACE_TYPE, EGL_PBUFFER_BIT,
    EGL_RENDERABLE_TYPE, EGL_OPENGL_BIT,
    EGL_RED_SIZE, 8,
    EGL_GREEN_SIZE, 8,
    EGL_BLUE_SIZE, 8,
    EGL_ALPHA_SIZE, 8,
    EGL_NONE, 0, 0,
)
config = C.c_void_p()
config_count = C.c_int()
if not eglChooseConfig(display, attributes, C.byref(config), 1, C.byref(config_count)) or config_count.value < 1:
    raise SystemExit("No OpenGL pbuffer configuration")

pbuffer_attributes = (C.c_int * 5)(EGL_WIDTH, W, EGL_HEIGHT, H, EGL_NONE)
surface = eglCreatePbufferSurface(display, config, pbuffer_attributes)
if not surface:
    raise SystemExit("Pbuffer creation failed")
if not eglBindAPI(EGL_OPENGL_API):
    raise SystemExit("eglBindAPI failed")
context_attributes = (C.c_int * 1)(EGL_NONE)
context = eglCreateContext(display, config, EGL_NO_CONTEXT, context_attributes)
if not context:
    raise SystemExit("OpenGL context creation failed")
if not eglMakeCurrent(display, surface, surface, context):
    raise SystemExit("eglMakeCurrent failed")

vertex_shader = compile_shader(GL_VERTEX_SHADER, VERTEX)
fragment_shader = compile_shader(GL_FRAGMENT_SHADER, source)
program = glCreateProgram()
glAttachShader(program, vertex_shader)
glAttachShader(program, fragment_shader)
glLinkProgram(program)
ok = C.c_int()
glGetProgramiv(program, GL_LINK_STATUS, C.byref(ok))
if not ok.value:
    length = C.c_int()
    glGetProgramiv(program, GL_INFO_LOG_LENGTH, C.byref(length))
    message = C.create_string_buffer(max(length.value, 1))
    glGetProgramInfoLog(program, len(message), None, message)
    raise RuntimeError(message.value.decode(errors="replace"))
glUseProgram(program)

vertices = (C.c_float * 8)(-1, -1, 1, -1, -1, 1, 1, 1)
vao = C.c_uint()
vbo = C.c_uint()
glGenVertexArrays(1, C.byref(vao))
glBindVertexArray(vao)
glGenBuffers(1, C.byref(vbo))
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, C.sizeof(vertices), C.cast(vertices, C.c_void_p), GL_STATIC_DRAW)
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)


def uniform(name):
    return glGetUniformLocation(program, name.encode())


locations = {name: uniform(name) for name in (
    "u_center", "u_half_height", "u_aspect", "u_resolution",
    "u_zero_count", "u_pole_count", "u_zeros", "u_poles",
)}
glUniform2f(locations["u_center"], 0.0, 0.0)
glUniform1f(locations["u_half_height"], 1.35)
glUniform1f(locations["u_aspect"], 1.0)
glUniform2f(locations["u_resolution"], W, H)
glUniform1i(locations["u_zero_count"], 4)
glUniform1i(locations["u_pole_count"], 0)
glViewport(0, 0, W, H)

ffmpeg = subprocess.Popen([
    "ffmpeg", "-y", "-loglevel", "error",
    "-f", "rawvideo", "-pixel_format", "rgba",
    "-video_size", f"{W}x{H}", "-framerate", str(FPS), "-i", "-",
    "-vf", "vflip", "-an", "-c:v", "libx264", "-preset", "veryfast",
    "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUT),
], stdin=subprocess.PIPE)

pixels = (C.c_ubyte * (W * H * 4))()
zeros = (C.c_float * 8)()
for frame in range(FRAMES):
    theta = 2.0 * math.pi * frame / FRAMES
    cosine = math.cos(theta)
    sine = math.sin(theta)
    values = (1.0, 0.0, -1.0, 0.0, cosine, sine, -cosine, -sine)
    for index, value in enumerate(values):
        zeros[index] = value
    glUniform2fv(locations["u_zeros"], 4, zeros)
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
    glFinish()
    glReadPixels(0, 0, W, H, GL_RGBA, GL_UNSIGNED_BYTE, pixels)
    ffmpeg.stdin.write(bytes(pixels))

ffmpeg.stdin.close()
if ffmpeg.wait():
    raise SystemExit("ffmpeg failed")

eglMakeCurrent(display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT)
eglDestroySurface(display, surface)
eglDestroyContext(display, context)
eglTerminate(display)
print(OUT)
