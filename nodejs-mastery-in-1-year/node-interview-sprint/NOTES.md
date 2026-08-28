# Notes — how to teach this sprint

## Learner

- Backend-leaning developer, Vietnamese first language.
- Reads code fluently. Reads English prose slowly.
- Comfortable with JavaScript. Node knowledge is real but rusty **in speech**.
- Has a real service to talk about: the **spine API**, a link shortener.
  It is built across weeks 21 to 50 of the parent course.

## Teaching rules for this workspace

1. **Every lesson ends in a spoken answer.** Reading is not the deliverable.
   Use `renderRecall` for the spoken drills.
2. **Short sentences.** One idea each. 20 words maximum.
3. **Never simplify a real name.** `EventEmitter`, `process.exitCode`,
   `AbortController`, `node:test`, `SIGTERM` stay exactly as they are.
4. **No new theory without an interview question attached.** If nobody asks it,
   it is out of scope this week.
5. **Link, do not repeat.** 29 lessons already exist in `../lessons/`.
   Point at them. Write new material only for the interview angle.
6. **Timed katas.** Live coding is a performance skill, not a knowledge skill.
   Every kata has a clock, a talking script, and a self-scoring checklist.
7. **The second run is the one that tells the truth.** Run every kata twice.

## The fixed lesson shape

Every lesson carries all ten of these. A lesson missing one is not finished.

| # | What | Where |
|---|---|---|
| 1 | `← The Map` breadcrumb | Very top |
| 2 | `.kicker` reading `Day N of 7 · Lesson N` | Above the `h1` |
| 3 | `.expertise` line naming one of the five abilities | After `.subtitle` |
| 4 | `.win` box | After `.expertise` |
| 5 | First-principles build-up — **problem first**, then derive | The body |
| 6 | `.feynman` block with **four parts** | After the build-up |
| 7 | At least one visual — inline `<svg>` in `.svg-fig`, or `.diagram` | The body |
| 8 | `renderQuiz` + `renderRecall` | Before `.remember` |
| 9 | `.remember` card, 5 to 7 bullets plus one bold line | Before the nav |
| 10 | `.footer-nav` with previous and next | Very bottom |

The Feynman block's four parts use these exact class names:

- `1 · In plain words`
- `2 · One analogy`
- `.part.limit` headed `…and where the analogy breaks`
- `3 · The sticking point`
- `.part.teachback` headed `4 · Now you explain it back`

The parent course's checker looks for those strings. Do not rename them.

## Quiz rule

**All four options must be within 1.4x of each other in length.** A longer
option gives the answer away. `quiz.js` shuffles order, so position is never a
clue. Wrong options must be plausible, never silly.

## Recall rule

`renderRecall` answers put the **sentence to say first**. Then a `<br>Why:` line
saying what the interviewer is listening for. That second line is the teaching.

## Numbers

Every number in this sub-course was measured on **Node v24.14.0** on
**2026-08-28**. Most came from the parent course. A few were measured while
writing this sprint, and those lessons say so.

**Never invent a number.** If you want one, run the code first.

Measured while writing this sprint:

- Main module, 20 runs: `setImmediate` ran before `setTimeout(…, 0)` 17 times.
  `setTimeout` won 3 times. The order is genuinely not fixed.
- Inside an `fs.readFile` callback, 10 runs: `setImmediate` ran first every time.
- A missing `await` inside `try`/`catch` is not caught. The process printed the
  next line, then crashed with an unhandled rejection and exit code 1.
- A worker pool over 500 items with a limit of 10 held peak concurrency of
  exactly 10.
- `readline` over a 9.5 MB log peaked at 61 MB RSS. Over a 190 MB log it peaked
  at 85 MB. `readFileSync` on the same 190 MB log peaked at 588 MB.
- Three jobs at 30 ms ok, 10 ms fail, 50 ms ok: `all` rejected at 0 ms, but the
  losers still finished at 61 ms and 90 ms. Nothing is cancelled.
- `AbortSignal.timeout` rejects with `err.name === 'TimeoutError'`. That is not
  the same as your own `AbortError`.
- A 50 ms heartbeat fired at 51, 102 and 153 ms during a 200 ms `await`. So
  `await` does not block the thread.
- The same heartbeat reported `late by 193 ms` against a 200 ms synchronous burst.
- `monitorEventLoopDelay({ resolution: 20 })`: idle `max` was 21 to 27 ms. After a
  300 ms burst, `max` was 308 to 318 ms.
- `'việt'` in UTF-8 is the bytes `76 69 e1 bb 87 74`.

### One number that is not reproducible, and why

The "**1093 of 2000** damaged CSV rows" figure comes from the parent course. It
does **not** reproduce on a different file. The count depends on row width and
chunk size — with 60-byte rows and 64 KB chunks the damage was 4 rows, and with
128-byte chunks it was over 2000 fragments.

Lesson 0008 attributes that number to the parent course and says the exact count
moves with chunk size. **The durable teaching point is that the damage is silent,
not that it is 1093.** Do not re-use 1093 as if it were universal.

## Naming

The folder name stays neutral. **Never put a company name in a path, a title, or
any file here.** The parent course has the same rule.

## Where this sits

This is a sub-course of the parent
[Node.js Mastery in 1 Year](../index.html). The parent is the long road. This is
the sprint. Every lesson links back to the parent lesson that covers the same
ground in depth, so nothing is learned twice.

## Open items for the main session

- **The parent Map does not link this sub-course yet.** `../index.html` has no
  link to `node-interview-sprint/`. The React course links its sprint from two
  places in `index.html`. This sub-course was not allowed to edit the parent, so
  that link is still missing.
- **The parent root `../../index.html` counts line** is not updated either.
- `assets/base.css` and `assets/quiz.js` here are **verbatim copies** taken on
  2026-08-28. If the parent's copies change, copy them again. Do not edit these.
