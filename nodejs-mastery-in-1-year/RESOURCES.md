# Node.js Resources

Every link on this page was checked and returned a live page on **2026-08-28**.
Two exceptions are marked below — Reddit and Stack Overflow block automated checks,
so those two were not machine-verified.

## Knowledge

### The primary source — read this before any blog post

- [Node.js API reference](https://nodejs.org/api/) — the docs for the runtime itself.
  Use for: the exact behaviour of any built-in module. This is the source that wins
  when a blog post disagrees with it.
- [Node.js Learn — Introduction](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
  Use for: the official framing of what Node is. Week 1.
- [Don't Block the Event Loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
  Official guide, and the most important page on the whole site for this course.
  Use for: weeks 1, 3, 22.
- [The Event Loop, Timers and `process.nextTick()`](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
  Use for: week 3. The phase order lives here — timers, pending, poll, check, close.
- [Asynchronous flow control](https://nodejs.org/en/learn/asynchronous-work/asynchronous-flow-control)
  Use for: weeks 5–7.

### Per-topic official docs

| Topic | Source | Weeks |
|---|---|---|
| Buffers and binary | [`buffer`](https://nodejs.org/api/buffer.html) | 14 |
| Streams | [`stream`](https://nodejs.org/api/stream.html) · [How to use streams](https://nodejs.org/en/learn/modules/how-to-use-streams) | 15–17 |
| Backpressure | [Backpressuring in Streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams) | 15 |
| Events | [`events`](https://nodejs.org/api/events.html) | 18 |
| TCP sockets | [`net`](https://nodejs.org/api/net.html) | 19 |
| HTTP server | [`http`](https://nodejs.org/api/http.html) | 20–21 |
| Modules | [`esm`](https://nodejs.org/api/esm.html) · [`modules`](https://nodejs.org/api/modules.html) · [`packages`](https://nodejs.org/api/packages.html) | 9, 11 |
| Publishing a package | [Publishing a package](https://nodejs.org/en/learn/modules/publishing-node-api-modules) | 11–12 |
| Process and signals | [`process`](https://nodejs.org/api/process.html) | 10, 27 |
| Errors | [`errors`](https://nodejs.org/api/errors.html) | 6, 28 |
| Worker threads | [`worker_threads`](https://nodejs.org/api/worker_threads.html) | 23 |
| Child processes | [`child_process`](https://nodejs.org/api/child_process.html) | 24 |
| Cluster | [`cluster`](https://nodejs.org/api/cluster.html) | 24–25 |
| Async context | [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html) | 29 |
| Instrumentation hooks | [`diagnostics_channel`](https://nodejs.org/api/diagnostics_channel.html) | 29 |
| Profiling | [Profiling a Node.js app](https://nodejs.org/en/learn/getting-started/profiling) | 31 |
| Memory | [Memory diagnostics](https://nodejs.org/en/learn/diagnostics/memory) | 32 |
| Testing | [`node:test`](https://nodejs.org/api/test.html) · [Test runner intro](https://nodejs.org/en/learn/test-runner/introduction) | 35–36 |
| Security | [Security best practices](https://nodejs.org/en/learn/getting-started/security-best-practices) | 37 |
| TypeScript in Node | [Node + TypeScript](https://nodejs.org/en/learn/typescript/introduction) | 44–46 |

### Below the runtime — why Node behaves as it does

- [libuv design overview](https://docs.libuv.org/en/v1.x/design.html)
  The C library that gives Node its event loop and its thread pool. Use for: week 1
  and week 22 — the honest answer to "what does the thread pool actually do?".
- [V8 documentation](https://v8.dev/docs)
  The JavaScript engine. Use for: week 32, when a heap snapshot needs interpreting.
- [nodejs/node on GitHub](https://github.com/nodejs/node)
  The runtime's own source. Use for: settling an argument the docs leave open.

### Books, talks, and long-form

- Talk: [Everything You Need to Know About Node.js Event Loop — Bert Belder](https://www.youtube.com/watch?v=zphcsoSJMvM)
  A Node core maintainer correcting the common wrong diagrams. Use for: week 3.
  Watch it *after* reading the official event loop page, not before.
- Talk: [What the heck is the event loop anyway? — Philip Roberts](https://www.youtube.com/watch?v=PNa9OMajw9w)
  The clearest visual explanation of the call stack, queue, and loop. It is about the
  **browser**, so the phase detail does not transfer — take the mental model, not the
  specifics. Use for: week 1.
- [Node.js Best Practices — Yoni Goldberg](https://github.com/goldbergyoni/nodebestpractices)
  Community-maintained, heavily cited, and organised by concern. Use for: weeks 27–38,
  and as an interview checklist in review weeks.
- [OWASP Node.js Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
  Use for: week 37.
- [MDN — Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
  and [MDN — `Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
  Use for: weeks 5–7. MDN is the better source than the Node docs for the language itself.

### Libraries the course actually uses

| Library | What it is | Weeks |
|---|---|---|
| [undici](https://github.com/nodejs/undici) | The HTTP client behind `fetch` in Node. Read it when `fetch` behaves oddly. | 7–8 |
| [p-limit](https://github.com/sindresorhus/p-limit) | A concurrency limiter, ~40 lines. Read the source; write your own first. | 7 |
| [pino](https://getpino.io/) | Structured JSON logging, fast enough to leave on. | 29 |
| [autocannon](https://github.com/mcollina/autocannon) | HTTP load generator. Every performance claim in this course goes through it. | 30, 34 |
| [Clinic.js](https://clinicjs.org/) | Profiling suite — flame graphs, event-loop delay, memory. | 31–34 |
| [node-postgres](https://node-postgres.com/) | The Postgres client. Pools and transactions. | 40, 43 |
| [Redis docs](https://redis.io/docs/latest/develop/) | Caching. | 41 |
| [BullMQ](https://docs.bullmq.io/) | The job queue used for background work. | 42–43 |
| [TypeScript](https://www.typescriptlang.org/docs/) · [tsconfig reference](https://www.typescriptlang.org/tsconfig/) · [tsx](https://tsx.is/) | Types and the build setup. | 44–46 |
| [NestJS](https://docs.nestjs.com/) · [Providers / DI](https://docs.nestjs.com/providers) · [Testing](https://docs.nestjs.com/fundamentals/testing) | The professional rebuild. | 47–50 |

## Wisdom (Communities)

Knowledge comes from the docs above. Wisdom comes from being corrected by people who
have run Node in production. Pick **one** and actually post in it — lurking is not
the exercise.

- [Node.js official Discord](https://discord.com/invite/nodejs)
  Run by the project. Highest signal for "is this behaviour a bug or my mistake".
  **Recommended first.** Use for: a real question in review week 13.
- [r/node](https://www.reddit.com/r/node/) — *not machine-checked; Reddit blocks
  automated requests.* Mixed quality, but good for code review of a small project.
  Use for: posting the week 12 CLI and the week 25 thumbnail service.
- [Stack Overflow `node.js` tag](https://stackoverflow.com/questions/tagged/node.js)
  — *not machine-checked; Stack Overflow blocks automated requests.* Use for: reading
  well-answered old questions, not for asking. Answering one is a review-week drill.
- [Node Weekly](https://nodeweekly.com/)
  A newsletter, not a community, but it is how you notice the runtime changed.
- [OpenJS Foundation](https://openjsf.org/)
  The governing body. Use for: release schedules and which Node version is LTS.

### Engineering blogs worth following

- [Platformatic blog](https://blog.platformatic.dev/) — written by Node core and
  Fastify maintainers. Deep, current, and often about performance.
- [Nearform insights](https://www.nearform.com/insights/) — the team behind Clinic.js.
  Use for: diagnostics and profiling write-ups.
- [NodeSource blog](https://nodesource.com/blog/) — mixed with marketing, but the
  memory and event-loop posts are solid.

## Gaps

Areas the mission needs where no single strong source was found yet:

- **NestJS beyond the official docs.** The docs are good on syntax and thin on
  architecture at scale. No trusted "large NestJS codebase" write-up found yet.
  Fill this before week 47.
- **Node system-design interviews.** General system-design material exists in volume;
  Node-specific material (when a worker pool, when a separate service, when not Node
  at all) is mostly absent. Week 51 currently relies on this course's own material.
- **Real memory-leak case studies.** Week 32 needs a leak with a public post-mortem.
  Candidates exist but none verified as high-trust yet.

## Community preference

No preference recorded yet. The recommendation on file is the **official Node.js
Discord** first, because the correction quality is highest there.
