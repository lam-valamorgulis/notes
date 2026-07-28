# Vibe Coding Platform — Architecture Resources

## Knowledge

### Primary source — the code itself

- [vercel/examples → apps/vibe-coding-platform](https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform)
  **The single highest-trust source for this course.** ~110 files. Every claim in every
  lesson must be traceable here. Read at commit `72aaac1` (2026-05-05).
  Use for: literally everything. When a lesson and the repo disagree, the repo wins.
- [The live demo](https://oss-vibe-coding-platform.vercel.app/)
  The running system. Use for: watching the streamed data parts arrive in real time
  (open DevTools → Network → the `/api/chat` response) before reading how it works.
- [Vercel template page](https://vercel.com/templates/next.js/vibe-coding-platform)
  The deploy wrapper. Use for: nothing technical — its feature copy is out of date
  (still says "GPT-5"). Noted here so it is not mistaken for a source.

### The AI SDK — the framework the whole backend is built on

- [AI SDK docs](https://ai-sdk.dev)
  Official docs for `streamText`, `tool`, `useChat`. The repo pins AI SDK v6.
- [Streaming Custom Data](https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data)
  **The most important single page for this course.** Explains the custom data-part
  mechanism that `ai/messages/data-parts.ts` is built on. Use for: Lesson 2.
- [Tools and Tool Calling](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling)
  How `tool({ description, inputSchema, execute })` works. Use for: Lessons 4–6.
- [Agents: Loop Control](https://ai-sdk.dev/docs/agents/loop-control)
  Covers `stopWhen` / `stepCountIs`, the mechanism capping the agent at 20 steps.
  Use for: the "how do you stop an agent looping forever?" interview question.

### Vercel platform pieces

- [Vercel Sandbox docs](https://vercel.com/docs/vercel-sandbox)
  The isolated Amazon Linux 2023 VM the agent writes into. Covers `Sandbox.create`,
  `writeFiles`, `runCommand`, timeouts, port exposure. Use for: Lessons 4 and 6.
- [Vercel AI Gateway docs](https://vercel.com/docs/ai-gateway)
  One endpoint, many model providers. Explains why `ai/gateway.ts` can swap Claude for
  Grok with a string change. Use for: Lesson 11 and the multi-model trade-off.
- [BotID docs](https://vercel.com/docs/botid)
  The invisible bot check wrapping both AI routes. Use for: Lesson 10 (security).

### Front-end pieces

- [Zustand docs](https://zustand.docs.pmnd.rs/)
  The client store in `app/state.ts`. Use for: Lesson 3 (where state lives).
- [SWR docs](https://swr.vercel.app/)
  Used for model list fetching and revalidation on tool call.
- [shadcn/ui](https://ui.shadcn.com) and [Tailwind CSS](https://tailwindcss.com)
  The component and styling layer. **Low priority** — explicitly out of scope in
  [MISSION.md](./MISSION.md), listed only for completeness of the stack answer.

## Wisdom (Communities)

- [Vercel Community](https://community.vercel.com/)
  Official forum, actively staffed by Vercel engineers. Use for: asking whether a
  trade-off reading is correct — e.g. "is a single shared sandbox per session a
  deliberate choice or a demo simplification?" Good place to test an architectural
  opinion before saying it in an interview.
- [AI SDK GitHub Discussions](https://github.com/vercel/ai/discussions)
  Where the AI SDK maintainers answer design questions. Use for: verifying claims about
  `streamText`, data parts, and loop control straight from the people who wrote it.
- [vercel/examples Issues and PRs](https://github.com/vercel/examples/issues)
  Use for: seeing which trade-offs the maintainers already know about. A trade-off the
  maintainers have publicly acknowledged is a *much* safer thing to raise in an interview
  than one invented from scratch.

## Gaps

- **No official architecture write-up exists for this app.** There is no blog post or
  design doc explaining *why* it is shaped this way. Every trade-off in this course is
  therefore read from the code, not quoted from the authors. Lessons must say so plainly,
  and the interview framing should be "reading the code, my read is…" rather than
  "Vercel says…". This is an honesty requirement, not a style preference.
- **No test suite in the repo.** There is nothing to learn from about how the authors
  would test an agent loop. If the interview goes toward testing agents, that has to come
  from elsewhere.
- **Community links above are listed but not yet used.** Lam has not said whether he wants
  to post publicly. Ask before recommending he open a thread.
