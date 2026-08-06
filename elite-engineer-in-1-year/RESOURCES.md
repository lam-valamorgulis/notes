# Elite Engineer Resources — front-end to the metal, then AI

Every link below was checked with an HTTP request on **2026-08-06** and returned 200. No link here is
from memory. If a link dies, remove it or replace it — do not leave it rotting.

Grouped by the month that needs it, because a resource with no month attached never gets read.

## Knowledge

### Month 1 — processes, threads, and what a tab is
- [cpu.land — how a CPU runs a program](https://cpu.land/)
  Free and illustrated: syscalls, ELF, virtual memory. Fastest way into the machine model.
- [Chromium: multi-process architecture](https://www.chromium.org/developers/design-documents/multi-process-architecture/)
  Primary source for browser process, renderer process, and site isolation.
- [Inside look at modern web browsers — Chrome developers](https://developer.chrome.com/blog/inside-browser-part1)
  The four-part series. Read all four; it is the clearest map of who does what.
- [Chrome DevTools: Performance panel docs](https://developer.chrome.com/docs/devtools/performance/)
  Needed for the Month 1 build, and for every month after it.
- [`man 2 fork`](https://man7.org/linux/man-pages/man2/fork.2.html)
  The actual contract of the syscall the shell is built on.
- [Systems Performance, 2nd ed — Brendan Gregg](https://www.brendangregg.com/sysperfbook.html)
  Not for the browser specifics — for the *method* of finding where time goes. Use in Months 1 and 7.

### Month 2 — the JavaScript engine and the event loop
- [Crafting Interpreters — Robert Nystrom (free online)](https://craftinginterpreters.com/)
  Build a language twice. I write part II in TypeScript; the translation is part of the work.
- [V8 blog](https://v8.dev/blog) and [V8 docs](https://v8.dev/docs)
  Hidden classes, inline caches, garbage collection, deoptimisation — from the people who wrote it.
- [ECMAScript specification](https://tc39.es/ecma262/)
  When a claim about JavaScript is disputed, the spec settles it. Read the lexical environment and
  job queue sections in this month, not before.
- [Tasks, microtasks, queues and schedules — Jake Archibald](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/)
  The clearest explanation of ordering that exists. The puzzle set for the Month 2 build.
- [MDN: JavaScript execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model)
  The plain-language companion to the spec sections above.

### Month 3 — the rendering pipeline
- [Web Browser Engineering — Panchekha & Harrelson](https://browser.engineering/)
  A whole browser, built chapter by chapter. **This is the book to follow for Month 3.**
- [Matt Brubeck: let's build a browser engine](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
  and its code, [robinson](https://github.com/mbrubeck/robinson). The shortest honest layout engine.
- [RenderingNG — Chrome developers](https://developer.chrome.com/docs/chromium/renderingng)
  How the modern pipeline is actually split across threads and processes.
- [MDN: how browsers work](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/How_browsers_work)
  The one-page overview to read first.
- [HTML parsing specification](https://html.spec.whatwg.org/multipage/parsing.html) and
  [CSS Flexbox specification](https://drafts.csswg.org/css-flexbox-1/)
  Primary sources for the two hardest parts of the build: parsing, and one flex row done correctly.

### Month 4 — the framework layer
- [React fiber architecture — Andrew Clark](https://github.com/acdlite/react-fiber-architecture)
  Written by a React core author. The mental model for the whole month.
- [Build your own React — Rodrigo Pombo](https://pomb.us/build-your-own-react/)
  A step-by-step reconciler. Use it to check yourself, not to copy from.
- [react.dev](https://react.dev/learn)
  Official docs; the effect timing and hook rules pages matter most here.

### Month 5 — the build layer
- [minipack](https://github.com/ronami/minipack)
  A tiny, readable bundler. The honest starting point.
- [Rollup docs](https://rollupjs.org/introduction/)
  The best explanation of tree shaking and why side effects defeat it.
- [esbuild docs](https://esbuild.github.io/)
  Architecture notes on why it is fast — a lesson in doing less work per file.
- [Vite: why](https://vite.dev/guide/why.html)
  Dev server design and how hot module replacement swaps a module.
- [Source map specification (TC39)](https://tc39.es/source-map/)
  Needed to hand-decode a `mappings` field, which is the Month 5 gate.

### Month 6 — the network
- [High Performance Browser Networking — Ilya Grigorik (free online)](https://hpbn.co/)
  TCP, TLS, HTTP/1.1, HTTP/2, WebSocket — and why each is slow.
- [RFC 9112 (HTTP/1.1)](https://www.rfc-editor.org/rfc/rfc9112.html) and
  [RFC 9110 (HTTP semantics)](https://www.rfc-editor.org/rfc/rfc9110.html)
  The framing rules your socket server must obey. Read the parsing sections properly.
- [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)
  Sockets from the bottom. The concepts carry straight to Node `net`.
- [Node `net` documentation](https://nodejs.org/api/net.html)
  The API the Month 6 build sits on.
- [React Server Components](https://react.dev/reference/rsc/server-components)
  For the streaming and hydration half of the month.

### Month 7 — performance
- [Core Web Vitals](https://web.dev/articles/vitals), [INP](https://web.dev/articles/inp),
  [optimising INP](https://web.dev/articles/optimize-inp)
  Definitions first, tactics second. Field data is the point.
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)
  For the CI budget gate. Lighthouse is a gate here, never the evidence.
- [Chrome DevTools Performance docs](https://developer.chrome.com/docs/devtools/performance/)
  Reading a trace properly is the skill this month is really about.

### Month 8 — taste, accessibility, deletion
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
  The patterns for the combobox and dialog builds. Follow it exactly, then test with a screen reader.
- [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/)
  The checklist. Failures here are correctness bugs.
- [A Philosophy of Software Design — John Ousterhout](https://web.stanford.edu/~ouster/cgi-bin/book.php)
  Deep modules, shallow interfaces, complexity as the enemy. The code-taste half of the month.
- [Google: how to do a code review](https://google.github.io/eng-practices/review/)
  The standard the review gate is written against, including severity language.
- [Martin Fowler on architecture](https://martinfowler.com/architecture/)
  Vocabulary for patterns and refactoring.

### Month 9 — state, offline, real-time, browser security
- [OWASP XSS prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
  and the [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MDN: Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
  and [SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained)
- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) and
  [IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
  The two primitives the offline build stands on.
- [TanStack Query](https://tanstack.com/query/latest)
  Not to use blindly — to read as a well-designed cache with explicit semantics.

### Month 10 — neural nets by hand
- [Neural Networks: Zero to Hero — Andrej Karpathy](https://github.com/karpathy/nn-zero-to-hero)
  Backpropagation to a small GPT, built by hand. Start with
  [micrograd](https://github.com/karpathy/micrograd), then [nanoGPT](https://github.com/karpathy/nanoGPT),
  then [nanochat](https://github.com/karpathy/nanochat) for the full pipeline.
- [The Annotated Transformer — Harvard NLP](https://nlp.seas.harvard.edu/annotated-transformer/)
  The paper as runnable code. Pair with [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
- [PyTorch tutorials (official)](https://pytorch.org/tutorials/)
  Tensors, autograd, the training loop.
- [Fluent Python, 2nd ed — Luciano Ramalho](https://fluentpython.com/)
  This is the month Python stops being a scripting habit and becomes a real second language.

### Month 11 — LLM systems and their interfaces
- [Building effective agents — Anthropic engineering](https://www.anthropic.com/engineering/building-effective-agents)
  Workflow patterns versus agents, and when not to use an agent at all.
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) and
  [Model Context Protocol docs](https://modelcontextprotocol.io/)
  Working code for tools, and the protocol for the MCP server build.
- [OpenAI Evals](https://github.com/openai/evals) and [DSPy](https://dspy.ai/)
  Evaluation harnesses and prompt optimisation as engineering, not craft.
- [AI Engineering / Designing ML Systems — Chip Huyen](https://huyenchip.com/books/)
  The production side: evaluation, data, drift, cost.
- [MDN: server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
  The transport for the streaming interface build.
- [AI SDK docs](https://ai-sdk.dev/docs/introduction)
  Read for streaming UI patterns — then build yours without it, so you know what it does.
- [Chrome built-in AI](https://developer.chrome.com/docs/ai/built-in)
  On-device inference in the browser, and when it beats a server call.

### Read, do not build — the topics this plan cuts
- [Designing Data-Intensive Applications — Martin Kleppmann](https://dataintensive.net/)
  Read chapters 1–2 and 5 for vocabulary. You will not build a storage engine this year.
- [The Raft paper (extended)](https://raft.github.io/raft.pdf)
  Read it once, in Month 9, for the idempotency and replication ideas. Do not implement it.
- [Teach Yourself Computer Science](https://teachyourselfcs.com/)
  The map of everything this plan skips. Useful for year two, not for this year.
- [Build your own X](https://github.com/codecrafters-io/build-your-own-x)
  Index of "build your own <thing>" guides, if a month's build needs an alternative target.

## Wisdom (communities) — where the work gets tested by strangers

- [Codecrafters](https://codecrafters.io/) — paid challenges with real test suites (build your own
  Git, shell, interpreter, HTTP server). Use it when you want an external judge for a build instead of
  your own tests.
- [Julia Evans' blog and zines](https://jvns.ca/) — the best model of *how* to learn systems in
  public: small experiments, plain words, published. Use for how to write the monthly post.
- [Papers We Love](https://paperswelove.org/) — reading systems papers with other people. Presenting
  one is the fastest way to find your gaps.
- **A live mock interview with a real senior engineer, once a quarter.** Months 4, 6, 9, 12. Free
  option: a friend in the industry. Paid options are cheaper than a lost offer. The gate is worthless
  if you judge it yourself.
- **One meetup a month, with one question asked out loud.** Attending is not the goal. Asking is.

## Gaps — no strong source picked yet, find one before the month starts

- **Month 7, real-user monitoring:** this space is mostly vendor marketing. Need one vendor-neutral
  source on collecting field vitals before Month 7 starts.
- **Month 9, authentication done properly in TypeScript:** the OWASP material is broad and uneven.
  Need one focused, current source.
- **Spaced-repetition tool:** the daily plan needs one — [Anki](https://apps.ankiweb.net/) is the
  obvious candidate. Pick it in Week 1 and record the choice in `NOTES.md`.

