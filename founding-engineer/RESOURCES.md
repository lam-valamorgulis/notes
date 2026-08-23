# Founding Engineer Resources

Every claim in a Lesson traces back to something on this page. If a fact has no
source here, it is marked in the Lesson as a bare fact, not dressed up as logic.

Last checked: **2026-08-23**.

---

## Knowledge

### The role itself

- [Article: "Thriving as a Founding Engineer: Lessons from the Trenches" — The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/thriving-as-a-founding-engineer)
  What the job is in practice: broad ownership, comfort with ambiguity, sitting on
  customer calls, and shipping something that works rather than something perfect.
  **Use for:** the definition of the role, and the speed-versus-quality boundary.
- [Article: "Being a founding engineer at an AI startup" — The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/being-a-founding-engineer-at-an-ai)
  A recent first-hand account. **Use for:** what the week actually looks like.
- [Guide: "What Is a Founding Engineer?" — FCTO](https://fcto.ai/guides/founding-engineer/)
  Its actual definition: "the first or one of the first engineering hires… takes
  full technical ownership of building the product." Equity by stage: 1%–3%
  pre-seed, 0.5%–1.5% seed, 0.25%–0.75% Series A. **Use for:** the role definition
  and the offer. A vendor site, so treat the hiring advice as marketing. **Note:**
  the "accountable for the company being able to act" line in F1 is *ours*, not
  theirs — this source does not use the words "act" or "accountable".
- [Guide: "Founding Engineer: 2026 Guide to Role & Rewards" — Underdog.io](https://underdog.io/blog/founding-engineer)
  Compensation shape: lower equity than founders, higher salary than a later hire.
  Its benchmark: 0.1%–2%, median 0.33%, 90th percentile 1.24%. Note it disagrees
  with FCTO, so quote a range and the stage, never one number.
  **Use for:** reading an offer. Depth, not core.

### Finding a real problem

- [Book: _The Mom Test_ — Rob Fitzpatrick](https://www.momtestbook.com/)
  The one book to read first. Three rules: talk about their life not your idea,
  ask about specific past events not hypothetical futures, talk less and listen
  more. **Use for:** every customer conversation, forever.
- [Notes: "The Mom Test" — Michael Lynch's book report](https://mtlynch.io/book-reports/the-mom-test/)
  A careful summary with examples of good and bad questions.
  **Use for:** a fast refresher before a call, when you do not have the book to hand.
- [Video + notes: "How to talk to users" — Gustaf Alströmer, YC Startup Library](https://www.ycombinator.com/library/Iq-how-to-talk-to-users)
  How to run a user interview and how to read the answers.
  **Use for:** interview structure, and how to interpret polite enthusiasm.
- [Essay: "What's A Startup? First Principles." — Steve Blank](https://steveblank.com/2010/01/25/whats-a-startup-first-principles/)
  A startup is a temporary organisation searching for a repeatable, scalable
  business model. **Use for:** why a startup's job is search, not execution.
- [Essay: "Search versus Execute" — Steve Blank](https://steveblank.com/2012/03/05/search-versus-execute/)
  The clearest statement of the difference between the two modes, and why
  importing big-company process into search mode kills startups.
  **Use for:** the kill rule, and for explaining why "just build the roadmap" fails.
- [Talk: "How to Get and Evaluate Startup Ideas" — Jared Friedman, YC Startup School](https://www.youtube.com/watch?v=Th8JoIan4dg)
  About half an hour. Four common founder mistakes, ten evaluation questions, and
  three signs that look bad and are good: **it looks like a lot of boring set-up
  work**, **the space is boring**, and **competitors already exist**. Having the
  problem yourself is evaluation question 5, not one of the three signs.
  **Use for:** lesson F3, choosing which problem.
- [Book: _The Lean Startup_ — Eric Ries](https://theleanstartup.com/book)
  Read it for two things only: **innovation accounting** (baseline, tune, then a
  scheduled decision) and the **pivot-or-persevere meeting** held on a fixed
  date. **Use for:** lesson F4, the kill rule. Skip the motivational chapters.
- [Book: _Quit_ — Annie Duke (2022)](https://x.com/AnnieDuke/status/1579891488221061120)
  **Kill criteria**, and the "states and dates" pattern: *if by (date) I have not
  reached (state), I quit.* This is the closest published source to lesson F4's
  template — closer than Ries or Blank. **Use for:** F4. The linked thread is
  Duke's own summary of the tool.

### Building the smallest real thing

- [Book (free online): _Shape Up_ — Ryan Singer, Basecamp](https://basecamp.com/shapeup)
  Shaping, betting, building. Appetite instead of estimate: fix the time and vary
  the scope. Pitches name the problem, the appetite, the solution, the rabbit
  holes and the no-gos. **Use for:** scoping any piece of work, and for writing a
  one-page pitch a founder can say yes or no to.
- [Video + notes: "How to plan an MVP" — Michael Seibel, YC Startup Library](https://www.ycombinator.com/library/6f-how-to-plan-an-mvp)
  How to choose the initial feature set, and why not to fall in love with your MVP.
  **Use for:** the MVP cut, and for arguing scope down without sounding lazy.
- [Article: "YC's Essential Startup Advice" — Michael Seibel](https://www.michaelseibel.com/blog/yc-s-essential-startup-advice)
  The real source for the customer-count point: "a small group of customers who
  love you is better than a large group who kind of like you… recruiting 10
  customers who have a burning problem is much better than 1000 customers who have
  a passing annoyance." **Use for:** B2. The often-quoted "100 versus 100,000"
  version is not in either Seibel source.
- [Essay: "Choose Boring Technology" — Dan McKinley (2015)](https://mcfunley.com/choose-boring-technology)
  Innovation tokens: you get about three novel choices, so spend them where they
  win. The real argument is failure modes — boring tools fail in ways you already
  understand. **Use for:** every stack decision, and for saying no to a shiny one.
- [Chapter: "Start with a Walking Skeleton" — Alistair Cockburn, _97 Things Every Software Architect Should Know_](https://www.oreilly.com/library/view/97-things-every/9780596800611/ch60.html)
  Two pages, behind an O'Reilly subscription. His full sentence: "a tiny
  implementation of the system that performs a small end-to-end function. **It need
  not use the final architecture**, but it should link together the main
  architectural components." The definition first appeared in his _Crystal Clear_
  (2004). **Use for:** lesson B4. Note the bolded clause: B4's stricter reading —
  real deploy, real database, no fakes — is *ours*, not his.

### Users, money, staying alive

- [Essay: "Do Things that Don't Scale" — Paul Graham (2013)](https://paulgraham.com/ds.html)
  Recruit your first users manually, one at a time, plus the "Collison
  installation". His own framing: over-engaging with early users is "a necessary
  part of the feedback loop that makes the product good". **Use for:** getting from
  zero users to ten. **Note:** the words "research", "sample" and "instrument" in
  L1 are *ours*; they do not appear in the essay.
- [Book: _Lean Analytics_ — Alistair Croll & Benjamin Yoskovitz (O'Reilly, 2013)](https://www.oreilly.com/library/view/lean-analytics/9781449335687/)
  The One Metric That Matters, and the five stages: empathy, stickiness,
  virality, revenue, scale. **Use for:** choosing what number to watch, and for
  refusing to build a dashboard of thirty.
- [Article: "Why your customers would be happier if you charged more" — Patrick McKenzie (Kalzumeus)](https://www.kalzumeus.com/2012/09/21/ramit-sethi-and-patrick-mckenzie-on-why-your-customers-would-be-happier-if-you-charged-more/)
  Old and still the clearest writing on why engineers underprice their own work,
  and why paying customers cost less support than free ones.
  **Use for:** lesson L2. Read it for the argument, not the numbers.
- [Podcast: SaaS pricing — Rob Walling and Patrick Campbell](https://saas.transistor.fm/episodes/saas-pricing-experts)
  The value-metric-first argument: get the customer focus and the value metric
  right and you can be wrong about everything else. **Use for:** choosing what to
  charge *per*, before choosing the number.
- [Q&A: discounting the first customers — SaaStr](https://www.saastr.com/is-it-a-good-idea-to-give-the-first-customers-of-a-new-saas-startup-a-discount-to-get-them-on-board)
  Price fairly so price is not the blocker on the reference account. **Use for:**
  the trade-off that a first discount becomes the number they quote to friends.
- [Article: "Production observability for solo developers"](https://dev.to/alexcloudstar/what-happens-after-you-vibe-code-production-observability-for-solo-developers-2iba)
  Error tracking first — the step with the biggest effect — then uptime checks, then
  structured logs on payments, sign-up and integrations, plus a one-paragraph
  incident note. **Use for:** lesson L4. A practitioner post, not a study.
- [Reference: DORA metrics](https://dora.dev/guides/dora-metrics/)
  Deploy frequency and change failure rate: smaller changes fail less often. The
  best-evidenced claim in lesson L4, and the only one there resting on research
  rather than practitioner opinion. **Use for:** L4's fearless-deploy argument.
- [Reference: the 3-2-1 backup rule](https://www.uschamber.com/co/run/technology/3-2-1-backup-rule) · [and its modern 3-2-1-1-0 version](https://www.druva.com/learning-center/glossary/3-2-1-backup-rule) · [a restore-drill checklist](https://www.momentslog.com/development/database-backup-restore-drill-checklist-how-to-prove-recovery-works-before-an-outage)
  Three copies, two media, one off-site; one immutable copy and zero errors on
  verified restores. Plus what to list before a drill and why to record failed
  attempts. **Use for:** lesson L4's restore drill, RPO and RTO.
- [Library: YC Startup Library](https://www.ycombinator.com/library)
  The whole free library, searchable. **Use for:** pricing, launching, first
  customers, and the standard advice on almost every early decision.

---

## Wisdom (Communities)

Start with one, not five.

- [Indie Hackers](https://www.indiehackers.com/)
  Founders building small products in public, posting real revenue numbers and
  real failures. **Use for:** sanity-checking a problem, pricing, and first-user
  tactics from people who did it last month.
- [Hacker News](https://news.ycombinator.com/) — especially `Show HN`
  Run by Y Combinator. Harsh, technical, and the best free critique you will get.
  **Use for:** launching something small and finding out what breaks. A `Show HN`
  post is a real test of whether the pitch makes sense in one sentence.
- [YC Startup School](https://www.startupschool.org/)
  Free structured course plus co-founder matching. **Use for:** meeting people
  who are actually doing this now, not reading about it.
- [WIP](https://wip.co/)
  Makers who log what they shipped, publicly, and hold each other to it.
  **Use for:** the accountability problem — shipping when nobody is asking you to.
- [Product Hunt discussions](https://www.producthunt.com/discussions)
  More design and product focused than Hacker News.
  **Use for:** feedback on how a product *presents*, not how it is built.

---

## Gaps

Things the mission needs and no strong source has been found for. Every Lesson
that stands on one of these says so on the page, rather than borrowing authority
it does not have.

- **Operations for exactly one engineer.** *Partly closed.* Everything on
  reliability assumes a team — the Google SRE book, on-call rotations, error
  budgets. Lesson L4 is therefore **derived** from the quality boundary in B4 and
  assembled from the practitioner posts listed above. It is the weakest-sourced
  Lesson in the course and it opens by saying so.
- **The first price, with evidence.** *Still open.* The sources above are
  experience, not measurement. Nobody has run a controlled trial on a first price.
  Lesson L2 carries a warning box for this reason. Treat its numbers as starting
  points.
- **Quitting versus pivoting, with data.** *Partly closed on 2026-08-23.* A review
  pass found Annie Duke's **kill criteria** and its "states and dates" pattern,
  which is a much closer source for F4's template than Ries or Blank. What is still
  open is *frequency* data: nobody has counted how often a pivot beats a kill, so
  F4 no longer claims the pivot is "usually" right. Lesson F4 says this in Step 8.
- **Saying no to a founder.** *Closed by writing it ourselves.* The role guides all
  say "push back" and none of them show the sentences. So every Lesson now carries
  `renderRecall` cards with the actual sentences to drill. They are this course's
  wording, not a citation.
- **How often a pivot beats a kill.** *Open, and probably unanswerable.* An earlier
  draft of F4 taught that the pivot path is "usually the right one". Nothing
  supports that. The claim was removed from five places, including a quiz answer
  that marked it correct.
- **Post-mortems of dead small products.** *Still open.* Failure write-ups are
  rarer and more useful than success stories. Worth hunting for a curated set —
  this would strengthen F3, F4 and L2 more than anything else on this page.
