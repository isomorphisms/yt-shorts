# On-screen mathematical typography

Visible mathematical text in the Pearcey Short should not use programming notation. In particular:

- render the cutoff as a real subscript in `P_T`, not the literal characters `P_T`;
- render powers as superscripts: `t⁴`, `t²`, `x²`, `y³`;
- render the cusp as `27x² + 8y³ = 0`;
- render integral bounds above and below the integral sign rather than as `[-T,T]` inside an ASCII approximation of the formula;
- keep ordinary explanatory text separate from displayed mathematics.

The MP4 committed on this branch is explicitly a draft; typography is part of the render, not an afterthought in the lesson notes.
