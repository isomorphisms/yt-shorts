# Elias Wegert's *Complex Beauties* — lesson notes

This folder turns the *Complex Beauties* calendars into prompts for original lessons and short videos. It is **not** a mirror of the calendars.

The calendar order is kept only as provenance. A video can use any entry at any time. The useful unit is:

1. the complex function or construction;
2. the mathematician connected to it;
3. the mathematical or biographical story that makes the function worth looking at;
4. a small visual question we can actually show with Wegert-style phase/domain coloring.

## Source and reuse boundary

TU Bergakademie Freiberg's official calendar page says the series ran from 2011 through the fourteenth and final edition in 2024. Each month places a phase portrait of a complex function beside a mathematician whose work is connected with it, with mathematical background and a short biography on the reverse.

Official source and downloads for all editions:

- https://blogs.hrz.tu-freiberg.de/mathekalender/english/

Do **not** vendor the calendar PDFs or extracted calendar artwork in this repository until the reuse terms for that material have been established. For now, link to the official copies and make our own renders, diagrams, narration, and notes.

Private correspondence is intentionally not committed here.

## Wegert background

The phase-portrait method itself is worth a video before any individual calendar entry.

- Elias Wegert and Gunter Semmler, **"Phase Plots of Complex Functions: a Journey in Illustration"**, *Notices of the AMS* 58(6), 2011, 768–780. Preprint: https://arxiv.org/abs/1007.2295
- Elias Wegert, **Visual Complex Functions: An Introduction with Phase Portraits**, Birkhäuser, 2012. https://doi.org/10.1007/978-3-0348-0180-5
- Wikipedia background: https://en.wikipedia.org/wiki/Domain_coloring

The core visual idea is simple enough for the channel: color a point `z` according to the argument/phase of `f(z)`, optionally adding modulus contours. Zeros, poles, branch behavior, symmetry, and rapid change then become visible as geometry rather than as a list of values.

## Short-video template

Do not try to reproduce the calendar page. Start from a question.

- **Question:** one concrete thing to notice. “Why does `z^z` need a cut?” “What does a low-pass filter look like as a complex function?” “Why do these zeros pile up on this curve?”
- **Picture:** render the relevant function with the Wegert coloring engine. Begin static long enough to see it, then move one parameter, zoom, mark a zero/pole/cut, or compare two branches.
- **Person:** one fact that explains why this particular function became a mathematical object worth studying. Avoid generic prestige biography.
- **Payoff:** return to the picture and identify the mathematical fact the color field is showing.
- **Reading:** link the original calendar entry, a Wikipedia article when useful, and at least one paper/book/source that gets closer to the mathematics.

A month may yield several independent videos. The calendar's month/year is metadata, not a publishing schedule.

## Files

- [2024](2024.md) — all twelve entries from the final calendar, converted into lesson/video seeds.
- [2023](2023.md) — all twelve entries, converted into lesson/video seeds.
- 2011–2022 — next research pass. Keep the same format and prefer the original calendar bibliography over secondary summaries.

## Editorial rule

The function comes first. “Famous mathematician of the day” is usually the wrong framing. A useful entry should answer:

> What can I make the viewer *see* about this function that is hard to see from the formula alone, and why did somebody care about it?
