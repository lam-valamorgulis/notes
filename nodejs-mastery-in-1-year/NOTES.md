# Working notes


## The fixed lesson shape

Every lesson carries these five things, in this order. The `teach` skill requires all
five; a lesson missing one is not finished.

| # | What | Where it goes |
|---|---|---|
| 0 | `.expertise` line | Right after `.subtitle`. Names the `core`/`depth` tag, the week (`Week N of 52`), and which of the five expert abilities the lesson moves forward. Links to the plan anchor and the glossary. |
| 1 | First-principles build-up | Open with the **problem**, then derive. Name the assumptions. Say when a step is only a convention. |
| 2 | Feynman block — **four parts** | Plain words · one analogy **and where the analogy breaks** · the sticking point · a teach-back prompt. All four. The teach-back is the part that turns reading into understanding, so it is never dropped. |
| 3 | At least one visual | An SVG figure in `.svg-fig`, or a `.diagram` ASCII block. A good visual carries more than another paragraph. |
| 4 | `.remember` recap | Last thing before `.footer-nav`. 5–7 bullets plus one bold "If you remember one thing: …". Scannable in about 20 seconds. |

Also: a `← The Map` breadcrumb at the very top, one recommended primary source, and a
line telling the learner to ask the teacher follow-up questions.

## Components in `./assets/`

- `base.css` — the whole design system. Reuse it; never inline CSS in a lesson.
  Key classes: `.win`, `.note`, `.tip`, `.trap`, `.soundbite`, `.drill`, `.expertise`,
  `.remember`, `.svg-fig`, `.diagram`, `.footer-nav`, `.ask`, `.pill`.
- `quiz.js` — two widgets. `renderQuiz(selector, questions)` for multiple choice with
  instant feedback. `renderRecall(selector, cards)` for spoken free-recall.

Quiz rule from the skill: **every option must be about the same length.** A longer option
is a clue.

## The 2026-08-28 recut — what changed and why

The course was 12 months. It is now **52 weeks**. Three things changed at once:

1. **A week is the unit of work**, because a week is the unit a person actually plans in.
   13 modules inside 4 phases of 13 weeks. Ten modules are four weeks; module 11 is
   three and module 13 is two. Weeks 13, 26 and 39 sit outside every module.
2. **Four review weeks — 13, 26, 39 and 52 — carry no new material.** Retrieval practice,
   interleaved questions, one mock interview each. This is the `teach` skill's storage-
   strength rule made into calendar time, not a nice idea in a paragraph.
3. **The starting point was corrected.** The old Map said "new to JavaScript and Node".
   That contradicted `MISSION.md` in three sibling courses, which all record professional
   front-end work and comfort with JavaScript. Week 2 is now an **audit**, not a course.

Also added, because the updated `teach` skill requires them and they were missing:
`MISSION.md` (with the 20% core and its sources), `RESOURCES.md`,
`reference/glossary.html`, the `core`/`depth` tag on every lesson and every week, and the
Core chapter at the top of The Map.

`reference/12-month-plan.html` was **deleted**, not kept. Two plans drift apart, and the
sibling `founding-engineer` course already records that as a real trap. The 52-week plan
is the only master checklist.

## The Feynman block — fixed 2026-08-28, do not regress it

Every live lesson carries the required **4-part Feynman block**, inserted
between the first-principles build-up and the "Build it for real" section:

1. In plain words · 2. One analogy · 2b. **…and where the analogy breaks** ·
3. The sticking point · 4. Now you explain it back (teach-back).

The bottom card was renamed from "Remember this · the Feynman summary" to
**"Remember this · the 20-second recap"**, because those are now two different jobs and
having both say "Feynman" was confusing. The build-up shows *why the idea has to be true*;
the Feynman block makes it *sayable out loud*; the recap is the quick-review glance.

Style is `.feynman` in `base.css`. The analogy's limit uses `.part.limit` and is drawn in
the warning colour on purpose — an analogy with no stated limit becomes a wrong mental
model the learner has to unlearn later, so it must not be skimmable.

**Every new lesson needs all four parts.** Week 9 onward, no exceptions.

## The 80/20 audit — 2026-08-28

Audited every one of the 52 weeks against the 12 core items. **Five core weeks were
orphaned** — they taught material the core list did not name: 20 and 21 (HTTP from
scratch, the spine v1), 37 and 38 (security), and 51 (system design).

Fixed by widening the list, not by re-tagging the weeks:

- Item 6 was "EventEmitter". It is now **"EventEmitter, and the server built on it"** —
  weeks 18, 20, 21. Honest, because `req` and `res` *are* emitters and streams.
