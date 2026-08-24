# Θ / Theta

- **Pensieve source / credit:** Dror Bar-Natan, [Projects/Theta](https://drorbn.net/AcademicPensieve/Projects/Theta/)
- **Joint work:** [Roland van der Veen](https://www.rolandvdv.nl/)
- **Paper:** Bar-Natan and van der Veen, [A Fast, Strong, Topologically Meaningful and Fun Knot Invariant](https://arxiv.org/abs/2509.18456)

## What this is

The project studies a pair of knot invariants, Θ = (Δ, θ), with Δ the Alexander polynomial and θ a second invariant. The Pensieve emphasizes an unusual combination: polynomial-time computability, strong empirical separation power, and direct topological information such as a genus bound.

The project page reports computations on large random knots and comparative tests against other knot invariants. Those performance/separation claims should be attributed to the Bar-Natan–van der Veen project rather than generalized beyond the experiments.

## Citation trail

The Pensieve situates θ near work of **Tomotada Ohtsuki**, continuing a line associated with **Lev Rozansky**, **Andrew Kricker**, and **Stavros Garoufalidis**. Useful upstream papers include:

- Lev Rozansky, [A Contribution of the Trivial Connection to Jones Polynomial and Witten's Invariant of 3d Manifolds I](https://arxiv.org/abs/hep-th/9401061)
- Lev Rozansky, [The Universal R-Matrix, Burau Representation and the Melvin-Morton Expansion of the Colored Jones Polynomial](https://arxiv.org/abs/q-alg/9604005)
- Lev Rozansky, [A universal U(1)-RCC invariant of links and rationality conjecture](https://arxiv.org/abs/math/0201139)
- Andrew Kricker, [The lines of the Kontsevich integral and Rozansky's rationality conjecture](https://arxiv.org/abs/math/0005284)
- Stavros Garoufalidis and Lev Rozansky, [The loop expansion of the Kontsevich integral, the null move and S-equivalence](https://arxiv.org/abs/math/0003187)

The Pensieve also links Ohtsuki's relevant work, van der Veen's own Θ material, a Gil Kalai discussion, and a 2026 Quanta article.

## What the notebooks are working out

The notebooks test fibered knots, genus behavior, separation power, random rotational virtual knots, and weave knots, and maintain the computational package used for Θ. The recurring question is whether a strong invariant can remain fast enough to be used on knots far beyond the sizes normally used for exhaustive tabulations.