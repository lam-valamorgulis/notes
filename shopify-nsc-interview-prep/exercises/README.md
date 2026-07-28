# Live-coding katas — build the muscle the client will test

Round 1 never asked you to write code. The client round can. This folder is where you
build that muscle. Each kata is a small, real backend task — the kind you will actually
get for a Shopify + Node sync role. Not LeetCode. Real work.

## The rule that makes this work

**Do not read the model answer first.** The whole point is retrieval — struggling to
recall and type it from a blank file is what builds the memory. Reading a finished
solution feels productive but teaches almost nothing.

## The practice protocol (run this for every kata)

1. **Read only the prompt** (the top of the kata file). Cover the model answer.
2. **Set a timer** — 20–25 minutes per kata.
3. **Clarify out loud first.** Even alone, say the questions you would ask the client
   and the assumptions you are making. This is the #1 senior signal (see
   [lesson 26](../lessons/0026-be-the-one-they-pick.html)).
4. **Say your 3-step plan** before you type.
5. **Code from a blank file, narrating.** Talk through every trade-off as if the client
   is watching. Happy path first, then the reliability layer.
6. **Only then** open the model answer and diff. Note what you missed — it is almost
   always a failure mode (retry, dedupe, ordering, timeout).
7. **Repeat the same kata** a day later until it flows without the model answer.

## Do it out loud, on a keyboard

Type it in a real editor or a scratch Node project, not in your head. Say the words you
would say in the room. The client is scoring how you think, and they can only hear that
if you talk.

## The katas

All model answers are **TypeScript** (the JD names it), so practice typing typed
backend code, not just plain JS.

| # | Kata | Format | Skill it builds |
|---|------|--------|-----------------|
| 01 | [Shopify webhook handler](kata-01-webhook-handler.html) | Build from blank | HMAC verify, fast 200, enqueue — the core Shopify ingestion piece |
| 02 | [Debug the double-charge](kata-02-debug-race-condition.html) | Debug &amp; fix | Find and fix a race condition / async bug, explaining out loud |
| 03 | [Idempotent ERP sync worker](kata-03-idempotent-sync-worker.html) | Build from blank | Dedupe + idempotent create-or-update — the other half of Kata 01 |
| 04 | [NestJS orders module](kata-04-nestjs-orders-module.html) | Build from blank | Controller / service / DTO / dependency injection — clean structure |
| 05 | [Retry &amp; dead-letter](kata-05-retry-and-dead-letter.html) | Build from blank | Bounded retry, exponential backoff + jitter, DLQ — the reliability layer |

**Suggested order:** 01 → 03 → 05 follow one job end to end (ingest → write → survive
failure). 02 sharpens debugging. 04 is standalone framework practice. Do 01 and 03 back to
back — together they are the whole sync pipeline the client cares about.

## What "good" looks like when you finish a kata

- You clarified before coding.
- The happy path is correct **and** you named the failure modes.
- You narrated trade-offs — the interviewer never had to ask "what are you thinking?"
- When stuck, you got to a working slow version first, out loud.
- You can say how you would **test** it and what you would **monitor** in production.
