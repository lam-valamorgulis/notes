# Mission: Node.js

## Why
Node.js is the runtime this career runs on next. The goal, in order: **pass a Node
backend interview, then be the person at work who can debug what nobody else can,
then run a product alone.** The gap it closes is not syntax. It is knowing what the
runtime is really doing under a request, and being able to say it out loud.


## Success looks like
- Can predict the print order of any mix of sync code, `setTimeout`, `process.nextTick`
  and `Promise.then`, and explain the rule that produced it.
- Can write, live and without notes, a fetch of 500 URLs at 10 at a time, with
  retries and timeouts.
- Can move a 4 GB file through a Node process in constant memory, and explain
  backpressure without saying "it just handles it".
- Can take a service that freezes under CPU-heavy work and fix it — with a worker
  pool, with `cluster`, or by saying honestly that Node is the wrong tool here.
- Can find a real memory leak with a heap snapshot, and say what held the reference.
- Can shut a server down without dropping a single in-flight request.
- Can rebuild the same API in **NestJS** and say what dependency injection bought,
  and what it cost.
- Can sit in a system-design round and design a Node service end to end — queues,
  cache, database, failure modes — and defend every choice.

## Domain expert goal
> "Give me any Node service and I can say what it is doing on the single thread,
> where it will break under load, and how to prove it — then fix it and explain
> the fix to a room."

The standard for expert stays the five abilities:

- Explain it from first principles, with no jargon and no notes
- Predict how it behaves in a case never seen before
- Say why it was built this way, and what that choice gives up
- Debug a problem in it that has no ready answer online
- Judge someone else's work in it, and say what is wrong and why

## The shape of the year
The year is **52 weeks**, not 12 months. A week is the unit of work, because a week
is the unit you actually plan your life in. Every week has one goal, one thing to
build, skills to tick, and a drill.

Weeks group into **13 modules** inside **4 phases of 13 weeks**. Ten modules are four
weeks long; module 11 is three and module 13 is two. Weeks 13, 26 and 39 stand outside
every module, because a review week belongs to none of them. The last week of every phase (13, 26, 39, 52) is a **review week** —
no new material, only retrieval practice, interleaved drills, and a mock interview.
That is deliberate. Spacing and interleaving are what turn fluency into memory.

| Phase | Weeks | Name | The question it answers |
|---|---|---|---|
| 1 | 1–13 | The runtime | What is Node actually doing, and how does async really work? |
| 2 | 14–26 | The hard core | Streams, servers from raw sockets, and more than one thread. |
| 3 | 27–39 | Production | Will it survive real traffic, and can you prove it? |
| 4 | 40–52 | Professional | Data, TypeScript, NestJS, and saying all of it under pressure. |

From **week 21 onward there is one API** — the spine. Every later week hardens the
same service rather than starting a new toy. That is on purpose: a real system
teaches things twelve toys cannot.

The full week list is in [reference/52-week-plan.html](reference/52-week-plan.html).

## The 20% core
Twelve items, listed in teaching order. Nothing outside this list is taught until
these are solid. Everything else is **depth** — queued, not deleted.

Every item names the weeks that serve it, so the claim is checkable rather than
decorative. The twelve account for **42** weeks, and week 51 is a 43rd core week that
belongs to all twelve at once — so **43 of the 52 weeks are core**. The other nine are
five depth weeks and four review weeks. Note that four of the depth weeks (11, 29, 33,
45) sit *inside* an item's week range: a four-week module can carry one depth week.

