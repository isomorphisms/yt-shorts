# Pearcey draft revision notes

Next visual pass:

- **retain** the bottom interval bar; the earlier note to remove it is superseded. Pair it with changing integral notation so it reads as the truncation interval rather than as a playback/pinch control;
- show the full Pearcey definition with a properly typeset limiting formula, `T → ∞`, rather than the programming-style `∫[-T,T]` string;
- in each frame, show the current symmetric bounds directly on an integral: for example `−1.1` to `1.1`, then `−1.2` to `1.2`, etc.;
- use one decimal place for the moving cutoff readout. More digits are visual noise here;
- use a mathematical minus sign in visible text and normal mathematical placement for integral limits, subscripts, and superscripts;
- if a future overlay genuinely needs several fractional digits, let successive digits recede at roughly 90% of the previous digit size, analogous to recursively nested HTML `<small>` tags;
- add an explicit spatial camera move: begin closer on the cusp/interference region, zoom out fairly quickly, then spend substantially longer at the final full-field view;
- let the final natural Pearcey field sit completely unmarked before explaining it;
- do **not** trace the cusp in the same visual language as the Wegert field;
- when the caustic is explained, introduce a clearly separate dashed annotation labeled `caustic overlay` / `27x² + 8y³ = 0`, preferably after a brief text cue such as `stationary-point boundary`;
- the viewer should first be able to decide that the cusp is present in the computed field, and only afterward see the mathematical curve laid over it.

Timing direction: longer overall, faster early zoom-out, longer final hold.

Current timing contract: the camera reaches the full field at 5.5 seconds, the cutoff reaches `T = 3.0` at 6 seconds, and both then hold still on the unmarked Wegert field until the caustic label at 18 seconds and dashed curve at 19 seconds.

Verification: the regenerated small preview and the full CI render both complete the changing bounds by 6 seconds, remain visually fixed through 17 seconds, and preserve the delayed 18/19-second explanatory sequence.
