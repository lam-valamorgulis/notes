# Mission — Shopify Data Sync (sub-course 6)

Status: **PLAN, build started 2026-08-06.** Folders and assets exist. No pages written yet.

## Why this sub-course exists

Sync is the centre of the Game Locker job, and it is the one topic in this repo that is
taught **everywhere and nowhere**. It appears as a section inside twelve different pages. It
has never been the subject of its own course.

The migration sub-course says this out loud in its own index:

> "It does not teach ongoing sync. Different problem, different lesson."

That lesson was never written. This is it.

## The frame (revised by Lam, 2026-08-06)

**One real-shaped store, built forward.** Not "here is an abstract integration". The course
follows a single card shop from a plain Shopify storefront to a working integration:

> **Harbour City Cards** — a Sydney trading-card shop. A physical counter with a Game Locker
> POS kiosk, and a Shopify storefront selling singles online. It is **store 17** on the Game
> Locker platform, and it sells the **$480 near-mint Charizard** used in
> `game-locker/lessons/0003`. The store is a worked example, not a real business. Game Locker
> itself is real and every claim about it comes from their public site or the job description.

The arc is deliberately in this order:

1. **Build the storefront first.** What a card shop looks like as Shopify data only — product,
   variants, inventory, the theme reading stock. No external system at all.
2. **Hit the wall.** The counter sells the same physical card, and Shopify has no idea.
3. **Put Game Locker behind it.** Now two systems hold one card. Every remaining lesson is one
   piece of making that safe.

The reader should be able to say: *"I have seen this exact store go from broken to trustworthy,
step by step."* That is the whole design goal.

## The three decisions (confirmed by Lam, 2026-08-06)

1. **A new sub-course**, `shopify-data-sync/`, same folder shape as the other five.
2. **One running store, built forward** — Harbour City Cards, as above.
3. **Design only. No implementation code.** Ownership matrices, minute-by-minute timelines,
   failure tables, and the sentences to say in an interview. GraphQL mutation *names* are
   fine; worker bodies are not. Liquid and admin data shapes are fine — they are the storefront.

## What already exists (this sub-course routes, it does not repeat)

Audited on 2026-08-06 by reading each file, not by guessing from filenames.

| Page | Sync content it already holds |
|---|---|
| `game-locker/lessons/0003-the-sync-engine.html` | 41 KB. The deepest page. Ownership matrix, echo loop, absolute vs delta, `compareQuantity`, the 14:05 oversell minute, 4 defences, webhook rules, reconciliation, 5 worked cases. |
| `game-locker/lessons/0002-tcg-card-data-on-shopify.html` | The TCG data model — printing as product, condition × language × finish as the 3 options, metafields for set and rarity. **L01 here builds on this instead of redoing it.** |
| `lessons/0011-system-design-shopify-erp-sync.html` | 27 KB. Sync as a system-design interview. Clarify, architecture, reliability, rate limits both sides, mapping, §5½ two-way conflicts. |
| `lessons/0002-webhooks-done-right.html` | The return channel mechanics. |
| `lessons/0012-event-driven-messaging.html` | Queues, retries, dead letters. |
| `lessons/0018-shopify-bulk-operations.html` | `bulkOperationRunMutation` / `RunQuery`. |
| `stockinstore-omnichannel/lessons/0002` | Ingestion, three arrival modes, dedupe key + staleness guard, §5½ snapshot vs delta. |
| `stockinstore-omnichannel/lessons/0007` | Event backbone, four reliability rules, fan-out. |
| `stockinstore-omnichannel/lessons/0008` | Source of truth per fact, eventual consistency, dual-write and the outbox. |
| `stockinstore-omnichannel/lessons/0016` | Four webhook streams, delivery rules, write-back, ordering, three-way reconciliation. |
| `stockinstore-omnichannel/lessons/0013` | Identifier mapping registry. |
| `shopify-data-migration/lessons/0003` | The matching key, custom ID, idempotency, `productSet` list-deletion trap. |
| `pos-in-store/lessons/0002`, `0003` | Three ways in-store stock reaches a storefront; 8 inventory states, `safety_stock`. |
| `theme-architecture/` | The storefront side. L01 here links out rather than teaching Liquid. |

**Consequence for the plan:** roughly half of this sub-course is *review by re-teaching* — the
same idea, said again in one place, in a tighter order, with the Harbour City Cards story
carrying it. The other half is genuinely new. Each lesson below is labelled.

## The real gaps found in the audit

These are not covered anywhere in the repo. They are the reason a 6th sub-course is worth
building rather than just a review page.

