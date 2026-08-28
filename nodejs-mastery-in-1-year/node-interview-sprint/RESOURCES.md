# 7-Day Node.js Interview Sprint — Resources

Every link below returned a live page on **2026-08-28**. One exception is marked.

Read the primary source for the day you are on. Do not read ahead. The reading
is there to back up an answer you will say out loud, not to add new topics.

## Day 1 — The runtime

- [The event loop, timers, and `process.nextTick`](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
  The single most quoted page in Node interviews. Use for: phase order, and why
  `process.nextTick` runs before promises.
- [Don't block the event loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
  Use for: the one rule. Blocking the thread stops every other request.
- [libuv design overview](https://docs.libuv.org/en/v1.x/design.html)
  Use for: the honest answer about the thread pool. Node is not single-threaded
  all the way down.

## Day 2 — Async under pressure

- [MDN — `Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
  Use for: `all`, `allSettled`, `race`, `any`. Know which one keeps going.
- [Node — Errors](https://nodejs.org/api/errors.html)
  Use for: error classes, `error.code`, and what an unhandled rejection does.
- [Asynchronous flow control](https://nodejs.org/en/learn/asynchronous-work/asynchronous-flow-control)
  Use for: the ladder from callbacks to promises, in the official words.
- [`p-limit`](https://github.com/sindresorhus/p-limit)
  Use for: the library you name after you have written the pool by hand.

## Day 3 — Streams and memory

- [Backpressuring in streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams)
  The best single page on the topic anywhere. Use for: why `write()` returns a
  boolean, and what ignoring it costs.
- [Node — `stream`](https://nodejs.org/api/stream.html)
  Use for: `pipeline`, `highWaterMark`, and the four stream types.
- [Node — `readline`](https://nodejs.org/api/readline.html)
  Use for: reading a file line by line without holding it in memory.
- [Node — `buffer`](https://nodejs.org/api/buffer.html)
  Use for: bytes versus characters, and why cutting a chunk can break a letter.

## Day 4 — Your own service

Your service is the source here. There is no page to read.

- [Node — `http`](https://nodejs.org/api/http.html)
  Use for: the exact objects your handlers receive.
- [Node — `events`](https://nodejs.org/api/events.html)
  Use for: the pattern under `req` and `res`. Both are emitters.
- [NestJS docs](https://docs.nestjs.com/)
  Use for: the rebuild story, and what dependency injection bought.

## Day 5 — Production

- [Node — `process`](https://nodejs.org/api/process.html)
  Use for: signals, `process.exitCode`, and `uncaughtException`.
- [Memory diagnostics](https://nodejs.org/en/learn/diagnostics/memory)
  Use for: heap snapshots and the retainer path.
- [Profiling](https://nodejs.org/en/learn/getting-started/profiling)
  Use for: `--cpu-prof`, and self time versus total time.
- [Node — `perf_hooks`](https://nodejs.org/api/perf_hooks.html)
  Use for: `monitorEventLoopDelay`, the number that proves a hang.
- [`autocannon`](https://github.com/mcollina/autocannon)
  Use for: producing the load you profile under.

## Day 6 — Scale and design

- [Node — `worker_threads`](https://nodejs.org/api/worker_threads.html)
  Use for: separate memory, message copying, and `transferList`.
- [Node — `cluster`](https://nodejs.org/api/cluster.html)
  Use for: one process per core, and why they share nothing.
- [node-postgres](https://node-postgres.com/)
  Use for: the connection pool answer, with real numbers.
- [BullMQ](https://docs.bullmq.io/)
  Use for: the queue answer. Retries, backoff, and the dead-letter queue.
- [Redis — develop](https://redis.io/docs/latest/develop/)
  Use for: cache invalidation and the TTL you can defend.
- [`undici`](https://github.com/nodejs/undici)
  Use for: the HTTP client answer, and connection reuse.

## Day 7 — The mock

- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
  Use for: a last skim. Read the headings only, not the bodies.
- [OWASP Node.js Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html)
  Use for: the one security question that always comes.
- [Node — `node:test`](https://nodejs.org/api/test.html)
  Use for: "how do you test async code without flakes".

## Wisdom (communities)

- [Node.js official Discord](https://discord.com/invite/nodejs)
  The highest correction quality anywhere. Use for: sanity-checking an answer
  before you say it in an interview.
- r/node — `https://www.reddit.com/r/node/`. **Not machine-checked**: Reddit
  blocks automated requests, so this link was not confirmed on 2026-08-28.

## Gaps — stated honestly

- No public source describes any specific company's Node interview loop.
  Every prediction in this sub-course is an informed guess, not a leak.
- The numbers in these lessons are real measurements on one machine, on
  **Node v24.14.0**, on **2026-08-28**. Another machine gives different numbers.
  The **shape** of the result is the durable part, not the digits.
