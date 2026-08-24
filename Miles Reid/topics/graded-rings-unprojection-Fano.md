# Graded rings, unprojection, Fano construction, Ice Cream and Diptychs

Primary Reid resource pages:

- Graded rings / 3-folds: https://mreid.warwick.ac.uk/3folds/
- Ice Cream / orbifold Riemann–Roch: https://mreid.warwick.ac.uk/Ice/
- Codimension 4 Gorenstein: https://mreid.warwick.ac.uk/codim4/

This is the explicit-construction side of Reid's later work: encode a variety in a graded ring, study the ring's Gorenstein structure, and use projection/unprojection to build or relate varieties.

## Graded rings and birational geometry

Miles Reid, *Graded rings and birational geometry*: https://mreid.warwick.ac.uk/3folds/Ki/Ki.pdf

Status: **abstract-read**.

Reid starts from graded rings such as:

- canonical rings of surfaces of general type;
- graded rings over polarized K3 surfaces;
- anticanonical rings of Fano varieties.

In favorable cases these are Gorenstein rings. Small codimension has familiar algebraic models:

- codimension 1: hypersurface;
- codimension 2: complete intersection;
- codimension 3: Pfaffian constructions;
- codimension 4 and beyond: no comparably simple universal structure theorem, so projection/unprojection becomes a practical method.

Concept atoms:

- a projective variety encoded by a graded coordinate ring;
- Hilbert series as dimension data for graded pieces;
- Gorenstein symmetry;
- codimension as algebraic complexity;
- projection simplifying an embedded variety;
- unprojection reversing that simplification;
- serial unprojection building high-codimension examples step by step;
- graded-ring methods constructing Fano 3-folds and canonical surfaces;
- Sarkisov links reflected in algebraic operations on rings.

## Kustin–Miller unprojection without complexes

Stavros Papadakis and Miles Reid: https://arxiv.org/abs/math/0011094

Status: **abstract-read**.

The paper explains an inverse to Gorenstein projection. Starting from a simpler Gorenstein ring and suitable divisor data, unprojection constructs a more complicated Gorenstein ring and raises codimension by one.

Small units:

- projection lowers apparent complexity;
- unprojection restores the lost variable/data;
- del Pezzo surfaces provide a concrete model;
- codimension increases by one;
- adjunction/dualising sheaves replace the heavier complex machinery used in the original Kustin–Miller theorem;
- the construction is scheme-theoretic and not tied to one ambient affine space.

Attribution: the underlying unprojection theorem is due to Andrew Kustin and Matthew Miller; Papadakis and Reid give a reformulation/proof adapted to birational geometry.

## Type IV unprojection

Miles Reid, *Examples of Type IV unprojection*: arXiv: https://arxiv.org/abs/math/0108037

Status: **index-only**.

Keep this as a follow-up item after Kustin–Miller rather than describing details from the title alone.

## Fano 3-folds, K3 surfaces and graded rings

Selma Altınok, Gavin Brown and Miles Reid: https://arxiv.org/abs/math/0202092

Status: **index/abstract-level**.

The recurring construction pattern is:

- start with numerical data such as a Hilbert series;
- guess generator degrees/weights;
- place the variety in weighted projective space;
- construct equations using Gorenstein structure and unprojection;
- use K3 sections as a lower-dimensional testing ground for Fano 3-folds.

Credit all three authors.

## Weighted Grassmannians

Alessio Corti and Miles Reid: https://arxiv.org/abs/math/0206011

Status: **abstract-read**.

The paper develops weighted-projective analogues of homogeneous spaces such as `Gr(2,5)` and `OGr(5,10)` and uses them as ambient spaces for explicit constructions.

Concept atoms:

- ordinary Grassmannians parametrize linear subspaces;
- weighted projective geometry changes coordinate weights;
- homogeneous spaces can be given weighted analogues;
- these weighted spaces provide structured ambient varieties for K3/Fano constructions;
- Mukai-style linear-section descriptions motivate the construction.

## Constructing algebraic varieties via commutative algebra

Miles Reid: https://mreid.warwick.ac.uk/surf/ECM4.pdf

