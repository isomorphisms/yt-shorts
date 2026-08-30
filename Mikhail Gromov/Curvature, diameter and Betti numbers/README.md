# Curvature, diameter and Betti numbers

Michael Gromov, **“Curvature, diameter and Betti numbers,”** *Commentarii Mathematici Helvetici* **56** (1981), 179–195.

- Author-hosted paper page: https://www.ihes.fr/~gromov/distancegeometry/101/
- Author-hosted PDF: https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/332.pdf
- DOI: https://doi.org/10.1007/BF02566208
- E-Periodica record: https://www.e-periodica.ch/cntmng?pid=com-001%3A1981%3A56%3A%3A20

## Source and reuse boundary

Use the author-hosted PDF as the reading/citation source, but do **not** vendor the PDF into this repository. The scan itself carries a 1981 Birkhäuser copyright notice. E-Periodica likewise says that the digitized journal rights generally remain with the publisher or other rights holders and that republication of images requires permission. Link to the source; redraw mathematical diagrams from the underlying ideas rather than copying page images into the Short.

The paper appears to contain no numbered geometric figures. The appendix does contain a small commutative algebra diagram. For animation purposes this is useful: the visual language can be designed from the mathematics rather than imitating an existing illustration.

## What the paper is trying to prove

Fix the dimension. Gromov proves that a lower sectional-curvature bound together with a diameter bound limits how complicated the topology of a compact Riemannian manifold can be, as measured by the sum of its Betti numbers. In the nonnegative-curvature case the bound depends only on dimension.

The useful conceptual chain for a Short is

**curvature → triangle comparison → separated directions → controlled ball coverings → controlled homology → bounded Betti numbers.**

This is much more visual than the theorem statement first suggests.

## Section-by-section reading notes

### §0. Introduction

#### 0.1 Sectional curvature

Gromov starts by giving sectional curvature a metric meaning rather than beginning with tensors. Near a point, nonnegative curvature can be expressed by comparing the manifold with a Euclidean ball through the exponential map: distances in the manifold do not exceed the corresponding Euclidean distances. For a general lower curvature bound, the comparison model is a sphere or hyperbolic space of constant curvature.

**Visual use:** put the same small triangle in flat, positively curved, and negatively curved model spaces and show how the comparison changes its opposite side. This is background, not yet the main Short.

#### 0.2 Estimates for Betti numbers

This states the target. For a compact connected \(n\)-manifold of nonnegative sectional curvature, the total Betti number is bounded by a constant depending only on \(n\). With sectional curvature bounded below by \(-\kappa^2\), the bound also depends on the scale-free product \(\kappa D\), where \(D\) is diameter.

The point is not that Gromov obtains a sharp numerical constant; he explicitly notes that the estimates are far from the expected optimum. The point is that metric constraints force a finite topological-complexity bound at all.

**Visual use:** this is the closing statement. Do not open the video with a giant Betti-number inequality.

### §1. Distance function

#### 1.1 Critical points

Fix \(x\in V\) and look at the distance function \(d_x(y)=d(x,y)\). It is not smooth everywhere, but Gromov uses a Morse-theory-like notion of a critical point. If an annular region between two concentric balls contains no critical points, the isotopy lemma says that the larger ball can be pushed into the smaller one without changing anything outside the region.

This is the first topology bridge: **if no critical event occurs while the radius changes, no new topological complication is forced.**

**Visual use:** an expanding distance circle/ball passes through ordinary regions smoothly; a marked critical radius is where the animation is allowed to change topology.

#### 1.2 Comparison theorems

Toponogov comparison controls a triangle in the manifold by a triangle in a constant-curvature model. In the nonnegative-curvature case, the side opposite a given angle is no longer than the Euclidean comparison side. Gromov immediately extracts two deliberately crude special cases; these are the versions he actually needs later.

**Equation purpose:** Toponogov is not decorative curvature theory here. It turns a lower curvature bound into inequalities between three distances and an angle, which can then constrain how different critical directions may coexist.

**Visual use:** this is an excellent animated beat: draw a triangle, pin the two radial lengths and included angle, and compare the third side with the Euclidean model.

#### 1.3 An inequality for a critical point

For a critical point \(y\) of the distance from \(x\), a sufficiently remote point \(z\) cannot sit in an arbitrary metric configuration with \(x\) and \(y\). The critical-point condition gives a minimizing geodesic making an angle at most \(\pi/2\), and Toponogov converts that angle statement into a distance inequality.

**Equation purpose:** this packages “critical point + curvature comparison” into a reusable distance estimate. Section 1.4 then applies it twice rather than redoing the geometric argument.

#### 1.4 An inequality for two critical points

Take two critical points for the same basepoint \(x\), with one at least twice as far from \(x\) as the other. Their minimizing directions at \(x\) must have a definite angular separation. If the angle were too small, the comparison inequalities from 1.2 and the critical-point inequality from 1.3 would contradict one another.

