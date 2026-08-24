# Trevor Pearcey — animated Pearcey-integral Short

This file records the current plan for turning the April 2024 *Complex Beauties* Pearcey-integral entry into an original animated Short using the actual `isomorphisms/wegert` coloring package.

## Core question

> Why does this interference pattern have a cusp?

The featured function is the Pearcey integral

\[
\Psi_2(x,y)=\int_{-\infty}^{\infty}
\exp\!\left(i\left(t^4+y t^2+x t\right)\right)\,dt.
\]

The calendar uses this oscillatory integral to describe diffraction near a cusp caustic. The point of the Short should be to show the integral building the visible interference field, not merely to put a static formula next to a finished picture.

## Primary animation: build the integral by varying the cutoff

The main animation should vary the amount of the integration interval that has been accumulated.

Define

\[
P_T(x,y)=\int_{-T}^{T}
\exp\!\left(i\left(t^4+y t^2+x t\right)\right)\,dt.
\]

Animate `T` upward from a small value toward a sufficiently large `T_max`.

At each frame:

1. evaluate `P_T(x,y)` over the visible `(x,y)` grid;
2. obtain one complex value for every pixel/sample point;
3. feed that complex value into the actual Wegert coloring core;
4. increase `T`;
5. watch the cusp and interference structure emerge as additional oscillatory contributions enter the integral.

This is preferable to treating `t` as a parameter of a different function. `t` remains the integration variable; `T` is the animated cutoff controlling how much of the integral has been included.

### Suggested progression

The exact numerical values can change after the first real render, but a useful first sequence is:

- `T = 0.2`: nearly featureless or very broad field;
- `T = 0.5`: first large-scale structure;
- `T = 1.0`: recognizable interference begins;
- `T = 1.5`: bands become clear;
- `T = 2.0` to `3.0`: cusp structure becomes obvious;
- hold the converged-looking portrait for several seconds.

The animation should be continuous rather than jumping between those exact values; they are checkpoints for judging whether the visual development is readable.

## Show what is being integrated

A small inset can make the construction literal.

Draw a simple real `t` axis and show the active integration interval `[-T,T]`. As `T` grows, two endpoints move outward from zero. This lets the viewer see that the portrait is changing because more of the oscillatory integral is being accumulated.

Do not let the inset dominate the picture. The Wegert portrait is the main object.

## Cusp geometry

After the accumulated portrait has become recognizable, explain why a cusp appears.

The phase of the integrand is

\[
\phi(t)=t^4+y t^2+x t.
\]

Stationary points satisfy

\[
\phi'(t)=4t^3+2yt+x=0.
\]

The transition between one and three real stationary points occurs on the discriminant curve

\[
27x^2+8y^3=0.
\]

That curve is the cusp caustic.

The payoff should be visual:

- outside the cusp: one real stationary point contributes;
- inside the cusp: three real stationary points contribute;
- their interference produces the reorganized fringe pattern visible in the Pearcey field.

This should come after the viewer has already watched the integral build the pattern.

## Secondary overlay sequence

Once the field is substantially formed:

1. draw the cusp curve `27x^2 + 8y^3 = 0` as a thin white overlay;
2. optionally sweep a horizontal line `y = c` through the field;
3. show a small intensity slice

\[
I_c(x)=|\Psi_2(x,c)|^2;
\]

4. freeze at a useful value such as `y = -3` and briefly show

\[
\phi(t)=t^4-3t^2+x t
\]

with its stationary points marked;
5. return to the colored field and hold.

The cusp overlay is explanatory. It should not replace the `T`-build as the main animation.

## Suggested Short structure

### 0–4 s — let the picture appear

Start with a very small `T` and let the Wegert-colored field begin to form as `T` increases.

Minimal text:

> Pearcey integral

or

> What happens as we add more of this integral?

### 4–10 s — accumulate the integral

Continue increasing `T`.

If useful, show the small `[-T,T]` inset. The viewer should be able to watch interference bands appear and organize.

### 10–14 s — reveal the cusp

When the portrait is close to its final form, draw

\[
27x^2+8y^3=0.
\]

Question/text:

> Why this cusp?

### 14–18 s — stationary-point payoff

Show

\[
4t^3+2yt+x=0
\]

and the transition

> 1 stationary point → 3 stationary points

Then return to the completed Wegert portrait and hold long enough to inspect it.

