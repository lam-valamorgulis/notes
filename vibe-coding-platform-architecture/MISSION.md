# Mission: Vibe Coding Platform — Architecture Deep Dive

## Why

Lam is interviewing for **AI Engineer** roles. Talking about "I used the AI SDK" is not
enough at that level — interviewers push on *why the system is shaped this way* and *what
you would change*. This repo (Vercel's open-source
[vibe-coding-platform](https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform))
is a real, production-grade agent product that is small enough to hold in one head. Learning
it end to end gives Lam one concrete system he can reason about out loud, under pressure,
for the whole interview loop — architecture, trade-offs, and the full stack.

## Success looks like

- Draw the whole request lifecycle from memory on a whiteboard in under 3 minutes:
  browser → `/api/chat` → agent loop → tool → Sandbox → streamed data part → UI panel.
- Explain the **custom data-part streaming protocol** and why it beats returning tool
  results as plain text.
- Name any of the five features (sandbox, file generation, run command, preview,
  auto-fix errors) and walk it end to end, naming the real files involved.
- State at least 8 architectural trade-offs as "they chose X, which costs Y, and I would
  consider Z instead" — without notes.
- Answer "why is there a second LLM call inside the `generate-files` tool?" correctly.
- Name every backend and frontend technology in the stack and justify why it is there.
- Survive a 45-minute mock interview on this system, answering aloud, not in writing.

## Constraints

- The interview is the deadline — depth on architecture and trade-offs beats breadth on
  syntax. Do not spend time on CSS details or shadcn component internals.
- Every claim must be traceable to a real file in the repo. No hand-waving from memory —
  this is the difference between sounding senior and getting caught out.
- Lam is a strong full-stack engineer (React, Node, TypeScript). Do not re-teach React
  hooks, TypeScript basics, or REST. Teach the agent-specific and architecture-specific parts.
- Answers must be practised **out loud**. Reading is not preparation for speaking.

## Out of scope

- Building a competing product from scratch.
- Deep model theory (transformer internals, fine-tuning, embeddings math).
- Vercel platform operations (billing, team settings, DNS).
- The `pnpm-lock.yaml` / dependency-version archaeology.