This is one of the best pieces of the paper for animation.

**Visual use:** place \(x\) in the center, put critical points at geometrically separated radii, and draw the minimizing rays. Attempt to squeeze two rays together; the relevant distance bounds collide and the configuration is rejected.

#### 1.5 Noncompact manifolds

Gromov inserts a simple Euclidean packing fact: in \(\mathbb R^n\), only finitely many nonzero vectors can have every pair separated by a fixed positive angle. Combining that with 1.4 shows that the critical points of \(d_x\) on a complete nonnegatively curved manifold cannot continue outward through infinitely many well-separated distance scales. They are confined to a compact region.

The corollary is finite topological type for the noncompact manifold.

**Visual use:** this is the clearest “why finiteness appears” moment. Pack rays around a point. Once every pair needs a minimum angle, there is simply no room for arbitrarily many essential directions.

### §2. Coverings by balls

#### 2.1 Volumes of balls

Volume comparison gives bounds on the ratio of volumes of balls. In nonnegative curvature this resembles the familiar Euclidean power law; with a negative lower curvature bound the comparison uses hyperbolic balls.

**Equation purpose:** the volume inequalities become counting inequalities. If many small balls are disjoint inside a larger controlled ball, their total volume cannot exceed the volume available.

**Visual use:** fill a large disk/ball with disjoint smaller ones, then enlarge them until they cover. Curvature controls how many can fit.

#### 2.2 Minimal coverings

Gromov constructs a maximal separated set of centers. The corresponding small balls cover the desired region, while half-sized balls around the same centers are disjoint. Volume comparison therefore bounds the number of balls and, more importantly, the combinatorial complexity of their intersections.

He calls the number of nonempty multiple intersections the **index** of the covering.

**Visual use:** this is almost tailor-made for animation. First scatter centers with a minimum separation, then draw the disjoint half-balls, then grow them into a cover, then highlight pair/triple intersections.

#### 2.3 Topological lemma

Gromov defines the **content** of a ball using the rank of an inclusion map on total homology. For the whole manifold, this content becomes the sum of the Betti numbers. A covering with bounded intersection complexity and bounded local content gives a bound on the content of the larger ball.

Leray’s spectral sequence is the algebraic mechanism behind this step; its details are deferred to the appendix.

**Equation purpose:** this is where a combinatorial bound on the cover is converted into a homological bound.

**Visual use:** circles/balls and their overlap nerve can carry this explanation. The spectral sequence itself should probably not be the first Short.

#### 2.4 Main covering lemmas

The volume/counting results of 2.1–2.2 and the topological lemma of 2.3 are bundled into reusable statements. If sufficiently small balls have bounded content, then a larger ball has bounded content; for a compact manifold of controlled diameter and curvature the same mechanism controls the whole manifold.

**Equation purpose:** these lemmas are the induction engine. They turn a local homology bound into a larger-scale homology bound with a dimension-dependent multiplicative cost.

### §3. Proof of the theorems 0.2.A and 0.2.B

#### 3.1 Rank and corank

Gromov defines special critical balls at separated radii and then defines the **corank** of a set by how many such scales can coexist while their enlarged balls still contain that set. The key proposition bounds corank by a number depending only on dimension.

Gromov’s own summary is that this bounds the number of **“essential directions”** in the manifold. That phrase is the best organizing sentence for a Short.

The proof returns to the angle-packing argument from §1: too many critical scales would produce too many geodesic directions, forcing two directions too close together, contradicting the critical-point comparison inequality.

**Visual use:** nested scales plus rays. This can be the central sequence of the first Short.

#### 3.2 Inductive lemmas

Rank is defined from the maximum possible corank. Rank-zero balls have no critical point of the relevant kind, so the isotopy lemma makes them topologically simple and their content is one. Let \(P_k\) be a bound on the content of balls of rank at most \(k\). Gromov proves a recurrence of the form

\(P_{k+1}\le (n+1)J P_k.\)

Because the rank can increase only finitely many times, iterating this recurrence yields a finite bound for the content of the whole manifold, hence for the total Betti number.

**Equation purpose:** this recurrence is the final bookkeeping step. All the geometry has been compressed into two facts: only finitely many ranks exist, and each increase in rank costs only a controlled multiplicative factor.

#### 3.3 Incompressible balls

A ball is called compressible when its relevant inner portion can be isotoped into a much smaller ball inside it. Every ball contains an incompressible ball carrying at least as much content. For an incompressible ball, failure of such a compression forces a critical point of an appropriate distance function. Adding the corresponding critical ball lowers rank on the smaller pieces, so the covering lemma and induction apply.

**Visual use:** a ball tries to squeeze into a smaller ball. If it can, no new complexity is needed; if it cannot, a critical point must appear. That critical point is exactly what allows the rank induction to proceed.

