# Chapters on Algebraic Surfaces

**Miles Reid**, *Chapters on Algebraic Surfaces*, IAS/Park City lecture notes; published in *Complex Algebraic Geometry* (1997).

- arXiv: https://arxiv.org/abs/alg-geom/9602006
- Reid's surface page: https://mreid.warwick.ac.uk/surf/
- Reid's own PDF: https://mreid.warwick.ac.uk/surf/Reid_Park_City_chapters.pdf

Status: **contents-read** with several chapter descriptions and excerpts inspected.

Reid describes this as a first graduate course meant to lift a reader into research-level surface theory without pretending to be exhaustive. The book moves from concrete projective geometry into intersection theory, sheaves/cohomology, K3 surfaces, singularities, Mori theory and the classification of surfaces.

## Chapter 1. The cubic surface

Reid begins with a very concrete object and uses it to introduce techniques that recur throughout algebraic geometry.

Idea units:

- all 27 lines on a smooth cubic surface;
- the lattice associated to divisor classes on the surface;
- scalar/intersection products;
- symmetric treatment of the 27 lines rather than discovering them one by one;
- the divisor class group / Picard group;
- intersection numbers;
- conic bundles on a cubic surface;
- different birational models of the same surface;
- blowups;
- the cubic surface as `P²` blown up at six points;
- how a geometric configuration of curves becomes a lattice/combinatorial object.

Cross-link: compare the more elementary Chapter 7 of *Undergraduate Algebraic Geometry*.

## Chapter 2. Rational scrolls

This chapter turns a family of examples into a reusable construction.

Idea units:

- products `P^{l-1} × P^{m-1}` as the simplest model;
- the scroll `F(a₁,…,aₙ)`;
- viewing a scroll as a fibre bundle;
- bihomogeneous polynomials;
- special low-dimensional cases;
- negative subscrolls and base loci of linear systems;
- the surface scroll `F_a = F(0,a)`;
- the Maroni invariant of a trigonal curve as a worked example;
- elliptic surfaces inside a 3-dimensional scroll;
- Weierstrass fibrations.

The useful visual theme is that complicated embedded varieties can be organized as families of linear spaces parameterized by a base.

## Chapter A. Curves on surfaces and intersection numbers

This is one of the structural bridges from pictures to computation.

Concept atoms:

- divisors as formal combinations of curves;
- intersection multiplicity versus global intersection number;
- self-intersection;
- numerical equivalence;
- intersection matrices;
- adjunction: recovering information about a curve from its embedding in a surface;
- exceptional curves and negative self-intersection;
- why intersection theory is the bookkeeping language for birational surface geometry.

## Chapter B. Sheaves and coherent cohomology

The chapter introduces technical language only after concrete surface examples have motivated it.

Potential idea units:

- why “functions varying from open set to open set” need sheaf language;
- line bundles / invertible sheaves as geometric data attached to divisors;
- sections as global geometric objects satisfying local conditions;
- exact sequences as a way to compare functions/sections on a surface, divisor and complement;
- coherent cohomology measuring the failure of local data to glue globally;
- Euler characteristics and dimension counts.

Do not oversimplify theorems here from the heading alone; this pass has not independently reconstructed every proof.

## Chapter C. Guide to the classification of surfaces

This is the road map before the main classification proof.

Core ideas to separate:

- classification is done up to birational modification, not merely equation-by-equation;
- minimal models remove unnecessary exceptional curves;
- the canonical divisor is a primary organizing invariant;
- Kodaira dimension separates surfaces into qualitatively different classes;
- rational/ruled, K3/abelian/elliptic and general-type behaviour sit in different regions of the classification.

## Chapter 3. K3 surfaces

K3 surfaces are a major recurring object in Reid's work.

Potential units:

- what defines a K3 surface;
- the trivial canonical bundle;
- curves and divisor lattices on a K3;
- polarizations;
- linear systems;
- K3 surfaces as hyperplane sections of Fano 3-folds;
- why K3 geometry repeatedly interacts with graded rings and higher-dimensional birational geometry.

Cross-links: Reid's early papers on linear systems on K3 surfaces and later work on graded rings over K3 surfaces.

## Chapter 4. Singularities and surfaces

Reid says the main object is a normal isolated surface singularity `P ∈ X` and a resolution `Y → X`, whose exceptional fibre is a configuration of curves.

The chapter treats three central classes:

1. Du Val singularities;
2. more general rational singularities;
3. elliptic Gorenstein singularities.

Strong concept atoms:

