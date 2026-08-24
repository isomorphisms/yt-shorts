# Undergraduate Algebraic Geometry

**Miles Reid**, *Undergraduate Algebraic Geometry*, LMS Student Texts 12, Cambridge University Press (1988).

Primary bibliographic entry: https://mreid.warwick.ac.uk/Personal/works

Cambridge contents page: https://www.cambridge.org/core/books/abs/undergraduate-algebraic-geometry/contents/916690500E360CCA5652923CE927F26E

Status for this note: **contents-read**, with portions of the online text inspected. Reid describes the book as a self-contained undergraduate introduction and deliberately mixes concrete calculations with a small amount of general theory.

The useful feature for Shorts is that the book is already broken into many small geometric claims and examples.

## 0. Woffle

Concept atoms:

- What an algebraic variety is: a locus cut out by polynomial equations.
- The same polynomial locus can be studied from number theory, topology, singularity theory, or geometry.
- **Specific calculation versus general theory**: explicit tricks work beautifully in small examples, while general theory becomes necessary as complexity grows.
- Why algebraic geometry privileges polynomial and rational functions instead of arbitrary continuous or smooth functions.
- “Geometry from polynomials”: the equation is not merely notation; its algebra carries geometric information.
- Different categories of geometry correspond to different allowed function classes.

This introductory material is useful for explaining why algebraic geometry feels simultaneously visual and algebraic.

## I. Playing with plane curves

### 1. Plane conics

Sections in Reid's contents include parametrised curves, conics over the reals, the projective plane, equations of conics, classification, parametrisation, easy cases of Bézout, pencils of conics and intersections of conics.

Small ideas worth preserving separately:

- Parametrising a conic by drawing lines through a known point.
- Why a smooth projective conic with a point behaves like a projective line.
- How the projective plane adds a “line at infinity”.
- Asymptotic directions becoming actual points at infinity.
- Classifying projective conics by coordinate change.
- Homogeneous coordinates as a way to make infinity algebraic rather than exceptional.
- Bézout in the easiest visible cases: a line meets a degree-`d` curve in `d` points when multiplicity and complex/projective points are counted correctly.
- A conic is determined by five general points.
- The **space of all conics** is itself a projective parameter space.
- A pencil of conics through common points.
- Degenerate conics appearing as special members of a pencil.
- Two conics meeting in four points as the first strong visual taste of Bézout.

### 2. Cubics and the group law

This chapter is exceptionally dense with reusable ideas.

- Examples of parametrised cubic curves.
- A smooth cubic such as `y² = x(x-1)(x-λ)` is not rationally parametrised in the same way as a conic.
- Linear systems of plane curves through prescribed points.
- Cubics through eight general points form a pencil.
- **The ninth-point phenomenon**: if two cubics meet in nine points, a cubic constrained through eight of the common points is forced through the ninth in the relevant setup.
- The chord-and-tangent construction of the group law on a nonsingular cubic.
- Why associativity is the non-obvious part of the elliptic-curve group law.
- Continuity arguments in algebraic geometry.
- **Pascal's mystic hexagon** as a relation among six points on a conic.
- Inflexion points and normal forms of cubics.
- How choosing an inflexion as identity simplifies the group law.
- The topology of a nonsingular complex cubic.
- Genus as the invariant distinguishing a conic from a smooth cubic at a deeper level.
- Reid's bridge from genus to topology, differential geometry, moduli, number theory and Mordell–Weil/Faltings.

## II. The category of affine varieties

### 3. Affine varieties and the Nullstellensatz

Concept atoms:

- Noetherian rings: ascending chains eventually stop.
- Hilbert's Basis Theorem: polynomial rings over Noetherian rings remain Noetherian.
- The `V` operation: equations produce geometric zero sets.
- The `I` operation: geometric sets produce ideals of functions vanishing on them.
- Zariski topology: algebraic sets are closed.
- Irreducible algebraic sets: geometry that cannot be split into two smaller closed pieces.
- Radical ideals and why repeated powers of equations do not change the ordinary zero set.
- Hilbert's Nullstellensatz as the dictionary between algebraic sets and radical ideals over an algebraically closed field.
- Finite algebras.
- Noether normalisation: an affine variety is finite over an affine space of the same dimension.
- Reduction to a hypersurface.