The exact duration can change after the first real render. The important ordering is: **integral builds first, explanation second**.

## Wegert renderer boundary

Use the actual `isomorphisms/wegert` package for coloring.

Do **not** encode the Pearcey function as fake zeros and poles and do not bend the rational-function interaction model to imitate it.

The intended ownership boundary is the same one established for the Teleman render:

- this Short owns the mathematical evaluation of `P_T(x,y)` / `Psi_2(x,y)`;
- Wegert owns the phase/log-modulus-to-color mapping;
- overlays such as the cusp curve, integration interval, sweep line, and annotations belong to the Short compositor.

Each computed complex value should be passed into the reusable Wegert coloring entry point, rather than rebuilding the palette independently in the Short.

## Numerical evaluation

The infinite oscillatory integral should not be evaluated by naive brute-force real-axis quadrature for every pixel of every frame.

The calendar source notes numerical evaluation using contour deformation / steepest descent. That is the right numerical direction for a production implementation.

For an initial prototype, possible strategies are:

- evaluate on a coarser `(x,y)` grid and interpolate for preview renders;
- exploit incremental accumulation in `T` so consecutive frames reuse previous work rather than recomputing the entire integral;
- precompute the final field and a sequence of partial fields if real-time evaluation is unnecessary;
- move to contour deformation / steepest descent for the durable renderer once the visual sequence is settled.

The first engineering goal is not maximum generality. It is one reproducible Pearcey animation that uses the correct function and the correct Wegert coloring.

## First render target

A reasonable first portrait window is approximately

- `x in [-6, 6]`;
- `y in [-6, 3]`.

This should be adjusted based on where the cusp and strongest interference structure fit best in a vertical frame.

Suggested output:

- vertical 9:16;
- 1080 × 1920 final target;
- 30 fps;
- roughly 18 seconds;
- no synthetic voice required;
- preserve several seconds of relatively static viewing once the main pattern is formed.

## Visual priorities

1. The actual Wegert coloring must be recognizable and consistent with the package.
2. The viewer should see the integral accumulate rather than only seeing a finished field.
3. The cusp should emerge from the mathematics, not be decorative artwork.
4. Keep annotations thin and sparse.
5. The final portrait deserves time on screen without motion or explanatory clutter.

## Narration/text possibilities

### Preferred plain-English conceptual copy

> Geometrical optics says rays pile up at a caustic and predicts an infinite intensity there. Wave optics fixes that: the arriving waves interfere instead, giving a finite structured diffraction pattern. The Pearcey function is the canonical wave pattern that smooths a cusp singularity.

This is the current best top-down explanation: start with what physical problem the Pearcey function solves, then let the conventional formula underneath show exactly how the computation is done.

This can work entirely with text.

Possible sequence:

1. “This pattern comes from one oscillatory integral.”
2. “Add more of the integral.”
3. “A cusp appears.”
4. “Outside: one stationary point.”
5. “Inside: three.”
6. “Their interference draws the cusp.”

A question-first variant:

1. “Why does this interference pattern have a cusp?”
2. show the `T` build;
3. reveal the discriminant curve;
4. show the stationary-point transition.

## Historical point

Trevor Pearcey introduced the integral in the study of electromagnetic fields near a cusp of a caustic. The function was produced by a wave-optics problem; the elaborate visual structure is therefore tied directly to physical interference rather than being an arbitrary special-function curiosity.

Pearcey was also a computing pioneer in Australia and was closely associated with the machine later called CSIRAC. That biography can support a separate Short, but the first animation should remain centered on the function and the cusp mechanism.

## References

- Elias Wegert, Gunter Semmler, Pamela Gorkin, Ulrich Daepp, *Complex Beauties 2024*, April: Trevor Pearcey / caustics and interference.
- T. Pearcey, “The structure of an electromagnetic field in the neighbourhood of a cusp of a caustic,” *Philosophical Magazine* 37 (1946), 311–317.
- Pearcey integral — Wikipedia, as a starting index into later literature.
- Caustics / catastrophe theory for the fold-versus-cusp geometric background.

## Concept-art warning

Any image-generated Pearcey picture made during brainstorming is only concept art. It is not evidence that the mathematical field was evaluated correctly and it is not a Wegert render.

If such a draft is retained in the repository, mark it explicitly as a concept draft. The production Short should replace it with output generated from the numerical Pearcey evaluator plus the actual Wegert coloring package.
