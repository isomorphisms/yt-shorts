# Minimal surfaces — Matthias Weber gallery notes

This folder is a source notebook for making **original visual Shorts about minimal surfaces**. It is not a mirror of Matthias Weber's old gallery, and it is not yet a set of video scripts.

The immediate goal is just to keep a queue of surfaces and visual experiments worth returning to.

## Source trail

The old Indiana University minimal-surfaces site survives in the Wayback Machine:

- archived site root: https://web.archive.org/web/20170604162141/http://www.indiana.edu/~minimal/index.html
- old aesthetic gallery path: http://www.indiana.edu/~minimal/gallery/index/index.html
- old mathematical archive path: http://www.indiana.edu/~minimal/archive/index.html

A contemporary description of Weber's site distinguishes the two galleries: the first put minimal surfaces into imaginary landscapes for their visual effect; the second was intended to illustrate mathematical facts and included material for numerical/visual experiments:

- https://www.sciencedaily.com/releases/2005/12/051229113035.htm

A large surviving collection of the same minimal-surface material is now available through the 3DXM Virtual Math Museum:

- https://www.virtualmathmuseum.org/Surface/gallery_m.html

Useful Weber background:

- Matthias Weber, *Classical Minimal Surfaces in Euclidean Space by Examples* (lecture notes): https://virtualmathmuseum.org/Surface/minimal_surface__matthias_weber.html
- Matthias Weber, David Hoffman, Michael Wolf, *An embedded genus-one helicoid*: https://annals.math.princeton.edu/2009/169-2/p01
- arXiv version: https://arxiv.org/abs/math/0401080

## Credit / reuse rule

Treat Weber's old site and the 3DXM pages as **sources and visual references**, not as a pool of images to copy into videos. Make our own meshes, renders, diagrams, rotations, parameter sweeps, and annotations unless the reuse terms for a specific source image are clear.

Also do not attribute every surface or every 3DXM rendering to Weber. The archive is a collection. Individual entries explicitly point to work by people including Hermann Karcher, David Hoffman, Fusheng Wei, Alan Schoen, Karsten Grosse-Brauckmann, Meinhard Wohlgemuth, and others. Preserve the per-surface attribution when a Short gets developed.

## Strong first visual candidates

### Helicoid ↔ catenoid

The 3DXM page explicitly shows a continuous associate-family deformation between a helicoid and a catenoid. The striking fact is that the surfaces in this family are isometric: intrinsic lengths do not change even though the embedding in 3-space changes radically.

Visuals to try:

- morph continuously from catenoid to helicoid;
- draw a few parameter-grid curves and keep them attached during the morph;
- mark two points and show that a surface-path length stays fixed;
- end on a side-by-side silhouette of the two apparently unrelated shapes.

Source: https://www.virtualmathmuseum.org/Surface/helicoid-catenoid/helicoid-catenoid.html

### Genus-one helicoid

Weber, Hoffman, and Wolf proved the existence of a properly embedded minimal surface with one handle and one end asymptotic to a helicoid. This is particularly good for a visual because the ordinary helicoid is immediately recognizable and the extra handle is a concrete topological change.

Visuals to try:

- start with an ordinary helicoid;
- reveal the handle near the axis;
- rotate slowly enough that the handle cannot be mistaken for a perspective overlap;
- compare a large-radius view with the ordinary helicoid to show the shared asymptotic behavior.

Sources:

- https://annals.math.princeton.edu/2009/169-2/p01
- https://arxiv.org/abs/math/0401080

### Scherk surfaces

Scherk found new nontrivial minimal surfaces in 1834 after the plane, catenoid, and helicoid had dominated the classical examples. There are singly and doubly periodic Scherk surfaces.

Visuals to try:

- begin with one fundamental patch and replicate it by translation;
- for the doubly periodic surface, reveal the checkerboard structure from above;
- rotate from the distorted top view to a horizontal view of a fundamental piece;
- show the singly periodic implicit surface inside an expanding ball;
- draw the two principal curvature circles at one point to show equal-and-opposite principal curvatures.

Source: https://www.virtualmathmuseum.org/Surface/scherk/scherk.html

### Scherk surface with a handle

