# Claude Certified Architect – Foundations (CCAR-F) — Resources

All URLs verified live on **2026-07-15**. Docs now live on `code.claude.com`,
`platform.claude.com`, and `modelcontextprotocol.io` (old `docs.anthropic.com` links
redirect). Prefer these over memory. Organized by the **five real exam domains** and their
weights. The full objectives are in the Exam Guide PDF saved in this folder.

## The exam itself
- [Certification page](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) — signup + the 3 PDFs (Exam Guide, Terms, Policy). **Exam Guide PDF is already downloaded into this folder** and read; see [[learning-records/0002-real-exam-blueprint.md]].
- Delivered by **Pearson VUE**. Name on ID must match registration exactly. Support: certifications-support@anthropic.com.

## Domain 1 — Agentic Architecture & Orchestration (27%)
- [How tool use works (the agentic loop)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) — the loop: send request → check `stop_reason` (`tool_use` vs `end_turn`) → run tool → append `tool_result` → repeat. **This is the single highest-weight concept.**
- [Tool use overview](https://platform.claude.com/docs/en/build-with-claude/tool-use/overview) — `tool_use` blocks, `tool_result`, `stop_reason`, `tool_choice`. Read the "How tool use works" section end to end.
- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) — building your own agents on Claude Code's engine.
- [Agent SDK — Subagents](https://code.claude.com/docs/en/agent-sdk/subagents) — `AgentDefinition`, the `Task`/`Agent` tool, `allowedTools` must include the spawn tool, subagents start with **fresh context** (pass everything they need in the prompt), tool restrictions, parallel spawning, resume. Core for coordinator-subagent questions.
- [Agent SDK — TypeScript reference](https://code.claude.com/docs/en/agent-sdk/typescript) — **hooks** (`PostToolUse`), `resume`, `forkSession`, sessions. Use for hook-based enforcement and session state / fork / resume objectives.

## Domain 3 — Claude Code Configuration & Workflows (20%)
- [Memory & CLAUDE.md](https://code.claude.com/docs/en/memory) — the hierarchy (user `~/.claude/CLAUDE.md`, project `.claude/CLAUDE.md` or root, directory-level), `@import`, `/memory` command.
- [Settings](https://code.claude.com/docs/en/settings) — `.claude/rules/` files, config, permissions.
- [Skills](https://code.claude.com/docs/en/skills) — `SKILL.md` frontmatter: `context: fork` (isolate output), `allowed-tools`, `argument-hint`; skills vs CLAUDE.md.
- [Slash commands](https://code.claude.com/docs/en/slash-commands) — project `.claude/commands/` (shared) vs user `~/.claude/commands/` (personal).
- [Plan mode / workflows](https://code.claude.com/docs/en/overview) — plan mode vs direct execution; the `Explore` subagent for verbose discovery.
- [CLI reference](https://code.claude.com/docs/en/cli-reference) — `-p` / `--print` (non-interactive CI), `--output-format json`, `--json-schema`.

## Domain 4 — Prompt Engineering & Structured Output (20%)
- [Tool use overview](https://platform.claude.com/docs/en/build-with-claude/tool-use/overview) + [Define tools / forcing tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) — `tool_choice` `auto` vs `any` vs forced `{"type":"tool","name":"..."}`; `strict: true` for schema conformance. **`tool_use` + JSON schema is the reliable structured-output path.**
- [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) — `tool_result` formatting and error signaling; feeds validation-retry loops.
- [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) — 50% cost, up to 24h, no latency SLA, no multi-turn tool calls, `custom_id` correlation. Know **when it fits** (overnight, latency-tolerant) vs not (blocking pre-merge checks).
- Key ideas (no single doc — see the Exam Guide task statements): explicit categorical criteria beat vague "be conservative"; few-shot (2–4 examples) for ambiguous cases; nullable/optional schema fields to prevent fabrication; enum `"other"` + detail for extensible categories; validation-retry only helps for format/structural errors, not missing information.

## Domain 2 — Tool Design & MCP Integration (18%)
- [Tool use overview](https://platform.claude.com/docs/en/build-with-claude/tool-use/overview) — tool **descriptions are the primary signal** Claude uses to pick a tool; ambiguous/overlapping descriptions cause misrouting; split generic tools into purpose-specific ones.
- [MCP in Claude Code](https://code.claude.com/docs/en/mcp) — `.mcp.json` project scope vs `~/.claude.json` user scope, env-var expansion (`${GITHUB_TOKEN}`) for secrets, all servers' tools available at connect time.
- [What is MCP?](https://modelcontextprotocol.io/introduction) + [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) — client/server/transport; **tools** (actions), **resources** (data catalogs), **prompts** (templates).
- Structured errors (Exam Guide task 2.2): MCP `isError` flag, `errorCategory` (transient / validation / permission), `isRetryable` boolean, distinguish access failures from valid empty results. (No single doc — study the task statement.)

## Domain 5 — Context Management & Reliability (15%)
- Mostly **judgment patterns** from the Exam Guide task statements (no single doc):
  - Preserve transactional facts (amounts, dates, IDs) in a persistent "case facts" block, not in summaries; trim verbose tool outputs before they fill context; mitigate "lost in the middle" by putting key findings first.
  - Escalation: escalate on explicit customer request, policy gaps, or no progress — **not** on sentiment or self-reported confidence; ask for more identifiers when a lookup returns multiple matches.
  - Error propagation: return structured error context (failure type, attempted query, partial results) so a coordinator can recover; never silently swallow errors or kill the whole workflow on one failure.
  - Human review: stratified sampling of high-confidence extractions; calibrate field-level confidence with labeled sets; check accuracy per document type, not just an aggregate.
  - Provenance: keep claim→source mappings through synthesis; annotate conflicting values with sources; include publication dates.

## Built-in tutors (in this Claude Code session)
- **`claude-api` skill** — model IDs, `tool_use`, `tool_choice`, `stop_reason`, JSON schema, batches. Note: rate limits / pricing / caching internals are OUT of scope, so ignore those parts.
- **`claude-code-guide` agent** — deep Q&A on Claude Code config, the Agent SDK, and the API. Use it as a live tutor for any domain.

## Explicitly OUT of scope (per the Exam Guide — do not waste time here)
Fine-tuning / model internals / RLHF; API auth, billing, OAuth, key rotation; rate limits, quotas, pricing math; token-counting algorithms; prompt-caching internals; streaming / SSE implementation; **hosting/deploying MCP servers**; embeddings / vector DBs; computer use; vision; cloud-provider (AWS/GCP/Azure) configs.
