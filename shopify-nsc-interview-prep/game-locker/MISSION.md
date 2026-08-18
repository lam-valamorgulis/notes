# Mission — Game Locker

## Two goals, two parts

Revised **2026-08-17**. The sub-course used to have one goal: pass an interview. It now has two,
and it splits to match.

| Part | Goal |
|---|---|
| **A — Build It** | Understand Game Locker well enough to **rebuild the platform**. Not use it. Build it |
| **B — Win the Room** | Pass the interview. Positioning, spoken answers, the honesty line |

Part A is the bigger change. It exists because on 2026-08-17 a much better source arrived, and it
made a rebuild actually specifiable. Before that, the course was written from Game Locker's public
website and the job description — enough to talk, not enough to build.

## The job

**Shopify Engineer** at **Game Locker** (gamelocker.co). Australian owned, role based in Vietnam,
Engineering team, full time. Source: the job description PDF, read 2026-08-03.

## The source that changed everything

A real integration discovery, written against a **live Game Locker tenant** by an engineer at the
user's own agency, for a client who is a Game Locker **customer**. Two documents:

- **D1** — the original discovery, 2026-07-07, plus nine follow-up notes. Superseded.
- **D2** — the current state of record, 2026-07-31, plus three follow-up notes. Supersedes D1.

All of it came from **authenticated read-only sessions**. Nothing was written. Several of D1's
claims were **retracted by their own author** within three weeks, and those retractions travel with
the facts.

Everything checkable now lives in one place: **`reference/verified-facts.html`**. Lessons cite a row
there rather than re-arguing a fact. Four confidence labels: **verified · reported · inference ·
gap**.

## The confidentiality rule — read before editing any file here

The discovery is an agency's confidential work product about a **named client**. It contains that
client's name, six people by name, AUD budget figures, an internal communications hold, a vendor's
refusal email, and a logged client complaint.

**None of that enters this folder.** Two reasons, both real:

1. This folder is **published to a web host**. See the publishing notes in the parent course.
2. The course prepares for an interview at **Game Locker — who is the vendor in that story**.
   Quoting it in the room leaks your employer's and their client's business to a third party, and
   marks you as someone who leaks.

| Allowed in | Never in |
|---|---|
| Facts about **Game Locker's own product** — API shape, auth model, data model, tag and metafield names, buy-rule types, ledger columns, sync direction, catalogue scale, reprice cadence | The client's name. Any person's name. Budget figures. Ticket keys. Repository paths. Project status. Vendor emails. The client's internal tool names. Internal disagreements |

Exact source locators are deliberately **outside this repository**, in the session notes for
2026-08-17.

### How the user may say they know it

> "I've read a detailed integration discovery written against your platform."

Not *"I built it."* Nothing on that project is assigned to the user. This is still a strong, true
position, and **B01** and **B05** both teach it as one.

## What the new source corrected

Six things this course used to teach that were wrong. Full detail with evidence in
`reference/verified-facts.html` §3.

| Was | Is |
|---|---|
| "~145M cards, 18+ games" | **1,122,612** catalogue items, **19 games**, MTG 869,531, ~201 new/day |
| "daily repricing" | Right, and exact: a nightly batch that **publishes at 06:00**. Only **~4.4%** of MTG cards move on a given day; **~0.04%** move ≥30% |
| "a direct Shopify integration" | Confirmed at the strongest tier — Shopify's own event log shows the **Game Locker app creating and publishing products**. No public App Store listing |
| "Game Locker is the system of record; Shopify is a channel off it" | True for catalogue and price. **False for inventory** — their guidance is to write stock **in Shopify** and let it sync back |
| "condition × language × finish, fighting the 3-option cap" | **One** option axis: `Condition: NM/LP/MP/HP/DMG` = 5 variants. **Foil is a separate product.** Language is not modelled |
| "card attributes go to metafields and metaobjects" | Attributes arrive as **tags**. Two product metafields exist, **with no definitions**. Every variant metafield is empty |

