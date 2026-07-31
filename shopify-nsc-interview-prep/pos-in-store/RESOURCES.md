# Resources — POS & In-Store on Shopify

Trusted sources for this sub-course. Every factual claim in a lesson should trace to
something here. Verified dates matter: Shopify's platform surface changes, so a fact
checked a year ago is not a fact.

## Primary — Shopify official

| Source | Why it is trusted | What it settles | Verified |
|---|---|---|---|
| [shopify.dev · Build POS apps](https://shopify.dev/docs/apps/build/pos) | Platform owner | What a POS app can do across the purchase lifecycle: custom discounts and loyalty, low-inventory alerts, real-time availability across stores, ship-from-store suggestions, custom payment flows, receipts, gift cards, analytics. Extensions render as native components on iOS and Android. | 2026-07-31 |
| [shopify.dev · POS UI Extensions](https://shopify.dev/docs/api/pos-ui-extensions) | Platform owner | The stack (TSX/JSX, Preact, TOML config, `remote-dom`) and the target names: `pos.home.tile.render`, `pos.home.modal.render`, `pos.product-details.block.render`, `pos.cart.line-item-details.action.render`. Three target *kinds*: tile, action, block. | 2026-07-31 |
| [shopify.dev · Liquid `order` object](https://shopify.dev/docs/api/liquid/objects/order) | Platform owner | **The bridge.** `order.attributes` = "the attributes on the order… Attributes are collected with the cart." This is what proves a cart attribute survives checkout. | 2026-07-31 |
| [shopify.dev · Liquid `cart` object](https://shopify.dev/docs/api/liquid/objects/cart) | Platform owner | `cart.attributes` = "additional attributes entered by the customer with the cart." Also documents the `__` prefix for **private** attributes that do not affect page rendering and improve caching. | 2026-07-31 |
| [shopify.dev · Cart AJAX API](https://shopify.dev/docs/api/ajax/reference/cart) | Platform owner | `POST /cart/update.js` takes `attributes` as key-value pairs. **Open question:** the docs do not state whether this merges with or replaces existing attributes. Test before relying on it. | 2026-07-31 |
| [shopify.dev · Inventory management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps) | Platform owner | **The eight inventory states**, quoted in Lesson 3: `available` ("the inventory that a merchant can sell"), `committed`, `reserved`, `damaged`, `safety_stock` ("set aside to help guard against overselling"), `quality_control`, `on_hand` (physical total), `incoming` (the only state not physically present). Plus the three mutations: `inventoryAdjustQuantities` (delta), `inventorySetQuantities` (absolute, `on_hand`/`available` only), `inventoryMoveQuantities` (between states). | 2026-07-31 |
| [shopify.dev · Location object](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location) | Platform owner | A Location is "a physical place where merchants manage and fulfill inventory". Fields used in Lesson 3: `fulfillsOnlineOrders`, `localPickupSettingsV2`, `isActive`, `inventoryLevels`, `hasUnfulfilledOrders`, `activatable`. | 2026-07-31 |
| [shopify.dev · DeliveryMethodType](https://shopify.dev/docs/api/admin-graphql/latest/enums/DeliveryMethodType) | Platform owner | All six values with quotes: `RETAIL` ("in-store sale, no delivery needed" — **how a POS sale looks**), `PICK_UP`, `SHIPPING`, `LOCAL`, `PICKUP_POINT`, `NONE`. | 2026-07-31 |
| [shopify.dev · POS UI Extensions APIs](https://shopify.dev/docs/api/pos-ui-extensions/apis) | Platform owner | Three API families. **Contextual:** Cart, Cart Line Item, Customer, Draft Order, Order, Product. **Platform:** Connectivity, Device, Navigation, PinPad, Print, Scanner, Storage. **Standard:** Action, Locale, Product Search, Session, Toast. Cart API writes ("add, remove, and modify cart items, apply discounts"); Cart Line Item API is read-only. | 2026-07-31 |
| [help.shopify.com · POS Lite vs POS Pro](https://help.shopify.com/en/manual/sell-in-person/getting-started/pos-subscription-overview) | Platform owner | The tier split used in Lesson 4. **Pro-only:** "Pickup in store", "Local delivery fulfillment", "Retail staff permissions and management", "Exchanges", "Receiving stock transfers", "Daily sales reports", plus ship-to-home and save/retrieve cart. **In Lite:** multi-location inventory, cash tracking, refunds, smart grid, staff PINs. Pro is priced **per location** — check [POS pricing](https://www.shopify.com/pos/pricing) rather than quoting a figure. | 2026-07-31 |

## Primary — the code itself

Read directly, not summarised. These are the real integrations this sub-course teaches from.


## Vendor documentation

| Source | What it is good for | Caution |
|---|---|---|
| [Retail Express](https://www.retailexpress.com.au/) | AU retail POS + inventory platform. Vocabulary: **outlet** = shop. | Marketing pages, not API docs. Treat capability claims as sales copy. |
| [stockinstore](https://www.stockinstore.com/) | AU omnichannel SaaS: Find in Store, Store Locator, Click & Collect, Ship from Store. | Same caution. The sibling sub-course already covers this domain in depth. |

## Sibling material in this workspace

| Where | Why go there instead |
|---|---|
| [`../stockinstore-omnichannel/`](../stockinstore-omnichannel/index.html) | The omnichannel **domain** — inventory sync, availability, allocation. This sub-course deliberately does not repeat it. |
| [`../lessons/0023-checkout-extensibility.html`](../lessons/0023-checkout-extensibility.html) | Extension targets, tiles/actions/blocks. Same shape as POS UI Extensions. |
| [`../lessons/0018-shopify-bulk-operations.html`](../lessons/0018-shopify-bulk-operations.html) | Moving catalogue and inventory data at volume — relevant to a POS migration's cutover. |

## Communities — where wisdom comes from

Knowledge and skills come from the sources above. Judgement comes from people who have
actually cut a retailer over from one till to another.

| Community | Why it is worth the time |
|---|---|
| [Shopify Community — Retail & POS board](https://community.shopify.com/) | Merchants and partners describing real POS rollouts and what broke. Search before posting. |
| [r/shopify](https://www.reddit.com/r/shopify/) and [r/ShopifyAppDev](https://www.reddit.com/r/ShopifyAppDev/) | Candid accounts of migrations, including the failures that never appear in a case study. |
| [Shopify Partners Slack / Discord communities](https://www.shopify.com/partners) | Where agency engineers compare notes on vendor integrations. Closest thing to asking a peer. |

**A good question to take to a community:** *"For Click & Collect on Shopify, when did you
choose cart attributes over a proper app with webhooks — and did you regret it?"* That is a
judgement question. No documentation answers it.

## Gaps — what is not yet sourced

Honest list of what is still unresolved. Three of the original four gaps were closed on
2026-07-31 and their sources are in the table above.

**Closed:**

- ~~Multi-location inventory mechanics~~ — sourced. Eight states + three mutations, now Lesson 3.
- ~~POS Pro vs POS Lite~~ — sourced from the help centre subscription overview, now Lesson 4.
  Note the POS UI Extensions docs do *not* mention the tiers; that was the wrong place to look.
- ~~Identifying an in-store sale~~ — sourced. `DeliveryMethodType.RETAIL`, now Lesson 4.

**Still open:**

- **Merge vs replace** for `POST /cart/update.js` `attributes` — genuinely undocumented. Needs a
  dev-store test. Lesson 2 states this honestly rather than guessing, and that is the right
  answer in an interview too.
- **Reserving stock before checkout completes** — a pickup order moves units to `committed`
  once placed (consistent with the sibling sub-course's `PICK_UP` work), but whether stock can
  be *held* at a location before checkout finishes is unverified. Matters for any "reserve for
  30 minutes" requirement.
- **The current POS Pro price per location** — deliberately not recorded here. Prices change;
  read the pricing page at the time of the conversation.
- **A first-hand cutover account.** Lesson 6 is built from a written statement of work, not from
  someone who has lived through a POS migration. That is a wisdom gap, not a knowledge gap, and
  the community links above are the way to close it.