- Item 10 was "Testing async code without flakes". It is now **"Evidence — tests that do
  not flake, and input you hardened"** — weeks 35–38. Both halves answer the same
  question: *how do you know?*
- Week 51 is stated as belonging to **no single item**. It is core by synthesis, because
  system design is where all twelve are used at once.

The result is in `reference/52-week-plan.html#coverage`: a table where all 52 weeks
appear. Weeks 11, 29, 33 and 45 appear twice on purpose — inside a core item's week range
*and* in the depth row, because a four-week module can carry one depth week.

**The answer to "is the 80/20 rule applied to all 52 weeks?" is yes, but the ratio looks
inverted and that is correct.** The 20% is twelve *ideas* out of Node's whole surface.
43 of 52 weeks going deep on those twelve is the rule working. A course that spent a
fifth of its weeks on core would be the wide, shallow tour the rule exists to prevent.

## The spine

From **week 21** there is one API, and every week after hardens that same service. This
is the single most important structural decision in the course. If a future session
proposes "start a fresh project for the NestJS rebuild", that is wrong — week 50 is a
rebuild *of the spine*, so the before/after load numbers mean something.

## Staleness traps in this course

These numbers are hard-coded in more than one place. Changing one means changing all.

- **Core progress lives in three places.** `index.html` has the `.core-meter` (12 `<i>`
  spans, 3 with `class="done"`) plus the caption "3 of 12 core items taught · 8 of 52
  weeks written". `MISSION.md` has the numbered core list. `reference/52-week-plan.html`
  has the per-week `core`/`depth` pills. All three must move together.
- **The lesson count is hard-coded in the repo root too.** `../index.html` carries a
  counts line for this course. It is a different file in a different folder and it is
  easy to forget.
- **`Week N of 52` appears in every lesson**, in the kicker and again in the `.expertise`
  line. Renumbering a week means editing that lesson twice.
- **The plan anchors (`#w1` … `#w52`) are linked from The Map and from every lesson's
  `.expertise` line.** Do not renumber the `id` attributes on the week cards.
- **The localStorage key changed** from `node1y-plan-` to `node1y-w-`. Old ticks from the
  12-month plan are not carried over, on purpose — the weeks are not the months.
- **The five depth weeks are named in FIVE places**: the `.note` on The Map, the dashed
  `.wk.depth` cards in the plan, the `dp` class on the week-index grid links, the Depth
  row of the coverage table, and the trap box under it. They are weeks 11, 19, 29, 33
  and 45.
- **Each week card in the plan carries a `Lesson:` link.** Writing a lesson and not
  adding that link is the trap that fired on weeks 9 and 10. `check-counts.py` now
  catches it.

## Link honesty

Every external link in `MISSION.md`, `RESOURCES.md` and `reference/52-week-plan.html` was
checked with an HTTP request on **2026-08-28** and returned a live page. Two exceptions
are marked in `RESOURCES.md`: Reddit and Stack Overflow block automated checks, so those
two were not machine-verified. Keep that habit — a dead citation is worse than no
citation, because it looks like evidence.

## The prose guard has one exemption

`check-prose.py` skips the **4-line paragraph rule** for the `Sources` line at the bottom of
each lesson (`<p class="small" id="src">`). It is a citation block — versions, dates, what was
measured — and readers scan it rather than read it. Breaking it into four paragraphs adds noise
without adding clarity.

The **20-word sentence rule still applies to it.** A citation may be long. It may not be hard to
read.

## What the guards learned on 2026-08-28

Five gaps found in one session. Four of them let a broken thing pass silently, which is the worst
kind of guard bug.

| Gap | What it let through | Fixed by |
|---|---|---|
| `check-prose.py` matched filter arguments against the **basename** | `check-prose.py lessons/0048-x.html` matched nothing and printed `0 problems` | It now exits 2 when an argument matches no lesson |
| The sentence splitter did not break on `?"` | A 37-word "sentence" that was really two | The split regex allows a closing quote before the space |
| A `<span class="h">` heading merged into the first sentence | Four extra words counted on every Feynman part | Heading labels are stripped, like `<code>` already was |
| Nothing checked links **inside** lesson prose | 14 cross-lesson links pointing at invented filenames | `check-counts.py` now resolves every relative link on every page |
| Nothing checked the previous/next **order** | Four chain links pointed past the newly inserted depth lessons | `check-counts.py` now checks each lesson links to its neighbours |

The real state hidden by the first three: **275 long sentences across 31 files**, reported as clean.

**A guard that silently passes is worse than no guard.** When a check reports success, ask what it
would have had to see to fail.

The prose fixes were applied with a script that **validates each replacement against the same rules
before writing it**. Without that, shortening one sentence kept producing a new 21-word one.