This is a genus-one version of Scherk's doubly periodic surface. The archive material specifically suggests associate-family morphing as a way to see the conjugate fundamental domain and the embeddedness picture.

Visuals to try:

- compare ordinary Scherk with Scherk-with-handle;
- isolate a fundamental piece, then reflect/translate it to build the full periodic surface;
- morph through the associate family;
- later, if the period computation is made explicit, animate the parameter until the period closes.

Source: https://www.virtualmathmuseum.org/Surface/scherk_w_handle/scherk_w_handle.html

### Enneper surface and higher-order Enneper surfaces

The Enneper page already suggests several useful animations: expand the plotted domain, switch Cartesian/polar parameter grids, zoom far out, and increase the symmetry order.

Visuals to try:

- grow the parameter domain so the global self-intersecting shape emerges from a simple central patch;
- switch from Cartesian to polar grid lines to make the symmetry visible;
- compare the ordinary Enneper surface with 3-fold, 6-fold, and higher-order versions;
- put principal curvature circles on a point;
- use the far-away description as a separate animation rather than trying to explain the whole surface at once.

Source: https://www.virtualmathmuseum.org/Surface/enneper/enneper.html

Related queue: Double Enneper, Wavy Enneper, Planar Enneper, Catenoid-Enneper.

### Riemann's minimal examples

These look like families of parallel planes joined by necks/handles. The archive material also has an associate-family morph.

Visuals to try:

- begin with apparently separate parallel planes and reveal the connecting handles;
- translate the camera by one period to make the periodicity obvious;
- highlight the straight lines and 180-degree rotational symmetries;
- animate the associate family and watch catenoid-like necks turn into helicoid-like pieces.

Source: https://www.virtualmathmuseum.org/Surface/riemann/riemann.html

### Costa and Costa–Hoffman–Meeks surfaces

Costa's surface is a natural gateway to finite-total-curvature embedded surfaces with nonzero genus. Costa–Hoffman–Meeks gives a family where genus and dihedral symmetry grow.

Visuals to try:

- rotate the Costa surface with ends separately marked;
- show a sequence of Costa–Hoffman–Meeks examples as the symmetry/genus parameter increases;
- isolate a fundamental region, then replicate it by symmetry.

Sources:

- https://www.virtualmathmuseum.org/Surface/costa/costa.html
- https://virtualmathmuseum.org/Surface/costa-h-m/costa-h-m.html

### Chen–Gackstatter / handle addition

The Chen–Gackstatter material is especially useful for showing a period problem visually. The archived description says the morph indicates how a period closes for one parameter value by an intermediate-value argument.

Visuals to try:

- sweep the parameter through under-closed → closed → over-closed configurations;
- freeze at the closing value;
- compare the surface with Enneper to make the added handle/topology visible.

Source: https://virtualmathmuseum.org/Surface/chen_gackstatter/chen_gackstatter.html

### Schwarz P/D family → gyroid

The Schwarz PD page describes a two-parameter family of triply periodic genus-3 surfaces. The P and D surfaces sit in an associate family containing Schoen's gyroid.

Visuals to try:

- show one fundamental patch inside a brick/cell, then reflect it until space fills;
- morph P → intermediate associate surfaces → gyroid → D;
- keep the lattice cell visible while the surface changes;
- use a cutaway or transparency to show the two labyrinthine sides of a gyroid.

Sources:

- https://www.virtualmathmuseum.org/Surface/schwarz_pd_family/schwarz_pd_family.html
- https://www.virtualmathmuseum.org/Surface/gyroid/gyroid.html

### Gyroid by itself

The gyroid page already contains excellent animation prompts: build the surface by adding hexagonal pieces, rotate through special symmetry directions, and show the 3-fold rotational symmetry around a central hexagon. It also gives a connection to materials science: gyroid geometry occurs as interfaces in polymer systems.

Visuals to try:

- build one fundamental cell piece by piece;
- rotate into the 3-fold symmetry view and stop there;
- mark translation vectors;
- show a single channel and then the complementary channel;
- make a separate materials-science Short only after finding a good primary source for the physical example.

Source: https://www.virtualmathmuseum.org/Surface/gyroid/gyroid.html

### Schwarz H family → Lidinoid

