# Cars at 55 mph while the road rotates

## Core experiment

Keep every car's **actual speed fixed at 55 mph**. Rotate the road relative to the viewer and watch the *projected* motion change.

Define `α` as how far the road has rotated away from being exactly perpendicular to the viewer's line of sight:

- `α = 0°`: cars move completely across the viewer's line of sight;
- increasing `α`: some of the 55 mph is now toward/away from the viewer;
- `α = 90°`: the road points straight toward/away from the viewer.

The two velocity components are

`v_across = 55 cos α`

`v_radial = 55 sin α`.

For the first Short, do **not** rotate all the way to 90°. The requested 0° → 10° → 20° → 30° range is enough to see the effect while the scene still looks like an ordinary road crossing the field of view.

| road rotation α | across-view component | toward/away component |
|---:|---:|---:|
| 0° | 55.0 mph | 0.0 mph |
| 10° | 54.2 mph | 9.6 mph |
| 20° | 51.7 mph | 18.8 mph |
| 30° | 47.6 mph | 27.5 mph |

The interesting contrast is that after a 30° rotation the cars are still actually doing 55 mph, but only 47.6 mph of that motion is across the view and 27.5 mph is directed toward/away from the viewer.

## First animation experiment

Use a top-down view first so there is no perspective ambiguity.

1. Viewer/camera sits at the bottom of frame.
2. Road initially runs left-right, exactly perpendicular to the line from viewer to the road's center.
3. Cars cross at a fixed 55 mph; put one 55 mph arrow along the road.
4. Rotate the entire road by 10°, then 20°, then 30°, keeping car speed unchanged.
5. At each stop decompose the same 55 mph velocity arrow into an across-view component and a radial component.
6. Optionally put four copies side by side so the projected distances traveled during the same one-second interval can be compared directly.

A second version can switch from the top-down construction to a roadside/observer view once the components are understood.

## Radar / Doppler connection

This geometry is also the reason a radar device measures the component of velocity along its beam. If the beam is not aligned with the car's velocity, the reported radial speed is a trigonometric projection rather than the car's full speed.

Keep that as a separate Short unless it helps explain what “speed relative to you” means. The clean first experiment is simply one fixed 55 mph vector being resolved in different directions.

## Important wording

Do not say that the car itself speeds up or slows down when the road rotates. Its speed is fixed. What changes is the component the observer sees in a chosen direction.
