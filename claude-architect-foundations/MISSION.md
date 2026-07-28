# Mission: Pass the Claude Certified Architect – Foundations exam (CCAR-F)

## Why
Lam wants to earn the **Claude Certified Architect – Foundations** certification from
Anthropic. The exam validates that a practitioner can **make informed decisions about
tradeoffs when building real-world solutions with Claude**. The goal is not trivia — it is
practical judgment: given a production scenario, pick the right pattern and defend it.

## Exam facts (from the official Exam Guide, v1.0, effective July 2026)
- **Exam code:** CCAR-F. **Fee:** $125 USD. **Validity:** 12 months (then free renewal assessment, or re-take).
- **60 items** — multiple-choice and multiple-response (each item says how many to pick).
- **4 scenarios**, drawn at random from a **bank of 6** (see NOTES.md). Every question sits inside a realistic production scenario.
- **120 minutes.** Proctored by Pearson VUE (online or test center).
- **Passing score: 720** on a scaled range of 100–1000. Criterion-referenced (pass by meeting a fixed standard, not by beating other people).
- Score report shows **percent-correct per domain** (helpful for a re-take, but pass/fail is the total scaled score).
- **Retake waits:** 14 days after the 1st fail, 30 after the 2nd, 90 after the 3rd; up to 4 attempts per rolling 12 months. Fee each time.

## What the exam tests — the 5 weighted domains
| # | Domain | Weight |
|---|--------|--------|
| 1 | **Agentic Architecture & Orchestration** — agentic loops (`stop_reason`), coordinator-subagent patterns, subagent context passing, task decomposition, Agent SDK hooks, session state / fork / resume | **27%** |
| 3 | **Claude Code Configuration & Workflows** — CLAUDE.md hierarchy, `.claude/rules/` path-scoping, slash commands, skills (`context: fork`, `allowed-tools`), plan mode vs direct, CI with `-p` / `--output-format json` | **20%** |
| 4 | **Prompt Engineering & Structured Output** — explicit criteria to cut false positives, few-shot, `tool_use` + JSON schema, `tool_choice`, validation-retry loops, Message Batches, multi-pass review | **20%** |
| 2 | **Tool Design & MCP Integration** — clear tool descriptions, structured errors (`isError`, retryable), tool distribution / `tool_choice`, MCP server scoping (`.mcp.json`), built-in tools | **18%** |
| 5 | **Context Management & Reliability** — preserving key facts across long chats, escalation / human-in-the-loop, error propagation across agents, large-codebase context, confidence calibration, provenance | **15%** |

## Success looks like
- Read a production scenario and pick the **most effective** fix, explaining why the other three options are worse (that is exactly how the sample questions are written).
- Reason clearly about the recurring exam themes: **deterministic enforcement (hooks/prerequisites) vs probabilistic prompting**; **least privilege for tools**; **root cause vs treating symptoms**; **structured data over prose** when passing context.

## Out of scope (the Exam Guide says these are NOT tested — do not over-study them)
- Fine-tuning / training custom models; Claude's internal architecture, RLHF, Constitutional AI.
- Claude API **authentication, billing, account management**; OAuth / key rotation.
- **API rate limits, quotas, pricing math**; **token-counting algorithms**; **prompt-caching internals** (beyond "it exists"); **streaming / SSE implementation**.
- **Deploying / hosting MCP servers** (infrastructure, networking, containers).
- Embeddings / vector DBs; computer use; vision; specific cloud-provider configs (AWS/GCP/Azure).