1. **The event loop, and the one rule** — one thread runs your JavaScript, and
   blocking it stops every other request. This is the fact every other Node fact
   hangs off. *Weeks 1–4, 22.*
   ([Don't Block the Event Loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop),
   [Event Loop, Timers and nextTick](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick))
2. **The async model end to end** — promises, `async`/`await`, and how an error
   travels through them. Async error handling is the single most common source of
   silent production failure. *Weeks 5–6.*
   ([Errors](https://nodejs.org/api/errors.html),
   [Node Best Practices §2](https://github.com/goldbergyoni/nodebestpractices))
3. **Bounded concurrency** — running N things at once, with a limit, a timeout, and
   a retry. Unbounded `Promise.all` over a big list is the most common way a Node
   service kills itself or a downstream API. *Weeks 7–8.*
   ([MDN: Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise))
4. **The module system** — CommonJS versus ESM, how Node resolves a specifier, and
   the process APIs a real command-line tool needs. Every project hits this, usually
   as an error message at 6pm. *Weeks 9–12.*
   ([ESM](https://nodejs.org/api/esm.html), [packages](https://nodejs.org/api/packages.html),
   [process](https://nodejs.org/api/process.html))
5. **Streams and backpressure** — moving data larger than memory, and the pull model
   that stops a fast producer drowning a slow consumer. *Weeks 14–17.*
   ([stream](https://nodejs.org/api/stream.html),
   [Backpressuring in Streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams))
6. **EventEmitter, and the server built on it** — the pattern the runtime itself is
   made from. Streams, sockets, processes and the HTTP server are all emitters, so
   learning it once explains all of them — and then `http` stops being magic.
   *Weeks 18, 20, 21.*
   ([events](https://nodejs.org/api/events.html), [http](https://nodejs.org/api/http.html))
7. **Beyond one thread** — worker threads for CPU work, `cluster` for using every
   core. The honest answer to "Node is single-threaded, so how do you scale?"
   *Weeks 22–25.*
   ([worker_threads](https://nodejs.org/api/worker_threads.html),
   [cluster](https://nodejs.org/api/cluster.html))
8. **Process lifecycle** — signals, graceful shutdown, and the difference between an
   operational error and a programmer error. This is what separates "a script" from
   "a service". *Weeks 27–30.*
   ([process signals](https://nodejs.org/api/process.html#signal-events),
   [errors](https://nodejs.org/api/errors.html))
9. **Measure before you fix** — CPU profiles and heap snapshots. A performance claim
   with no measurement behind it is an opinion. *Weeks 31–34.*
   ([Profiling](https://nodejs.org/en/learn/getting-started/profiling),
   [Memory diagnostics](https://nodejs.org/en/learn/diagnostics/memory))
10. **Evidence — tests that do not flake, and input you hardened** — `node:test`,
    mocking, coverage you can defend, and the boundary checks that stop a JSON body
    hurting you. Both halves answer the same question: *how do you know?*
    A flaky test is worse than no test, because it teaches the team to ignore red.
    *Weeks 35–38.*
    ([node:test](https://nodejs.org/api/test.html),
    [Security best practices](https://nodejs.org/en/learn/getting-started/security-best-practices),
    [OWASP Node.js Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html))
11. **The data layer** — a connection pool, a transaction, a cache, and a job queue.
    These four are in almost every production Node service. *Weeks 40–43.*
    ([node-postgres](https://node-postgres.com/), [BullMQ](https://docs.bullmq.io/))
12. **TypeScript, then NestJS** — the shape professional Node teams actually hire for.
    Nest is the choice for this course, not Express, because the interview target is
    structured backend teams. *Weeks 44–50.*
    ([TypeScript](https://www.typescriptlang.org/docs/),
    [NestJS](https://docs.nestjs.com/))

**Week 51 belongs to no single item.** System design is where all twelve are used at
once, under pressure, with nothing to look at. It is core because the mission is an
interview, and it is the only week that is core by synthesis rather than by subject.

Two items are ranked lower than instinct suggests, and the plan page says so on each
card: `net` and raw TCP is **depth** (week 19), and `diagnostics_channel` with
`AsyncLocalStorage` is **depth** (week 29). Both are real. Neither is touched weekly
by a Node backend engineer.

## Constraints
- **~10 hours a week.** Roughly 2 hours on the lesson, 1 hour on the primary source,
  6–7 hours building. About 520 hours over the year.
- **Starting point: comfortable with JavaScript and React; new to Node in depth.**
  Week 2 is an *audit* of the JavaScript that Node leans on, not a re-teach. If the
  audit is easy, week 2 is a short week — that is the intended outcome.
- **NestJS, not Express.** Fixed for the year. Express appears only as the thing Nest
  runs on top of.
- **The spine API from week 21.** One service, hardened for 30 weeks. Do not restart it.

## Out of scope
- **Express as a subject.** Learned incidentally, never taught.
- **Deno and Bun.** Interesting, not the hiring target.
- **Frontend JavaScript.** Covered by [the React course](../react-mastery-in-1-year/index.html)
  and [the Frontend tree](../frontend-mastery-tree/index.html).
- **LeetCode-style algorithm puzzles.** The interview drills here are Node drills.
- **Kubernetes and cloud platform work.** Deployment appears only as far as the spine
  API needs it.
