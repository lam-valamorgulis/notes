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
- 2026-07-29: new **`theme-architecture/` sub-course** added (3 lessons): Dawn architecture,
  Horizon & theme blocks, Cart AJAX API. Structured as a sub-course, not as lessons 0030+,
  because `MISSION.md` puts theme/Liquid **out of scope** for the main course ("already a
  strength"). The sub-course says up front that it does not re-teach Liquid syntax — it covers
  only what is new (Horizon, announced 2025-05-21) or easy to get wrong (`update.js` overselling,
  `line` vs line item `key`, `sections_url` needing a leading `/`). Linked from the parent
  `index.html` next to the stockinstore card, and from the root `../index.html` (counts bumped:
  sub-courses 2→3, pages 122→126, lessons 71→74). Facts verified 2026-07-29 against shopify.dev
  and help.shopify.com for the documented contract, plus real source for implementation detail:
  a local copy of **Dawn 15.3.0** (`assets/cart.js`, `product-form.js`, `global.js`,
  `layout/theme.liquid`) and the public `Shopify/horizon` repo (112 files in `blocks/`,
  `component.js`, `morph.js`, single `base.css`). File counts are version-specific and will
  drift; each lesson's "verified" line says so. One claim is flagged as engineering judgement
  rather than documented: sending cart writes sequentially — Shopify publishes no explicit
  concurrency warning. Only public/open-source theme source was used; no client theme code.
- 2026-07-29 (same session): **lesson 4 added — "Discounts on the Storefront"**, so the sub-course
  is now 4 lessons / 5 pages and the Map gained a Ch 4. Scoped to the storefront on purpose:
  discount **Functions** stay in main-course L24 and the lesson links there rather than repeating
  it. The spine of the lesson is "the theme displays discounts, it never decides them." Highest-
  value facts, all verified: (a) an **invalid discount code still returns 200** with a normal cart —
  you must check `data.discount_codes[]` for `applicable === false`; (b) `line_item.price`,
  `line_price`, `total_discount`, `discounts`, and `cart.discounts` are **deprecated because they
  only ever held Shopify Scripts discounts**, so post-Scripts-sunset they miss codes and automatic
  discounts entirely — this is the "line prices don't add up to the total" bug; (c) the `discount`
  param on `/cart/update.js` replaces the whole set, so there is **no remove-one call**; (d) max
  **5 product/order codes + 1 shipping code** per order, classes calculate product→order→shipping,
  and discounts do **not** combine unless configured; (e) shareable `/discount/CODE?redirect=`
  needs zero theme code. Best Dawn↔Horizon contrast in the sub-course: **Dawn 15.3.0 ships no
  discount input at all** (verified by grep — display only), while Horizon has `cart-discount.js`
  with pills and error states. Second flagged non-documented claim: the `discount_codes` array
  with `code`/`applicable` is **absent from the Cart AJAX reference** but used and typed in
  Horizon's production source — taught as real-but-unspecified, with advice to code defensively.
  Subtle real detail worth keeping: a **shipping** code can return `applicable: true` and still
  render nothing (no address until checkout); Horizon detects it by diffing the rendered pills
  against the cart payload. Root index counts bumped again: pages 126→127, lessons 74→75.
