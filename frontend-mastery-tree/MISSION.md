# Mission: Frontend Mastery Tree

## Why
The goal is durable, mechanism-level mastery of the 175 "atomic cores" in the knowledge tree — first for the day job (debugging, performance, architecture calls), and second for senior front-end interviews. Recognition is not the goal; reconstruction from cold memory is.

## The goal — become a domain expert
Reading a lot is not the goal. The end state is being a **domain expert in front-end mechanisms**, which means five specific abilities. Every lesson names the one it moves forward.

1. **Explain it from first principles** — no jargon, no notes. Rebuild the mechanism from how the engine or the browser actually works.
2. **Predict behaviour in a case never seen before** — say the output, the frame, or the request order before running it.
3. **Say why it was built this way, and what that choice gives up** — every design in the platform traded something away.
4. **Debug a problem with no ready answer online** — reason from the mechanism, not from a Stack Overflow match.
5. **Judge someone else's work and say what is wrong and why** — read a PR, a trace, or a theme and name the defect in mechanism terms.

Abilities 1 and 2 are exactly the first two parts of the gate rule below, so passing gates is the same as building expertise. Ability 3 is what turns a senior interview from recall into a conversation. Abilities 4 and 5 are the day job.

## The 80/20 core — the short version
Of the 84 cores in Chapters 1–3 (the physics: language, rendering, network), **21 carry most of the real-world value**. Those are the `core` items. Everything else is `depth` — not deleted, queued.

The full list, with the reason and the citation for each, lives in the **Core** chapter of `index.html` (The Map). In short:

- **Chapter 1 · Language & Runtime (9)** — call stack & execution context · scope chain / lexical environment · closures · `this` binding · task queue & one-task-per-tick · microtask queue drains before render · long tasks, starvation, input delay · promise state machine · leak shapes (detached DOM, listeners, timers, closures).
- **Chapter 2 · Rendering (7)** — CSSOM & render-blocking CSS · parser-blocking scripts vs `defer`/`async`/module · cascade, specificity, inheritance, layers · which properties trigger layout vs paint vs composite · layout thrashing & forced synchronous layout · the 16.67 ms frame budget · LCP, CLS, INP.
- **Chapter 3 · Network & Delivery (5)** — DNS → TCP → TLS handshake cost in RTTs · `Cache-Control` & immutable assets · resource hints · waterfall vs parallel in the Network panel · retry with exponential backoff + jitter.

Rule: **no `depth` lesson while a `core` item is untaught**, unless Lam asks for it by name. Every `core` lesson ends by naming the `depth` items it deliberately skipped.

## Success looks like
- For any core in the tree, Lam can pass its **gate rule**: (1) state the mechanism, (2) predict an output before running it, and (3) point at it in a real profile, trace, or spec.
- **First principles, not memorised facts.** Lam can rebuild the mechanism from the ground up — from how the engine/browser actually works — not recite a rule he read somewhere.
- **The Feynman test.** Lam can explain any locked-in core to someone else, in plain English, with no jargon, as if teaching a junior who has never seen it. If the explanation leans on an unexplained term, the core is not actually understood yet.
- At work: can debug a rendering, network, or memory problem in a Shopify theme by reasoning from the mechanism, not by trial and error.
- In interviews: can whiteboard any locked-in core in five minutes with no notes.
- The tree tracker (`reference/frontend-mastery-tree.html`) fills up honestly — a core is only marked done after passing its gate.

## Constraints
- 15+ hours per week. Aggressive pace: short daily lessons plus a weekly retrieval-practice (review) session.
- Work-first sequencing: when two cores are equally next, prefer the one the day job exercises (rendering, network, platform).
- Traversal order: **core-first inside depth-first**. Chapters run 1 → 2 → 3 as the tree recommends, but inside each chapter only the `core` items are taught until all 21 are done.
- Every lesson carries three required practice sections, not just reading: a **live coding session** (type the code yourself, predict, run it, then break it), an **interview session** (a scripted mock-interview dialogue — question, spoken answer, likely follow-up), and an **explain-it-back** check (write or say the mechanism as if teaching a junior, first-principles, no jargon).

## Out of scope
- Backend/server engineering beyond what a front-end developer must know (e.g. writing APIs). Stratum 3 covers the network from the client side only.
- Framework API trivia (React hooks lists, Vue option names). The tree teaches mechanisms; framework syntax lives in the sibling courses.
- Native mobile (Flutter has its own course in `../flutter-mastery-in-1-year/`).
