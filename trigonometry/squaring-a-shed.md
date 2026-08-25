# Squaring a shed — how much does one degree matter?

## Core picture

A rectangular shed frame can have the correct side lengths and still be racked into a parallelogram. Measuring both diagonals turns a small angular error into a much easier length measurement.

Let the adjacent sides have lengths `a` and `b`, and let one corner be `90° + δ`. The two diagonals are

`d₊ = √(a² + b² + 2ab sin δ)`

and

`d₋ = √(a² + b² - 2ab sin δ)`.

When `δ = 0`, the diagonals are equal. For a small error in radians,

`d₊ - d₋ ≈ (2ab / √(a²+b²)) δ`.

That approximation is a good visual endpoint because it says directly how an angular error becomes a tape-measure error.

## Concrete 8 ft × 12 ft example

For an 8 ft by 12 ft frame:

| angular error from square | difference between diagonals |
|---:|---:|
| 0.5° | 1.4 in |
| 1° | 2.8 in |
| 2° | 5.6 in |
| 3° | 8.4 in |
| 5° | 13.9 in |

So being only about one degree off square already makes the two diagonals differ by nearly three inches on an 8 × 12 shed.

## First animation experiment

1. Draw an 8 × 12 rectangle and its two equal diagonals.
2. Pin the four side lengths and drag the top edge sideways so the rectangle racks.
3. Keep a small angle label on one corner: `90.0° → 90.5° → 91.0° → 92.0°`.
4. Measure both diagonals on screen with tape-measure-style labels.
5. Freeze at 1° and emphasize that the diagonal mismatch is already about 2.8 in.
6. Return the frame to square by pulling until the diagonals match.

The construction action should come before the formula: somebody can understand why builders compare diagonals without first knowing the law of cosines.

## Possible related practical passes

- 3-4-5 triangle layout: show how a builder establishes a right angle without measuring the angle directly.
- Long wall amplification: compare the same 1° angular error on small and large rectangles.
- One diagonal only is not enough unless side lengths/shape constraints are also known; show why comparing both diagonals is such a convenient field test.
