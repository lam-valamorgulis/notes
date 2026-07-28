# Gap review — a tech lead reads the course so far

Date: 2026-07-28. Reviewed against the repo at commit `72aaac1`.

This is a candid review of the course as it stood after the first session: **Lesson 1 (the
agent loop)** and the **glossary**. I am reviewing my own work, so the tone is direct. The
goal is not to defend the lessons. The goal is to find every place a reader would get stuck,
then fix it.

I read all ~110 files in the repo before writing this. Several gaps below exist because the
first session had not yet read the files that reveal them.

---

## How I reviewed

Three passes, each asking a different question.

1. **Junior pass.** "A capable engineer who has never built an AI feature reads Lesson 1.
   Where do they stop understanding?"
2. **Senior pass.** "A strong engineer reads the repo. What would they still get wrong or
   fail to notice?"
3. **Coverage pass.** "What is in the repo that no lesson mentions at all?"

The third pass found the biggest hole: **the course taught the agent and skipped the
framework.** Lesson 1 names files like `app/api/chat/route.ts` as if the reader already knows
what a Route Handler is. That is a real teaching failure, and it is what the new Week 1 fixes.

---

## Part 1 — Gaps a junior would hit

Ordered by how badly they block progress. "Blocks" means the reader cannot continue
honestly; "slows" means they can proceed but with a fuzzy model.

| # | Gap | Why it hurts | Now taught |
|---|---|---|---|
| 1 | **No Next.js grounding.** Lesson 1 uses `route.ts`, `layout.tsx`, `page.tsx` without ever saying what they are. | Blocks. Every file path is meaningless. | Days 2–7 |
| 2 | **Which code runs where.** Nothing explains `'use client'`, or that `app/state.ts` runs in the browser while `route.ts` never does. | Blocks. This is *the* Next.js confusion. | Day 3 |
| 3 | **What "streaming" means over HTTP.** Lesson 1 says "streamed as it happens". A junior will assume WebSockets. | Blocks. It is one long HTTP response, not a socket. | Day 5 |
| 4 | **Zod is never introduced.** `inferSchema`, `.describe()`, `safeParse` all appear with no explanation. | Blocks. Zod does double duty here: it validates input *and* tells the model what the arguments mean. | Day 9 |
| 5 | **How the model "picks" a tool.** Lesson 1 says the model picks one. It does not say the model emits structured JSON that the SDK matches against the schema and dispatches. | Blocks. Otherwise it reads as telepathy. | Day 9 |
| 6 | **Async generators.** `async function*`, `yield`, `for await...of` are central to file generation and log streaming. Never mentioned. | Blocks Days 17–18. | Day 5, Day 17 |
| 7 | **`toolCallId` as an update key.** Mentioned once in a recall card. It is the reason a status card updates in place instead of duplicating. | Slows, then confuses. | Day 8 |
| 8 | **Where secrets and auth come from.** `.env.example` has exactly one line: `AI_GATEWAY_API_KEY`. How does it authenticate to Sandbox? Never asked. | Slows. Also a common interview question. | Day 25 |
| 9 | **No cost intuition.** A 148-line system prompt resent across 20 steps costs real money. Without that, prompt caching and the bot check look like decoration. | Slows badly — it hides *why* half the design exists. | Day 24 |
| 10 | **Scary SDK generics.** `UIMessageStreamWriter<UIMessage<never, DataPart>>` appears with no help. | Slows. Readers skip code they find intimidating. | Day 8 |
| 11 | **The four panels are never explained as a layout.** Resizable panels, cookie-persisted sizes, and a separate mobile tab layout are all real features. | Slows. It is also the most visible part of the product. | Day 4 |
| 12 | **Settings live in the URL, not in React state.** The repo uses `nuqs` so model choice is a query parameter. Completely absent from the course. | Slows. It is a genuinely interesting design choice. | Day 6 |
| 13 | **Error-handling helpers.** `getRichError` and the custom `Deferred` class look like noise until you know what problem each solves. | Slows. | Day 26 |
| 14 | **Small real features unmentioned.** Prompt input saved to local storage, ANSI colour codes stripped from logs, model list cached for 300 seconds. | Minor, but juniors notice and wonder. | Day 27–28 |

---

