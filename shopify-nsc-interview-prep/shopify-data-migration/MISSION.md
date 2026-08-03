# Mission — Shopify Data Migration

## Why

Every Shopify job eventually hands you the same task: *"here is their old data, get it into Shopify."*
It arrives as an onboarding job (a new merchant joins the platform), a replatform (they are
leaving Magento, WooCommerce, Lightspeed, a legacy till), or a store-to-store move. It is high
risk and highly visible — wrong prices go live, order history disappears, SEO traffic drops the
day the domain switches. The goal is to own one of these end to end, and to answer for it in an
interview without guessing.

## Success looks like

- Say, from memory, **which records move, which break, and which can never move** — and why
  customer passwords are in the third group.
- Choose the **matching key** for a migration in the first five minutes, and explain why that one
  decision is what makes the whole job re-runnable.
- Pick between **CSV import, single mutations, and bulk operations** by naming the real limit that
  decides it (15 MB, 100 MB, 5 concurrent operations, 24 hours).
- Import a **historical order** with the right date on it, and name the trap that emails the whole
  team once per imported order.
- Write the **cutover sequence** and the **reconciliation report** that proves the migration
  worked — because the deliverable is the proof, not the script.
- Answer *"walk me through a data migration you have run"* for four minutes without hedging.

## Constraints

- **Plain, simple English, short sentences.** Keep every identifier exact (`productSet`,
  `processedAt`, `compareQuantity`) and explain it once in plain words.
- **Nothing from memory.** Every number and every quoted sentence in these lessons comes from
  shopify.dev or help.shopify.com, with the link on the page and the date it was checked.
- **Retrieval over reading.** Mid-lesson recall prompts, an end quiz, and spoken answers — the
  same shape as the sibling sub-courses.
- **Route, do not repeat.** `lessons/0018` already teaches bulk-operation mechanics,
  `lessons/0011` teaches ongoing sync, and `pos-in-store/0006` teaches the project shape of
  leaving a legacy till. This sub-course links to them instead of re-explaining them.

## Out of scope

- **Ongoing two-way sync.** That is `lessons/0011` and the whole `stockinstore-omnichannel/`
  sub-course. A migration is a one-time move with an end date; a sync never ends. Lesson 1 draws
  the line and then stays on the migration side of it.
- **The project-management shape of a cutover programme** (ownership matrix, six phases, parallel
  run). Already covered in `pos-in-store/0006`. This sub-course covers the **records**, not the
  programme — Lesson 8 only adds the parts that are specific to data.
- **Theme and app rebuild work.** A replatform involves both; Lesson 7 names them as
  dependencies and stops there.
- **Any one source platform in depth.** Magento- or WooCommerce-specific export quirks are
  lookup work, not skill. The skill is the shape that is the same every time.

## Facts verified while writing this (2026-08-03)

Checked against shopify.dev and help.shopify.com. Recorded here so no future session re-derives
them from memory.

| Fact | Source |
|---|---|
| Import order is forced: **products → customers → orders**, "so that products and customers can be properly connected to the orders" | help.shopify.com · Migrate to Shopify |
| Customer **passwords cannot be migrated**; current customer accounts are **passwordless** — "They enter their email address and receive a one-time 6-digit verification code. A password isn't required to sign in." | help.shopify.com · Migrate to Shopify; Customer accounts |
| **Historical orders have no CSV import.** Migration apps, the Order API, and the Transaction API are the documented routes | help.shopify.com · Migrate to Shopify |
| `orderCreate` supports backdating: **`processedAt`** — "If you're importing orders from an app or another platform, then you can set processed_at to a date and time in the past to match when the original order was created." | shopify.dev · OrderCreateOrderInput |
| `orderCreate` needs `write_orders`, is **"only accessible to apps authenticated using offline tokens"**, caps at **5 orders per minute on trial or development stores**, and does not support multiple discounts | shopify.dev · orderCreate |
| Importing orders **emails the team**: "any staff member, including the account owner, that is set to receive new order notifications will receive a new order email for each imported order" | help.shopify.com · Migrate to Shopify |
| Product CSV: **15 MB cap**, UTF-8, **Handle** is the match key, blank non-required columns overwrite as blank while omitted columns are left alone, **imports cannot be cancelled once started**, sorting the file in Excel or Numbers can lose the image links, and changing an Option value **deletes variant IDs and creates new ones** | help.shopify.com · Importing products with a CSV file |
| Bulk import: JSONL **cannot exceed 100 MB**, must finish **within 24 hours**, from API version **2026-01** each app may run **five bulk mutations per shop at once**, and the mutation passed in is **limited to one connection field** | shopify.dev · Bulk operation imports |
| `productSet` "performs multiple operations to create or update products in a single request"; the **`identifier`** argument "specifies the identifier that will be used to lookup the resource"; list fields (variants, metafields, collections) **delete entries not included in the input**, other fields are left unchanged when omitted | shopify.dev · productSet |
| **2048 variants** per product by default; **3 options** per product — "products with more than 3 options won't have their options imported" | shopify.dev · productSet; help.shopify.com · Migrate from WooCommerce |
| `metafieldsSet` is an upsert — "Metafield values will be set regardless if they were previously created or not" — capped at **25 metafields per call, 10 MB payload**, with `compareDigest` compare-and-set since **2024-07** | shopify.dev · metafieldsSet |
| `inventorySetQuantities` writes absolute values, `name` accepts **only `available` or `on_hand`**, `reason` is required, `referenceDocumentUri` records "why the inventory change happened", and `compareQuantity` "will only update the quantity if the persisted quantity matches" — a mismatch returns an error | shopify.dev · inventorySetQuantities; InventorySetQuantitiesInput |
| Bulk URL redirects: `urlRedirectImportCreate` takes a **staged CSV upload** and needs `write_online_store_navigation`, then `urlRedirectImportSubmit` runs it | shopify.dev · urlRedirectImportCreate |
| Images can be pulled by URL — `fileCreate`: "Provide a URL and Shopify handles downloading, processing, and storing the file." Images cap at **20 MB / 4472 × 4472 px**; apps may create **1,000 videos per store per week** | shopify.dev · Product media |
| `giftCardCreate` accepts your own code; without one "the system generates a random 16 character alphanumeric code" | shopify.dev · giftCardCreate |
| Reviews do not move — "You can't export or migrate reviews from WooCommerce to Shopify" | help.shopify.com · Migrate from WooCommerce |
| Shopify's own **Store Migration app** is early access, desktop only, sets prices to the product's highest price, and drops options past three | help.shopify.com · Migrate from WooCommerce |

## Layout

Same shape and page template as the sibling sub-courses, with its own `assets/base.css` +
`quiz.js` copied from `pos-in-store/`.

```
shopify-data-migration/
  index.html      the Map — single source of truth
  MISSION.md      this file
  RESOURCES.md    trusted sources + communities
  assets/         base.css + quiz.js
  lessons/  0001 what a data migration actually is
            0002 what moves, what breaks, what never moves
            0003 the matching key & idempotency      ← the core lesson
            0004 three ways to push the data
            0005 the huge catalogue load
            0006 historical orders & money
            0007 Shopify → Shopify replatform
            0008 the cutover & the proof
            0009 the migration interview             ← capstone
  reference/  glossary.html
              what-moves-matrix.html   printable feasibility matrix
              runbook.html             printable cutover runbook
  learning-records/
```

Reading order is L01 → L09 straight through.
