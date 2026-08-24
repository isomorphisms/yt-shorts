# Gromov — *Sign and Geometric Meaning of Curvature*

M. Gromov, *Rendiconti del Seminario Matematico e Fisico di Milano* 61 (1991), 9–123.  
Official page: https://www.ihes.fr/~gromov/expository/34/  
Direct PDF: https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/177.pdf

This is a worked example of extracting **many small visual ideas** from a few pages rather than treating a section as one video.

Page convention below: “file page” counts the first PDF page as 1; “printed page” is the journal page printed on the scan.

## Opening micro-ideas

### 1. First derivative → monotonicity; second derivative → convexity

**Locator:** file page 2 / printed p. 10. `verified`

Gromov starts with the simplest model for the relationship he wants between infinitesimal quantities and visible geometry: the sign of a first derivative corresponds to monotonicity, while a sign condition on the second derivative corresponds to convexity.

**Picture:** one moving graph. First highlight tangent slopes and the left-to-right direction of motion. Then replace slope arrows by a chord and show the graph sitting on the convex side of its secants/midpoints.

**Possible Short-sized question:** “What does a second derivative look like if you refuse to draw the formula?”

This is independent enough to be its own piece.

### 2. Second fundamental form = second-order departure from the tangent plane

**Locator:** file page 3 / printed p. 11, Fig. 1. `verified`

Gromov gives the familiar curve picture and describes the second fundamental form as measuring the second-order infinitesimal deviation of a hypersurface from its affine tangent space.

**Picture:** draw a curve and its tangent line at one point. Zoom in until they appear almost identical, then exaggerate the normal-direction gap by a scale factor. The first-order difference vanishes at the tangent point; the remaining leading departure is quadratic.

This is probably a better visual introduction to the second fundamental form than beginning with coordinates.

### 3. Curvature sign and convexity

**Locator:** file pages 3–4 / printed pp. 11–12. `verified`, but keep Gromov's coorientation/local/global qualifications.

The text connects positivity of the second fundamental form with convexity. Gromov then pauses to make the statement precise by choosing the interior/coorientation and distinguishing local from global convexity.

**Picture:** show two curve segments with the same tangent line. One stays entirely on the chosen interior side near the contact point; another crosses the tangent line. Flip the normal arrow to show why sign requires a chosen side.

**Do not say:** “positive curvature means convex” without specifying what curvature/form and what hypotheses are in play.

### 4. Equidistant deformation: move every point a fixed signed distance

**Locator:** file page 5 / printed p. 13, continuing on file page 6 / printed p. 14, Fig. 3. `verified`

Gromov switches from the affine definition to one built from distance. The level sets of signed distance are equidistant hypersurfaces. Small offsets remain smooth; inward offsets of a convex hypersurface eventually become singular. A round sphere is the kindergarten case: concentric spheres shrink to the center.

**Picture:** start with a circle, then a nonround smooth convex curve. Animate parallel inward/outward offsets. The circle dies at one instant; the nonround curve develops singular behavior before disappearing.

This is one of the strongest first Shorts because the motion itself carries the idea.

### 5. Second fundamental form as the rate at which the induced metric changes under offsets

**Locator:** file pages 6–7 / printed pp. 14–15. `verified`

Gromov defines the same geometric object through equidistant deformation: compare the metric on nearby offset hypersurfaces and differentiate at zero offset. He immediately checks the unit sphere/circle example.

**Picture:** take a circle of radius 1 and an offset circle of radius `1 + ε`. Mark a small arc and show its length changing with ε. Only after the animation reveal that the rate of metric change is encoding the second fundamental form.

Good follow-up to fragment 4; do not combine them unless the final animation remains simple.

### 6. Principal curvatures evolve under parallel offsets

**Locator:** file pages 7–8 / printed pp. 15–16. `verified`

The tube formula tracks the shape operator/principal curvatures during the offset. The sphere gives the cleanest visible check: radius changes from `r` to `r + ε`, so its curvature changes reciprocally.

**Picture:** two or three osculating circles/principal directions on a surface patch, then move to a parallel surface and update their radii. For a first Short, the planar circle version may be enough.

### 7. Nearest-point projection onto a closed convex hypersurface does not increase distance

**Locator:** file page 8 / printed p. 16. `verified` at statement level.

For an exterior point, take the unique nearest boundary point reached along the normal. Gromov states that the resulting projection from the exterior to the convex hypersurface is distance-decreasing.

**Picture:** two points outside a convex body; draw their nearest boundary points; move the exterior pair around while comparing the two separations.

**Before scripting:** check exactly which ambient/induced distance convention should be displayed so the visual does not silently change the statement.

### 8. Inward offsets of a nonround convex body develop singularities over an interval

**Locator:** file page 9 / printed p. 17, Fig. 4. `verified`

For a round sphere there is one collapse time. Gromov contrasts this with a nonround convex hypersurface, where the singular region occupies an interval of inward offset values before the set disappears.

**Picture:** use a smooth rounded rectangle/ellipse-like convex curve. Erode it by distance. Track the first cusp/ridge/medial-axis-like event and continue until extinction. Put the circle next to it as the special one-time collapse.

This is visually strong and requires very little notation.

### 9. Infinitesimal convexity produces a global synthetic picture

**Locator:** file page 10 / printed p. 18. `verified`

Gromov explicitly pauses for the “moral”: a tensorial infinitesimal condition on the second fundamental form has global geometric interpretations, and the synthetic viewpoint naturally admits singular convex hypersurfaces as limits of smooth ones.

**Picture:** begin zoomed in on the tangent/normal quadratic bending information, then zoom out to the whole convex body and its singular inward offsets.

This is more of a connective Short than a theorem Short.

### 10. Mean curvature as first-order area growth of outward offsets

**Locator:** file pages 10–11 / printed pp. 18–19. `verified`

Gromov generalizes ordinary convexity by taking the trace of the second fundamental form. Positive mean curvature corresponds to monotonic increase of the volume element of an infinitesimally outward equidistant deformation. He then relates it to the signed distance function being subharmonic, with the necessary generalized interpretation at singular points.

**Picture:** mark a small patch on a surface and push it outward a tiny distance. Compare the patch area before/after. This gives a geometric meaning to the trace before introducing the Laplacian statement.

Keep “area/volume element growth” and “signed distance is subharmonic” as separate Shorts unless the latter can be made visually intelligible without rushing.

## First three prototypes I would attempt

1. **Equidistant offsets and singularity formation** — fragments 4 + maybe 8, if the animation remains legible.
2. **Departure from the tangent plane** — fragment 2.
3. **First derivative / second derivative: direction versus shape** — fragment 1.

They have low prerequisite cost, are genuinely tied to the opening pages of Gromov's text, and can end by pointing the viewer to the source rather than pretending to teach all of curvature.

## Later nearby material

The contents of the same monograph continue through generalized convexity, Riemannian length/distance/metric, equidistant deformation and sectional curvature, small balls, positive and negative sectional curvature, Ricci curvature, scalar curvature, the curvature operator, harmonic maps, and related metric classes. Each of those headings should be searched for similarly small internal fragments rather than assigned wholesale to a video.