A particularly useful explanatory thread is the gradual sharpening of the slogan **geometry ↔ ideals**.

### 4. Functions on varieties

- The coordinate ring `k[V]` as the algebra of polynomial functions on an affine variety.
- Algebraic subsets of a variety encoded by ideals in its coordinate ring.
- Polynomial maps and their pullback maps on functions.
- Isomorphisms of affine varieties seen contravariantly through coordinate rings.
- The function field `k(V)`.
- Rational functions are only partially defined.
- Rational maps and their domains of definition.
- Dominant rational maps and embeddings of function fields in the opposite direction.
- Why composition of rational maps needs care.
- Standard open sets.
- The elliptic-curve addition law as a morphism rather than merely a pointwise trick.

## III. Applications

### 5. Projective and birational geometry

- Why affine space is sometimes too small: projective completion prevents points from “escaping to infinity”.
- Graded rings and homogeneous ideals.
- Projective versions of the `V`–`I` correspondence and Nullstellensatz.
- Rational functions on projective varieties.
- Covering projective varieties by affine charts.
- Rational maps versus everywhere-defined morphisms.
- Quadric surfaces and the Veronese surface as concrete examples.
- Birational maps: two varieties can agree on dense open pieces without being isomorphic everywhere.
- Rational varieties.
- Every variety being birational to a hypersurface in an appropriate sense.
- Products of varieties.

### 6. Tangent space, nonsingularity and dimension

- The Jacobian/implicit-function viewpoint on nonsingular points of a hypersurface.
- Nonsingular points are dense.
- Tangent space defined algebraically.
- Tangent-space dimension can jump upward at special points.
- Generic tangent-space dimension equals the dimension of the variety.
- `dim V = tr.deg k(V)` — geometric dimension equals transcendence degree of the function field.
- Tangent space is intrinsic, not an artefact of a chosen embedding.
- Blowup as a worked example.
- Resolution of singularities by replacing a bad point with geometric information about directions through it.

### 7. The 27 lines on a cubic surface

This is one of the strongest self-contained visual clusters in the book.

- Every nonsingular cubic surface contains a line.
- Once one line is known, study the lines meeting it.
- Five pairs of lines meet a given line in the classical configuration.
- Finding two disjoint lines.
- Producing all 27 lines.
- The incidence configuration of the 27 lines.
- Rationality of the cubic surface.
- Polar forms and elimination in the existence proof.
- The Hessian as an associated construction.

The number **27** should not be presented as a disconnected curiosity; Reid's chapter gives a path showing how the entire configuration emerges.

### 8. Final comments

Reid closes with unusually useful meta-mathematical material:

- prehistory of algebraic geometry;
- the first wave of rigour;
- the Grothendieck era;
- the postwar “big bang” of abstraction;
- computation versus theory;
- real versus complex geometry;
- regular functions and sheaves;
- why projective algebraic geometry is surprisingly sufficient for many purposes;
- affine varieties versus schemes;
- what additional information schemes keep that ordinary point sets lose.

These should be treated as Reid's perspective/history rather than neutral historical fact unless independently sourced.

## Source notes

- Reid's own list of works identifies the book as item 17: https://mreid.warwick.ac.uk/Personal/works
- Cambridge's contents page confirms the large-scale structure: `0 Woffle`, Part I plane curves, Part II affine varieties, Part III applications.
- Reid's Warwick course page also treats this book as the baseline undergraduate text: https://mreid.warwick.ac.uk/MA4A5/

## Good cross-links inside the Reid folder

- The cubic-surface material reappears at a more advanced level in *Chapters on Algebraic Surfaces*.
- Blowups and singularities lead naturally into the Du Val and cyclic quotient notes.
- Cubics and the group law connect to Reid's elliptic-curve teaching.
- Graded rings in projective geometry lead into Reid's later work on Fano varieties and unprojection.
