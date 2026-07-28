# Working notes

## How Lam wants to be taught

- **Plain English section** at the end of any explanation or recommendation (global rule).
- **Simple vocabulary** in every written document. Short sentences, one idea each.
  Keep real technical names exactly as they are (`streamText`, `data-run-command`,
  `Sandbox.get`) and explain them once in plain words.
- **Never guess.** Every claim in a lesson must point at a real file and line in the repo.
  If something cannot be found in the source, say so out loud instead of assuming.
- **Out loud practice.** The mission is a spoken interview. Recall cards (`renderRecall`)
  matter more than multiple choice here. Multiple choice checks facts; speaking checks
  whether he can actually explain it.

## Source of truth for this course

The repo is sparse-cloned locally for reading during sessions:

```
git clone --filter=blob:none --sparse --depth 1 https://github.com/vercel/examples.git
cd examples && git sparse-checkout set apps/vibe-coding-platform
```

Last read at commit `72aaac1` (2026-05-05, "add AI Gateway app attribution headers").
If a future session sees different code, re-read before teaching — the repo moves.

## Known drift to keep in mind

- The Vercel template landing page still advertises "GPT-5". The repo actually supports
  Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.3 Codex, and Grok 4.1 Reasoning
  (`ai/constants.ts`). Trust the repo.
- `package.json` has `"name": "vibe-coding-agent"` while the folder is
  `vibe-coding-platform`. Leftover from a rename. Harmless, but confusing when grepping.

## Assets reused from sibling courses

- `assets/quiz.js` copied verbatim from `../flutter-mastery-in-1-year/assets/quiz.js`.
  Provides `renderQuiz()` and `renderRecall()`. Do not fork it — if it needs a change,
  change it in a way both courses can use.
- `assets/base.css` follows the same class names as the sibling courses so `quiz.js`
  works unchanged. New in this course: the `.tradeoff` card and the `.filepath` label.

## Teaching decisions made

- Week order is deliberate: **framework → agent core → features → trade-offs.**
  Trade-offs only make sense once the features are concrete. Do not front-load them
  even though the mission lists them early.
- **Week 1 is Next.js**, added after the gap review. The first version of this course
  skipped the framework entirely and named files like `route.ts` without ever saying
  what they were. Every Week 1 example must be a real file from this repo — no tutorial
  toys, no generic counter components.
- Day 8 (the streaming contract) is the single highest-value lesson for the interview.
  It is the one genuinely non-obvious idea in the codebase. It now sits *after* HTTP
  streaming (Days 4–5), because data parts cannot be understood before chunked responses.
- Days 14, 21 and 30 add **no new material** on purpose — spaced retrieval and spoken
  drills. Do not fill them with content if a week runs short.

## Pacing

30 days × 2 hours. The per-day shape is on The Map. The 1:50–2:00 block — saying the recall
cards **out loud** — is the block that actually serves the mission, and the one most likely
to get skipped. Ask about it directly rather than assuming it happened.

Lesson file numbers are creation order, not day order. Day order lives only on The Map.
Lesson `0003` covers Days 4 and 5 together because it is a long one.

## Hard rule learned from the gap review

**Never teach a file that has not been read in the current session.** Three real findings —
the `echo` status-check hack, inconsistent Zod validation across route handlers, and
`get-sandbox-url.ts` breaking its siblings' error pattern — were all invisible until the file
was actually open. See [GAPS.md](./GAPS.md) items 15–17.