| Gap | Where it is missing today |
|---|---|
| **The storefront-first view of sync.** Every existing page starts at the integration. None starts at the shop and asks what it needs. | Nowhere. This is the new frame, and it is L01–L02. |
| **Deletes.** A card leaves Game Locker — delete, archive, draft, or set stock to 0? What `productDelete` does to old orders, saved URLs and search traffic. | Nowhere. "Delete" is the most dangerous verb in sync and no page names it. |
| **Field-level ownership.** Every existing page owns data per *record*. Real conflicts are per *field* — a merchant edits the title in the Shopify admin while Game Locker owns the price. | `game-locker/0003` mentions this in one recall answer and moves on. |
| **Clocks and ordering.** Two systems, two clocks. Out-of-order webhooks. Why `updated_at` is a weak guard and per-key ordering is enough. | `stockinstore/0016 §5` touches ordering. Clock disagreement is nowhere. |
| **The backlog.** The sync is 40 minutes behind. Replay every message, or keep only the newest per card? Why stock messages may collapse and order messages may not. | Nowhere. `stockinstore/0002 §6` is about not hammering, which is the opposite problem. |
| **One store among many.** Harbour City Cards is store 17 of ~400. Rate limits are per shop; the worker pool is shared. Another store's backfill delays yours. | `stockinstore/0009` covers multi-tenancy in general, never the sync queue. |
| **The lag conversation.** Naming the accepted delay to the shop owner, in writing, before it is a complaint. | One sentence in a `game-locker/0003` recall answer. |

## The eleven lessons

Reading order is straight through, L01 → L11. Every lesson is Harbour City Cards.

### Chapter 1 — Build the store, then break it

| # | Lesson | New or review | Content |
|---|---|---|---|
| L01 | The store on Shopify, and nothing else | **New frame** | Harbour City Cards as Shopify data only. Printing = product, condition × language × finish = the 3 options, one location, `InventoryLevel` = the number the theme reads. What the product page actually shows and where that number comes from. Then the wall: the counter sells the same card and Shopify never hears. Links to `game-locker/0002` for the data model and `theme-architecture/` for Liquid. |
| L02 | Game Locker behind the counter | **Review**, retold | What the platform owns: the shared card catalogue, the daily reprice, the POS kiosk. Now two systems hold one card. The three arrows out of store 17. Refuse the phrase "keep them in sync" — the only question is *when they disagree, who is right?* |

### Chapter 2 — Decide before you build anything

| # | Lesson | New or review | Content |
|---|---|---|---|
| L03 | Ownership, per field not per record | **New** | The matrix rebuilt at field level for this store. The contested register — a written list of fields both sides can write, kept short on purpose. The owner edits a title by hand in the Shopify admin: the three honest answers (overwrite, respect, alarm). Why every new two-way field multiplies the cases you must reason about. |

### Chapter 3 — The write path out, Game Locker → Shopify

| # | Lesson | New or review | Content |
|---|---|---|---|
| L04 | Absolute writes, and why replay must be safe | **Review**, retold | `inventorySetQuantities` vs `inventoryAdjustQuantities`, as a 2×2 of lost message vs duplicate message. `compareQuantity` as a stop sign, not a fix — the re-read is what finds the truth. Idempotency keyed on the order id. |
| L05 | Deletes, archives and tombstones | **New — biggest gap** | The four ways to say "this card is gone": stock 0, `DRAFT`, `ARCHIVED`, deleted. What each does to old orders, the saved URL, and search traffic. Why the sync should almost never delete. Soft-delete on the Game Locker side. The case that forces it: a card is pulled because it was a fake. |
| L06 | Clocks, order and staleness | **New** | Two systems, two clocks, and why "latest wins" needs a clock you trust. Out-of-order webhooks. Per-card ordering is enough; global ordering is expensive and unnecessary. The staleness guard, and the case it cannot catch. |

### Chapter 4 — The read path back, Shopify → Game Locker

| # | Lesson | New or review | Content |
|---|---|---|---|
| L07 | Webhooks are a hint, not a guarantee | **Review**, retold | At-least-once. Finite retries, then the subscription is removed and nobody is told. The handler enqueues and returns 200; the worker does the work. Why a hint plus a backstop beats a promise. The echo loop, and marking the origin of every write. |

### Chapter 5 — When it is behind, or wrong

| # | Lesson | New or review | Content |
|---|---|---|---|
| L08 | The backlog | **New** | 40 minutes behind at 5 pm on release day. Queue depth as the first metric. Collapsing messages per key — keep the newest stock level, keep *every* order. Catch-up order: what to sync first when you cannot sync everything. Shedding vs queueing. |
| L09 | Reconciliation, and numbers that do not lie | **Review**, deepened | Nightly read-back with a bulk query. Heal the explainable, alarm on the unexplainable. Alarm on the *rate*, not each mismatch. The unfulfillable report as the only place an oversell is visible. The metric list: lag, queue depth, mismatch rate, rejected-write rate. |

### Chapter 6 — The store is not alone

| # | Lesson | New or review | Content |
|---|---|---|---|
| L10 | Store 17 of four hundred | **New** | Rate limits are per shop; the worker pool is shared. The noisy neighbour: one shop's backfill starving the rest. Fair scheduling per shop. Per-shop circuit breaker. A new shop onboarding while 399 others sync — the handover from the migration sub-course. |
| L11 | The sync conversation, and the interview | **Review**, reframed | Naming the lag out loud, in writing, before it is a complaint. What costs money vs what costs engineering time. The pre-agreed apology. Then the drill: three question shapes, a five-stage design script, red-flag answers, 20 interleaved questions, a self-scoring rubric. |

