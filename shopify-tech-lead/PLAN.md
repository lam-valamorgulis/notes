# Plan — `shopify-tech-lead/`

Written 2026-08-23, after a five-round grilling session. Terms used here are
defined in [CONTEXT.md](CONTEXT.md). The data-handling rule is
[ADR 0001](docs/adr/0001-synthetic-catalogue-from-shape-samples.md).

## The goal, and why the old Course cannot serve it

**Goal:** a confident Shopify tech lead who can hold a real design conversation
with a client and a PM.

The old Course (`../shopify-nsc-interview-prep/`) was built to pass one interview
in one week. A Course of HTML pages cannot build hands-on experience. Only
building a working sync can. So the new Course has a running **Project** at its
centre, and the reading exists to serve the build.


## What was decided

| # | Decision |
|---|---|
| 1 | New folder `shopify-tech-lead/`. The old folder is deleted only at the end, once every surviving Lesson has a home and the link check passes |
| 2 | Three Tracks: **Platform**, **Apps & Integrations**, **The Room** |
| 3 | Vocabulary fixed: Course → Track → Chapter → Lesson. "Sub-course" retires |
| 4 | All six old sub-courses dissolve. Their content merges into the three Tracks |
| 5 | Interviews stay, as one Chapter inside The Room. They are no longer the mission |
| 6 | Every Lesson has four fixed blocks: **How it works → Where it hurts → What you say to a client/PM → Remember this** |
| 7 | Each Track gets one **Scars** Reference that collects its "Where it hurts" blocks |
| 8 |The company-specific sub-course is removed. Its technical *patterns* survive, with no company, client, tenant or traceable number |
| 9 | `stockinstore` keeps its real name. Its integration half survives; its SaaS-design half compresses hard |
| 10 | The **Project** is a NestJS + Postgres service syncing a **Fake ERP** with a **Dev store**. It lives in `shopify-tech-lead/project/` in the private `learn` repo, excluded from publishing |
| 11 | The Client store is read-only, used for shape, scale, and reading a real integration in flight. See ADR 0001 |
| 12 | Backend depth is scoped to what the Project needs — about four Lessons. `nodejs-mastery-in-1-year` has no NestJS Lesson yet, so it cannot be linked for that |
| 13 | 10–15 hours a week, no deadline |

## Size — the honest number

I estimated 40–50 Lessons during the grilling. Doing the merge properly lands at
**67**. Cutting to 45 would mean dropping real gaps, not trimming fat.

So 67 Lessons, with **47 marked as the core path** and **20 marked optional
depth**. At 12 hours a week the core path plus the Project is about 3 months; all
67 is about 4 to 5 months.

### Then the territory map added 16 more

That estimate was the *merge* of the old course. It was not a survey of Shopify.
Building `reference/territory-map.html` — rating every area a tech lead meets by
core / important / edge and by pain — named **fourteen areas with no coverage at
all**, plus shipping and tax, which the merge had missed entirely.

Filling them added **16 Lessons**, so the real total is **83**: three Chapters new
to Track 1 (P8 After the sale, P9 Other ways to sell, P10 Conversion, content and
risk), P7 for shipping and tax, one Lesson each added to P4, A1 and A2.

**Final: 83 Lessons — 58 core, 25 depth.** At 10–15 hours a week the core path plus
the Project is three to four months; all 83 is five to six.

Per Track: Platform **23 core / 13 depth** · Apps & Integrations **20 core / 3
depth plus the 5 Project steps** (it is the point of the Course, so almost nothing
is optional) · The Room **10 core / 9 depth**. Depth is concentrated in Track 1's
storefront and theme Chapters, because those are already a strength, and in Track
3's long-form design walkthroughs.

```
old: 93 Lessons · 41 References · 10 katas · 151 pages · 7 Maps
new: 83 Lessons · 15 References ·  0 katas (they became Project steps) · 4 Maps
```

---

## Track 1 — Platform (36 Lessons)

What Shopify itself is. The vocabulary you need before any integration
conversation makes sense.

