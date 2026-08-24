# DPG / DoPeGDO

- **Pensieve source / credit:** Dror Bar-Natan, [Projects/DPG](https://drorbn.net/AcademicPensieve/Projects/DPG/)
- **Joint work:** Roland van der Veen

## What this is

The project develops a computational category called **DoPeGDO**, expanded on the Pensieve as “docile perturbed Gaussian differential operators.” Bar-Natan and van der Veen use it to package structures around a solvable/perturbed approximation denoted roughly sl₂⁺ᵋ.

The striking claim of the project is structural rather than merely numerical: products, coproducts, R-matrices, and related universal-enveloping/quantization data can be encoded by Gaussian-like operators that remain manageable enough for polynomial-time computation.

## Citation trail

The page links a MathOverflow discussion on “two-stage Gaussian integration” and related material by **Abdelmalek Abdesselam**. Those are antecedents/context, not coauthorship of the Pensieve project.

## What Bar-Natan and van der Veen are trying to demonstrate

The guiding idea is that one may approximate a difficult Lie algebra in a way that preserves the information needed for strong knot invariants while replacing expensive symbolic algebra by a much tamer Gaussian calculus. This is the larger framework from which BabyDoPeGDO and later implementations grow.