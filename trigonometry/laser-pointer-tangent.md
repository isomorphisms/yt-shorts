# Laser pointer on a wall — tangent running away

## Core picture

Put the laser pointer at a fixed perpendicular distance `d` from a long wall. Rotate it at the pointer while the spot runs along the wall.

If `θ` is the beam angle measured from the perpendicular to the wall and `x` is the spot's sideways displacement from the nearest point on the wall,

`x = d tan θ`.

The useful visual is not merely a right triangle. It is that **equal changes in angle do not make equal changes in spot position**. Near 90°, the beam is almost parallel to the wall and a tiny turn of the pointer sends the spot a huge distance.

## First animation experiment

Use a wall 10 ft away. Sweep through equal 10° steps and leave a faint mark after each step:

| θ | x = 10 tan θ |
|---:|---:|
| 0° | 0.0 ft |
| 10° | 1.8 ft |
| 20° | 3.6 ft |
| 30° | 5.8 ft |
| 40° | 8.4 ft |
| 50° | 11.9 ft |
| 60° | 17.3 ft |
| 70° | 27.5 ft |
| 80° | 56.7 ft |
| 85° | 114.3 ft |

Do not start with the table. Start with the beam and wall, move through the equal angular steps, then put the numbers beside the marks after the acceleration in spacing is obvious.

A second pass can rotate the pointer at constant angular speed. Then

`dx/dt = d ω sec² θ`,

so the spot's linear speed itself grows without bound in the ideal infinite-wall model as `θ → 90°`.

## Possible Short structure

1. Laser points straight at the wall; mark `0°`.
2. Rotate through `10°, 20°, 30°...` at equal time intervals.
3. Keep every previous wall mark visible.
4. Camera widens as the gaps become larger.
5. Reveal the right triangle and `x = d tan θ` only after the behavior is clear.
6. Optional final beat: continue toward 90° and let the spot leave the finite wall/frame.

## Physical caveat

On a real finite wall the spot simply leaves the wall. The divergence belongs to the idealization of an infinite wall. That is useful rather than embarrassing: the physical disappearance is exactly what the formula is warning about.