The Schwarz H family can be thought of as being built from "triangular catenoids" spanning pairs of parallel equilateral triangles. The Lidinoid lies in an associate family of one of these H surfaces.

Visuals to try:

- start with two triangular boundary curves and grow the minimal annulus between them;
- replicate the patch to form the triply periodic H surface;
- morph the H surface into the Lidinoid while keeping the translation cell visible;
- on the Lidinoid, build up the curved-hexagon structure and mark 120-degree rotational symmetry.

Sources:

- https://www.virtualmathmuseum.org/Surface/schwarz_h_family/schwarz_h_family.html
- https://www.virtualmathmuseum.org/Surface/lidinoid/lidinoid.html

### Saddle towers and twisted Scherk surfaces

These are good candidates for parameter animations because the number and arrangement of ends can be made visually explicit.

Visuals to try:

- vary the number of saddle-tower wings;
- replicate a fundamental piece along the periodic direction;
- for twisted Scherk examples, animate increasing twist/number of ends and compare limiting helicoid-like behavior where appropriate.

Sources:

- https://virtualmathmuseum.org/Surface/karcher_jd_st/karcher_jd_st.html
- https://virtualmathmuseum.org/Surface/twisted_scherk/twisted_scherk.html

### Neovius and Schoen triply periodic families

The surviving pages have less exposition, but they show fundamental regions and belong naturally with the triply periodic sequence.

Visuals to try:

- highlight one fundamental region;
- replicate it by symmetry to fill a cell and then a larger block;
- compare cubic, hexagonal, and other lattice organization across the families.

Sources:

- https://www.virtualmathmuseum.org/Surface/neovius/neovius.html
- https://www.virtualmathmuseum.org/Surface/schoen_ss/schoen_ss.html
- https://www.virtualmathmuseum.org/Surface/schoen_ht_hex/schoen_ht_hex.html
- https://www.virtualmathmuseum.org/Surface/schoen_tw/schoen_tw.html

### Fujimori–Weber

Keep this in the queue, but the current 3DXM page is mostly an image/animation index with very little accompanying text. Before designing a mathematical Short, follow the linked PDF and identify the exact family, parameters, and attribution.

Source: https://www.virtualmathmuseum.org/Surface/fujimori_weber/fujimori_weber.html

## Broader gallery queue

The surviving 3DXM index is useful as a checklist for later passes.

**Classical**

- Catenoid
- Helicoid–Catenoid
- Scherk surface
- Henneberg surface
- Catalan surface
- Enneper surface
- Riemann's surface

**Punctured sphere**

- Double Enneper
- Wavy Enneper
- Planar Enneper
- Catenoid–Enneper
- Symmetric 4-noid
- Skew 4-noid
- Saddle tower
- Twisted Scherk
- López–Ros no-go theorem
- Catenoid chain
- Inverted Boy
- Kusner

**Punctured torus**

- Chen–Gackstatter
- Costa surface
- Catenoid fence
- Schoen no-go theorem
- Catenoid field
- Karcher JE saddle tower
- Karcher JD saddle tower
- Scherk with handle
- Costa–Hoffman–Meeks surface

**Triply periodic**

- Schwarz H family
- Lidinoid
- Schwarz PD family
- Gyroid
- Neovius
- Schoen S-S family
- Schoen HT hexagonal family
- Schoen TW family
- Fujimori–Weber

Index: https://www.virtualmathmuseum.org/Surface/gallery_m.html

## Reusable visual vocabulary for this folder

A lot of these surfaces can be turned into Shorts without inventing a story around them. Reuse a small number of mathematically meaningful operations:

- **rotate** a static surface slowly enough to understand the topology;
- **grow the parameter domain** to reveal ends and self-intersections;
- **build from a fundamental patch** by reflections/translations;
- **show the lattice cell** for periodic surfaces;
- **morph an associate family** while retaining grid curves or marked points;
- **vary one construction parameter** and stop at the special value where a period closes;
- **mark symmetry axes/planes/points** and actually perform the symmetry;
- **draw principal curvature circles** at one or two points;
- **compare topology** by adding a handle or changing the number of ends;
- **zoom far out** to show asymptotic behavior.

For this folder, those geometric actions are the content. Do not clutter them with generic biography or narration unless a person/history fact explains what the viewer is seeing.
