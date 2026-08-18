# Teaching notes (agent scratchpad)

## User preferences
- Work-first framing: tie every core to Shopify theme work (debugging, DevTools, performance) where possible; interview drills ride along inside each lesson.
- Pace: 15+ hrs/week — one short lesson per sitting, multiple sittings per day is fine. Keep each lesson completable in ~30–40 minutes.
- Every lesson ends with retrieval practice: `renderQuiz` (equal-length answer options) + `renderRecall` (mock-interview cards).

## Required lesson sections (every lesson, in this order)
1. **Teach the mechanism from first principles** — build it up from how the engine/browser actually works, not a rule to memorise. This is the existing numbered-`h2` teaching content.
2. **Point at it** — show where the mechanism is visible in a real tool (DevTools, a trace, a spec). Already the pattern in lesson 0001.
3. **Live coding session** (`.livecode` box) — a guided type-along task: open a scratch file, type the lesson's code without copying, predict the output on paper first, run it, then deliberately break it in a way that exercises the failure mode just taught.
4. **Explain it back** (`.feynman` box) — the Feynman check: prompt Lam to write or say the mechanism in plain English, as if teaching a junior with no background, no jargon. This is what actually proves gate #1 (state the mechanism), not just reading the teaching content.
5. **Prove it** — `renderQuiz` (predict-before-clicking multiple choice, unchanged) + `renderRecall`, reframed as an **interview session**: each card is `{ prompt, answer }` where `prompt` is phrased as the interviewer's question and `answer`'s HTML ends with a short "Likely follow-up: …" line, not just a flat model answer.
6. **The gate box** — unchanged 3-gate rule (mechanism / predict / point-at-it), tie gate #1 back to the explain-it-back exercise in its wording.

## Course mechanics
- Syllabus + progress tracker = `reference/frontend-mastery-tree.html` (175 cores, localStorage persistence). A core is marked done only after passing the gate rule (mechanism / predict / point-at-it).
- Traversal: depth-first from Stratum 1 → Execution model → Event loop → Memory → Async → TS types → Engine.
- Lesson numbering: `0001-…` onwards. Reference docs grow per branch (one cheat sheet per branch, e.g. `reference/execution-model.html`).
- Design system: `assets/base.css` (probe blue #1F6C8C + amber #C86A08, structural classes shared with sibling courses) + `assets/quiz.js` (unchanged shared component).
- Root landing page (`../index.html`) has hard-coded counts — update when lessons/references are added.

## Next up
- Lesson 0003: closures — captured environment, not copied values (third leaf of Execution model).
- Then 0004: hoisting & the temporal dead zone.
