# Teleman Riemann-surface: Wegert loop

A 7-second silent test clip for

`w = sqrt((z^2 - 1)(z^2 - k^2))`

with `k = exp(i theta)` making one trip around the unit circle.

This uses the actual `isomorphisms/wegert` repository as a pinned Git submodule at `third_party/wegert`. The renderer loads Wegert's production fragment shader from `app/src/main/assets/wegert.frag`; it does not copy the Wegert palette into this repository.

The four factors are placed at `+1`, `-1`, `+k`, and `-k`. Because Teleman's expression takes the square root of their product, the short renderer applies exponent `1/2` to Wegert's accumulated phase and log-modulus immediately before Wegert's existing colour calculation. The HCL conversion, palette constants, modulus bands, hue bands, and factor markers therefore remain Wegert's implementation.

There is deliberately no narration or synthetic voice in this test. This is only the moving plot.

## Render

```sh
git submodule update --init --recursive
python3 teleman-riemann-surface/render_wegert_loop.py
```

Output:

`teleman-riemann-surface/wegert-k-loop.mp4`
