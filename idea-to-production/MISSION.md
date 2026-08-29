# Mission: Idea to Production — the build half

## Why

This course covers one job. Someone has decided what to build. Now put it in
front of real users, and keep it working.

That gap is where most side projects die. The code gets written. The thing never
becomes a product that strangers can use on a Tuesday at 3am.

This course is the **build half** of the work. The other half — finding a real
problem, cutting it to an MVP, first users, first price — is already taught in
[../founding-engineer/index.html](../founding-engineer/index.html). The two do
not repeat each other. That course decides *what* and *whether*. This one does
*how*, and *is it still up*.


## Success looks like

- Can write a design doc for a real feature in one sitting, and it names at
  least one option that was rejected, with the reason.
- Can take a feature and cut it into thin end-to-end slices, and ship slice one
  to production before slice two is designed.
- Can look at a database schema and say which change will be cheap in a year and
  which will be a six-week migration.
- Has a pipeline where a commit reaches production with no human touching a
  server, and has rolled a release back on purpose at least once.
- Can add a field to a live table with users on it, and not take the site down.
- Can answer "is it healthy?" with a number, not a feeling.
- Can break the thing on purpose, get paged, fix it, and write the postmortem
  without blaming a person.
- Can read someone else's production system and say what will page them at 3am.

## Domain expert goal

> "Hand me a decided idea. I will put it in production, alone, with tests, a
> pipeline, alarms and a rollback — and I can say why each decision was right
> and what it gave up."

The standard for expert stays the five abilities:

- Explain it from first principles, with no jargon and no notes
- Predict how it behaves in a case never seen before
- Say why it was built this way, and what that choice gives up
- Debug a problem in it that has no ready answer online
- Judge someone else's work in it, and say what is wrong and why

## The running product: Speck

Every Lesson builds one thing. **Speck** is a hosted feedback widget. A site
owner pastes one `<script>` tag. Visitors leave a short note. The owner reads
the notes in a dashboard.

Speck is small enough to build alone, and it carries almost every production
problem worth learning:

| Speck has | So the course must teach |
|---|---|
| A public write endpoint anyone can call | Rate limits, abuse, CORS, input validation |
| Many site owners in one database | Access control — OWASP's number one risk |
| A `<script>` tag on other people's sites | A public contract you can never break |
| A daily digest email | Background jobs, retries, doing a thing exactly once |
| Growth from 10 rows to 10 million | Schema change with users on the table |
| A dashboard behind a login | Sessions, secrets, config per environment |

Speck is invented. No company is the study subject, because patterns survive and
companies do not.

## The shape of the course

Four **Stages**, in the real order of the work. Twelve core Lessons, one per two
weeks. **24 weeks, about six months.**

A Stage is not a calendar block. It is a question, and it ends with a **gate** —
one sentence that must be true before the next Stage starts.

| Stage | Weeks | The question it answers | The gate |
|---|---|---|---|
| 1 — Decide | 1–4 | Do we agree what we are building, and in what order? | A design doc exists, someone else read it, and it names a rejected option |
| 2 — Shape | 5–10 | Which decisions will be expensive to undo? | Schema, public API and config are written down; a stranger can run Speck in 30 minutes |
| 3 — Deliver | 11–18 | How does code get to users, safely and often? | A commit reaches production untouched by hand, and one release has been rolled back on purpose |
| 4 — Operate | 19–24 | How do we know it is alive, and what happens when it is not? | Speck was broken on purpose, the phone rang, and the postmortem is written |

Each two-week block has:

- **one core Lesson** — the idea the block is built on
- **one or two depth Lessons** — the parts that turn the idea into work
- **one artefact** — a file, a deploy, an alarm, a document
- **the Stage gate** at the end of the Stage

The full week-by-week order is in
[reference/the-build-order.html](reference/the-build-order.html).

## The 20% core

Twelve items. Nothing in the depth queue is taught until these are solid. Each
one is here because practitioners touch it constantly, or because getting it
wrong is expensive to undo.

**Stage 1 — Decide** (weeks 1–4)

