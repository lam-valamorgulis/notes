# Idea to Production — Resources

Every claim in a Lesson traces back to something on this page. If a fact has no
source here, the Lesson marks it as a bare fact, or says plainly that the step is
ours and not the source's.

Last checked: **2026-08-29**. Every URL below was fetched or searched on that
date. Two were corrected during the check:

- `martinfowler.com/articles/practicalTestPyramid.html` returns **404**. The live
  URL is `practical-test-pyramid.html`, with hyphens.
- Secondary blogs say a Google design doc is "3 to 20 pages". The primary source
  says **1–3 pages** for a small change and **10–20** for a large one. Use the
  primary.

---

## Knowledge

### Stage 1 — Decide

- [Article: "Design Docs at Google" — Malte Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/)
  The best single page on what goes in a design doc: context and scope, goals and
  **non-goals**, the actual design, alternatives considered, cross-cutting
  concerns. Also says when *not* to write one.
  **Use for:** the design doc template, and the argument for non-goals.
- [Book chapter: _Software Engineering at Google_, ch. 10 — Documentation](https://abseil.io/resources/swe-book/html/ch10.html)
  Free online. Treats documentation as code: reviewed, owned, versioned.
  **Use for:** why a doc rots, and how to stop it.
- [Article: "Start with a Walking Skeleton" — Matt Blodgett](https://www.mattblodgett.com/2020/09/start-with-walking-skeleton.html)
  Clear retelling of Alistair Cockburn's term: the thinnest slice of real
  function that you can build, deploy and test end to end, automatically.
  **Use for:** the definition, and why slice zero is deploy, not login.
- [Exercise: Elephant Carpaccio — Alistair Cockburn / Henrik Kniberg](https://docs.google.com/document/d/1TCuuu-8Mm14oxsOnlk8DqfZAA1cvtYu9WGv67Yj_sSk/preview)
  A workshop where teams learn to find 15–20 slices where they first saw 3.
  **Use for:** the slicing drill in Lesson 0002. Practise, not theory.

### Stage 2 — Shape

- [Book: _Designing Data-Intensive Applications_ — Martin Kleppmann](https://dataintensive.net/)
  The reference for data models, storage, and what "consistent" actually means.
  Dense. **Use for:** the data-model Lesson, and every "will this scale" question.
  Do not read cover to cover; read chapters 2 and 3 first.
- [Article: "Versioning Best Practices in REST API Design" — Speakeasy](https://www.speakeasy.com/api-design/versioning/)
  A precise definition of a breaking change: a client that conformed before can
  now fail, without the client changing. Lists what is additive and what is not.
  **Use for:** the breaking-change rules table. A vendor blog, so use it for the
  rules, not for the tool recommendation.
- [Book chapter: _Automating API Delivery_, ch. 4 — Breaking change checks](https://www.oreilly.com/library/view/automating-api-delivery/9781633438781/OEBPS/Text/chapter-4.html)
  How to make CI fail when a supposedly additive release removes a field.
  **Use for:** turning the rules above into a pipeline stage. Paywalled.
- [Spec: The Twelve-Factor App](https://12factor.net/)
  Now open source and being revised. Factors III (config), X (dev/prod parity)
  and XI (logs as event streams) carry most of the weight for a small product.
  **Use for:** config, environments, and why the same build ships everywhere.
- [Essay: "Choose Boring Technology" — Dan McKinley](https://mcfunley.com/choose-boring-technology)
  You get about three "innovation tokens". Spend them where they win.
  **Use for:** the stack choice, once, in week 5. Also cited by
  [founding-engineer Lesson 0007](../founding-engineer/lessons/0007-boring-stack-innovation-tokens.html)
  — read that one instead of repeating it here.

### Stage 3 — Deliver

- [Guide: "Trunk-based development" — DORA](https://dora.dev/capabilities/trunk-based-development/)
  The research behind the practice. Its exact numbers: **three or fewer active
  branches**, **merge to trunk at least once a day**, branches lasting hours not
  days. Based on DORA data from 2016 and 2017.
  **Use for:** the branching Lesson. Quote the numbers, and quote the year.
- [Site: trunkbaseddevelopment.com — Paul Hammant](https://trunkbaseddevelopment.com/)
  The full pattern, including the honest note that very small teams may commit
  straight to trunk. **Use for:** what a one-person version looks like.
- [Article: "The Practical Test Pyramid" — Ham Vocke, 2018](https://martinfowler.com/articles/practical-test-pyramid.html)
  Long, worked, with code. The pyramid plus the warning that the layer names
  mean different things to different people.
  **Use for:** the test strategy Lesson. The 2012 short version is
  [Fowler's bliki: Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html).
- [Article: "Deployment Pipeline" — Martin Fowler](https://www.martinfowler.com/bliki/DeploymentPipeline.html)
  Stages of increasing confidence at increasing cost. The idea the whole of CI/CD
  hangs on. **Use for:** designing Speck's pipeline stages and their order.
- [Article: "Feature Toggles (aka Feature Flags)" — Pete Hodgson](https://martinfowler.com/articles/feature-toggles.html)
  The four kinds — release, experiment, ops, permission — and why mixing them up
  causes the mess. **Use for:** separating deploy from release, and for knowing
  which flags must be deleted.
- [Paper: "Expand and Contract" — Tim Wellhausen](https://www.tim-wellhausen.de/papers/ExpandAndContract/ExpandAndContract.html)
  The three-phase schema change, written as a pattern. Also called **parallel
  change**. Its key property: every step can be rolled back on its own.
  **Use for:** the zero-downtime migration Lesson.
- [Guide: "Using the Four Keys to measure your DevOps performance" — Google Cloud](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)
  Deployment frequency, change lead time, change failure rate, recovery time.
  **Use for:** the scoreboard. Note the 2025 DORA report replaced the
  Elite/High/Medium/Low bands with seven team profiles, so do not quote the old
  bands as current.

### Stage 4 — Operate

- [Book chapter: _Site Reliability Engineering_, ch. 6 — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
  Free. The four golden signals: latency, traffic, errors, saturation. Also the
  rule that every page should need a human to think.
  **Use for:** the observability Lesson, and for what deserves an alert.
- [Book chapter: _The SRE Workbook_ — Postmortem Culture](https://sre.google/workbook/postmortem-culture/)
  Free. Blameless means assuming everyone acted on the best information they had.
  **Use for:** the postmortem template and the tone rules.
- [Guide: Google Incident Management Guide (PDF)](https://sre.google/static/pdf/IncidentManagementGuide.pdf)
  Roles, escalation, and how to run the first ten minutes.
  **Use for:** the one-person version of an incident process.
- [Standard: OWASP Top 10:2025](https://owasp.org/Top10/2025/)
  Current as of this check. **A01 Broken Access Control** is still number one.
  New in 2025: **A03 Software Supply Chain Failures** and **A10 Mishandling of
  Exceptional Conditions**. SSRF was folded into A01.
  **Use for:** the security baseline. Always cite the 2025 list, not 2021.
- [Standard: OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
  The checklist version, at three levels. Level 1 is the right target for Speck.
  **Use for:** turning "be secure" into items you can tick.

### Cross-cutting

- [Book: _Accelerate_ — Forsgren, Humble, Kim](https://itrevolution.com/product/accelerate/)
  The research that produced the four key metrics. **Use for:** the argument that
  speed and stability rise together, rather than trading off.
- [Book: _Continuous Delivery_ — Humble & Farley](https://continuousdelivery.com/)
  The original long-form source for the deployment pipeline.
  **Use for:** depth, once the pipeline Lesson has landed.

---

## Wisdom (Communities)

The user has not opted out of communities. None joined yet — pick one in Stage 3,
when there is something real to show.

- [r/ExperiencedDevs](https://www.reddit.com/r/ExperiencedDevs/)
  Moderated hard against beginner questions and career-bait. Good for "is this
  design mad?" **Use for:** a sanity check on the Speck design doc.
- [r/devops](https://www.reddit.com/r/devops/)
  **Use for:** pipeline and alerting questions. Ignore the tool-war threads.
- [Rands Leadership Slack](https://randsinrepose.com/welcome-to-rands-leadership-slack/)
  Large, well moderated, has active `#sre` and `#engineering-practices` channels.
  **Use for:** asking a real practitioner what pages them at night.
- [Hacker News](https://news.ycombinator.com/)
  **Use for:** the comment threads under the sources above, not the articles.
  The Design Docs at Google [thread](https://news.ycombinator.com/item?id=23915521)
  is a good example: practitioners disagreeing usefully.

---

## Gaps

Named honestly, because these drive the next search.

- **No strong source for solo on-call.** Every SRE source assumes 6–8 people in
  the rotation. The one-person version in Stage 4 will be **ours**, derived from
  the SRE principles, and the Lesson must say so out loud.
- **No good primary source for "how much testing is enough when alone."** The
  test pyramid gives a shape, not an amount. Expect to state a rule of our own.
- **The 2025 DORA report itself is not yet read.** Only secondary summaries have
  been checked. Read the primary before quoting any 2025 number beyond the four
  metric names.
- **Data modelling has no short source.** Kleppmann is a book, not an article.
  Look for a good 20-minute read before the Stage 2 Lesson is written.
