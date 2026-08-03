# Shopify Data Migration — Resources

Every source here was opened and read on **2026-08-03**. Numbers in Shopify docs drift; if a fact
is load-bearing in an interview, re-open the link before you quote it.

## Knowledge — the primary sources

- [help.shopify.com · Migrate to Shopify](https://help.shopify.com/en/manual/migrating-to-shopify)
  The single most useful page in this sub-course. Gives the forced import order (products →
  customers → orders), the list of what can move, and the two caveats nobody expects: customer
  passwords cannot move, and importing orders emails the team once per order.
  **Use for:** the shape of any migration, and the "what moves" matrix in Lesson 2.

- [help.shopify.com · Importing products with a CSV file](https://help.shopify.com/en/manual/products/import-export/import-products)
  The rules of the CSV route: 15 MB cap, UTF-8, Handle as the match key, and the three traps
  (imports cannot be cancelled, spreadsheet sorting can lose image links, changing an Option
  value creates new variant IDs).
  **Use for:** Lesson 4 whenever someone says "just use a CSV."

- [help.shopify.com · Using CSV files to import and export products](https://help.shopify.com/en/manual/products/import-export/using-csv)
  The column-by-column reference for the product CSV.
  **Use for:** field mapping work, not for concepts.

- [shopify.dev · Bulk operation imports](https://shopify.dev/docs/api/usage/bulk-operations/imports)
  The five steps of `bulkOperationRunMutation`, plus the limits that decide your batch size:
  100 MB JSONL, 24-hour completion, five concurrent bulk mutations per shop per app from API
  version 2026-01, and one connection field per mutation.
  **Use for:** Lessons 4 and 5. Pair it with main-course `lessons/0018`.

- [shopify.dev · productSet](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet)
  The upsert mutation, and the `identifier` argument that makes a migration re-runnable. Read the
  list-field warning carefully: variants, metafields and collections not in your input are
  **deleted**.
  **Use for:** Lesson 3, the core lesson.

- [shopify.dev · orderCreate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCreate) and
  [OrderCreateOrderInput](https://shopify.dev/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput)
  The only documented API route for historical orders. The input object is where `processedAt`
  lives, with an explicit sentence about backdating imported orders.
  **Use for:** Lesson 6.

- [shopify.dev · Import B2B orders](https://shopify.dev/docs/apps/build/b2b/import-orders)
  A worked example of `orderCreate` used as an import tool, and a reminder that dependencies
  (companies, locations, contacts, products) must exist first.
  **Use for:** Lesson 6, and as proof that "import via orderCreate" is the intended pattern.

- [shopify.dev · metafieldsSet](https://shopify.dev/docs/api/admin-graphql/latest/mutations/metafieldsSet)
  The upsert for metafields — 25 per call, 10 MB, and `compareDigest` for safe concurrent writes.
  **Use for:** Lesson 3, where a metafield holds the legacy ID.

- [shopify.dev · inventorySetQuantities](https://shopify.dev/docs/api/admin-graphql/latest/mutations/inventorySetQuantities)
  Absolute inventory writes, `available` or `on_hand` only, a required `reason`, and
  `compareQuantity` for compare-and-set.
  **Use for:** Lesson 8, where inventory is written last.

- [shopify.dev · urlRedirectImportCreate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/urlRedirectImportCreate)
  Bulk redirects from a staged CSV, then `urlRedirectImportSubmit`.
  **Use for:** Lesson 8. This is the step that protects the client's search traffic.

- [shopify.dev · Product media](https://shopify.dev/docs/apps/build/online-store/product-media)
  `fileCreate` pulls an image from a URL — "Provide a URL and Shopify handles downloading,
  processing, and storing the file" — versus `stagedUploadsCreate` for large or private files.
  Image cap: 20 MB and 4472 × 4472 px.
  **Use for:** Lesson 5, where images are usually the slowest part of the job.

- [shopify.dev · giftCardCreate](https://shopify.dev/docs/api/admin-graphql/latest/mutations/giftCardCreate)
  You may supply the existing code, which is the only way outstanding gift cards keep working
  after a move.
  **Use for:** Lesson 6.

- [help.shopify.com · Customer accounts](https://help.shopify.com/en/manual/customers/customer-accounts)
  Passwordless sign-in with a one-time 6-digit code. This is why "passwords cannot be migrated"
  is a smaller problem in 2026 than it used to be — and knowing that is a good interview moment.
  **Use for:** Lesson 2.

- [help.shopify.com · Migrate from WooCommerce](https://help.shopify.com/en/manual/migrating-to-shopify/migrating-from-woocommerce)
  The best of the per-platform guides. Concrete phase order, the 3-option cap restated, weight
  unit conversion, redirects before the domain switch, and the named third-party tools.
  **Use for:** a worked example when a lesson needs one. The other platform guides
  (Magento, Lightspeed, Square, Etsy, Wix, Amazon, Clover, eBay) follow the same shape.

## Wisdom — communities

- [Shopify Community · Technical Q&A](https://community.shopify.com/)
  Shopify's own forum. Migration threads are common and app vendors answer in them.
  **Use for:** "has anyone moved X to Shopify" questions, and sanity-checking a plan before
  committing to it.
- [r/shopify](https://www.reddit.com/r/shopify/) and [r/ShopifyDev](https://www.reddit.com/r/ShopifyDev/)
  Merchants and developers respectively. r/ShopifyDev is the higher-signal one for API work.
  **Use for:** what actually went wrong on other people's cutovers — the failure stories that
  never reach the docs.
- [Shopify Partners Slack / Partner community](https://www.shopify.com/partners)
  Where agency people compare migration tooling.
  **Use for:** tool selection, and pricing a migration.

## Gaps — deliberately not resolved

- **No official page ranks the migration tools.** Shopify's own guides name Matrixify,
  LitExtension and Ablestar without comparing them. Treat any ranking you read as an opinion,
  including a vendor's own.
- **No documented maximum for the `quantities` array** on `inventorySetQuantities`. The doc pages
  read on 2026-08-03 do not state one. An earlier course note claimed 50,000 — that number is
  **not** repeated in these lessons because it could not be confirmed. Batch conservatively and
  measure.
- **No official guidance on reconciliation.** Shopify documents how to write data in and says
  nothing about how to prove it landed. The reconciliation report in Lesson 8 is engineering
  practice, not a documented Shopify process, and is labelled as such on the page.
- **Store-to-store (Shopify → Shopify) has no dedicated official guide.** Lesson 7 is assembled
  from the export/import pages plus what is structurally true of the API, and it flags which
  claims are inference rather than documentation.
