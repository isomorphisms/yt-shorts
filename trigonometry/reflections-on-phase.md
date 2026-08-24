# Reflections on phase

This is a bridge note for people who are already using sine and cosine but may not yet have a stable intuition for **phase**. It can feed several Shorts rather than one comprehensive explanation.

The recurring rule: show the same phenomenon in two representations and do not force a verdict about which picture is the "real" one.

## Two pictures of the same thing

### 1. Sine-wave picture

Start with

`y(t) = A sin(ωt + φ)`.

Keep `A` and `ω` fixed and change only `φ`. On screen, phase is simply where the oscillation is in its cycle relative to a reference.

Useful animation:

- two identical waves;
- slide one horizontally while keeping its shape unchanged;
- mark 0°, 90°, 180°, 270°;
- then replace the horizontal shift by a single angle `φ`.

### 2. Complex / rotating-vector picture

Represent the same sinusoidal quantity by a rotating complex number or phasor. A quarter-turn in this picture is a quarter-cycle of phase in the wave picture.

Show both pictures simultaneously:

- left: the sine wave shifts by one-quarter period;
- right: the corresponding vector rotates by 90°;
- then put `× j` between two frames of the vector picture.

With the common modern `e^{jωt}` convention, multiplication by `j` is a +90° rotation. Historical sources may use the opposite time/sign convention, so the important invariant is **quarter-turn / quarter-period**, not the word "lead" or "lag" by itself.

The point of the Short is not to announce that complex numbers are secretly geometry or secretly electrical engineering. Show both readings and let the viewer build a preference.

## Electricity

Natural examples:

- voltage and current at the same frequency but different phase;
- inductive and capacitive lead/lag;
- power factor `cos φ`;
- a rotating generator/phasor whose projection produces a sine wave.

This should cross-link to [electricity.md](electricity.md), rather than duplicate its RMS and power-factor material.

## Light

Use light when a literal wave picture is more useful than a circuit picture.

Possible Shorts:

- two same-frequency light waves with adjustable phase difference;
- path-length difference becoming phase difference;
- constructive and destructive interference as phase alignment/misalignment;
- reflection at a boundary as a later, source-grounded example because the phase behavior depends on the boundary conditions.

The visual goal is to make `φ` feel like a position in a repeating cycle before introducing more optics terminology.

## Historical anchor — Steinmetz

The date to keep straight is:

- **International Electrical Congress, Chicago: August 21–25, 1893**;
- the AIEE **proceedings were published in 1894**;
- Steinmetz's paper **"Complex Quantities and Their Use in Electrical Engineering"** appears there, pp. 33–74/75 depending on the scan/index.

This is unusually good source material for the phase interpretation. Steinmetz explicitly treats multiplication by `j` as rotating a sinusoidal quantity by 90°, i.e. shifting it by one-quarter period. His sign convention describes which direction is advance/retard differently from the common modern `e^{jωt}` convention, so preserve that caveat in any finished Short.

The **1897** date is also real but belongs to Steinmetz's book *Theory and Calculation of Alternating Current Phenomena*, not to the Chicago congress. That may be the source of the date collision.

Primary/history sources:

- *Proceedings of the International Electrical Congress Held in the City of Chicago, August 21st to 25th, 1893*, AIEE, 1894: https://books.google.com/books?id=BV5KAAAAMAAJ
- UPenn Online Books index for the same proceedings: https://onlinebooks.library.upenn.edu/webbin/book/lookupid?key=ha001616266
- Steinmetz and Berg, *Theory and Calculation of Alternating Current Phenomena* (1897 edition): https://books.google.com/books?id=82xKAAAAMAAJ

## Playlist role

Do not remake good explanations merely to own every step. This note can function as connective tissue between linked videos by other creators: one Short establishes the common phase picture, then the playlist can branch into electricity, light, interference, phasors, complex numbers, and Fourier material.

## Strong first Short

**What does `j` do in electrical engineering?**

1. Show a sine wave.
2. Duplicate it one-quarter period away.
3. Replace the two waves by their rotating-vector versions.
4. Rotate one vector by 90° and write `× j`.
5. Split the final frame: **quarter-turn in the complex plane / quarter-period in the wave**.

No need to settle whether the geometric or phase interpretation deserves conceptual priority. The equivalence is the content.
