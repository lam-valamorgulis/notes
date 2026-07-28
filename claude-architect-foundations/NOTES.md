# Notes & Preferences


## How to teach Lam
- **Bolt exam concepts onto what he already does in Claude Code.** "You do X every day — the exam calls it Y, here is the tradeoff and when NOT to use it."
- The exam is **scenario + judgment**: every question gives a production situation and asks for the *most effective* fix. Teach the *why the other options are worse*, not just the right answer.
- Drill the **recurring exam themes** (these decide most questions):
  1. **Deterministic enforcement** (hooks, prerequisite gates) **vs probabilistic prompting** — when money/identity is at stake, code beats prompt instructions.
  2. **Root cause vs symptom** — fix the actual problem (e.g. weak tool descriptions), not a bigger hammer (routing layer, more few-shot).
  3. **Least privilege for tools** — fewer, scoped tools select more reliably; give an agent only its role's tools.
  4. **Structured data over prose** when passing context between agents (claim/source, IDs, dates).
  5. **Proportionate first response** — try the cheap, targeted fix (better description, explicit criteria) before adding ML/classifiers/infrastructure.
- Use retrieval practice (quizzes via `assets/quiz.js`, "say it aloud"). Verify facts against RESOURCES.md and the `claude-api` skill; never guess.

## The 6 exam scenarios (4 appear on your exam, drawn at random)
1. **Customer Support Resolution Agent** — Agent SDK, custom MCP tools (get_customer, lookup_order, process_refund, escalate_to_human); 80%+ first-contact resolution + knowing when to escalate. Domains 1, 2, 5.
2. **Code Generation with Claude Code** — slash commands, CLAUDE.md, plan mode vs direct. Domains 3, 5.
3. **Multi-Agent Research System** — coordinator delegates to search / analyze / synthesize / report subagents; cited reports. Domains 1, 2, 5.
4. **Developer Productivity with Claude** — Agent SDK, built-in tools (Read/Write/Bash/Grep/Glob), MCP servers, explore legacy code. Domains 2, 3, 1.
5. **Claude Code for CI** — automated review, test gen, PR feedback; `-p`, `--output-format json`, minimize false positives. Domains 3, 4.
6. **Structured Data Extraction** — `tool_use` + JSON schema, validation, edge cases, downstream integration. Domains 4, 5.

## Working notes
- Folder created 2026-07-15, mirroring `shopify-nsc-interview-prep` layout.
- **2026-07-15 — scaffold corrected.** First pass guessed the exam was "4 tools (Claude Code / Agent SDK / API / MCP)". The real Exam Guide (v1.0, CCAR-F) has **5 weighted domains** (see MISSION.md) and a large OUT-OF-SCOPE list. All core files were rewritten to match. See [[learning-records/0002-real-exam-blueprint.md]].
- Doc-host facts verified 2026-07-15: Claude Code + Agent SDK → `code.claude.com/docs`; Claude API / tool use / batches → `platform.claude.com/docs`; MCP → `modelcontextprotocol.io`. Deep links for tool use, Agent SDK subagents, and Agent SDK TS reference (hooks) all verified live.
- Exam facts confirmed from the PDF: 60 items, 4 of 6 scenarios, 120 min, pass = 720/1000, $125, valid 12 months, retake waits 14/30/90 days.
- **2026-07-15 — lessons built.** Six HTML lessons in `lessons/` (one per domain in study order + a mock finale), built with parallel subagents against the exact house template (`base.css` + `quiz.js`). Reading order = study order: L1 Domain 1 (Agentic) → L2 Domain 4 (Prompt/Structured) → L3 Domain 2 (Tool/MCP) → L4 Domain 5 (Context/Reliability) → L5 Domain 3 (Claude Code Config) → L6 Exam Strategy + 15-question mock. Each lesson: 10 scenario quiz questions (15 in the mock) + recall cards + `trap`/`soundbite` callouts + verified doc links. Study-plan domain boxes link to each lesson. Verified: no invented CSS classes, nav chain intact, all `answer: 0` (quiz.js shuffles options so this is correct, not a bug).