### P1 · The shape of Shopify (3)
| Lesson | Source |
|---|---|
| The Shopify object model, end to end | **NEW** — gap. Shop, product, variant, inventory item, inventory level, location, order, fulfillment order, customer, and how they hang together |
| The two APIs, and the rate limit model | `lessons/0001` — revise. REST Admin is **legacy since 2024-10-01**; new public apps must be GraphQL-only **since 2025-04-01** ([changelog](https://shopify.dev/changelog/starting-april-2025-new-public-apps-submitted-to-shopify-app-store-must-use-graphql)) |
| API versioning and the quarterly upgrade | **NEW** — gap. Why "we upgrade every quarter" is a line item in every estimate |

### P2 · Custom data (2) — missing entirely from the old Course
| Lesson | Source |
|---|---|
| Metafields, definitions, and the cost of skipping them | **NEW**. Carries the absorbed pattern: a real integration writing metafields with **no definitions**, so the admin shows nothing and nothing is queryable |
| Metaobjects, and when data does not belong on the product | **NEW** |

### P3 · Inventory, locations and the till (3) — from `pos-in-store` (8 → 3)
| Lesson | Source |
|---|---|
| Locations and multi-location inventory | `pos-in-store/0003` — survives |
| The till: POS Lite, POS Pro, the retail order, and UI extensions | merge `pos-in-store/0001` + `0004` + `0005` + `0008` |
| Three ways in-store stock reaches the storefront | `pos-in-store/0002` — survives. The best sync-shaped Lesson in that folder |

### P4 · The storefront (4) — from `theme-architecture` + absorbed
| Lesson | Source |
|---|---|
| Dawn, Horizon and theme blocks | merge `theme-architecture/0001` + `0002` |
| The Cart AJAX API | `theme-architecture/0003` — survives |
| Discounts on the storefront | `theme-architecture/0004` — survives. Keeps the verified deprecated-price-fields trap |
| Liquid or headless — the client conversation | **NEW**, absorbingtwo Lessons from the removed sub-course and `stockinstore/0014` (theme app extensions) |

### P5 · Checkout, money and Plus (4)
| Lesson | Source |
|---|---|
| Checkout extensibility | `lessons/0023` — survives |
| Shopify Functions | `lessons/0024` — survives, keeps the verified `paymentMethodHide` fix |
| Shopify Plus, and Markets | `lessons/0025` + **NEW** Markets content — gap |
| Flow: when automation replaces your code | **NEW** — gap. A tech lead has to know when *not* to write an app |

### P6 · Getting data in and out (6) — from `shopify-data-migration` (9 → 6)
| Lesson | Source |
|---|---|
| What a migration is, and what never moves | merge `.../0001` + `0002` |
| The matching key, and custom IDs | `.../0003` — survives. Holds the custom-ID discovery |
| Three ways to push it, and bulk operations | merge `.../0004` + `lessons/0018` |
| The huge catalogue load, and the throttle that only starts at 500,000 | `.../0005` — survives, **with a correction**. Re-verified 2026-08-23: the old lesson's "two pages disagree" framing is now stale. Both shopify.dev pages agree — the extra throttle starts at **500,000 variants on the store**, then caps new ones at **10,000/day**, and Plus is exempt |
| Orders, money, and the Shopify → Shopify replatform | merge `.../0006` + `0007` |
| The cutover and the proof | merge `.../0008` + `pos-in-store/0006` |

**Track 1 Scars** — one Reference collecting every "Where it hurts" above.

---

## Track 2 — Apps & Integrations (28 Lessons) · the heart of the Course

You integrate Shopify by building an app. The app is the vehicle; the sync is the
job. This Track carries the Project.

### A1 · What an app is (4)
| Lesson | Source |
|---|---|
| Anatomy of a Shopify app | `lessons/0004` — revise: public vs custom, app config as code |
| App auth: session tokens and token exchange | `lessons/0003` — survives |
| Webhooks done right | `lessons/0002` — survives |
| Scopes, protected customer data, and the mandatory webhooks | `stockinstore/0017` — reshaped |

### A2 · The backend the app needs (4) — hard-scoped to the Project
| Lesson | Source |
|---|---|
| The NestJS module shape for a sync service | `lessons/0007` + `lessons/0008` merged and trimmed |
| A Postgres schema for a sync store | `lessons/0009` — reshaped from "SQL vs NoSQL" into "the schema you need" |
| One queue, with retries and a dead-letter | merge `lessons/0012` + `stockinstore/0007` + kata 05 |
| Run it: docker-compose, CI, and what to log | merge `lessons/0013` + `lessons/0014` |

`lessons/0006` (Node event loop) **dies here** — it links out to
`../nodejs-mastery-in-1-year/lessons/0003`, which does cover it.

### A3 · The sync discipline (7) — from `shopify-data-sync` (11 → 7)
The strongest material in the old Course. It survives nearly whole.

| Lesson | Source |
|---|---|
| Shopify alone, and what a second system adds | merge `sync/0001` + `0002`. **Genericise** — `0002` namesa company in its title |
| Ownership, per field not per record | `sync/0003` — survives. The spine of the Track |
| Absolute writes, safe replay, and tombstones | merge `sync/0004` + `0005` |
| Webhooks are a hint — clocks, order and staleness | merge `sync/0007` + `0006` |
| The backlog | `sync/0008` — survives |
| Reconciliation, and numbers that do not lie | `sync/0009` — survives |
| Store 17 of four hundred | `sync/0010` — survives. Multi-tenancy |

`sync/0011` splits: the client-conversation half goes to The Room, the interview
half dies.

### A4 · Real connectors (6)
| Lesson | Source |
|---|---|
| Integration patterns: ERP, CRM, payments, fulfillment | merge `lessons/0005` + `lessons/0027` |
| Set piece: design a Shopify ↔ ERP sync at scale | `lessons/0011` — survives |
| The vendor stock-feed connector: CSV and SFTP | `stockinstore/0012` — survives. What half of real clients actually give you |
| Identifier mapping and the mapping registry | `stockinstore/0013` — survives |
| When the vendor will not give you an API | `game-locker/0012` — **genericised**. No company, no tenant |
| Worked example: integrating a stock-availability SaaS | merge `stockinstore/0011` + `0015` + `0004` + `0005` + `0016` |

### A5 · The Project (5) — the running build
Not reading. A repo with commits, run against a Plus **Dev store**.

| Step | What you build |
|---|---|
| **0** | The Dev store, the Shape sample, and the synthetic catalogue generator (ADR 0001) |
| **1** | The Fake ERP — products, prices, stock per location, an order inbox, and switches to break it on purpose |
| **2** | Catalogue out: the bulk load, then keeping it fresh. Absorbs kata 03 |
| **3** | Webhooks in and inventory back: HMAC on the raw body, 200 inside 5s, dedupe on `X-Shopify-Webhook-Id`, and the race. Absorbs katas 01 and 02 |
| **4** | The queue, the dead-letter, the reconciliation report — then break the ERP and prove the report catches it. Absorbs kata 05 |

All 10 old katas become Project steps. None survive as standalone drills.

**Track 2 Scars** — includes the absorbed patterns, company-free:

- A vendor refuses to issue API keys, so you integrate server-side or not at all
- A price is **derived from rules, never stored**, so you cannot read it back
- SKU identity is `{itemId}_{locationId}`, and the product-level id silently
  matches only one variant
- The vendor holds a **credit ledger**, so issuing store credit in Shopify creates
  two ledgers for the same money. Note: **not demonstrable on a Dev store** —
  Store Credit and Gift Cards are unsupported there ([Dev stores](https://shopify.dev/docs/apps/build/dev-dashboard/stores/development-stores))
- Inventory is written in **Shopify** and flows *back* to the system of record,
  reversing who owns the field. The single best "where it hurts" lesson available

---

## Track 3 — The Room (19 Lessons)

Every human-facing conversation: client, PM, mentee, interviewer. Same muscle.

### R1 · Talking about systems (4)
| Lesson | Source |
|---|---|
| System design, explained out loud | `lessons/0010` — re-aimed from "know it" to "say it" |
| Design a stock-availability platform: domain and engine | compress `stockinstore/0001` + `0003` |
| Allocation, data model, consistency and failure at scale | compress `stockinstore/0006` + `0008` + `0009` |
| The design conversation: whiteboard for a client, not a grader | merge `stockinstore/0010` + `0020` |

`stockinstore/0002` merges into A3. `stockinstore/0007` merges into A2.

### R2 · Owning the work (6)
| Lesson | Source |
|---|---|
| Owning ambiguous scope | `lessons/0019` |
| Estimating, pacing, and holding two projects | merge `lessons/0020` + `0021` |
| Communicating with a busy client | `lessons/0022` + `reference/pm-talk-prep` |
| Agile delivery as a senior | `lessons/0017` |
| The integration project: discovery to rollout | `stockinstore/0018` |
| Build vs buy, lock-in, and the exit | `stockinstore/0019` |

### R3 · The sentences (4) — English under pressure
Fixed phrases to drill out loud. This is where "confident" actually comes from.

| Lesson | Source |
|---|---|
| Buying thinking time, and saying "I don't know yet" | **NEW** |
| Saying no without sounding negative | **NEW** |
| A range, not a number | **NEW** |
| Disagreeing upward, and the senior narrative | `lessons/0015` + **NEW** |

### R4 · Mentoring and pressure (2)
| Lesson | Source |
|---|---|
| Mentoring and code review, both directions | `lessons/0028` |
| Confident problem-solving under pressure | `lessons/0029` + `reference/management-scenarios-drill` |

### R5 · Interviews (3)
| Lesson | Source |
|---|---|
| What a Shopify tech-lead interview actually probes | **NEW** — replaces four company-specific interview Lessons |
| The full mock | `lessons/0016` — survives |
| The experience gap: talking about what you have not built | `game-locker/0008` — **genericised**. You just lived this one |

Dying: `game-locker/0007`, `pos-in-store/0007`, `shopify-data-migration/0009`,
`lessons/0026`. Their questions merge into the **Rapid-fire** Reference.

**Track 3 Scars** — the conversation traps: the estimate you gave too early, the
"yes" that became a commitment, the design you defended past the point of being
right.

---

## References (41 → 15)

**Survive or merge:** Glossary (four old glossaries merged) · Shopify object model
card **NEW** · Rate limits and throttles card **NEW** · Ownership matrix ·
Conflict cases · What-moves matrix · Migration runbook · Rapid-fire (two merged,
plus the dead interview Lessons' questions) · Mock run sheets · Behavioral STAR
worksheet · Client/PM phrasebook **NEW** (collects R3) · three **Scars** pages.

**Die:** every sprint-pacing page — `study-plan-7day`, `study-plan` ×2,
`24-hour-plan`, `day1-mastery-diagnostic`, `day5-recall-check`,
`night-before-onepager`, `onepager` ×2. They assumed a one-week deadline that no
longer exists. Also `company-brief` and `verified-facts`.

**Move to `project/`, as real code:** `auth-token-exchange-recipe`,
`nestjs-orders-module-recipe`, `webhook-erp-worker`, `background-workers`. They
are code, not reading.

---

## Build order and status

| Phase | Deliverable | Status |
|---|---|---|
| **0** | Scaffold: `CONTEXT.md`, `MISSION.md`, ADR 0001, `assets/`, root Map, three Track Maps | **done** |
| **1** | A5 Steps 0–2 + the catalogue generator (runs, typechecks, deterministic) | **done** |
| **2** | Track 2: A1 → A4, 21 Lessons | **done** |
| **3** | Track 1 Platform, 22 Lessons | **done** |
| **4** | Track 3 The Room, 19 Lessons | **done** |
| **4b** | All 15 References, including three Scars pages | **done** |
| **5** | Root landing page recount, delete `../shopify-nsc-interview-prep/` | **done** |
| **6** | Commit and deploy | **done** |
| **7** | `reference/territory-map.html` — rate every area, name every gap | **done** |
| **8** | Fill all 16 gaps: P7, P8, P9, P10, P4.5, A1.5, A2.5 | **done** |
| **9** | Check-and-fix pass: links, cross-references, counts, Scars coverage, fact sweep | **done** |

### What is written

**All 83 Lessons**, including Project Steps 3 and 4 — webhooks in with inventory flowing back, and
the queue plus dead-letter plus the reconciliation report with its ten-row break-it table.

Nothing is left to *write*. What remains is to **do**: build the Project. Step 3 onward needs a Dev
store and a public tunnel, and the store work was deliberately deferred.

**All 15 References:** three Scars pages, the territory map, the Glossary, object model card, what-moves matrix,
migration runbook, ownership matrix, conflict cases, rate limits card, phrasebook, rapid-fire,
STAR worksheet, mock run sheets.

### Verified after the build

| Check | Result |
|---|---|
| Broken internal links, repo-wide | **0 of 3,850** |
| `<div>` balance, every page | all balanced |
| Orphan files not linked from a Map | **0** |
| Lessons missing one of the four fixed blocks | **0 of 65** |
| Mislabelled cross-references (an `A3.2` link pointing elsewhere) | **0 of 62** |
| Markdown syntax leaking into HTML | none |
| Malformed tags | none |
| Secret-bearing files staged for publishing | none |
| Personal prose surviving into the published copy | none |

### Content errors found and fixed in the verification pass

1. **Project Step 2 asserted CSV import limits** — "15 MB cap, cannot be cancelled" — which
   Lesson P6.2 explicitly says were *not* verified, because those rules live on help.shopify.com
   rather than shopify.dev. Step 2 now points at the unverified note instead of stating numbers.
2. **The Track 2 Map still called the variant throttle a live doc disagreement.** It was resolved
   on 2026-08-23 when both shopify.dev pages were re-checked and found to agree. The Map now
   describes the card as dating every number instead.
3. Three malformed tags from earlier drafts (`</summary>`, `</question>`, `</b]`) and one markdown
   `**bold**` inside HTML, all caught by the structural sweep.

### The check-and-fix pass after the gap-filling (2026-08-23)

Phase 8 added 16 Lessons. Phase 9 checked the whole Course again and found six real
faults. All are fixed.

1. **Two lessons were inserted mid-Chapter, which silently renumbered the Lessons
   after them.** `0036` went into P4 before Discounts, so Discounts moved from P4.4
   to P4.5. `0027` went into A1 before Scopes, so Scopes moved from A1.4 to A1.5.
   Six cross-references elsewhere still pointed at the old positions. Both new
   Lessons were moved to the **end** of their Chapter, which restores every existing
   number and reads better anyway. **The lesson: inserting into the middle of an
   ordered list is a breaking change.**
2. **Three broken links** — `../reference/` written from inside `platform/lessons/`,
   which needs `../../reference/`.
3. **Every count claim was stale.** The Course Map said 71 Lessons and the site
   landing page said 65; disk said 83. Both recounted from disk, per the counting
   rule.
4. **The territory map still listed all fourteen gaps as open** after every one had
   been filled. Rewritten: the fourteen moved into the covered table, and the gap
   list was rebuilt from scratch by searching every page for each candidate area.
   **Nine real gaps remain** — starting with fulfillment orders and bundles.
5. **Two Lessons made stale claims about the map** — Track 1 called P8 "the top gap"
   and `0036` said it "closes the last gap". Both rewritten to say what is now true.
6. **The Scars pages were missing 13 Lessons entirely**, including P6.1, the
   matching key — the single most important Lesson in the Course. Their subtitles
   claim "Every 'Where it hurts' from Track 1", which was false. Fixed by generating
   the missing scars **verbatim from the Lesson sources** rather than rewriting them,
   so no fact was restated from memory. All 78 Chapter Lessons are now cited.

Checks that came back clean: 0 broken links · 0 unbalanced `<div>` · 0 orphan pages ·
0 malformed tags · 0 Markdown residue outside code blocks · 83/83 Lessons carry all
four blocks and a recall card · 266 cross-references checked, 0 mismatched · the
number sweep found the only repeated old figures (50,000 / 1,000 per day) to be
deliberate history notes about the doc disagreement, not errors.

### The old Course is deleted — what it needed first

Deleting `shopify-nsc-interview-prep/` was not a one-line job. Three things had to happen first, and
they are worth recording because the same trap will recur:

1. **The React course linked into it 42 times** across 7 files in
   `react-mastery-in-1-year/frontend-interview-sprint/`. Deleting first would have broken that course
   and failed the deploy link check. Every link was remapped to its Track 3 successor. Two old
   sprint-pacing references — `night-before-onepager` and `four-hard-moments-drill` — have no
   successor, so those now point at the nearest honest equivalents (mock run sheets, phrasebook).
2. **`game-locker/RESTRUCTURE-PLAN.md` was untracked**, so git would not have kept it. Copied to
   `~/.claude/session-data/2026-08-23-game-locker-RESTRUCTURE-PLAN.md` before deletion.
3. **The root landing page's stats block was stale.** Recounted from disk rather than incremented, as
   the counting rule requires: 271→204 pages, 180→152 lessons, 62→35 references, 14→4 katas.

187 files removed with `git rm`, so the history keeps them.

### Deliberately still open

- **Building the Project.** All five steps are written; none is built. That is the point — the
  scaffold is given, the logic is typed.
- **The Dev store.**The store domain is in `.env.example`, but whether it is genuinely a
  development store is **unverified** — `plan.partnerDevelopment` was never read, because switching
  stores kept revoking the MCP token. **Confirm before loading 10,000 synthetic products into it.**
- **Deploy.** Nothing has been published. `--check-only` passes.

## Accountability

- **Checklist used:** source-first verification per the global rule. Every Shopify
  claim in this plan was read from shopify.dev on 2026-08-23, not from memory.
  `deploy-site.sh`, `.gitignore`, and all 93 Lesson titles were read from disk.
- **Evidence:** REST-legacy and GraphQL-only dates — shopify.dev changelog.
  Dev-store plans including Plus at no cost, and the Store Credit / Gift Card
  limitation — shopify.dev Dev stores page. Publishing behaviour — `deploy-site.sh`
  lines 30–75, read directly. Corrected one of my own recommendations mid-session:
  `nodejs-mastery-in-1-year` has 8 Lessons and **no NestJS Lesson**, so it cannot
  carry the backend depth.
- **Phase 9 evidence:** the check battery above, re-run to green after each fix.
  Scars additions were machine-extracted from the Lesson files, not retyped. The
  nine new territory-map gaps were each confirmed absent by searching every page
  before being listed.
- **Accountable:** Lam Dang.
- **If wrong:** every phase is additive inside `shopify-tech-lead/`. Roll back with
  `rm -rf shopify-tech-lead/`. The old Course is untouched until Phase 5, so
  nothing is lost until the plan has already proven itself.

## Resolved item — the variant throttle

Re-verified 2026-08-23, and the answer moved. As of 2026-08-03 two Shopify pages
disagreed: 1,000 variants/day versus 10,000/day. Both shopify.dev pages now agree:

- The extra throttle applies once a store holds **500,000 product variants**.
- Past that, **no more than 10,000 new variants per day**.
- **Plus stores are exempt.**
- It covers `productCreate`, `productUpdate`, `productVariantCreate` and the
  matching REST product endpoints.

Sources, both read on 2026-08-23:
[GraphQL limits](https://shopify.dev/docs/api/usage/limits) ·
[REST rate limits](https://shopify.dev/docs/api/admin-rest/usage/rate-limits).

**Two consequences.** First, the old lesson's "the docs disagree, so measure it
yourself" framing is stale and must not be copied forward — though the *habit* of
measuring survives, since this is the second time this number has moved. Second,
the Project's synthetic catalogue sits far below 500,000 variants, so this throttle
will never fire during the build. What will actually slow Step 2 down is the
ordinary rate limit: the GraphQL cost bucket, and on a non-Plus store the smaller
REST bucket of 40 requests with a 2/second leak, against 400 and 20/second on Plus.
