# Storyboard: periodic Wegert plane → torus

Status: design only. Do not render this yet.

Parent shot: `isomorphisms/yt-shorts#3`  
Manimi capability blocker: `isomorphisms/yt-shorts#4`  
Wegert coloring seam: `isomorphisms/wegert#19`  
First real Ithon/Manimi render: `isomorphisms/ithon#4`

## Mathematical guardrail

Do **not** make the existing raw `z`-plane render of

`w = sqrt((z^2 - 1)(z^2 - k^2))`

look periodic by simply tiling it. That function on the `z`-plane is multivalued and its raw Wegert picture is not the lattice-periodic plane required by this shot.

The repeating plane in this storyboard is the **uniformizing `u`-plane** of the compactified curve

`w^2 = (z^2 - 1)(z^2 - k^2)`.

Choose the Abelian coordinate schematically by

`u = ∫ dz / w`.

After inversion, `z(u)` and `w(u)` are elliptic functions with a period lattice

`Λ = <ω1, ω2>`.

The Wegert coloring used in this shot must therefore be the same coloring evaluated on a single-valued elliptic function on the `u`-plane (for example the pulled-back `w(u)`), so translation by either period really does reproduce the picture. The embedded torus must carry those same `u mod Λ` texture coordinates.

This is the whole point of the transition: the repeated plane is not decoration; it is the universal cover, and quotienting by the period lattice gives the torus.

## Sequence

Timing is provisional. Aim for roughly 20–30 seconds; shorten by cutting holds rather than skipping the quotient steps.

### 1. Start close on the colored `u`-plane — 0:00–0:03

- Full vertical frame is Wegert coloring with no lattice drawn yet.
- Camera is close enough that the viewer does not immediately read it as a tiled pattern.
- No motion except a very slight drift if the frame feels dead.
- This asset begins after the paper/equation shot; do not spend time reintroducing the equation here.

### 2. Zoom out and let the repetition reveal itself — 0:03–0:08

- Camera pulls steadily back.
- Identical translated patches become visible naturally.
- Do not flash a grid immediately; give the eye about a second to notice repetition first.
- The texture itself stays fixed in mathematical coordinates while the camera changes scale.

Visual claim: **the plane repeats by translations.**

### 3. Sketch the period lattice over the zoomed-out plane — 0:08–0:11

- Draw one lattice vector `ω1` from the origin.
- Draw the second vector `ω2`.
- Extend faint copies to a rank-2 lattice / parallelogram tiling.
- Lattice lines should be subordinate to the Wegert coloring, not replace it.

Optional minimal label: `Λ = <ω1, ω2>`.

### 4. Pick one fundamental parallelogram — 0:11–0:14

- Brighten one cell.
- Fade surrounding lattice cells slightly without changing their texture.
- Keep enough neighboring copies visible that it is obvious the selected cell is one repeat among many.

Visual claim: **one cell contains all distinct points modulo the lattice.**

### 5. Mark the edge identifications — 0:14–0:17

- Mark one pair of opposite edges with the same cue.
- Mark the other pair with a second cue.
- Small arrows may show matching orientation.
- Do not yet distort the cell.

The correspondence must be tied to texture coordinates: matching points on opposite edges are the same point after quotienting.

### 6. First quotient: parallelogram → cylinder — 0:17–0:21

Preferred version:

- Lift the selected cell away from the faded copies.
- Bend it in 3-space so the first marked edge pair approaches and meets.
- Preserve the Wegert texture continuously during the bend.
- When the edges meet, the seam should disappear or become nearly invisible.

Fallback if Manimi cannot yet perform the continuous textured bend cleanly:

- cut from the flat cell to a textured cylinder with the exact same UV correspondence;
- briefly leave the matched-edge cue visible so the cut still reads as gluing, not teleportation.

Visual claim: **identifying one period makes a cylinder.**

### 7. Second quotient: cylinder → embedded torus — 0:21–0:26

- Bend the cylinder until its remaining boundary circles meet.
- Keep the texture locked to the same `(u,v)` coordinates throughout.
- Join the circles to form the ordinary embedded donut-shaped torus in 3-space.
- The geometry is only an embedding for visualization; the intrinsic quotient is `C / Λ`.

Visual claim: **identifying the second period closes the cylinder into a torus.**

### 8. Hold and rotate the finished torus — 0:26–0:30

- Slow three-quarter rotation, enough to read the hole and the continuous texture.
- Fade the lattice plane completely if it has not already disappeared.
- Optional very small final label: `C / Λ`.
- Do not cover the final torus with explanatory text.

## Continuity rules

1. The Wegert coloring is one mathematical texture throughout: universal-cover plane, selected cell, cylinder, torus.
2. No fake repetition of the raw `z`-plane render.
3. Camera zoom is separate from lattice scaling; mathematical lattice vectors remain fixed in the scene.
4. Opposite-edge markers refer to actual UV identifications and must stay consistent through the wrap.
5. If a continuous deform causes texture swimming, prefer a clean cut with exact UV continuity.
6. The torus is an embedded visualization of the quotient, not a claim that the original `z`-plane is physically rolled into a donut.

## Scene assets / interfaces needed

- elliptic-uniformization data for the chosen `k`: period basis `ω1, ω2` and a way to evaluate a single-valued elliptic `z(u)` or `w(u)`;
- renderer-independent Wegert color evaluator (`wegert#19`);
- repeated textured plane whose domain is parameterized by `u`;
- lattice overlay and highlighted fundamental parallelogram;
- texture-coordinate-preserving flat → cylinder → torus geometry (`yt-shorts#4`);
- camera zoom and later 3D orbit;
- Ithon path to a real Manimi frame (`ithon#4`) before this is called Ithon-native.

## Not decided yet

- which fixed value of `k` gives the clearest lattice and coloring;
- whether to color `z(u)`, `w(u)`, or another elliptic quantity derived from the same curve;
- continuous roll for both gluings versus one or two editorial cuts;
- narration. The visual logic should work without narration first.
