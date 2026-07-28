# Mission: Pass the client interview (2 rounds) — Senior Backend (Shopify + Node)

## Why
Lam passed the first round (with the outsourcing / staffing company). Now come **two rounds
with the real client**. The bar is higher: the client asks **deeper and more detailed**
questions, may run **live coding**, and will push harder on **behavioral** answers.

Lam has **one week** to prepare for both client rounds.

## What changed from round 1 (read this — it is the key shift)
Round-1 prep made one scope decision: *"talk about systems, do not build."* No live coding.
See `../shopify-erp-sync-1st-interview/learning-records/0002-scope-talk-not-build.md`.

**That decision is now reversed for the client.** The client round may include live coding.
The kind of coding to expect (confirmed with Lam):
- **Practical backend build** — write a real thing live: a webhook handler, a REST/GraphQL
  endpoint, a NestJS module, a small sync worker. This is the most likely format for a
  Shopify backend role.
- **Debugging / fix-it** — they show broken code (an async bug, a race condition, a failing
  test) and ask Lam to find and fix it while explaining out loud.
- **Not** classic LeetCode / algorithm puzzles. We do not grind data-structure puzzles.

## Success looks like
1. **Master every detail** of the round-1 content. Not just the headline — the *why*, the
   edge cases, and the follow-up questions under each topic. The client will ask "why?"
   three times deep. (Days 1–3.)
2. **Code it live, out loud.** Build a webhook handler, an idempotent worker, a NestJS
   module, and a queue consumer from a blank file while narrating trade-offs. Fix planted
   bugs. (Days 4–6.)
3. **Answer harder Q&A** — the detail-level and "what would break?" questions an experienced
   client engineer asks, not the surface questions a recruiter asks.
4. **Deliver senior behavioral answers** — deeper STAR stories, conflict, trade-offs,
   mentoring, and sharp questions to ask the client.

## Constraints
- **One week, two rounds.** Days 1–3: lock the round-1 detail. Days 4–7: live coding +
  harder Q&A + behavioral depth + mock.
- Client stack currently **unknown** — assume the same profile as round 1 (Shopify + Node,
  likely NestJS + a SQL DB + a queue). Lam will share the real job description later; when he
  does, re-target the prep to it.
- Keep round-1 strengths warm (Shopify domain, Node event loop already mastered) — reinforce,
  do not re-teach from zero.

## Out of scope
- LeetCode / algorithm grinding (client coding is practical, not puzzle).
- Re-teaching Shopify theme / Liquid (already a strength).
- Re-teaching the Node event loop from scratch (already mastered — see round-1 records
  0003–0004; only stretch it into harder follow-ups).
