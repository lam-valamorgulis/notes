# Working notes


## The fixed Lesson shape

Four numbered blocks, then the recall card. The CSS numbers the blocks, so a
missing block is visible at a glance.

| Block | Class | What goes in it |
|---|---|---|
| 01 | `.block.why` | First principles. The problem it was invented to solve, then the derivation. Assumptions named. |
| 02 | `.block.hurts` | Where it goes wrong. Each failure is a `.scar`. `.scar.slow` = fails quietly. `.scar.money` = costs real money. |
| 03 | `.block.feynman` | Plain words, one analogy **plus where the analogy breaks**, the sticking point, then a teach-back in `.explain` with the model answer hidden inside `details.model`. |
| 04 | `.block.do` | One task inside `.task`, ending in `.proof`. |
| — | `.remember` | 5 to 7 bullets plus one bold takeaway. Always last, before `.footer-nav`. |

Also required near the top of every Lesson: `.expertise` — which of the five
expert abilities this Lesson moves forward, and the `core` or `depth` tag.

## Components in `./assets/`

- `base.css` — the whole design system. Track colours (`body.t1`, `t2`, `t3`),
  the four blocks, `.scar`, `.task`, `.remember`, `.figure` + `.dg-*` SVG helper
  classes, and the print stylesheet. Add to this file; never inline CSS in a
  Lesson.
- `quiz.js` — two widgets. `renderQuiz(selector, questions)` for multiple choice
  with instant feedback (options are shuffled on every load, so position cannot
  be memorised). `renderRecall(selector, cards)` for spoken free-recall.

Quiz rule from the skill: **every option must be about the same length.** A
longer option is a clue.

## Lessons learned from the 2026-08-23 review pass

Four review agents read all 12 Lessons and found 114 issues. One defect appeared
in nine of the twelve Lessons, so it is now a rule:

- **Never attach a footnote to your own extension.** The pattern was: read a real
  source, extend its idea usefully, then cite the source for the extension too. It
  happened with McKinley (the "have I run this in production?" test), Cockburn (the
  "real components, no fakes" reading), Paul Graham ("research", "sample"),
  Seibel (a customer-number claim he never made), and the founding-engineer
  one-line definition. **Fix:** when a step is ours, the page says
  *"this step is ours, not his"* in the body, and the footnote repeats it.
- **A rule must survive its own arithmetic.** F3 said "score 1 to 5, then multiply,
  a zero is fatal" — but a 1-to-5 scale cannot produce a zero. The scale is now
  0 to 5. Check every worked example against the rule it demonstrates.
- **Do not teach a frequency you have not counted.** F4 taught that the pivot path
  is "usually" right, in five places including a quiz answer, on the same page that
  admitted it had no data. Removed.
- **Draw the important line last.** In an SVG, an opaque `.dg-box` fill covers
  anything drawn before it. Two diagrams had their key line hidden underneath a
  bar. Paint bars first, then the line that crosses them.
- **Low contrast is not a signal.** Faded boxes at `opacity="0.55"` on
  `--card-bg` are nearly invisible in both themes. Use `stroke-dasharray` to mean
  "this is cut", and fade the label with its box or the `<desc>` becomes a lie.
- **Separate the spoken words from the coaching note.** Every `renderRecall`
  answer now puts the sentence to say first, then `Why:` and the reasoning. Before
  the fix, a learner reading the card aloud would also say the author's commentary.
- **Never write a model answer a founder would resent.** One card told a founder
  that people without a kill rule are "quietly looking for the exit". Correct, and
  it would end the conversation. Model answers now criticise only the speaker.

## Staleness traps in this course

- `item N of 12` appears in the `.expertise` line of all 12 Lessons. Changing the
  core list means editing 12 files plus `index.html` plus `MISSION.md`. That is the
  cost of adding a thirteenth core item — pay it deliberately or move one out.
- `index.html` hard-codes the progress bar (12 spans), the caption, three
  "4 core · 4 written" lines and the reading order. All must move together.
- "Links checked 2026-08-23" appears in every Lesson footnote plus the glossary and
  `RESOURCES.md`. The date is per-page on purpose, so each page carries the honesty
  of its own claims.

