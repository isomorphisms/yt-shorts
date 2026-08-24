#!/usr/bin/env python3
"""Render a short visual for the Mellin step in Borcherds's theta lecture.

Source: Richard E. Borcherds, "Modular forms: Theta functions",
roughly 9:29–12:41.

The visual point is the substitution u = n^2 x:

    integral exp(-pi n^2 x) x^(s/2-1) dx
      = n^(-s) integral exp(-pi u) u^(s/2-1) du
      = Gamma(s/2) pi^(-s/2) n^(-s).

For s=2 the Mellin weight is 1, so n^-2 is literally visible as the
shrinking area under the horizontally squeezed Gaussian.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

FPS = 15
SECONDS = 12
OUTPUT = Path("theta_mellin_try.mp4")
PREVIEW = Path("theta_mellin_try_preview.png")

fig = plt.figure(figsize=(5.4, 9.6), dpi=100)
gs = fig.add_gridspec(12, 1, left=.12, right=.94, top=.96, bottom=.06, hspace=.35)
ax0 = fig.add_subplot(gs[:2, 0]); ax0.axis("off")
ax1 = fig.add_subplot(gs[2:7, 0])
ax2 = fig.add_subplot(gs[7:10, 0]); ax2.axis("off")
ax3 = fig.add_subplot(gs[10:, 0]); ax3.axis("off")

ax0.text(.5, .76, "Why does Mellin give", ha="center", va="center",
         fontsize=17, weight="bold")
ax0.text(.5, .50, r"$n^{-s}$  from a theta term?", ha="center", va="center",
         fontsize=18, weight="bold")
ax0.text(.5, .15, r"$\int_0^\infty e^{-\pi n^2x}x^{s/2-1}\,dx$",
         ha="center", va="center", fontsize=18)

x = np.linspace(0, 2.2, 600)
line, = ax1.plot([], [], lw=3)
ax1.set_xlim(0, 2.2)
ax1.set_ylim(0, 1.08)
ax1.set_xlabel("x")
ax1.set_ylabel(r"$e^{-\pi n^2x}$")
ax1.set_title("One theta term")
label = ax1.text(.98, .92, "", transform=ax1.transAxes,
                 ha="right", va="top", fontsize=14)

m1 = ax2.text(.5, .76, "", ha="center", va="center", fontsize=17)
m2 = ax2.text(.5, .42, "", ha="center", va="center", fontsize=15)
m3 = ax2.text(.5, .10, "", ha="center", va="center", fontsize=13)
e1 = ax3.text(.5, .70, "", ha="center", va="center", fontsize=16, weight="bold")
e2 = ax3.text(.5, .25, "", ha="center", va="center", fontsize=13)

fill = [None]


def smooth(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)


def draw(frame):
    sec = frame / FPS

    if fill[0] is not None:
        fill[0].remove()
        fill[0] = None

    for artist in (m1, m2, m3, e1, e2):
        artist.set_text("")

    if sec < 1.2:
        y = np.exp(-np.pi * x)
        label.set_text("n = 1")
        m1.set_text("Start with one Gaussian term.")

    elif sec < 4.3:
        t = smooth((sec - 1.2) / 3.1)
        n = 1 + 2.2 * t
        y = np.exp(-np.pi * n * n * x)
        label.set_text(f"n = {n:.1f}")
        m1.set_text(r"For $s=2$, the Mellin weight is $1$.")
        m2.set_text(r"Area $=\frac{1}{\pi n^2}$")
        m3.set_text("The horizontal scale shrinks by n².")

    elif sec < 7.0:
        t = smooth((sec - 4.3) / 2.7)
        n = 3.0
        y = ((1 - t) * np.exp(-np.pi * n * n * x)
             + t * np.exp(-np.pi * x))
        label.set_text(r"$u=n^2x$")
        m1.set_text(r"Rescale:  $u=n^2x$")
        m2.set_text(r"$x^{s/2-1}dx=n^{-s}u^{s/2-1}du$")
        m3.set_text("Now every n uses the same Gaussian.")

    elif sec < 9.3:
        y = np.exp(-np.pi * x)
        label.set_text(r"$e^{-\pi u}$")
        m1.set_text(r"$\int e^{-\pi n^2x}x^{s/2-1}dx$")
        m2.set_text(r"$=n^{-s}\int e^{-\pi u}u^{s/2-1}du$")
        m3.set_text(r"$=\Gamma(s/2)\pi^{-s/2}n^{-s}$")

    else:
        y = np.exp(-np.pi * x)
        label.set_text("")
        m1.set_text("Now sum the nonzero theta terms.")
        m2.set_text(r"$\frac{1}{2}\sum_{n\ne0}n^{-s}=\zeta(s)$")
        e1.set_text("Mellin turns scale into a power.")
        e2.set_text(
            r"$\frac{1}{2}\int(\theta(ix)-1)x^{s/2-1}dx"
            r"=\Gamma(s/2)\pi^{-s/2}\zeta(s)$"
        )

    line.set_data(x, y)
    fill[0] = ax1.fill_between(x, 0, y, alpha=.12)


draw(int(8 * FPS))
fig.savefig(PREVIEW, dpi=100)

writer = FFMpegWriter(
    fps=FPS,
    codec="libx264",
    extra_args=["-pix_fmt", "yuv420p", "-movflags", "+faststart"],
)
with writer.saving(fig, str(OUTPUT), dpi=100):
    for frame in range(FPS * SECONDS):
        draw(frame)
        writer.grab_frame()

plt.close(fig)
print(OUTPUT)
