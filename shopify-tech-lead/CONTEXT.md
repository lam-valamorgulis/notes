# Shopify Tech Lead — Course Context

The glossary for this course. It exists because the old course
(`shopify-nsc-interview-prep/`) used one word for two different things, and the
Map became confusing. Every word below has exactly one meaning here.

This file is a glossary and nothing else. Plans, chapter lists and decisions live
elsewhere.

## Course structure

**Course**:
The whole body of work in `shopify-tech-lead/`. There is exactly one.
_Avoid_: sub-course, mini-course, program

**Track**:
One of the three top-level divisions of the Course. Each Track has its own Map.
The three are Platform, Apps & Integrations, and The Room.
_Avoid_: sub-course, part, section, module

**Chapter**:
A named group of Lessons inside a Track. A Chapter is a navigation unit, not a file.
_Avoid_: unit, week, day, stage

**Lesson**:
One self-contained HTML file that teaches one tightly-scoped thing.
Named `NNNN-dash-case-slug.html`.
_Avoid_: page, article, topic

**Map**:
The `index.html` at the Course root, and one per Track. The single source of truth
that links every Lesson and Reference and tells the story that connects them.
_Avoid_: index, table of contents, home page

**Reference**:
A compressed, printable page that is looked up rather than read through — a cheat
sheet, a matrix, a glossary, a runbook.
_Avoid_: cheatsheet (as a filename), doc, appendix

**Scars**:
The one Reference per Track that collects every "Where it hurts" block from that
Track's Lessons into a single page.
_Avoid_: gotchas, pitfalls, traps, war stories

## Lesson anatomy

Every Lesson has these four blocks, in this order. The names are fixed.

**How it works**:
The mechanism. What the platform actually does, with a visual.

**Where it hurts**:
The failure modes. What breaks in production, what the docs do not say, and what
two Shopify pages disagree about.

**What you say to a client/PM**:
The spoken answer. How to explain the trade-off, the risk, or the "no" to a
non-engineer.

**Remember this**:
The recall card. Five to seven bullets plus one bold one-line takeaway.

## Stores

Three different Shopify stores appear in this Course. Mixing them up is the most
dangerous mistake available, so each has its own word.

**Dev store**:
A free Partner development store created in the Dev Dashboard, on the Plus plan.
Owned by the learner. Everything in the Project is built and broken here.
_Avoid_: test store, sandbox, staging store

**Client store**:
A real, live Shopify Plus store belonging to a client. **Read-only.** Nothing in
this Course ever writes to it. Used only to learn the shape and scale of real
data.
_Avoid_: production store, live store, real store

**Shape sample**:
An anonymised summary taken from the Client store — counts, field names, tag
conventions, structure. Never titles, SKUs, prices, customers or orders. A Shape
sample is what may enter the Course; a raw client export is not.
_Avoid_: export, dump, dataset, sample data

## The hands-on work

**Project**:
The one running application built across Track 2 — a NestJS + Postgres service
that syncs the Fake ERP with the Dev store. It lives in `project/` inside this
Course, in the private `learn` repo. `../deploy-site.sh` excludes that folder from
the published site, so a Lesson shows its code as text and never links to the file.
_Avoid_: app, exercise, capstone, lab

**Fake ERP**:
A small system the learner writes, standing in for the other side of the sync. It
exists so its failures can be caused on purpose — stale reads, duplicate
webhooks, downtime, a price change mid-sync.
_Avoid_: mock, stub, backend, external system

**Project step**:
One checkpoint in the Project, replacing what the old course called a kata. Built
from a blank file while narrating.
_Avoid_: kata, exercise, drill, assignment
