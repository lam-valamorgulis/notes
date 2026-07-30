# Teaching notes (agent scratchpad)

## User preferences
- Work-first framing: tie every core to Shopify theme work (debugging, DevTools, performance) where possible; interview drills ride along inside each lesson.
- Pace: 15+ hrs/week — one short lesson per sitting, multiple sittings per day is fine. Keep each lesson completable in ~30–40 minutes.
- Every lesson ends with retrieval practice: `renderQuiz` (equal-length answer options) + `renderRecall` (say-it-out-loud cards, interview style).

## Course mechanics
- Syllabus + progress tracker = `reference/frontend-mastery-tree.html` (175 cores, localStorage persistence). A core is marked done only after passing the gate rule (mechanism / predict / point-at-it).
- Traversal: depth-first from Stratum 1 → Execution model → Event loop → Memory → Async → TS types → Engine.
- Lesson numbering: `0001-…` onwards. Reference docs grow per branch (one cheat sheet per branch, e.g. `reference/execution-model.html`).
- Design system: `assets/base.css` (probe blue #1F6C8C + amber #C86A08, structural classes shared with sibling courses) + `assets/quiz.js` (unchanged shared component).
- Root landing page (`../index.html`) has hard-coded counts — update when lessons/references are added.

## Next up
- Lesson 0002: scope chain / lexical environment (second leaf of Execution model).
- Then 0003: closures — captured environment, not copied values.