Plus roughly eighteen facts the course did not have at all — the Cognito auth model, the
three-rule pricing engine (Sell / Buy / **Stop buy**), the finding that **buy price does not
reproduce** from the market price they expose, and the sharpest one: **Game Locker holds the
store-credit ledger**, keyed to the Shopify Customer ID.

## Hard constraints

- **The confidentiality rule above outranks everything else in this file.**
- **Confidence labels are mandatory.** A `gap` row is never stated as fact. Naming the edge of the
  knowledge is the point, not a weakness.
- **Retractions travel.** Where the source withdrew a claim, the course shows the withdrawal. A
  source that corrects itself in public is more trustworthy, not less — and the retracted numbers
  are exactly the ones a careless reader would quote.
- **The honesty line stays consistent with the rest of the course.** "I haven't authored a POS UI
  Extension. My agency shipped one and I've read it closely — found real bugs in it — but I haven't
  got one through review onto a shop floor." Pattern C (native Shopify POS) is never claimed as
  authored experience.
- **No invented facts about Game Locker.** Public site, the job description, or a labelled row in
  `verified-facts.html`. Inferences are labelled as inferences, with the sample size.

## Facts verified against shopify.dev on 2026-08-03 (do not re-derive)

- **Variant limit is 2048** per product, raised from **100** in **October 2025**. Media stays
  capped at **250** per product. Stores with 500k+ variants get a 10,000-new-variants-per-day
  limit.
- **Options per product remains 3.** Worth keeping even though Game Locker uses only **one** — the
  interesting question became *why they left two slots unused*, not *how to fit three things in*.
- **`productVariantsBulkUpdate` accepts up to 2048 variants per call.** The **250** figure is
  GraphQL *list pagination*, not a mutation limit. A single mutation caps at **50,000** inventory
  quantities.
- **`inventorySetQuantities` has `compareQuantity`** (compare-and-set) and
  **`ignoreCompareQuantity`** to bypass it. A mismatch returns a `userErrors` entry rather than
  overwriting.
- **Storefront API has no request rate limit** (they were removed); capacity scales with buyers by
  customer IP, and automated traffic is still throttled. Admin API remains cost-based. **Public**
  access tokens are for browser use; **private** ones are secrets for server-side calls.
- **Marketplace Kit is deprecated** — reference only. Shopify Collective is product *sourcing*;
  Markets is international selling. Multi-vendor is a third-party app or a custom build.
- **Core Web Vitals:** LCP ≤ 2.5s, CLS ≤ 0.1, **INP** ≤ 200ms (INP replaced FID). Shopify's **Web
  Performance report** is field data; **Lighthouse / PageSpeed** is a lab test.

Reused from the parent course, already verified there: the 8 inventory states, the
InventoryItem–Location–InventoryLevel triangle, `safety_stock`, pickup being POS Pro-only and
billed per location, the 6 `DeliveryMethodType` values including `RETAIL`, webhook retry being ~8
failures over ~4 hours then removal, and the POS UI Extension architecture.

## The rebuild target — decided 2026-08-17

**Game Locker itself**, the platform. Not the Shopify-side buy list, though that material is
carried inside A06 and B04.

**Stack: NestJS + Postgres**, TypeScript throughout, a queue for the batch jobs. Chosen to match
the `nodejs-mastery-in-1-year` course, which is NestJS not Express.

Eight modules, each with an observed behaviour as its acceptance test:

| Module | Must reproduce |
|---|---|
| `catalogue` | Cards, printings, sets, conditions. 19 games, ~1.12M items, ~201 new/day |
| `pricing` | Market feed → Sell / Buy / Stop-buy rules → global rounding. **Derived, never stored** |
| `reprice` | Nightly batch, publishes at 06:00. Only ~4% of rows move |
| `inventory` | Location-scoped stock. `{cardId}_{locationId}` identity. Multi-store |
| `buylist` | Orders with `orderType=buy`. Quoted → Reviewed → Completed. Cash or credit. `Profit %` |
| `ledger` | Per-customer credit balance, total spending, total sold, keyed to an external customer id |
| `shopify-sync` | Product and price out; inventory two-way. Tags not metafields. 5 condition variants, foil as a separate product |
| `api` | Tenant-scoped JWT, 24h tokens, one search endpoint serving two surfaces |

