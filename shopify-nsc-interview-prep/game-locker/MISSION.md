# Mission — Game Locker Shopify Engineer

## The job

**Shopify Engineer** at **Game Locker** (gamelocker.co). Australian owned, role based in
Vietnam, Engineering team, full time. Source: the job description PDF, read 2026-08-03.

## The deadline

**24 hours of net study time**, ending in a **live interview**. That is the whole constraint.
The plan is 24 one-hour blocks — see `reference/24-hour-plan.html`.

## The two weak spots (self-declared, front-loaded in the plan)

1. **POS + inventory sync** — 6 of the 24 blocks. Weakest area *and* the centre of their
   business, which is why it gets the most time.
2. **Speaking English under pressure** — 4 blocks, all spoken, no new material.

Together: 10 of 24 blocks. Deliberate. The knowledge is largely present (52 lessons already
written in the parent course); the gap is **retrieval and speech**, not reading.

## The finding that shaped everything

**Game Locker is not a Shopify store.** Their own site carries no Shopify signals. They are a
SaaS platform that game stores buy — card catalogue (~145M cards, 18+ games), daily repricing
from global price feeds, a **POS kiosk**, and **integrations with Shopify** plus an eBay
connector.

So they are the **system of record** and Shopify is a **channel hanging off them**. The role is
three arrows:

1. **Sync** — products, stock, prices out; orders, customers back. Fails quietly (drift).
2. **POS** — their kiosk owns the counter, so Shopify is downstream and briefly wrong after
   every counter sale. Fails loudly (oversell).
3. **Storefront** — themes for *their customers* (many game stores, one theme) plus the new
   TCG marketplace. Fails visibly.

This maps almost exactly onto material that already existed: `lessons/0011` (Shopify ↔ ERP
sync), the whole `stockinstore-omnichannel/` sub-course, the whole `pos-in-store/` sub-course,
and `lessons/0018` (bulk operations). The sub-course therefore **routes** rather than repeats.

## Gaps this sub-course exists to close

Audited against the parent course before writing anything:

| JD requirement | Was it covered? | Action |
|---|---|---|
| Admin API, webhooks, custom apps, bulk ops | Yes — `lessons/0001–0005`, `0018` | Route to it |
| POS, POS UI Extensions | Yes — `pos-in-store/` 8 lessons | Route to it |
| Inventory sync, oversell, click & collect | Yes — `stockinstore-omnichannel/` 11 lessons | Route to it |
| Liquid, OS 2.0, sections/blocks/JSON templates | Partly — `theme-architecture/` 4 lessons, but Liquid syntax is explicitly out of scope there | L05 applies it to multi-merchant |
| **Front-end performance** | **No** — one README mention only | **L05 §4** |
| Storefront API | Thin — mentioned in 6 pages, no dedicated treatment | **L06 §5** |
| **TCG card data modelling** | **No** | **L02** |
| **Multi-vendor marketplace** | **No** | **L06** |
| **The company itself** | **No** | **L01 + company brief** |
| Speaking under pressure | Partly — `lessons/0015`, `0029` are behavioural, not language | **speaking-drills.html** |

## Hard constraints

- **The honesty line stays consistent with the rest of the course.** "I haven't authored a POS
  UI Extension. My agency shipped one and I've read it closely — found real bugs in it — but I
  haven't got one through review onto a shop floor." Pattern C (native Shopify POS) is never
  claimed as authored experience. This matches `pos-in-store/MISSION.md` as revised 2026-08-03.
- **No invented facts about Game Locker.** Everything in `reference/company-brief.html` comes
  from their public site or the JD. Inferences are labelled as inferences.
- **No client or employer names** beyond what is already public. The PD Bitbucket repo is
  referred to only as "my agency shipped one".

## Facts verified against shopify.dev on 2026-08-03 (do not re-derive)

- **Variant limit is 2048** per product, raised from **100** in **October 2025**. Media stays
  capped at **250** per product. Stores with 500k+ variants get a 10,000-new-variants-per-day
  limit.
- **Options per product remains 3.** This is the constraint that decides the TCG data model —
  condition × language × finish, with set/rarity/artist pushed to metafields and metaobjects.
- **`productVariantsBulkUpdate` accepts up to 2048 variants per call.** The **250** figure is
  GraphQL *list pagination*, not a mutation limit. A single mutation caps at **50,000**
  inventory quantities.
- **`inventorySetQuantities` has `compareQuantity`** (compare-and-set) and
  **`ignoreCompareQuantity`** to bypass it. A mismatch returns a `userErrors` entry rather than
  overwriting. This was **not** covered anywhere in the existing course and is the strongest
  single answer to "how do you stop two syncs fighting".
- **Storefront API has no request rate limit** (they were removed); capacity scales with buyers
  by customer IP, and automated traffic (bots, crawlers) is still throttled. Carts have no
  global rate limit. Admin API remains cost-based. **Public** access tokens are for browser
  use; **private** ones are secrets for server-side calls.
- **Marketplace Kit is deprecated** — docs say reference only. Shopify Collective is product
  *sourcing* between brands, not a marketplace platform; Markets is international selling.
  Multi-vendor is therefore a third-party app or a custom build.
- **Core Web Vitals:** LCP ≤ 2.5s, CLS ≤ 0.1, **INP** ≤ 200ms (INP replaced FID). Shopify's
  **Web Performance report** is field data from real visitors; **Lighthouse / PageSpeed** is a
  lab test. Documented theme performance causes: too many sections per template, unpaginated
  large collections, third-party apps and tags, inefficient Liquid raising render time.

Facts reused from the existing course (already verified there, not re-checked): the 8 inventory
states, the InventoryItem–Location–InventoryLevel triangle, `safety_stock`, pickup being POS
Pro-only and billed per location, multi-location inventory being available on Lite, the 6
`DeliveryMethodType` values including `RETAIL`, webhook retry being ~8 failures over ~4 hours
then removal, and the POS UI Extension architecture (Preact/TSX + TOML, `remote-dom`, tile /
action / block targets, Cart API writes but read-only line items, Connectivity + Storage,
Direct API Access).

## Layout

Same shape and page template as the sibling sub-courses (`pos-in-store/`,
`stockinstore-omnichannel/`), with its own `assets/base.css` + `quiz.js` copied from
`pos-in-store/`.

```
game-locker/
  index.html                     the Map — single source of truth
  MISSION.md                     this file
  assets/                        base.css + quiz.js
  lessons/   0001 what Game Locker actually is
             0002 TCG card data on Shopify
             0003 the sync engine            ← the core lesson
             0004 POS and the counter
             0005 themes for game stores     ← incl. performance
             0006 Storefront API & the marketplace
             0007 the Game Locker interview  ← capstone
  reference/ 24-hour-plan.html   ← START HERE
             company-brief.html
             speaking-drills.html
             rapid-fire.html     50 questions
             onepager.html       the last hour
  learning-records/
```

Reading order is L01 → L02 → L03 → L04 → L05 → L06 → L07, but the **24-hour plan is the real
entry point** — it interleaves these seven with about 15 pages from the parent course and puts
the spoken drills at the end.

## Next, if there is time after the interview

- A learning record capturing which questions actually came up, and where the prep was wrong.
- If they use a public Shopify app, read its App Store listing for scopes and integration shape
  — that was listed as pre-call research and is not yet done.