- the ordinary double point `xz = y²` as the simplest laboratory;
- resolving a singularity by replacing the singular point with curves;
- the configuration/intersection matrix of exceptional curves;
- invariants measuring the difference between the singular surface and its resolution;
- Du Val singularities as the ADE family;
- rational singularities;
- elliptic Gorenstein singularities;
- canonical class under resolution;
- numerical cycles;
- the same curve configurations also appearing in singular fibres of surface fibrations.

Official companion chapter: https://mreid.warwick.ac.uk/surf/more/DuVal.pdf

## Chapter D. Minimal models of surfaces via Mori theory

This is the surface-level entry point to ideas that become central in Reid's 3-fold work.

Concept atoms:

- a birational surface may contain `(-1)`-curves that can be contracted;
- repeated contraction leads toward a minimal model;
- extremal curves/rays encode directions in which geometry can simplify;
- Mori theory turns the search for minimal models into a systematic process rather than ad hoc manipulation;
- the surface story is the cleanest model for flips and contractions in higher dimension.

## Chapter E. Proof of the classification of surfaces

Treat this as the culmination of the earlier pieces rather than a single Short-sized theorem.

Possible subtopics:

- how Kodaira dimension enters;
- how minimality reduces the cases;
- how intersection theory constrains each case;
- how canonical linear systems distinguish general type from special classes;
- where singularity theory enters the classification;
- why classification requires both global invariants and local birational moves.

## “More chapters” — sequel in preparation

Reid's surface page lists several chapters/projects intended as a continuation of the Park City notes. These are especially valuable because some are freely posted as stand-alone PDFs.

### Surface cyclic quotient singularities and Hirzebruch–Jung resolutions

PDF: https://mreid.warwick.ac.uk/surf/more/cyclic.pdf

Status: **source-read** at abstract/introduction level.

The basic singularity is `C²/(Z/r)` with diagonal action of type `1/r(1,a)`.

Idea units:

- quotienting `C²` by a finite cyclic symmetry;
- invariant monomials as coordinates on the quotient;
- why the origin becomes singular after quotienting;
- Hirzebruch–Jung continued fractions;
- the chain of exceptional curves in the minimal resolution;
- self-intersection numbers encoded by the continued fraction;
- the bridge from explicit quotient calculations to toric geometry;
- the historical role of these singularities in resolution of surface singularities;
- `G`-clusters and the resolution as a moduli space.

### The Du Val singularities `A_n, D_n, E_6, E_7, E_8`

PDF: https://mreid.warwick.ac.uk/surf/more/DuVal.pdf

Status: **source-read** at introduction/summary level.

Idea units:

- the ADE list as singular surfaces rather than only Dynkin diagrams;
- ordinary double point as the first example;
- resolutions producing configurations of `(-2)`-curves;
- quotient singularities `C²/G`;
- the canonical class being unchanged in the crepant resolution;
- the numerical cycle;
- multiplicity;
- why the same ADE patterns recur in Lie theory, group theory and algebraic geometry.

### Graded rings

Reid lists a chapter on graded rings and homework. This points directly toward his later construction program for K3 surfaces, Fano 3-folds and canonical surfaces.

Homework page: https://mreid.warwick.ac.uk/Homework/

### Graded rings over K3 surfaces

Follow-up reference: Altınok–Brown–Reid, *Fano 3-folds, K3 surfaces and graded rings*, arXiv:math/0202092.

### Surfaces with `p_g=3, K²=4`

Reid connects this to work of Horikawa and Duncan Dicks. A later paper or source audit should identify the exact construction stages before deriving smaller concept notes.

### Godeaux and Campedelli surfaces / small `p_g`, `K²`

This cluster includes several of Reid's early papers and later joint work. Useful organizing questions:

- how little geometric genus can a surface of general type have?
- how does small `K²` constrain the surface?
- what finite fundamental groups can occur?
- how do quotients and torsion enter explicit constructions?

## Citation trail from Reid's chapter 4

Reid explicitly names Artin and Laufer as major sources for the foundational singularity results, and Du Val as a historical source. Later Shorts using those results should not present them as if they originated with Reid merely because Reid's exposition is the immediate source.

## Source links

- arXiv record and synopsis: https://arxiv.org/abs/alg-geom/9602006
- official surfaces page: https://mreid.warwick.ac.uk/surf/
- cyclic quotient chapter: https://mreid.warwick.ac.uk/surf/more/cyclic.pdf
- Du Val chapter: https://mreid.warwick.ac.uk/surf/more/DuVal.pdf