A07 ends with a **runnable proof**, not a full build: the pricing engine plus its rounding, tested
against the four real observed values — **including the one that does not reproduce.**

## Layout

Filenames keep their existing numbers so no cross-course link breaks. The Map carries the A/B
labels.

```
game-locker/
  index.html                 the Map — the single source of truth
  MISSION.md                 this file
  RESTRUCTURE-PLAN.md        the 2026-08-17 plan and its fact ledger
  assets/                    base.css + quiz.js

  PART A — BUILD IT
  lessons/ A01  0001  what Game Locker actually is
           A02  0002  the card data model, as actually built
           A03  0009  the pricing engine                    NEW
           A04  0003  the sync engine and the integration app
           A05  0004  the counter and the locations
           A06  0010  the buy list and the credit ledger    NEW
           A07  0011  rebuild Game Locker — NestJS + Postgres  NEW

  PART B — WIN THE ROOM
           B01  0008  the experience gap        ← read first
           B02  0005  themes for game stores
           B03  0006  Storefront API and the marketplace
           B04  0012  when the vendor will not give you an API  NEW
           B05  0007  the Game Locker interview

  reference/ verified-facts.html   ← the fact ledger. Start here for anything checkable
             24-hour-plan.html     two tracks: build and interview
             company-brief.html
             speaking-drills.html
             rapid-fire.html
             onepager.html
  learning-records/
```

## Reading order

- **Interview soon?** B01 first, then the 24-hour plan, then Part B, dipping into Part A only for
  A01, A02 §5 and A03.
- **Building?** `verified-facts.html` → A01 → A02 → A03 → A04 → A05 → A06 → A07.
- **Both?** verified-facts → A01 → A02 → A03 → B01 → A04 → A06 → A07 → B04 → B05.

## Build status

| Phase | Contents | Status |
|---|---|---|
| 1 | MISSION.md · index.html · reference/verified-facts.html | **done 2026-08-17** |
| 2 | A03, A06, A07, B04 — the four new lessons | **done 2026-08-17** |
| 3 | A01, A02, A04, B01, B05 — revisions carrying corrected facts | **done 2026-08-17** |
| 4a | Corrected facts pushed into all five reference pages | **done 2026-08-17** |
| 4b | 24-hour plan re-cut into **two tracks** (build vs interview) | pending |

`reference/verified-facts.html` is authoritative in every disagreement.

### Verified on 2026-08-17 after phases 1–4a

| Check | Result |
|---|---|
| Confidential-identifier scan across every file | **clean** — no client, person, budget, ticket key, repo path, or internal tool name |
| Vendor infrastructure identifiers | **redacted** — Cognito pool and app-client ids replaced with placeholders |
| Internal links | **0 broken** across 19 pages |
| `renderQuiz` / `renderRecall` blocks parse | **18 / 18** |
| Stale claims (145M, three-option model, 10.8%, hourly reprice) | Present **only** inside labelled correction notes and do-not-say rows |

**One pre-existing bug fixed along the way.** `reference/24-hour-plan.html` had two unescaped
straight apostrophes inside single-quoted JavaScript strings (`shop's`, `merchant's`). They were a
syntax error, so **the entire quiz and recall drill on that page had never rendered**. Both are now
curly apostrophes. This was broken before this session, not by it.

### What phase 4b still needs

The 24-hour plan is still a single interview sprint. It now points at corrected facts, so it is
safe to use — but it does not yet route Part A as its own track. If the interview is not imminent,
read `verified-facts.html` → A01 → A02 → A03 → A04 → A05 → A06 → A07 and ignore the hour blocks.

## Next, after the interview

- A learning record capturing which questions actually came up, and where the prep was wrong.
- Close the `gap` rows in `verified-facts.html` if any of them get answered in the room.