## Reference pages

| Page | What it is |
|---|---|
| `reference/review-path.html` | The explicit **review route**, since re-learning is the stated goal. A numbered path through the sync sections that already exist across the repo, each with the one line it exists to teach, and a tick box. |
| `reference/the-store.html` | Harbour City Cards on one page — its catalogue shape, its two doors, its numbers. The card to glance at while reading any lesson. |
| `reference/ownership-matrix.html` | A blank field-level matrix to fill in during a scoping call. Printable. |
| `reference/conflict-cases.html` | The conflict taxonomy on one page: every conflict type, how you notice it, and the rule that resolves it. |
| `reference/onepager.html` | The last-hour card. The four pieces, the four defences, the six lines to say. |

Five references, eleven lessons, one index = **17 pages**.

## Facts to verify against shopify.dev before writing (do not write them from memory)

L05, L06, L07 and L10 depend on facts nobody in this repo has checked. Each must be read and
linked on the page, with the date, same rule as the migration sub-course.

- What `productDelete` does to line items on existing orders.
- Whether a deleted product's URL 404s, and whether Shopify creates a redirect.
- The exact effects of product status `ACTIVE` / `DRAFT` / `ARCHIVED`.
- Whether Shopify states any ordering guarantee for webhook delivery.
- The header carrying the event time on a webhook, and its exact name.
- Whether `inventory_levels/update` fires for writes your own app made — this decides how the
  echo loop is suppressed.
- Admin API rate-limit scope: per shop, per app, or per app-shop pair.
- Whether the ~8-failures-over-~4-hours retry rule is still current.

Facts already verified elsewhere in this repo and reused without re-checking: the 8 inventory
states, the InventoryItem–Location–InventoryLevel triangle, `safety_stock`, `compareQuantity`
and `ignoreCompareQuantity`, 50,000 inventory quantities per mutation, 2048 variants per
product and 3 options per product, and the custom-ID matching key.

## Hard constraints

- **Design only.** No worker code, no queue code, no tests. Mutation names yes; bodies no.
- **One store, all the way through.** If a lesson stops being about Harbour City Cards, it has
  drifted back into being an abstract integration page — which the repo already has.
- **No fact stated that could not be verified.** Where two Shopify pages disagree, say so on
  the page instead of picking one.
- **Do not repeat a page that already exists — link to it.** A review lesson retells the idea
  inside the store's story, then points at the deeper page.
- **The store is labelled as an example; Game Locker is not invented.** Everything about the
  platform comes from `game-locker/reference/company-brief.html`, their public site, or the JD.

## Layout

```
shopify-data-sync/
  index.html                 the Map — single source of truth
  MISSION.md                 this file
  assets/                    base.css + quiz.js, copied from shopify-data-migration/
  lessons/  0001 the store on Shopify, and nothing else
            0002 game locker behind the counter
            0003 ownership, per field not per record
            0004 absolute writes, and why replay must be safe
            0005 deletes, archives and tombstones        ← biggest new gap
            0006 clocks, order and staleness
            0007 webhooks are a hint, not a guarantee
            0008 the backlog
            0009 reconciliation, and numbers that do not lie
            0010 store 17 of four hundred
            0011 the sync conversation, and the interview   ← capstone
  reference/ review-path.html      ← START HERE for re-learning
             the-store.html
             ownership-matrix.html
             conflict-cases.html
             onepager.html
  learning-records/
```

## Definition of done (all of it, not part of it)

1. Eleven lessons, five reference pages, one index — each with the `← The Map` breadcrumb.
2. Every lesson has a `Check yourself` quiz and a `Say it out loud` recall block, same as its
   siblings.
3. `shopify-nsc-interview-prep/index.html` gets a **6th sub-course card**, and the new pages are
   woven into "The big picture" — not appended as a bare link. See the `keep-index-in-sync` rule.
4. `game-locker/lessons/0003-the-sync-engine.html` links out to this sub-course, and
   `shopify-data-migration/index.html` gets its "different lesson" sentence pointed here at last.
5. The repo-root `index.html` (the library landing page) counts re-derived, never incremented by
   hand, with **both** `.site/` and `*/.vercel-site/` excluded.
6. A learning record naming what the audit found and which facts were verified on which date.
7. `./deploy-site.sh` run so the live site matches.

## Build order

| Pass | What | Why in this order |
|---|---|---|
| 1 | `reference/the-store.html` + `reference/review-path.html` + `index.html` | The store must be defined before any lesson can use it, and the review goal is served on day one. |
| 2 | L01, L02 | The frame. Without these the storefront-first arc does not exist. |
| 3 | L05, L06, L08, L10 — the new-gap lessons | The only pages teaching something the repo does not already hold. |
| 4 | L03, L04, L07, L09, L11 + the other three references | The review-by-retelling half, plus the capstone. |
