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

## Wisdom (Communities)
- [Frontend Masters community / conference talks](https://frontendmasters.com/)
  High-signal deep-dive courses by recognized engineers. Use for: hearing how senior engineers narrate these mechanisms out loud.
- [r/ExperiencedDevs](https://reddit.com/r/ExperiencedDevs)
  Moderated, senior-level discussion. Use for: judgment cores in Stratum 7 (debt calculus, reversible decisions) where there is no spec to cite.

## Gaps
- No verified source yet for Stratum 8 (AI integration) — need first-party docs (Anthropic/OpenAI streaming + tool-calling guides) verified before those lessons are written.
- No a11y community chosen yet for Stratum 5 — candidate: the WAI-ARIA Authoring Practices Guide (APG) plus an accessibility Slack; verify when we reach it.
