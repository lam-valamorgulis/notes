# Shopify Theme Architecture — Sub-Course

The main course looks at Shopify **from the server**: apps, webhooks, ERP sync. This sub-folder
turns around and looks at the **storefront** — the theme itself — in the same style as the main
course.

Four lessons, in order:

1. **Dawn** — the Online Store 2.0 baseline that almost every live theme still follows.
2. **Horizon** — the newer theme-block architecture, and exactly what it changed.
3. **The Cart AJAX API** — where both themes make the same request and apply the answer in two
   different ways.
4. **Discounts** — the surface where the theme's authority ends: it can submit a code, but only
   Shopify decides what it is worth.

## The angle

Every page is framed as: **"Shopify's servers render the HTML, so what is left for you to
design?"** The answer is two things — **composition** (which reusable units exist, and who is
allowed to rearrange them) and **repainting** (how the page updates after the shopper acts).
Those two ideas run through all three lessons.

## Why this exists

The main course puts theme and Liquid work out of scope, because it is already a strength. This
sub-course does not re-teach Liquid syntax. It covers the parts that **changed recently or are
easy to get wrong**:

- Horizon and theme blocks are new (announced May 2025). Not knowing them dates you.
- The Cart AJAX API has traps that separate people who have shipped a cart from people who have
  read about one — `update.js` does not check stock, and `line` positions move under you.
- Bundled section rendering is the single most useful thing to know about updating a theme page,
  and it is easy to use wrong.
- Discounts look simple and are not. An invalid code returns a normal `200`, several Liquid price
  properties are deprecated in a way that hides modern discounts, and Dawn ships no discount
  input at all — so "add a discount box" is always custom work.

## Start here

1. **[index.html](index.html)** — the Map for this sub-course (single source of truth).
2. **[lessons/0001-dawn-theme-architecture.html](lessons/0001-dawn-theme-architecture.html)** — read this first; it sets the vocabulary.

## Folder map

| Folder | What's in it |
|--------|--------------|
| `index.html` | The Map — connects every page as one story. |
| `lessons/` | The three deep lessons. |
| `assets/` | Shared styles + quiz engine (copied so this folder is self-contained). |

## Build plan

**Lessons**

1. Dawn theme architecture (Online Store 2.0) ✅
2. Horizon & theme blocks ✅
3. The Cart AJAX API ✅
4. Discounts on the storefront ✅

**Status: the four planned lessons are built.** Each one carries a "verified" line recording
which claims were checked against `shopify.dev` and which were read from real theme source.

### Possible next lessons (not built)

If this sub-course grows, the obvious gaps are:

- Theme app extensions and app blocks (how an app injects UI into a theme).
- Performance: Core Web Vitals in a Liquid theme, image sizing, and the cost of many CSS files.
- Metaobjects and dynamic sources in the theme editor.
- A live-coding kata: build a cart drawer from a blank file.

## Facts and versions

Technical claims were verified on **2026-07-29**. Two kinds of source were used, and each lesson
says which is which at the bottom of the page:

- **`shopify.dev` / `help.shopify.com`** for the documented contract — folder rules, block
  limits, endpoint parameters. These are stable.
- **Real theme source** for the implementation detail — a local copy of **Dawn 15.3.0** and the
  public `Shopify/horizon` repository. File counts here drift between theme releases. The
  architecture does not.

Where a claim is **not** backed by the documented contract, the lesson says so on the page. Two
points are flagged this way:

- **Lesson 3** — sending cart writes one at a time. This follows from how the cart works, but
  Shopify does not publish an explicit concurrency warning.
- **Lesson 4** — the `discount_codes` array (each entry having `code` and `applicable`) on the
  cart response. It is **not** in the Cart AJAX API reference, which only says the response is
  "the JSON of the cart". Horizon depends on it in production and types it in its own source, so
  the lesson teaches it as real but unspecified, and says to code defensively in case it is
  missing.

## How we work

Say **"next"** to build the next lesson, **"go deeper on X"** for more detail on any topic, or
**"mock me on themes"** for a storefront-focused drill.

**Keeping the Map current:** whenever a page is added, `index.html` is updated in the same
session — the new file joins the right chapter with a one-line description, and no link is ever
left broken. Keeping the Map in sync is part of "done."
