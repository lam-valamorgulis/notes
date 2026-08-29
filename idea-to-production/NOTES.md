# Working notes


## The running product: Speck

A hosted feedback widget. One `<script>` tag, a public write endpoint, a
multi-tenant database, a dashboard, a daily digest email.

Every Lesson task is done on Speck. It stays the same product for all 24 weeks,
so the schema change in week 17 hits the table designed in week 5. That is the
point — a fresh toy per Lesson would hide every real problem.

## The fixed Lesson shape

Four numbered blocks, then the recall card. The CSS numbers the blocks, so a
missing block is visible at a glance.

**Note the order differs from founding-engineer.** Here Feynman is block 02, not
03. The teaching rule says the plain-words explanation comes right after the
build-up, before the failure stories.

| Block | Class | What goes in it |
|---|---|---|
| 01 | `.block.why` | First principles. The problem it was invented to solve, then the derivation. Assumptions named. |
| 02 | `.block.feynman` | Plain words, one analogy **plus where the analogy breaks**, the sticking point, then a teach-back in `.explain` with the model answer hidden inside `details.model`. |
| — | `.figure` | The diagram. Sits right after block 02. Inline SVG using the `.dg-*` classes. Never an image file. |
| 03 | `.block.hurts` | How this fails in production. Each failure is a `.scar`. `.scar.slow` = fails quietly. `.scar.money` = costs real money. |
| 04 | `.block.do` | One task on Speck inside `.task`, ending in `.proof`. |
| — | `.remember` | 5 to 7 bullets plus one bold takeaway. Always last, before `.footer-nav`. |

Also required near the top of every Lesson:

- `.mapnav` — the "← The Map" breadcrumb. First element inside `.wrap`.
- `.win` — the one tangible win this Lesson gives.
- `.expertise` — which of the five expert abilities this Lesson moves forward,
  and the `core` or `depth` tag.
- `.stagenote` — sits after `.win`. Names the Stage, the weeks, the other Lessons
  in the same two-week block (as `li.planned` when not yet written), and the
  Stage gate. This is the only place a Lesson says where it sits in the 24 weeks,
  so it is not optional.

And at the bottom, before `.footer-nav`:

- One **primary source** link, marked as the thing to read or watch this week.
- The `.ask` box reminding the reader to send questions back to the agent.

## Components in `./assets/`

- `base.css` — the whole design system. Copied from
  `../founding-engineer/assets/base.css` so the repo looks like one course, then
  changed in four places: the header comment, the block badge numbers (Feynman is
  02 here), a fourth Stage colour `--t4`, and `.month` renamed to `.stage`.
  Add to this file; never inline CSS in a Lesson.
- `quiz.js` — two widgets, unchanged from founding-engineer.
  `renderQuiz(selector, questions)` for multiple choice with instant feedback.
  Options are shuffled on every load, so position cannot be memorised.
  `renderRecall(selector, cards)` for spoken free-recall.

Quiz rule from the teaching skill: **every option must be about the same
length.** A longer option is a clue.

## Stage colours

| Stage | Class on `<body>` | Colour |
|---|---|---|
| 1 — Decide | `t1` | purple |
| 2 — Shape | `t2` | blue |
| 3 — Deliver | `t3` | orange |
| 4 — Operate | `t4` | deep teal |

## Rules for writing a Lesson in this course

1. **Every load-bearing number carries its source and its year.** "Three or fewer
   active branches" is a DORA finding from 2016–2017 data, not a law.
2. **Name what the Lesson deliberately skipped.** A `core` Lesson ends by naming
   the `depth` items it left out. Silence reads as "that is everything".
3. **Never assume a team.** No reviewer, no QA, no ops rota. Where a practice
   normally needs another person, say what the one-person version costs.
4. **The task must be doable in the two-week block.** If it needs a paid service,
   say the free tier that works, or give an offline substitute.
5. **Link sideways, not down.** When a Lesson touches something already taught in
   founding-engineer, Node, React or Backend, link to it instead of repeating it.
