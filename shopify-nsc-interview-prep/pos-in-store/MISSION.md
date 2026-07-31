# Mission — POS & In-Store on Shopify

## Why this sub-course exists

The main course prepares for a Senior Backend (Shopify + Node) interview. One topic in it
has a real gap: **selling in a physical shop**.

The gap is specific. Day-to-day work happens inside Shopify themes that *are* integrated
with third-party point-of-sale and omnichannel systems. So the words are familiar — Click &
Collect, outlets, store locator, stock lookup. But the integration layer itself was written
by other people. That means the knowledge is second-hand, and second-hand knowledge falls
apart under a follow-up question.

This sub-course replaces the second-hand version with mechanism that can be pointed at.

## What "done" looks like

Able to answer, out loud and without notes:

1. **"How would you show in-store stock on a Shopify product page?"** — name the three
   patterns (vendor drop-in, theme-woven widget, native Shopify POS) and say what each one
   costs.
2. **"A shopper picks a pickup store in a third-party widget. How does fulfilment see it?"**
   — the cart-attribute bridge, end to end, including why it survives checkout.
3. **"Review this integration code."** — spot silent failure, stale identifiers,
   cookie-dependent state, and missed platform features, unprompted.
4. **"How would you migrate a shop off a legacy till onto Shopify POS?"** — data ownership
   first, then inventory model, then parallel run, then cutover timing.
5. **"Have you built a Shopify POS app?"** — answer honestly, in one sentence, without
   losing credibility.

## The honesty constraint

This one is a hard rule, not a preference.

**Do not claim the POS integration work as authored.** The third-party POS and omnichannel
integrations in these themes were built by others — this was confirmed while auditing the
repos for CV evidence, and the CV notes record it explicitly. No repo on this machine
contains a Shopify app or a POS UI Extension either: there is no `shopify.app.toml`
anywhere, so Pattern C is learned knowledge, not shipped experience.

The safe framing, which costs nothing:

> "I've maintained storefronts integrated with third-party POS systems, so I know that
> integration layer well. I haven't shipped a POS UI Extension myself."

Every lesson must respect this. Where a lesson quotes real code, it is code that was read
and maintained — never code that was authored.

## Grounding rules for lessons

- **Verify Shopify platform claims against shopify.dev** before stating them. Where the
  docs do not answer a question, say so in the lesson rather than guessing. One example is
  already flagged: the Cart AJAX docs do not state whether `attributes` merges or replaces.
- **Grep before describing.** A snippet that exists is not an integration. Lesson 2 was
  rewritten around this after finding a complete-looking vendor integration that nothing
  ever renders.
- **Prefer real code over invented examples.** The failure modes that teach best are the
  ones actually shipped.

## Publishing note

This course is published publicly. Client names are wrapped in
`` markers so the deploy script strips them.
Vendor product names (Retail Express, stockinstore) stay, matching the earlier decision for
the sibling sub-course. **No credentials or API keys ever go in a lesson** — one integration
read for this course had a hard-coded Google Maps key in theme source, and it is
deliberately not reproduced here.
