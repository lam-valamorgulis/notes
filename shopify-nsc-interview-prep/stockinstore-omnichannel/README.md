# stockinstore-style Omnichannel — Interview Sub-Course

The PM said the client's system "is like the **stockinstore** app." This sub-folder
teaches that one domain in depth, in the same style as the main course.

**stockinstore** is an omnichannel (unified commerce) platform. It joins an online store
(Shopify, BigCommerce, Salesforce, etc.) to the stock sitting in physical shops. It has four
customer-facing products — **Find in Store**, **Store Locator**, **Click & Collect (BOPIS)**,
and **Ship from Store** — but the real engineering is the back end that syncs stock from many
store systems, computes trustworthy availability, and routes pickup and delivery orders.

## The two angles

"Like stockinstore" means one of two jobs, so the sub-course teaches both to the same depth.

**Track A — build it** (Lessons 1–10). Framed as: **"You are the backend engineer designing and
building a stockinstore-like system on Shopify + Node/NestJS."** Not a guide to *using* the real
app — a guide to *building one*.

**Track B — integrate it** (Lessons 11–20). The client bought the platform. Framed as: **"You are
the engineer wiring a third-party omnichannel SaaS into their Shopify store and their tills."**
The vendor owns availability, reservations and allocation; you own the stock feed, the identifier
mapping, the storefront surfaces and the write-back — and that is where integrations actually fail.

Ask the client which job it is on day one. Lesson 1 (the domain) serves both.

## Why this exists

The main course already teaches "Shopify ↔ ERP sync at scale" as an abstract design.
stockinstore is that exact problem made concrete, with real edge cases: multi-source stock
feeds, a stock-availability engine, geospatial "near me" queries, and order allocation with a
fairness rule. Same reliability patterns (webhooks, queues, idempotent workers,
reconciliation) — new domain shape.

## Start here

1. **[index.html](index.html)** — the Map for this sub-course (single source of truth).
2. **[reference/study-plan.html](reference/study-plan.html)** — the 5-day schedule through all 20 lessons, 5 katas, and 5 reference cards (Days 1–3 build it, Days 4–5 integrate it).
3. **[lessons/0001-omnichannel-problem-and-domain.html](lessons/0001-omnichannel-problem-and-domain.html)** — read this first.

## Folder map

| Folder | What's in it |
|--------|--------------|
| `index.html` | The Map — connects every page as one story. |
| `lessons/` | Deep lessons on the domain and how to build it. |
| `exercises/` | Live-coding katas (build-from-blank and debug-and-fix). |
| `reference/` | Cheat sheets: glossary, "Design stockinstore" card, data model, rapid-fire Q&A. |
| `learning-records/` | Progress notes, one per milestone. |
| `assets/` | Shared styles + quiz engine (copied so this folder is self-contained). |

## Build plan (built across sessions)

**Lessons**
1. The omnichannel problem & the stockinstore domain ✅
2. Inventory ingestion & multi-source sync ✅
3. The stock availability engine ✅
4. Find in Store & Store Locator — the read path ✅
5. Click & Collect / BOPIS order flow ✅
6. Ship from Store & the OMS fairness allocation ✅
7. Event-driven backbone: webhooks & queues ✅
8. Data model & consistency ✅
9. Scale, multi-tenancy & failure modes ✅
10. System-design interview: "Design stockinstore" ✅

**Track B — integrate the SaaS instead of building it** (Chapter 7 on the Map)

11. Integrating Shopify with the stockinstore SaaS — the overview and the responsibility split ✅
12. The vendor stock-feed connector — a relay, not an ingest ✅
13. Identifier mapping & the mapping registry ✅
14. The storefront surface — theme app extensions in depth ✅
15. Click & Collect at checkout (integration POV) ✅
16. Webhooks, write-back & reconciliation ✅
17. Vendor risk: scopes, protected customer data, SLA & fallback ✅
18. The integration project: discovery to rollout ✅
19. Build vs buy, lock-in & the exit ✅
20. The Track B interview drill (capstone) ✅

**Katas:** idempotent inventory upsert ✅ · find-in-store query API ✅ · Click & Collect reservation
+ re-check ✅ · order-allocation fairness scorer ✅ · the vendor feed connector (Track B) ✅

**Reference:** domain glossary ✅ · "Design stockinstore" cheat sheet ✅ · data-model card ✅ ·
rapid-fire Q&A ✅ · "Integrate the SaaS" cheat sheet ✅ · study plan ✅

**Status: the sub-course is complete on both tracks** — 20 lessons, 5 katas, 5 reference cards.
Lessons 1–10 teach how to **build** an omnichannel platform; Lessons 11–20 teach how to
**integrate** one the client has already bought, to the same depth. Every Shopify and vendor fact
in Lessons 12–20 was verified against shopify.dev and stockinstore.com on 2026-08-04, and each
lesson carries a footnote saying exactly what was checked and what is engineering opinion.

Two corrections landed in Lesson 11 during that pass, both recorded in its footnote [2]: the
pickup-fulfilment scope is `write_merchant_managed_fulfillment_orders` (not the narrower-sounding
assigned scope, because a retail store is a merchant-managed location), and stockinstore's own
Click & Collect app targets **Shopify Plus** while their Find in Store app runs on Basic — a
vendor plan gate that is separate from Shopify's.

## How we work

Say **"next"** to build the next lesson, **"go deeper on X"** for more detail on any topic,
**"mock me on stockinstore"** for the build-it system-design drill, **"mock me on Track B"** for
the integration drill, or **"mock me on build vs buy"** for just that decision. When you get the
real job description, paste it and I re-target this sub-course to the client's actual stack.

**Keeping the Map current:** whenever a page is added, `index.html` is updated in the same
session — the new file joins the right chapter with a one-line description, and no link is ever
left broken. Keeping the Map in sync is part of "done."
