# Notes — how to teach this course

Working notes and stated preferences. Read before designing any lesson.


Rule that follows from the recut: **every foundation month must point at the browser.** Processes are
taught through what a tab is. The interpreter exists to explain closures and the event loop. The
socket server exists to prove why streaming HTML beats buffering. A foundation topic with no line
back to the interface does not belong in this course.


## Teaching decisions made

- **Same design system as the sibling courses.** `assets/base.css` is copied from
  `../flutter-mastery-in-1-year/assets/base.css`; only the palette changed — indigo `#3730a3` for
  the work, signal red `#b91c1c` for the monthly gate. Structural class names are unchanged, so the
  shared `assets/quiz.js` works here without edits. Do not rename structural classes.
- **New CSS classes added for this course** (all in `base.css`, never inline in a page):
  `.month` (a milestone block), `.spec` with `.k` (the Learn / Build / Ship / Prove / Teach rows),
  `.gate` (the red pass-or-fail box), `.stage` + `.stage-sub` (the four quarter dividers), and
  `ol.rules`.
- **The gate is written before the work starts, and it names the failure.** Every gate says both
  "you pass when…" and "you fail if…". This is deliberate: a gate you can reinterpret in Week 4 is
  not a gate. Keep this pattern in every lesson that adds an exercise.
- **The plan was written before any lesson.** Unusual for this repo, but the learner asked for the
  plan first. `index.html` says plainly that no lessons exist yet — keep that honesty as lessons land.
- **Every link in `RESOURCES.md` and in the plan page was verified with an HTTP request on
  2026-08-06** and returned 200. Three candidates were dropped or replaced because they did not:
  an old Brendan Gregg book URL, a USENIX page for the Raft paper (use `raft.github.io/raft.pdf`),
  and a 6.5840 lab deep link (link the course root instead). **Do not add a link you have not
  checked.**
- **Deep links exist into the plan:** `reference/12-month-plan.html#m1` … `#m12`. The Map uses them.
  Keep the `id="mN"` attributes if the plan page is rewritten.
- **SVG colours must use `style="fill: var(--accent);"`, not `fill="var(--accent)"`.** That is the
  convention proven in the sibling courses. The first draft of this course used presentation
  attributes and was converted.
- **The outside-judge months are 4, 6, 9, and 12** — not 3, 6, 9, 12. Month 4 (the mini React) is the
  first point where an outside engineer can grill the learner properly.
- **"Read, do not build" is a real category here.** Database internals, Raft, and fleet operations are
  cut on purpose and listed as cut in both `MISSION.md` and the plan page. Do not quietly reintroduce
  them because a month feels thin.
- **The two backup files** from the pre-recut version (the broad full-stack plan and its Map) are in
  this session's scratchpad, not in the repo. They are not needed; the recut is the plan.

## Backlog — next sessions

1. **`lessons/0001-what-a-browser-tab-really-is.html`** — day one of Month 1: from pressing Enter on a
   URL to pixels on screen, naming each process and thread, with the shell as the first exercise.
   Needs a process/thread diagram, a file-descriptor diagram, a `renderQuiz` check, and a
   `.remember` card.
2. **`reference/evidence-ledger.md`** — a fill-in template the learner appends to daily, so the ledger
   is not retyped from the reference page every day.
3. **`reference/glossary.html`** — start it in Month 1 and grow it all year. Terms already piling up:
   syscall, page fault, file descriptor, renderer process, compositor thread, microtask, hidden class,
   reflow, fiber, hydration, INP.
4. **Pick the spaced-repetition tool in Week 1** (Anki is the obvious candidate) and record the choice
   here. The daily plan depends on it and currently names no tool.
5. **Fill the gaps in `RESOURCES.md`** before the month that needs them: real-user monitoring
   (Month 7) and authentication in TypeScript (Month 9).
6. **Find the outside judge for Month 4 by the end of Month 1**, not in Month 4. Booking a real senior
   engineer takes longer than the learner expects, and the gate is worthless without one.
