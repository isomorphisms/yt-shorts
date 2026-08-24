# Complex Beauties 2024 — PDF-first source audit

This is the second pass: start from the actual calendar text, then widen the history through the calendar bibliography, Wikipedia, and primary/expository literature. The lesson notes in `2024.md` should eventually absorb this material.

Author-uploaded searchable calendar copy:

- https://www.researchgate.net/publication/395478093_The_Calendar_Complex_Beauties_2024

Official calendar/download page:

- https://blogs.hrz.tu-freiberg.de/mathekalender/english/

## January — Jost Bürgi — *Finite Differences in the Complex Plane*

**Calendar text.** Guest contribution by Bengt Fornberg. The calendar does not merely discuss a generic finite-difference formula. It studies finite-difference stencils for analytic functions **in the complex plane** and associates a stencil with a rational characteristic function whose simple poles are the stencil nodes and whose residues are the stencil weights. The displayed eighth-order approximation to `f''` uses a small square complex stencil. The phase portrait is therefore a picture of the numerical differentiation formula itself.

The calendar connects this to Jost/Jobst Bürgi, describing him as an early pioneer of finite-difference approximation because he used finite differences together with trigonometric identities in constructing a sine table, before differential calculus existed. It also notes his independent work on logarithms alongside John Napier and his work as a clock/instrument maker.

**Research graph.** Bürgi → finite-difference tables/interpolation → Newton and Leibniz calculus → modern finite-difference algorithms → Bengt Fornberg's work on weights and complex-plane finite differences.

