# Visual style notes

These are repo-wide defaults for mathematical and numeric overlays unless a particular Short has a reason to depart from them.

## Mathematical notation

- Render visible mathematics as mathematics rather than programming notation when practical.
- Use a mathematical minus sign (`−`) rather than a hyphen-minus (`-`) in visible labels.
- Put integral limits, subscripts, and superscripts in their normal mathematical positions. A renderer such as MathText/LaTeX is preferable to strings like `∫[-T,T]`, `_`, and `^` when the formula is prominent.
- When an animation is explaining a limiting process, the notation may move with the parameter when that adds information rather than duplicating motion already clear in the picture.

## Decimal readouts

- Do not show precision the viewer does not need. One decimal place is the default for qualitative moving parameters such as the Pearcey cutoff `T`.
- If extra fractional digits are genuinely useful, they may visually recede instead of all having equal weight. The intended HTML-like model is nested `<small>` elements: each successive fractional digit is about 90% of the size of the previous digit.
- The decreasing-size treatment is typographic hierarchy, not a claim about numerical uncertainty.

## Pearcey example

For the Pearcey cutoff animation, do not use the interval bar. The camera motion and evolving field already provide the visual change. Keep the full definition properly typeset, and use a compact numeric cutoff readout only if the current value of `T` needs to be made explicit.
