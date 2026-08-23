# Frontend Mastery Tree — Resources

High-trust sources only. Every lesson cites from here, not from memory.

## Knowledge

### Primary sources (specs — the ground truth)
- [ECMAScript Language Specification (tc39.es/ecma262)](https://tc39.es/ecma262/)
  The JavaScript spec itself. Use for: execution contexts, the promise state machine, `this` resolution, anything in Stratum 1 where "what does the language actually do" matters. Read the algorithm steps, not just the prose.
- [HTML Living Standard — Event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops)
  The browser side of the event loop: tasks, microtasks, rendering opportunities. Use for: Stratum 1 event-loop cores and Stratum 2 frame-budget cores.

### Reference documentation
- [MDN — JavaScript execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model) ✅ verified 2026-07-30
  One page covering agents, realms, the stack of execution contexts, and the job queue — with a worked stack example. Use for: lesson 0001 and the whole "Execution model" branch. **Primary source for Stratum 1 · Execution model.**
- [MDN Web Docs](https://developer.mozilla.org/)
  Default reference for every Web API in the tree. Use when a lesson touches a concrete API (AbortController, IntersectionObserver, Cache API, …).

### Engine & browser internals
- [V8 blog (v8.dev/blog)](https://v8.dev/blog)
  First-party posts on hidden classes, inline caches, GC. Use for: "Engine optimization" and "Memory" branches — written by the people who built it.
- [web.dev](https://web.dev/)
  Google's performance and Core Web Vitals documentation. Use for: Stratum 2 (rendering, LCP/CLS/INP) and Stratum 3 (caching, resource hints).
- [Jake Archibald — "Tasks, microtasks, queues and schedules"](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)
  The classic interactive explainer of task vs microtask ordering. Use for: the "Event loop" branch — its predict-the-output style matches our gate rule.

### Structured tutorials
- [javascript.info (The Modern JavaScript Tutorial)](https://javascript.info/)
  Careful, deep, free tutorial. Use for: a second explanation of any Stratum 1 core when the spec is too dense.

### Rendering & Core Web Vitals (Chapter 2)
- [MDN — Critical rendering path](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path) ✅ verified 2026-08-23
  Parse → style → layout → paint → composite in one page, with which resources block which step. **Primary source for Chapter 2 · Parse and Style.**
- [MDN — `<script>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script) ✅ verified 2026-08-23
  The exact `defer` / `async` / `type=module` table. Pair with the spec: [HTML Standard § script async](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-async).
- [MDN — CSS cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Cascade) ✅ verified 2026-08-23
  Origin, layers, specificity, order of appearance — the real algorithm, in order. Spec: [CSS Cascade 5](https://drafts.csswg.org/css-cascade-5/), where `@layer` is defined.
- [Paul Irish — "What forces layout / reflow"](https://gist.github.com/paulirish/5d52fb081b3570c81e3a) ✅ verified 2026-08-23
  The definitive list of properties and methods that force a synchronous layout. Use for: layout thrashing.
- [web.dev — Animations guide](https://web.dev/articles/animations-guide) ✅ verified 2026-08-23 and [compositor-only properties & layer count](https://web.dev/articles/stick-to-compositor-only-properties-and-manage-layer-count) ✅ verified 2026-08-23
  Which properties stay on the compositor, and what `will-change` costs.
- [web.dev — Core Web Vitals](https://web.dev/articles/vitals) ✅ verified 2026-08-23, with [LCP](https://web.dev/articles/lcp), [CLS](https://web.dev/articles/cls), [INP](https://web.dev/articles/inp), [Optimize INP](https://web.dev/articles/optimize-inp)
  Definitions and thresholds, first-party. **Primary source for Chapter 2 · Frame budget.**
- [Chrome DevTools — Performance panel](https://developer.chrome.com/docs/devtools/performance) ✅ verified 2026-08-23 and [Rendering panel](https://developer.chrome.com/docs/devtools/rendering) ✅ verified 2026-08-23
  Where the flame chart, paint flashing and layer borders live. Use for: every gate #3 in Chapter 2.

### Network & delivery (Chapter 3)
- [Ilya Grigorik — *High Performance Browser Networking*](https://hpbn.co/) ✅ verified 2026-08-23 (free full text; [TCP chapter](https://hpbn.co/building-blocks-of-tcp/))
  The book on why a request costs round trips. **Primary source for Chapter 3 · Protocol.**
- [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching) ✅ verified 2026-08-23 and [`Cache-Control` reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) ✅ verified 2026-08-23
  Directive by directive, plus the revalidation flow. Pair with [web.dev — HTTP cache](https://web.dev/articles/http-cache) for the decision tree.
- [web.dev — Preload critical assets](https://web.dev/articles/preload-critical-assets) ✅ verified 2026-08-23
  What each resource hint asks the browser to do, and when each one backfires.
- [Chrome DevTools — Network panel](https://developer.chrome.com/docs/devtools/network) ✅ verified 2026-08-23
  Reading a waterfall: queueing, stalled, TTFB, download. Use for: gate #3 in Chapter 3.
- [AWS Builders' Library — "Timeouts, retries and backoff with jitter"](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) ✅ verified 2026-08-23
  Why naive retries make an outage worse, and what jitter fixes.

### Runtime timing & memory (Chapter 1)
- [MDN — Microtask guide](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide) ✅ verified 2026-08-23
  Microtask vs task, with `queueMicrotask`. Pair with [HTML Standard § event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops) for the processing model.
- [MDN — Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) ✅ verified 2026-08-23 and [MDN — `this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) ✅ verified 2026-08-23
  The two most-asked interview mechanisms in the branch.
- [ECMA-262 § Promise Objects](https://tc39.es/ecma262/#sec-promise-objects) ✅ verified 2026-08-23
  The resolve/reject algorithm as written, including why resolving with a thenable costs extra ticks.
- [Chrome DevTools — Fix memory problems](https://developer.chrome.com/docs/devtools/memory-problems/) ✅ verified 2026-08-23
  Heap snapshots, the three-snapshot technique, detached DOM nodes. **Primary source for Chapter 1 · Memory.**

## Wisdom (Communities)
- [Frontend Masters community / conference talks](https://frontendmasters.com/)
  High-signal deep-dive courses by recognized engineers. Use for: hearing how senior engineers narrate these mechanisms out loud.
- [r/ExperiencedDevs](https://reddit.com/r/ExperiencedDevs)
  Moderated, senior-level discussion. Use for: judgment cores in Stratum 7 (debt calculus, reversible decisions) where there is no spec to cite.

## Verification note
Every link marked ✅ was checked with an HTTP request on the date shown and returned 200. Unmarked entries are site roots that were not re-checked.

## Gaps
- No verified source yet for Stratum 8 (AI integration) — need first-party docs (Anthropic/OpenAI streaming + tool-calling guides) verified before those lessons are written.
- No a11y community chosen yet for Stratum 5 — candidate: the WAI-ARIA Authoring Practices Guide (APG) plus an accessibility Slack; verify when we reach it.
