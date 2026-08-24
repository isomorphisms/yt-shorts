# Visual style notes

These are repo-wide defaults for mathematical and numeric overlays unless a particular Short has a reason to depart from them.

## Mathematical notation

- Render visible mathematics as mathematics rather than programming notation when practical.
- Use a mathematical minus sign (`−`) rather than a hyphen-minus (`-`) in visible labels.
- Put integral limits, subscripts, and superscripts in their normal mathematical positions. A renderer such as MathText/LaTeX is preferable to strings like `∫[-T,T]`, `_`, and `^` when the formula is prominent.
- When an animation is explaining a limiting process, let the notation itself move with the parameter when that makes the changing mathematical object clearer.

## Decimal readouts

- Do not show precision the viewer does not need. One decimal place is the default for qualitative moving parameters such as the Pearcey cutoff `T`.
- If extra fractional digits are genuinely useful, they may visually recede instead of all having equal weight. The intended HTML-like model is nested `<small>` elements: each successive fractional digit is about 90% of the size of the previous digit.
- The decreasing-size treatment is typographic hierarchy, not a claim about numerical uncertainty.

## Pearcey example

For the Pearcey cutoff animation, retain the interval bar and pair it with a properly typeset numeric integral. The full definition should make the limiting role of `T` explicit. During the build, the integral limits should show the current symmetric cutoff directly—for example `−1.1` to `1.1`, then `−1.2` to `1.2`—with only one decimal place.