**Follow.** [Finite difference](https://en.wikipedia.org/wiki/Finite_difference), [Jost Bürgi](https://en.wikipedia.org/wiki/Jost_B%C3%BCrgi), Bengt Fornberg, *Generation of Finite Difference Formulas on Arbitrarily Spaced Grids*, Math. Comp. 51 (1988), 699–706, plus Fornberg's recent work on finite differences in the complex plane.

**Better Short.** Do not begin with Bürgi's biography. Put the stencil on the complex plane, show that each stencil point becomes a pole of one rational function, then ask why the tiny complex stencil can beat a much wider real stencil.

## February — Elwin Bruno Christoffel — *Gauss-Christoffel Quadrature*

**Calendar text.** Guest contribution by Jan Zur. The calendar explicitly gives the historical chain: equally spaced nodes lead to Newton-Cotes formulas; Gauss showed that an `n`-node rule can achieve degree `2n-1`; Jacobi identified the optimal nodes as zeros of orthogonal polynomials; Christoffel extended the theory to weighted integrals. The pictured function is not the quadrature rule itself but the **complex interpolation error** `f(z)-p(z)` for `f(z)=exp(-z^3)` at six nodes with Chebyshev weight `1/sqrt(1-x^2)`. The six real nodes appear as zeros of the error function. The calendar also points back to Runge's phenomenon (January 2016).

**Research graph.** Newton-Cotes → Gauss → Jacobi → Christoffel → orthogonal polynomials → Chebyshev nodes → Runge phenomenon.

**Follow.** [Gaussian quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature), [orthogonal polynomials](https://en.wikipedia.org/wiki/Orthogonal_polynomials), [Chebyshev polynomials](https://en.wikipedia.org/wiki/Chebyshev_polynomials), [Runge's phenomenon](https://en.wikipedia.org/wiki/Runge%27s_phenomenon), [Elwin Bruno Christoffel](https://en.wikipedia.org/wiki/Elwin_Bruno_Christoffel).

**Better Short.** Compare six equally spaced nodes with six Gaussian/Chebyshev nodes and domain-color the two interpolation errors. The history comes naturally out of the comparison.

## March — Édouard Goursat — *Eigenvalues and Contour Integrals*

**Calendar text.** Guest contribution by Marc van Barel. A nonlinear eigenproblem `T(lambda)v=0` can be restricted to eigenvalues inside a contour. Quadrature of contour integrals involving the resolvent `T(z)^(-1)` produces a rational filter

`b(z) = sum_j u_j/(t_j-z)`

that should be close to one inside the contour and zero outside. The calendar plots such a filter for a unit-square contour. Goursat is attached to the page because of the Cauchy-Goursat theorem: he removed Cauchy's continuity assumption on the derivative in the contour-integral theorem.

**Research graph.** Cauchy → Goursat → contour integration → resolvents/spectral projectors → modern contour-integral eigensolvers (Sakurai-Sugiura, Beyn, FEAST and related methods).

**Follow.** [Cauchy's integral theorem](https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem), [Édouard Goursat](https://en.wikipedia.org/wiki/%C3%89douard_Goursat), Wolf-Jürgen Beyn, *An integral method for solving nonlinear eigenvalue problems*, Linear Algebra Appl. 436 (2012), 3839–3863.

**Better Short.** Draw a box around only the eigenvalues we want and ask whether a complex integral can behave like a search filter. Then show the rational filter's phase portrait.

## April — Trevor Pearcey — *Caustics and Interference*

**Calendar text.** The page begins from visible caustics made by refracted/reflected light, explains why ray optics creates envelopes and cusp singularities, then adds wave interference. The relevant special function is the Pearcey integral

`Psi_2(x,y) = integral exp(i(t^4 + y t^2 + x t)) dt`.

The calendar treats it as a function of `x+i y`; Tom Trogdon performed the numerical evaluation by deforming the integration contour using steepest descent. The page notes that the resulting function is not holomorphic in `x+i y`. Pearcey's biography also matters here: besides the 1946 caustic work, he and Maston Beard built the Australian computer later called CSIRAC.

**Research graph.** geometric optics → caustics → catastrophe/singularity theory → wave diffraction → Pearcey integral; compare the Pearcey cusp integral with the Airy function for fold caustics.

**Follow.** [Pearcey integral](https://en.wikipedia.org/wiki/Pearcey_integral), [caustic](https://en.wikipedia.org/wiki/Caustic_(optics)), [catastrophe theory](https://en.wikipedia.org/wiki/Catastrophe_theory), Trevor Pearcey, *The structure of an electromagnetic field in the neighbourhood of a cusp of a caustic*, Philosophical Magazine 37 (1946), 311–317.

**Better Short.** Show a real glass-caustic cusp first, then show that the same universal cusp pattern is encoded by one oscillatory integral.

## May — Constantin Carathéodory — *Boundary Behavior of Conformal Maps*

**Calendar text.** Guest contribution by Olivier Sète. The calendar takes the complement of a star-shaped slit set and maps it conformally to the exterior disk. One geometric boundary point may need to count as several different boundary approaches. Carathéodory's **prime ends** make that distinction precise. For the example, a point in the interior of a slit has two prime ends and the origin has `2n` of them. The actual picture of the month is the phase portrait of the derivative of the conformal map.

**Research graph.** Riemann mapping theorem → Osgood/Carathéodory boundary extension → prime ends → later topological formulations (for example Epstein) → applications in complex dynamics (Milnor and others).

**Follow.** [Prime end](https://en.wikipedia.org/wiki/Prime_end), [Carathéodory's theorem](https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem), D. B. A. Epstein, *Prime Ends*, Proc. London Math. Soc. (1981), and John Milnor, *Dynamics in One Complex Variable*.

**Better Short.** Make two particles approach the same geometric point from opposite sides of a slit. Ask whether a conformal map is allowed to regard them as different boundary points.

## June — Maryam Mirzakhani — *Volume of Moduli Spaces*

**Calendar text.** This entry is much richer than “Mirzakhani/Fields Medal.” It explains moduli spaces as spaces whose points are isomorphism classes of surfaces, then describes Mirzakhani's recursive Weil-Petersson volume formula for bordered hyperbolic Riemann surfaces. The calendar notes earlier work of Scott Wolpert on the fact that the volume is a rational multiple of a power of `pi`. The function actually colored in the calendar is a polynomial family `F_(2k+1)` built from even zeta values, with `k=3` in the displayed picture. Her biography names Curtis McMullen as her doctoral advisor and later work with Alex Eskin.

**Research graph.** hyperbolic surfaces → moduli spaces → Weil-Petersson geometry (Wolpert) → Mirzakhani recursion → McShane identities/intersection theory → Mirzakhani-Eskin dynamics on moduli space.

**Follow.** [Maryam Mirzakhani](https://en.wikipedia.org/wiki/Maryam_Mirzakhani), [moduli space of curves](https://en.wikipedia.org/wiki/Moduli_space_of_curves), [Weil-Petersson metric](https://en.wikipedia.org/wiki/Weil%E2%80%93Petersson_metric), M. Mirzakhani, *Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces*, Invent. Math. 167 (2007), 179–222.

**Better Short.** Ask “How big is the space of all hyperbolic surfaces of this topological type?” Only after that introduce the zeta-coefficient function used for the phase portrait.

## July — Eduard Stiefel — *Stiefel Filter*

**Calendar text.** Guest contribution by Andrei Bogatyrev. This is explicitly a continuation of the February 2023 Butterworth/filter material. The filter problem is recast as best uniform rational approximation on several passbands and stopbands. The page starts from Zolotarev's one-passband/one-stopband 1877 solution, moves to Stiefel and H. R. Schwarz for one passband and two stopbands using a genus-two algebraic curve, then notes that modern algebraic-curve methods extend to more than one hundred bands. The image is a five-passband filter, plotted as `1/2-G(z)`.

**Calendar bibliography.** E. Stiefel (1961), R. A.-R. Amer & H. R. Schwarz (1964), A. B. Bogatyrev (2010).

**Research graph.** Zolotarev → elliptic/Zolotarev approximation → Cauer filters → Stiefel/Schwarz multiband problem → Bogatyrev and algebraic curves.

**Follow.** [Elliptic filter](https://en.wikipedia.org/wiki/Elliptic_filter) — notably also called a **Cauer** or **Zolotarev** filter — plus Bogatyrev, *Chebyshev representation of rational functions*, Sbornik: Mathematics 201 (2010), 1579–1598.

**Better Short.** Pair this with Butterworth: same order, but let ripple buy a much sharper transition, then widen from two bands to five and ask why the geometry suddenly needs a higher-genus curve.

## August — Rolf Nevanlinna — *Nevanlinna Functions*

**Calendar text.** The page distinguishes Nevanlinna's value-distribution theory from the particular function class used for the picture. A Nevanlinna function maps the upper half-plane into itself (or to a real constant), and the calendar gives its integral representation. It points out that the same class is also called **Herglotz** or **Herglotz-Nevanlinna** and illustrates closure under composition. The displayed function is `exp(i*pi/3 + i*tan(z))`. The biography names Ernst Lindelöf as Nevanlinna's supervisor and Lars Ahlfors as one of his students.

**Research graph.** Pick/Herglotz/Nevanlinna functions → integral representation → Stieltjes transforms and spectral theory; separately Nevanlinna value-distribution theory → Ahlfors.

**Follow.** [Nevanlinna function](https://en.wikipedia.org/wiki/Nevanlinna_function), which also indexes the names Herglotz and Pick and points to Louis de Branges' treatment of the integral representation; Lars Ahlfors, *Rolf Nevanlinna in memoriam*, Acta Math. 149 (1982).

**Better Short.** Color only the upper half-plane and ask: “Can the colors prove that the entire upper half-plane stays upstairs after we apply this function?”

## September — Walther Ritz — *Ritz Values and Ritz Vectors*

**Calendar text.** Guest contribution by Jörg Liesen. The page compresses a huge eigenvalue problem `Ax=lambda x` to `U* A U y=lambda y`; the eigenvalues of the small compressed matrix are Ritz values. The calendar uses a 50-dimensional Krylov subspace for a 500-by-500 Grcar matrix and domain-colors the degree-50 characteristic polynomial. It explicitly connects Ritz values to Lord Rayleigh, Galerkin projection, and Krylov subspaces.

**Expanded attribution.** The standard historical story is even less linear than the calendar's short version. The Rayleigh-Ritz literature discusses Rayleigh and Ritz as independent originators; Richard Courant commented on that history; work by Jesper Lützen found an analogous method in unpublished work of Joseph Liouville from 1845.

**Research graph.** Liouville? → Rayleigh → Ritz → Galerkin → Krylov → Arnoldi/Lanczos and modern large-scale eigensolvers.

**Follow.** [Rayleigh-Ritz method](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Ritz_method), A. W. Leissa, *The historical bases of the Rayleigh and Ritz methods*, J. Sound Vib.; Martin J. Gander & Gerhard Wanner, *From Euler, Ritz, and Galerkin to Modern Computing*, SIAM Review.

**Better Short.** Start with a 500×500 spectrum, reduce it to 50 Ritz values, and let the viewer watch which part of the spectrum is already captured. The disputed/layered attribution is a separate history Short.

## October — Paul Montel — *Normal Families*

**Calendar text.** This month follows the modern consequences, not only Montel's original theorem. After defining normal families, it cites Chang and Fang's 2005 fixed-point criterion and the later construction by Chang, Fang, and Lawrence Zalcman of **non-normal** families whose early iterates nevertheless have attracting fixed points. The picture is the 23rd iterate of one explicit function from that construction. The calendar points to Wegert's 2023 expository paper on the construction.

Montel's biography names Émile Borel as his doctoral advisor and Henri Cartan, Jean Dieudonné, and Miron Nicolescu among his students. The normal-family idea also became central to the Fatou/Julia theory of complex dynamics.

**Research graph.** Borel → Montel → Fatou/Julia → fixed-point criteria → Chang/Fang/Zalcman → Wegert's phase-plot exposition.

**Follow.** [Paul Montel](https://en.wikipedia.org/wiki/Paul_Montel), [normal family](https://en.wikipedia.org/wiki/Normal_family), E. Wegert, *About the Cover: Non-normal Families and Attracting Fixed Points*, Comput. Methods Funct. Theory 23 (2023), 17–21.

**Better Short.** Show an attracting fixed point and ask why that still does **not** guarantee normal behavior for the whole family.

## November — Johannes Erwin Papperitz — *The Riemann-Papperitz Equation*

**Calendar text.** The page starts from second-order Fuchsian equations with three regular singularities. Riemann analyzed the general three-singularity problem; Papperitz wrote the equation explicitly. With singularities moved to `0,1,infinity` it becomes the hypergeometric equation. Ratios of solutions map the upper half-plane to circular triangles; Schwarz reflection continues the inverse across the triangle edges. In the `(0,0,0)` case, the continuation is the modular lambda function. The calendar explicitly returns to Papperitz's 1889 paper on representing hypergeometric transcendents by single-valued functions.

Papperitz's biography adds an especially relevant local link: he studied under Felix Klein and later became a professor and rector at Bergakademie Freiberg.

**Research graph.** Gauss hypergeometric function → Riemann differential equation → Fuchsian singularities → Schwarz triangle functions/reflection → Papperitz → Klein/automorphic-function viewpoint → modular lambda.

**Follow.** [Riemann's differential equation](https://en.wikipedia.org/wiki/Riemann%27s_differential_equation) (also called the Papperitz equation), [hypergeometric function](https://en.wikipedia.org/wiki/Hypergeometric_function), [Schwarz triangle function](https://en.wikipedia.org/wiki/Schwarz_triangle_function), [modular lambda function](https://en.wikipedia.org/wiki/Modular_lambda_function), Papperitz's 1889 paper *Ueber die Darstellung der hypergeometrischen Transcendenten durch eindeutige Functionen*.

**Better Short.** Animate one circular triangle reflecting into a tessellation, then explain that the tessellation was hiding inside a differential equation.

## December — Henri Poincaré — *Automorphic Functions and Poincaré Series*

**Calendar text.** The final month begins from invariance `f(g(z))=f(z)` under a transformation group, reviews the finite icosahedral group from December 2023 and the one-generator Möbius group from July 2023, then moves to a two-generator Kleinian group. Poincaré series build automorphic forms; quotients of forms with the same automorphy factor give automorphic functions. The plotted function is a quotient `P_-1,-3/P_0,-4` for an explicit two-generator Kleinian group.

The numerical story is part of the lesson: David Wright evaluated **605,554 terms**, with group words up to length 3,639, taking more than 13 hours on the stated machine. The calendar explicitly recommends Mumford, Series & Wright, *Indra's Pearls*.

**Research graph.** Möbius transformations → Fuchs/Klein discrete groups → Poincaré automorphic functions/series → Kleinian groups → modern computational visualization by Mumford/Series/Wright.

**Follow.** [Poincaré series](https://en.wikipedia.org/wiki/Poincar%C3%A9_series_(modular_form)), [automorphic form](https://en.wikipedia.org/wiki/Automorphic_form), [Kleinian group](https://en.wikipedia.org/wiki/Kleinian_group), David Mumford, Caroline Series & David Wright, *Indra's Pearls: The Vision of Felix Klein* (2002).

**Better Short.** This should be a payoff to the Möbius/Coxeter material rather than an isolated biography: build a discrete group first, then ask how to manufacture a function that cannot tell when the group has moved its input.
