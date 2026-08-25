# Essential directions

First Manimi production slice for Gromov's 1981 paper *Curvature, diameter and Betti numbers*.

## Source

- M. Gromov, *Commentarii Mathematici Helvetici* 56 (1981), 179–195.
- Author-hosted PDF: https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/332.pdf
- Primary locations: §1.4, printed p. 184; §1.5, printed p. 184; §3.1, printed pp. 189–190.

The PDF is linked, not vendored. The Short redraws the mathematics rather than copying the scan.

## Mathematical contract

This episode illustrates one bottleneck in the proof. It does **not** claim to prove the Betti-number theorem in full.

1. Fix a basepoint `x`.
2. For two critical points of `dist_x`, if the farther point is at least twice as far from `x` as the nearer point, §1.4 proves that the angle between chosen minimizing segments at `x` is greater than `1/6` radian.
3. §1.5.A uses the elementary finite-dimensional packing fact that only finitely many nonzero vectors in `R^n` can be pairwise separated by a fixed positive angle; Gromov records a deliberately crude dimension-only bound `< (100)^n`.
4. §3.1 reuses this mechanism for critical balls at separated scales and describes the result as bounding the number of “essential directions”.
5. Later covering and homological arguments turn that finite geometric complexity into the Betti-number bound.

The first panel uses an explicit 5° rejected angle because `5° < 1/6` radian (`1/6` radian is about 9.55°). The accepted 22° picture is likewise only a clean schematic witness, not a reconstruction of a particular Riemannian manifold.

The many-ray panel is explicitly labeled a schematic tangent-space picture. Eight widely separated rays plus one visibly colliding candidate are used to communicate finite angular packing. The scene does not pretend that eight is Gromov's bound or the sharp packing number.

The final ball cover is a visual handoff to §2 and §3. It is not a diagram copied from the paper and it does not encode the full Leray spectral-sequence step.

## Rendering boundary

The scene is Ithon source (`scene.pi`) and is rendered by `isomorphisms/manimi`, not Manim Community.

The CI consumer pins:

- Manimi: `e4f8ab7b7033052787ee7561de67b63b68ddb2dd`
- Ithon: `2e0d634550ecf2eb78315c2c165fe0e85ea1980c`
- ai-ci finished-video verifier: `1ecde1ff3bcea2de371e9198ef49aad8d1f91315`

This is intentionally a dogfood test of Manimi's current checked-Ithon boundary. Much of the engine beneath the checked `.pi` scene is still foreign Python during the staged Manimi rewrite; this episode does not claim otherwise.

The review render is 540×960, 30 fps, H.264/yuv420p, silent, and 16.366667 seconds. A later finishing pass can raise resolution after the scene itself is stable.

The workflow performs the Ithon static check before installing the renderer dependencies. The check loads Ithon's checker modules explicitly rather than putting Ithon's forked `Lib/` ahead of the host Python standard library.

## First-render inspection

The first successful render exposed presentation defects that a codec/shape check would not catch:

- the long distance-scale caption reached the right edge;
- the “essential directions” conclusion crowded the persistent curvature hypothesis;
- `Circle(color=...)` and `Dot(color=...)` did not produce the intended rendered stroke/fill colors at the pinned Manimi head.

The corrected scene shortens/repositions the affected text and uses explicit `stroke_color=` for circles and `fill_color=` for dots. The corrected render was then inspected as a contact sheet across the main beats: the captions fit, the tangent-space circle is muted rather than red, the critical points have their intended colors, and the final ball cover has distinct cyan/green/yellow circles.

## Finished-video gate

`video.contract.tsv` owns this episode's visual witnesses. They are not universal motion rules.

The exact corrected render passes 10 assertions:

- decode;
- 540×960 dimensions;
- 16.25–16.50 second duration window (actual 16.366667);
- 30 fps;
- no audio;
- H.264/yuv420p;
- rejected-angle panel → separated-angle panel changes, MAE 3.308687;
- the collision/fan beat really holds, MAE 0.326138;
- “essential directions” visibly appears, MAE 22.010281;
- the final consequence visibly appears after the cover, MAE 22.980905.

## Visual sequence

- critical points at two distance scales;
- a 5° direction rejected against the `1/6`-radian lower bound;
- a separated direction accepted;
- tangent-space angular packing;
- freeze on Gromov's phrase “essential directions”;
- handoff to a controlled cover by balls;
- `controlled directions → controlled covers → bounded Betti numbers`.

No Wegert domain coloring is used: this paper has no natural complex-valued plane plot to color.