### Appendix: Leray spectral sequence

The appendix supplies the algebra behind §2.3. It reviews filtered and graded vector spaces, proves a rank inequality for a composition of filtered maps, then recalls the Leray spectral sequence for a cover. The stable page recovers the graded object associated with homology of the union, allowing ranks of homology maps for the whole covered space to be bounded by ranks coming from intersections of the covering sets.

There is a small commutative diagram in this appendix, but no geometric figure that needs to be reproduced.

**Visual use:** probably a later, more algebraic Short. For the first video it is enough to say that controlled overlaps prevent the cover from hiding arbitrary homology.

## Equation-purpose map

The paper’s important equations can be read as a sequence of jobs rather than as isolated formulas:

1. **0.2.A / 0.2.B:** state the final topological bound to be proved.
2. **1.2:** turn curvature into triangle-side inequalities via Toponogov.
3. **1.3:** turn “critical point” into a reusable distance inequality.
4. **1.4:** turn two critical points at separated scales into a lower bound on their angular separation.
5. **1.5.A:** turn angular separation into a finite packing bound in \(n\) dimensions.
6. **2.1:** turn curvature into ball-volume comparison.
7. **2.2:** turn volume comparison into a finite bound on the number and intersection pattern of covering balls.
8. **2.3 / 2.4:** turn bounded covering complexity into bounded homological content.
9. **3.1:** turn the angle-packing bound into finitely many essential critical directions/scales.
10. **3.2:** iterate a controlled recurrence across those finitely many ranks to obtain the Betti-number bound.
11. **Appendix:** justify the cover-to-homology rank estimate with filtered homology and Leray’s spectral sequence.

## First Short: recommended visual argument

Do not try to prove the full theorem in 20 seconds. Animate the geometric bottleneck that makes the theorem plausible.

1. Put a basepoint \(x\) on screen.
2. Add critical points at increasingly separated distance scales.
3. Draw minimizing geodesics from \(x\) toward those points.
4. State the comparison consequence: sufficiently separated critical scales force a definite angular separation between the directions.
5. Keep adding rays until the fixed-angle packing becomes visibly impossible.
6. Freeze on: **only finitely many essential directions**.
7. Zoom outward to a controlled covering by balls.
8. End with: controlled directions → controlled covers → controlled homology → bounded Betti numbers.

This gives the viewer an actual reason curvature can constrain topology instead of merely displaying the theorem.

## Manimi status and suitability

### Is Manimi ready?

**Ready for this first production slice, but not finished as an Ithon rewrite.**

As of 2026-08-24, `isomorphisms/manimi` master at `e4f8ab7b7033052787ee7561de67b63b68ddb2dd` has a checked Ithon scene entrypoint:

```text
./bin/manimi example_scene.pi IthonCircle
```

The current master workflows **Ithon render** and **Ithon migration** both pass. The repository has already rendered a checked Ithon scene through the host runtime. However, the migration document is explicit that much of the engine is still foreign Python while modules are converted in dependency order. A `.pi` scene is checked Ithon source calling into the still-partly-Python ManimGL engine; that is not the same thing as claiming the whole renderer is Ithon-native.

For Shorts this is a useful boundary: we can start exercising Manimi with real scenes now while continuing the engine migration separately.

### Is Manimi suited to this paper?

**Yes. This paper is unusually well suited to it.** The first visual needs ordinary mathematical-animation primitives rather than a specialized scientific renderer:

- points and labels;
- circles/balls and concentric annuli;
- line/geodesic surrogates;
- angle arcs;
- transformations that grow/shrink balls;
- groups of overlapping balls;
- optional simple 3D model surfaces later.

The safest first implementation should remain mostly schematic and 2D. We do not need to numerically solve geodesic equations on an arbitrary Riemannian metric to explain the proof mechanism. A flat comparison panel, a sphere-like positive-curvature panel, and diagrammatic geodesic rays are enough to test the visual idea without pretending to compute a general manifold.

This also makes the episode a good next Manimi test: it asks for substantially more than the current single-circle smoke scene, but it does not require a brand-new renderer.

## Wegert/domain-coloring question

There is **no natural Wegert complex plot in this paper**. The argument is Riemannian metric geometry and homology, not a complex-valued function on a complex plane. The mention of complex projective spaces in the introduction does not create a domain-coloring problem.

Do not force Wegert coloring onto the mathematics. We can reuse a restrained palette derived from the Wegert project if we want visual continuity across the channel, but that would be ordinary color design, not a Wegert domain-color plot.

Good native visuals here are instead:

- triangle comparison;
- angular packing of geodesic directions;
- expanding/nested balls;
- disjoint half-balls becoming a cover;
- overlap/nerve structure;
- compression versus a forced critical point.

If a later Gromov source introduces an actual complex-valued or holomorphic map, then Wegert becomes mathematically meaningful again.