1. **The design doc.** Write it before the code: context, goals, **non-goals**,
   the design, alternatives considered, and cross-cutting concerns. Google's
   own guidance gives 1–3 pages for a small change and 10–20 for a large one.
   It is a code review held before there is any code.
   ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/),
   [Software Engineering at Google, ch. 10](https://abseil.io/resources/swe-book/html/ch10.html))
2. **Vertical slices, not layers.** Build the thinnest slice that goes through
   every layer and deploys, then the next. Cockburn calls the first one a
   **walking skeleton**. Building all the database, then all the API, then all
   the UI is the failure this prevents.
   ([Walking skeleton](https://www.mattblodgett.com/2020/09/start-with-walking-skeleton.html))

**Stage 2 — Shape** (weeks 5–10)

3. **The data model outlives the code.** You will rewrite the front end twice
   and keep the schema. Model the nouns and the rules before the screens.
4. **The contract at the edge.** Design the API before you implement it, and
   know exactly what counts as a breaking change. Adding an optional field is
   safe. Removing a field, renaming it, or making it required is not.
   ([Breaking-change rules](https://www.speakeasy.com/api-design/versioning/),
   [Automating API Delivery, ch. 4](https://www.oreilly.com/library/view/automating-api-delivery/9781633438781/OEBPS/Text/chapter-4.html))
5. **Config from the environment.** Same build, different environment, no code
   change. Keep dev and production close. These are the twelve-factor rules that
   have survived fifteen years. ([The Twelve-Factor App](https://12factor.net/))

**Stage 3 — Deliver** (weeks 11–18)

6. **Trunk-based development and small batches.** Merge to trunk at least once a
   day. DORA found teams with three or fewer active branches deliver faster and
   more reliably. ([DORA: trunk-based development](https://dora.dev/capabilities/trunk-based-development/))
7. **A test strategy one person can maintain.** Many fast unit tests, fewer
   integration tests, very few end-to-end tests. The shape matters because slow
   flaky tests get switched off, and switched-off tests protect nothing.
   ([The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html))
8. **The deployment pipeline.** Stages that each raise confidence, each costing
   more time. The build that passes every stage is the build that ships.
   ([Fowler: Deployment Pipeline](https://www.martinfowler.com/bliki/DeploymentPipeline.html))
9. **Release is not deploy.** Deploy the code dark, turn it on with a flag, and
   change the schema in expand → migrate → contract steps so old and new code
   both work. This is the single habit that makes deploying boring.
   ([Feature Toggles](https://martinfowler.com/articles/feature-toggles.html),
   [Expand and Contract](https://www.tim-wellhausen.de/papers/ExpandAndContract/ExpandAndContract.html))

**Stage 4 — Operate** (weeks 19–24)

10. **The four golden signals and one SLO.** Latency, traffic, errors,
    saturation. Then one number that says whether users are having a good time.
    ([Google SRE Book, ch. 6](https://sre.google/sre-book/monitoring-distributed-systems/))
11. **The security baseline.** Broken access control is still the number one
    risk in OWASP's 2025 list. For a multi-tenant product like Speck, that is
    the risk, not exotic exploits.
    ([OWASP Top 10:2025](https://owasp.org/Top10/2025/))
12. **When it breaks.** Roll back first, diagnose second. Then a blameless
    postmortem, and the four DORA metrics as the scoreboard: deployment
    frequency, lead time, change failure rate, recovery time.
    ([SRE Workbook: postmortem culture](https://sre.google/workbook/postmortem-culture/),
    [DORA four keys](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance))

## Constraints

- **Alone, or one other engineer.** No PM, no designer, no QA, no ops team.
  Every practice is taught in the smallest version that still works. A six-person
  on-call rotation is not available, so the course never assumes one.
- **No product to ship yet.** Speck is the substitute. Every task is done on
  Speck, for real, and deployed for real.
- **English is a second language.** Every Lesson keeps sentences short and names
  things exactly. Technical names are never softened into descriptions.
- **Already strong:** JavaScript, TypeScript, React, front end, Shopify themes
  and Liquid, the Node event loop, backend basics. Do not re-teach these. Point
  at the existing courses instead:
  [Node](../nodejs-mastery-in-1-year/index.html),
  [React](../react-mastery-in-1-year/index.html),
  [Backend](../backend-mastery-tree/index.html),
  [Front end](../frontend-mastery-tree/index.html).
- **Stack is chosen once and kept boring.** Speck runs on TypeScript, Node,
  Postgres and one cloud host. The course is about the practice, not the tool.

## Out of scope

- Finding the problem, talking to users, pricing, metrics of a business. That is
  [founding-engineer](../founding-engineer/index.html).
- Kubernetes, service meshes, microservices. One deployable unit is correct for
  a product with no users. These sit in the depth queue.
- Language and framework tutorials.
- Managing people, hiring, and running a team. That is
  [engineering-manager-in-1-year](../engineering-manager-in-1-year/index.html).
- Interview preparation. This course is for doing the job, not describing it.
