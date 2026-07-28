# NSC Senior Backend (Shopify) — Interview Prep Resources

Verified against shopify.dev on 2026-07-09 (Shopify API version 2026-07). Prefer these over memory.

## Knowledge — Shopify (backend view)

- [Shopify GraphQL Admin API reference](https://shopify.dev/docs/api/admin-graphql)
  The primary Admin API. Use for: what you can read/write server-side, query cost / rate limits, bulk operations. **REST Admin API is now legacy — lead with GraphQL.**
- [Authentication & authorization for apps](https://shopify.dev/docs/apps/build/authentication-authorization)
  Session tokens + token exchange (managed install) is the current recommended flow. Use for: "how does a Shopify app log in / get an access token?"
- [Webhooks (build apps)](https://shopify.dev/docs/apps/build/webhooks)
  Subscribe, verify HMAC, retries, ordering, reliability. Use for: event-driven Shopify questions, idempotency.
- [Storefront API](https://shopify.dev/docs/api/storefront)
  Customer-facing GraphQL API for headless/custom storefronts and carts. Use for: Admin vs Storefront API contrast.
- [API rate limits overview](https://shopify.dev/docs/api/usage/rate-limits)
  REST bucket vs GraphQL calculated query cost. Use for: the rate-limit deep-dive answer.
- [Shopify app architecture / Shopify CLI](https://shopify.dev/docs/apps/build)
  How real apps are structured and scaffolded. Use for: "how would you build a Shopify app?"

## Knowledge — Backend engineering

- [NestJS official docs](https://docs.nestjs.com/)
  Modules, providers, dependency injection, guards, pipes, interceptors. Use for: the NestJS architecture answer.
- [Node.js — the event loop, timers & process.nextTick](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
  The single-threaded async model. Use for: "explain how Node handles concurrency."
- [The Twelve-Factor App](https://12factor.net/)
  Config, backing services, disposability, logs. Use for: sounding senior on service design & DevOps.
- [System Design Primer (donnemartin, GitHub)](https://github.com/donnemartin/system-design-primer)
  Caching, queues, load balancing, consistency, back-of-envelope. Use for: the system-design round.
- [AWS — Message queues & event-driven (SQS / SNS / EventBridge)](https://aws.amazon.com/message-queue/)
  Managed queue concepts. Use for: Kafka vs RabbitMQ vs SQS breadth question.

## Wisdom — Communities (test answers with real practitioners)

- [Shopify Community — App / API dev forums](https://community.shopify.com/c/shopify-developers/ct-p/appdev)
  Real integration problems + Shopify staff replies. Use for: sanity-checking your mental model before the interview.
- [Shopify Devs Discord](https://discord.gg/shopifydevs)
  Fast, high-signal Q&A from app builders. Use for: quick "is this how token exchange really works?" checks.
- [r/node](https://www.reddit.com/r/node/)
  Node/NestJS practice and architecture debates. Use for: backend framing.

## Gaps
- No single trusted source ties **Shopify ↔ ERP/CRM sync at scale** together — this is assembled from webhooks + queues + idempotency docs. The system-design lesson fills this gap.
- Behavioral / senior-narrative prep is coached in-lesson, not from an external source.