## Part 2 — Gaps even a strong senior would have

These are the things I would expect a good engineer to miss on a first read. Each one is an
interview weapon, because noticing it proves you read the code rather than the README.

### 1. Why is there a second model call *inside* a tool?
`generate-files.ts` calls `streamText` again, with its own system prompt and
`reasoningEffort: 'low'` hard-coded (`ai/tools/generate-files/get-contents.ts`). Most people
assume one agent loop. The obvious guess — "to keep file contents out of the main context" —
**is wrong**: the tool's return string includes the full contents of every file it wrote. So
the contents land in the main context anyway. The real reasons look like forced structured
output, a cheaper effort setting for a mechanical task, and streaming files out early.
→ **Day 16**

### 2. The `- 2` in the partial-output slice
```ts
items.files.slice(generated.length, items.files.length - 2)
```
While a structured answer is still streaming, the last one or two array entries are
half-written. The code deliberately ignores the tail so it never uploads a truncated file.
This off-by-two is the kind of detail that separates "I read it" from "I skimmed it".
→ **Day 17**

### 3. `consumeStream()` + `sendStart: false` + `writer.merge()`
Three lines of stream plumbing in `route.ts` that most readers skip. They control who owns
the stream and prevent a duplicate "start" event when merging the model output into an
already-open custom stream.
→ **Day 8**

### 4. Data parts are rewritten before the model sees them
In `route.ts`, every `data-report-errors` part is converted into a plain text message *before*
`convertToModelMessages` runs. So the auto-fix feature travels as typed data on the client
and as prose to the model. A protocol bridge hiding in a `.map()`.
→ **Day 20**

### 5. The "unified" model interface is not unified
`getModelOptions()` special-cases OpenAI (`serviceTier`, `reasoningEffort`) and Anthropic
(prompt caching, a `anthropic-beta` header). The gateway abstracts *providers*, not
*capabilities*. Every real multi-model system has this leak.
→ **Day 24**

### 6. The error monitor has four independent brakes
A feature that sends messages to itself must not spin. `error-monitor.tsx` layers: a 10-second
debounce, a 60-second minimum gap, a per-error-key counter capped at one, and a cursor marking
already-inspected logs. Most engineers ship one brake and get a runaway loop.
→ **Day 20**

### 7. The errors route bypasses the custom gateway
`app/api/errors/route.ts` passes `model: Models.OpenAIGPT53Codex` — a raw string — instead of
going through `getModelOptions()`. So that call skips the custom `baseURL` and the
attribution headers set in `ai/gateway.ts`. Reading the code, my read is that this is an
inconsistency rather than an intention.
→ **Day 26**

### 8. BotID protects one route on the client, two on the server
`instrumentation-client.ts` registers only `/api/chat` in `protect[]`, yet
`app/api/errors/route.ts` also calls `checkBotId()`. Worth raising as a question, not a
verdict — I have not proven the behaviour, only read the registration.
→ **Day 25**

### 9. Reaching into a package's `dist/` folder
`get-rich-error.ts` imports from `@vercel/sandbox/dist/api-client/api-error` — a private path
that no semver promise covers. A small, real smell.
→ **Day 26**

### 10. Two different Zod import paths
Nearly every file imports `zod/v3`; `components/error-monitor/schemas.ts` imports plain
`zod`. A migration artefact. Good "what would you tidy?" answer.
→ **Day 26**

### 11. `ChatUIMessage` is fully typed; the tool writer is not
`components/chat/types.tsx` builds `UIMessage<Metadata, DataPart, ToolSet>`, but
`ai/tools/index.ts` types the writer as `UIMessage<never, DataPart>`. The same message,
described two ways in two places.
→ **Day 8**

### 12. Panel sizes are read on the *server*
`page.tsx` is an async Server Component that reads cookies to get saved panel sizes before
rendering. The client writes those cookies with `document.cookie`. Result: no layout jump on
reload. A genuinely elegant trick, easy to miss.
→ **Day 4**

### 13. The model controls its own blocking
`runCommand` takes a `wait` boolean, and the *model* decides it. Handing concurrency control
to a language model is a real design decision and a fair thing to challenge.
→ **Day 18**

