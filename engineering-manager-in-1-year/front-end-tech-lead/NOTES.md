# Teaching notes & preferences — Front-End Tech Lead course

Working notes for how to teach Lam this course. Update as preferences emerge.


## How Lam likes to learn (carried over from the sibling courses)
- **Judgment-first.** Prefers "read a real scenario → pick the best move → know why the other
  options are worse" over abstract theory. Keep the scenario-drill + quiz style.
- **Beautiful, printable, Tufte-style** lessons. Reuse `assets/base.css` + `assets/quiz.js`
  (copied into this sub-folder so it is self-contained); never invent per-lesson CSS.
- **Plain English.** Lam is a non-native English reader. Use simple, common words and short
  sentences. Keep real technical terms (RFC, LCP, SSR, WCAG, design tokens) but define each
  once in the glossary and on first use.
- **Practical use case every lesson** — something to try at work this week, even with no reports.

## Teaching approach for THIS topic (Tech Lead)
- The role is a **two-sided** skill: (1) front-end technical depth (architecture, performance,
  design systems, testing, accessibility) and (2) leadership-by-influence (communication,
  RFCs, mentoring, driving decisions). Every phase should mix both, not silo them.
- Because Lam has no authority, the recurring meta-skill is **"how do I make this happen when
  I can't order anyone?"** — writing, credibility, alignment, disagree-and-commit. Bring it
  back inside later technical drills (spacing + interleaving).
- Skills-heavy, not knowledge-heavy: lean on retrieval drills, scenario practice, and real
  actions (write an RFC, run a perf audit, propose a design system), not just reading.

## Course structure decision (set 2026-07-21)
- Lives at `engineering-manager-in-1-year/front-end-tech-lead/` — a **separate, self-contained
  sub-course** chosen by Lam (keeps the EM course fully intact). Lesson and record numbering
  restarts at 0001 for this course.
- Pivot from the parent EM mission was explicit: Lam chose "Front-End Tech Lead (lead by
  influence)" over "Engineering Manager". See `learning-records/0001-*`.

## Global user rules that apply here
- "Never guess — check the source." Cite trusted resources in every lesson (see RESOURCES.md).
- Keep `index.html` (The Map) in sync whenever content is added/renamed/removed — part of "done".

## Open questions to revisit
- Is there a specific target company or an internal promo path for the Tech Lead role?
- Which front-end framework is the day-job on (React/Next, Vue, Angular)? Would let drills use
  the exact stack. Assume React/Next.js until told otherwise.
- Does Lam want to join a community now (e.g. a front-end / Staff-eng community), or later?