Status: **abstract-read**.

Reid's basic construction philosophy is to choose an intrinsic polarization `L`—often canonical or anticanonical—and study

`R(X,L) = ⊕ H⁰(X,L^n)`.

Concept atoms:

- geometry becomes a graded ring of sections;
- canonical/anticanonical classes determine natural projective embeddings;
- Gorenstein structure gives strong algebraic constraints;
- computer algebra becomes useful because explicit equations can be recovered from graded-ring data;
- old classification questions of Enriques/Fano are revisited with modern commutative algebra.

## Gorenstein in codimension 4

Miles Reid: https://arxiv.org/abs/1304.5248

Companion page: https://mreid.warwick.ac.uk/codim4/

Status: **resource-page read**.

The site includes slides, Magma scripts and related papers. The central problem is what structural replacement exists in codimension 4 for the clean hypersurface/complete-intersection/Pfaffian descriptions in smaller codimension.

Useful units:

- why codimension 4 is a structural threshold;
- free resolutions and Gorenstein symmetry;
- explicit equations versus abstract structure theory;
- computer algebra as part of mathematical experimentation;
- surface and Fano examples as test cases.

## Tom and Jerry

Gavin Brown, Michael Kerber and Miles Reid, *Fano 3-folds in codimension 4, Tom and Jerry, Part I*: https://arxiv.org/abs/1009.4313

Gavin Brown, Miles Reid and Jan Stevens, *Tutorial on Tom and Jerry*: https://arxiv.org/abs/1812.02594

Status: **abstract-read for the tutorial**.

Tom and Jerry are two concrete formats for codimension-4 Gorenstein unprojection.

The tutorial uses the two smoothing components of the anticanonical cone over `P(1,2,3)` as a first example.

Potential small units:

- one singular cone can have more than one smoothing component;
- two different unprojection formats can explain those two branches;
- codimension-4 equations can be organized by placing a divisor inside a Pfaffian-style codimension-3 object;
- “Tom” and “Jerry” are names for algebraic formats, not new varieties by themselves.

## Ice cream and orbifold Riemann–Roch

Anita Buckley, Miles Reid and Shengtian Zhou: https://arxiv.org/abs/1208.0457

Status: **abstract-read**.

They write the Hilbert series of a projectively Gorenstein quasismooth orbifold as a sum of pieces with matched integral/Gorenstein symmetry. The local orbifold corrections are called **ice cream functions**.

Concept atoms:

- Hilbert series packages the dimensions of all graded pieces into one rational function;
- singular orbifold points contribute correction terms;
- the correction terms can be written in a canonical integral symmetric form;
- local singularity data becomes visible in a global generating function;
- the decomposition is designed to be useful in computer algebra;
- examples include K3 surfaces and Calabi–Yau 3-folds.

Credit Buckley, Reid and Zhou.

## Diptych varieties

Gavin Brown and Miles Reid:

- Part I: https://arxiv.org/abs/1208.2446
- Part II: https://arxiv.org/abs/1208.5858

Status: **index-only** in this pass.

Keep as a future deep-read cluster connected to serial unprojection and explicit models of Mori flips. Reid's work-in-progress list also mentions Parts III and IV.

## Graded Ring Database / Kawamata bounds

Gavin Brown, Alexander Kasprzyk and Miles Reid manuscript: https://kasprzyk.work/research/pdf/grdb.pdf

Status: **abstract-read**.

The paper computes 39,550 candidate Hilbert series satisfying the relevant Kawamata/Bogomolov inequality. A candidate series need not correspond to an actual Fano 3-fold.

This makes a useful conceptual sequence:

1. boundedness theorem;
2. numerical inequality;
3. finite candidate list;
4. Hilbert series;
5. expected generator weights;
6. actual construction/existence remains a separate problem.

## General caution

Many works in this cluster are joint and depend on earlier theorems by Buchsbaum–Eisenbud, Kustin–Miller, Mukai, Kawamata and others. Reid's exposition is often the immediate source, but later credits should follow the theorem/construction actually being explained.
