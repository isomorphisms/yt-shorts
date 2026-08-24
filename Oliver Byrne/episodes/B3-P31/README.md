# Byrne III.31 — the right angle stays right

First production test of the Manim contract in `../../manim-production.md`.

## Point of the Short

Keep the diameter fixed, move the third vertex continuously along the semicircle, and keep the right-angle marker/readout attached to the moving vertex. The Short is only testing the invariant in the first part of Euclid III.31; it does not expand into the acute/obtuse segment cases from the rest of the proposition.

The animation is an original parametric reconstruction. No C82 diagram, HTML/CSS, Joyce diagram, or Slyusarev implementation is copied into the scene.

## Reproduce

From the repository root, with Docker installed:

```sh
bash './Oliver Byrne/episodes/B3-P31/render.sh'
```

The script pins the Manim Community Docker image to `v0.19.1` and renders with the Cairo renderer at 1080×1920, 30 fps. Generated media stays under this episode's ignored `media/` directory; the PR carries the source, not a binary video.

Expected scene length is about 8.8 seconds. The CI workflow uploads the rendered MP4 as `byrne-iii31-preview` so the production contract can be judged from the actual output.

## Geometry

Let the diameter endpoints be fixed points `B` and `C` on a circle and let `A` move on the upper semicircle. Every frame recomputes `AB`, `AC`, and the right-angle marker from the current position of `A`. This is the first claim of III.31: the angle `BAC` in the semicircle is right.

## Sources and credit

- Euclid, *Elements*, Book III, Proposition 31.
- Oliver Byrne, *The First Six Books of the Elements of Euclid* (1847), public-domain visual source: https://archive.org/details/firstsixbooksofe00byrn
- Byrne/C82 navigation and modern reference: https://www.c82.net/euclid/book3/
- David E. Joyce, proposition text and dependency check: https://mathcs.clarku.edu/~djoyce/elements/bookIII/propIII31.html

The on-screen source line credits Euclid III.31 and Oliver Byrne (1847). Joyce and C82 are linked here as research/navigation sources; their modern diagrams are not reused.
