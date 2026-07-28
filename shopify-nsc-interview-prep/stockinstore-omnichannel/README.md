# stockinstore-style Omnichannel — Interview Sub-Course

The PM said the client's system "is like the **stockinstore** app." This sub-folder
teaches that one domain in depth, in the same style as the main course.

**stockinstore** is an omnichannel (unified commerce) platform. It joins an online store
(Shopify, BigCommerce, Salesforce, etc.) to the stock sitting in physical shops. It has four
customer-facing products — **Find in Store**, **Store Locator**, **Click & Collect (BOPIS)**,
and **Ship from Store** — but the real engineering is the back end that syncs stock from many
store systems, computes trustworthy availability, and routes pickup and delivery orders.

## The angle

Every page is framed as: **"You are the backend engineer designing and building a
stockinstore-like system on Shopify + Node/NestJS."** This is not a guide to *using* the real
stockinstore app — it is a guide to *building one*, because that is what the client hires for.

## Why this exists

The main course already teaches "Shopify ↔ ERP sync at scale" as an abstract design.
stockinstore is that exact problem made concrete, with real edge cases: multi-source stock
feeds, a stock-availability engine, geospatial "near me" queries, and order allocation with a
fairness rule. Same reliability patterns (webhooks, queues, idempotent workers,
reconciliation) — new domain shape.

## Start here

1. **[index.html](index.html)** — the Map for this sub-course (single source of truth).
2. **[reference/study-plan.html](reference/study-plan.html)** — the 3-day schedule through all 11 lessons, 4 katas, and 4 reference cards.
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
11. Integrating Shopify with the stockinstore SaaS (Track B — integrate, not build) ✅

**Katas:** idempotent inventory upsert ✅ · find-in-store query API ✅ · Click & Collect reservation
+ re-check ✅ · order-allocation fairness scorer ✅

**Reference:** domain glossary ✅ · "Design stockinstore" cheat sheet ✅ · data-model card ✅ ·
rapid-fire Q&A ✅

**Status: the sub-course is complete** — 10 lessons, 4 katas, 4 reference cards. Each lesson was
built and then reviewed against four goals (correct, enough, detailed, clear) and fixed.

## How we work

Say **"next"** to build the next lesson, **"go deeper on X"** for more detail on any topic,
or **"mock me on stockinstore"** for a domain-specific system-design drill. When you get the
real job description, paste it and I re-target this sub-course to the client's actual stack.

**Keeping the Map current:** whenever a page is added, `index.html` is updated in the same
session — the new file joins the right chapter with a one-line description, and no link is ever
left broken. Keeping the Map in sync is part of "done."