### 14. There are no tests at all
Zero test files. The repo offers no answer to "how would you test an agent loop?" — so that
answer has to be built from scratch.
→ **Day 29**

### 15. The sandbox status check is a hack the authors documented
`app/api/sandboxes/[sandboxId]/route.tsx` answers "is this sandbox alive?" by running
`echo` inside it and catching an `APIError` with code `sandbox_stopped`. Above it sits the
maintainers' own comment: *"We must change the SDK to add data to the instance and then use
it to retrieve the status of the Sandbox."* A health check that costs a real command
execution. **This is the safest trade-off in the whole course to raise in an interview**,
because you are agreeing with a comment the authors wrote, not second-guessing them.
→ **Day 5** (taught), **Day 22** (as a trade-off)

### 16. Input validation is inconsistent across route handlers
The `files` route validates the path and query together with `FileParamsSchema.safeParse`
before touching the sandbox. The `logs` route and the `status` route pass awaited path
parameters straight into `Sandbox.get()` with no validation at all. Same codebase, same kind
of input, two different standards. My read is drift rather than intent.
→ **Day 5**

### 17. One tool breaks the pattern the other three follow
`get-sandbox-url.ts` differs from its three siblings in two ways: it returns an **object**
(`{ url }`) where the others return **strings**, and it has **no `try`/`catch`**, so it never
produces a `getRichError` message the way the others do. If `Sandbox.get` fails there, the
model gets a raw exception instead of a helpful sentence. A small but real consistency gap in
the most important interface in the app.
→ **Day 9** (tool design), **Day 26** (error handling)

---

## Part 3 — What was missing entirely: Next.js

The original plan had twelve lessons and **not one** covered the framework. Yet the repo
leans on a lot of Next.js, all of it verified in the source:

| Feature | Where | Why it matters here |
|---|---|---|
| App Router (`layout.tsx`, `page.tsx`) | `app/` | The whole file structure |
| Async Server Component | `app/page.tsx` | Reads cookies before render |
| `cookies()` from `next/headers` | `app/page.tsx` | Panel sizes, banner state |
| Server Action (`'use server'`) | `app/actions.ts` | Dismissing the welcome banner |
| `revalidatePath` | `app/actions.ts` | Refreshing after the cookie is set |
| Client Components (`'use client'`) | `app/chat.tsx` and most of `components/` | The interactive half |
| Route Handlers | six files under `app/api/` | The entire back end |
| Dynamic segments with async `params` | `app/api/sandboxes/[sandboxId]/...` | `params` is a Promise now |
| Streaming with `ReadableStream` | files and logs routes | Live logs and file reads |
| `Metadata` export | `app/layout.tsx` | Title, description, social images |
| `next.config.ts` custom loaders | `next.config.ts` | Importing `.md` as a string |
| Turbopack rules | `next.config.ts` | Same trick for the dev server |
| Image `remotePatterns` and CSP | `next.config.ts` | Avatar images, SVG hardening |
| `instrumentation-client.ts` | root | Client startup hook for BotID |
| Route-level `Cache-Control` | `app/api/models/route.tsx` | 300-second cache |
| TS module declaration | `markdown.d.ts` | Makes `import x from './y.md'` type-check |
| `Suspense` in the root layout | `app/layout.tsx` | Required by URL-state reading |

That table is now **Week 1** of the plan, plus a printable reference page.

---

## Part 4 — What changed as a result

- The course went from **12 lessons** to a **30-day plan**, two hours per day.
- A new **Week 1** teaches Next.js as this repo actually uses it — every example is a real
  file, not a tutorial toy.
- Every senior gap above is assigned to a specific day, so none of them get lost.
- Two review-and-drill days (14, 21) and a final mock interview (30) were added, because
  spacing and retrieval matter more than new material in the last week.
- `GAPS.md` — this file — stays in the workspace as the checklist. When a day is finished,
  the matching gap should be defensible **out loud**, not just read.

---

## Honest limits of this review

- I have read the code, not run it. Items 7 and 8 above are readings, not proven behaviour.
  Say "my read is…" when raising them.
- There is no official design document for this app, so every "why" in this course is
  inference from source. That framing is required, not optional.
- The repo moves. This review is pinned to commit `72aaac1` (2026-05-05). Re-read before
  trusting any file quote.
