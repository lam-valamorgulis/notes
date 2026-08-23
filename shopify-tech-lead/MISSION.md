# Mission: Shopify domain expert

## Why
Lam builds Shopify integrations, but has never run a live sync end to end. The
goal is to close that gap for real, and to become a **domain expert** in Shopify:
the person who can be handed any Shopify integration job and ship it **alone**.

**The proof is working code, not a conversation.** Decided 2026-08-23. The earlier
version of this Course aimed at "the person in the room who can explain a design
to a client". That goal produced a block in every Lesson called *What you say to a
client/PM*. It is gone. Understanding you cannot build is the failure mode this
Course now exists to prevent.


## Success looks like
- A **Project** that runs: a NestJS + Postgres service syncing a Fake ERP with a
  Plus Dev store. Bulk catalogue load, webhook receiver, inventory flowing back,
  a queue with a dead-letter, and a reconciliation report that catches a fault
  Lam caused on purpose. In a repo with real commits over real months.
- Can answer "who owns this field?" for any field in a Shopify store, and say
  what breaks when the answer is "both".
- Can look at a live Shopify store and read its integration: which app wrote which
  field, where the tags came from, whether inventory is written by the store or by
  an app.
- Can **explain any core Shopify idea to a beginner, out loud, without jargon.**
  That is the test, not recognising the term. Every Lesson has a *Say it out loud*
  block for exactly this, and its model answer is hidden so you have to try first.
- Can **finish the Build it task in every Lesson** against the Dev store. Each one
  ends in a proof — something to look at that says it worked.
- Can give a client a **range** instead of a number, say "I don't know yet"
  without losing the room, and disagree with a PM in English under pressure.
- Can size a large catalogue load and say honestly whether it is a 30-day job or a
  300-day job, and why the published limits do not settle it.

## Constraints
- 10–15 hours a week. No deadline.
- English is a second language. The conversation lessons are drilled out loud, as
  fixed sentences, not read.
- Strong already: Shopify themes and Liquid, JavaScript, React, front end. Do not
  re-teach these — extend them.
- Node event loop is already mastered. It links out to
  `../nodejs-mastery-in-1-year/`, it is not re-taught here.
- The Client store is **read-only**. All building happens on a Dev store, against
  a synthetic catalogue. See
  [ADR 0001](docs/adr/0001-synthetic-catalogue-from-shape-samples.md).

## Out of scope
- LeetCode and algorithm puzzles.
- Liquid syntax from zero. Only what is new (Horizon, theme blocks) or easy to get
  wrong.
- Node fundamentals from zero.
- Deep NestJS or Postgres beyond what the Project needs.
- Any named company as a study subject. Patterns survive; companies do not.
- Interview prep as the *purpose*. Interviews are one Chapter in Track 3, not the
  reason the Course exists.
