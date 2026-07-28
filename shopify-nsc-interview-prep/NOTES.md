# Notes & Preferences — Round 2 (client)


## What is new in round 2
- The client can ask Lam to **write code live**. Round 1 never tested this. This is the main
  new muscle to build. Two formats: **build a real backend piece** and **fix broken code**.
- Questions go **deeper**. Expect "why?" follow-ups, edge cases, and "what breaks at scale?".
  Surface-level answers that passed round 1 are not enough for the client engineers.

## How to teach Lam (carried over from round 1, still true)
- **Bolt new knowledge onto Shopify knowledge he already has.** "Same domain, from the server."
- Prefer **retrieval practice** — quizzes, "say it out loud", "code it from blank" — over
  passive reading. Struggling to recall builds memory; re-reading does not.
- Give **interview soundbites**: crisp 2–4 sentence spoken answers.
- Visual, step-through explanations worked well for hard mechanics (event loop). Reuse that.
- For coding: **type it from a blank file while narrating**, then compare to a model answer.
  Do not just read finished code.
- **Keep `index.html` (The Map) in sync.** It is the single source of truth that connects
  every lesson into one story. Whenever a session adds, renames, or removes content, update
  `index.html` in the same session: add it to the right chapter list with a one-line plain
  description, weave it into the "big picture" story, add the "← The Map" breadcrumb to any new
  page, and verify no link is broken and no file is left unlinked. This is part of "done".

## Working notes
- 2026-07-13: round-2 workspace created. Round-1 content moved to
  `../shopify-erp-sync-1st-interview/` unchanged. Structure mirrored here: `lessons/`,
  `reference/`, `exercises/` (new — live-coding katas), `learning-records/`, shared `assets/`.
- Shopify facts still verified as of round 1 (API version 2026-07): GraphQL Admin API primary
  (REST legacy); rate limit = calculated query cost (1000 pts, +50/s restore); webhooks need
  HMAC-SHA256 on raw body, respond 200 within 5s (1s connect / 5s total timeout), up to
  8 retries over ~4 hours, subscription auto-removed after repeated failures, dedupe via
  X-Shopify-Webhook-Id, idempotent handlers; app auth = session tokens + token exchange.
  Re-verify against shopify.dev before the interview if a detail is load-bearing.
- 2026-07-15: full 29-lesson pedagogy audit + fix pass. Systemic fix applied to every
  lesson: mid-lesson retrieval prompts (new `.recall` style in base.css) so practice is
  woven throughout, not only at the end; an explicit "You've got it when…" success bar;
  plainer English (idioms removed, technical terms kept exact). Set piece 0011 gained a
  two-way-sync/conflict section, a reliability step-through, and a type-from-blank ingestion
  kata. 0008 regrouped into 3 buckets with one `POST /v1/orders` example throughout. 0016
  mock now has a printable score sheet + answer-before-reveal gate + a reference architecture.
  0015 got a hard STAR rubric. Verified facts against shopify.dev (2026-07-15): (a) webhook
  retries = 8 over ~4h then subscription removed — CORRECT/current (Sept-2024 changelog),
  keep it; (b) GraphQL rate limits: teach the MODEL — ~1000-point bucket, plan-scaled restore
  rate (docs show both 50/s and 100/s), single query capped at 1000 points — not one number;
  (c) 0024 code bug FIXED: Payment Customization Function uses `paymentMethodHide` +
  export `cartPaymentMethodsTransformRun`, not `hide`/`run`.
