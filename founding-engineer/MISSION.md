# Mission: Building a real software product in a startup

## Why
This course is about being a **founding engineer** — engineer number 1 to 5 at an
early startup, the person accountable for a product existing at all. The gap it
closes is not coding. It is knowing what to build, what to cut, and how to tell
whether it worked.


## Success looks like
- Can sit in a customer call, ask five questions that pass **The Mom Test**, and
  come out with a written problem statement nobody argued with.
- Can take a vague founder idea and return, in one page: the riskiest guess in
  it, the smallest thing that tests that guess, and the date it ships.
- Can say **"we are not building that"** to a founder, out loud, with the reason,
  and keep the room.
- Has shipped one real product to real strangers — deployed, priced, and used by
  people who are not friends. Small is fine. Live is not optional.
- Can name the **one metric that matters** for a product at its current stage,
  and say what it would take to change it.
- Can run a product alone: backups that were restored once on purpose, errors
  that reach a phone, and a deploy that takes minutes not evenings.
- Can look at a startup's product and say what is over-built, what is missing,
  and which guess it never tested.

## Domain expert goal
> "Any early startup can hand me a vague idea and I can take it all the way to a
> live product with paying users — alone if I have to — and I can say why each
> decision was right."

The standard for expert stays the five abilities:

- Explain it from first principles, with no jargon and no notes
- Predict how it behaves in a case never seen before
- Say why it was built this way, and what that choice gives up
- Debug a problem in it that has no ready answer online
- Judge someone else's work in it, and say what is wrong and why

## The 20% core
Twelve items. Four per Track. Nothing else is taught until these are solid.

**Track 1 — Find** (is there a real problem?)

1. **The founding engineer's job** — the role is "first person accountable for
   the company being able to act", not "first person to write code". That
   one-line wording is *ours*; the sources say "full technical ownership".
   ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/thriving-as-a-founding-engineer), [FCTO guide](https://fcto.ai/guides/founding-engineer/))
2. **The Mom Test** — talk about their life, not your idea; ask about the past,
   not the future; listen more than you talk. Every other discovery method is
   built on this. ([The Mom Test](https://mtlynch.io/book-reports/the-mom-test/), [YC: How to talk to users](https://www.ycombinator.com/library/Iq-how-to-talk-to-users))
3. **Choosing which problem to build** — four filters: frequency, pain, who holds
   the budget, and whether you can reach these people. Score 0 to 5 and multiply.
   Picking wrong makes every later decision worthless.
   ([Jared Friedman, YC](https://www.youtube.com/watch?v=Th8JoIan4dg))
4. **The kill rule** — deciding, in advance, what evidence would make you stop.
   Without it you never stop, and the runway decides for you. Elsewhere this is
   called **kill criteria**.
   ([Annie Duke, _Quit_](https://x.com/AnnieDuke/status/1579891488221061120), and
   [Steve Blank: search vs execute](https://steveblank.com/2012/03/05/search-versus-execute/))

**Track 2 — Build** (make the smallest real thing)

5. **Appetite, not estimate** — fix the time, vary the scope. This is the single
   habit that stops six-week features becoming six-month features.
   ([Shape Up](https://basecamp.com/shapeup))
6. **Cutting to the MVP** — decide the initial feature set, and say out loud what
   is deliberately missing. ([YC: How to plan an MVP](https://www.ycombinator.com/library/6f-how-to-plan-an-mvp))
7. **Boring stack and innovation tokens** — you get about three novel choices;
   spend them where they win, not on your database.
   ([Choose Boring Technology](https://mcfunley.com/choose-boring-technology))
8. **The walking skeleton and the quality boundary** — deploy something end to
   end on day one, then go fast everywhere except where a failure loses data or
   trust. The boundary rule is this course's own; the skeleton is Cockburn's.
   ([Alistair Cockburn](https://www.oreilly.com/library/view/97-things-every/9780596800611/ch60.html))

**Track 3 — Live** (users, money, and staying alive)

9. **The first ten users, by hand** — recruit them one at a time. The point is
   not the users, it is what you learn standing next to them.
   ([Paul Graham: Do Things that Don't Scale](https://paulgraham.com/ds.html))
10. **The first price** — charging is a test, not a reward. Free usage measures
    curiosity, which is abundant. Weakest-sourced item in the course, and the
    Lesson says so.
    ([Patrick McKenzie](https://www.kalzumeus.com/2012/09/21/ramit-sethi-and-patrick-mckenzie-on-why-your-customers-would-be-happier-if-you-charged-more/))
11. **The one metric that matters** — one number per stage: empathy, stickiness,
    virality, revenue, scale. ([Lean Analytics](https://www.oreilly.com/library/view/lean-analytics/9781449335687/))
12. **Keeping it alive alone** — the smallest set of operations work that stops
    you losing data or trust: backups you have restored, errors that reach you,
    a deploy you are not afraid of.
    ([Choose Boring Technology](https://mcfunley.com/choose-boring-technology) — failure modes you already understand)

Everything else is **depth** and waits. The full depth queue is on
[The Map](index.html).

## Constraints
- **No product idea yet.** Track 1 has to produce one. The course cannot assume
  a problem is already chosen.
- **English is a second language.** Every Lesson has a *Say it out loud* block
  with fixed sentences to drill, because the job needs speech under pressure:
  saying no to a founder, running a customer call.
- **Already strong:** JavaScript, React, front end, Shopify themes and Liquid,
  the Node event loop, backend basics. Do not re-teach these. Point at the
  existing courses in this repo instead:
  [Node](../nodejs-mastery-in-1-year/index.html),
  [React](../react-mastery-in-1-year/index.html),
  [Backend](../backend-mastery-tree/index.html).
- **No company is the study subject.** Patterns survive; companies do not.

## Out of scope
- Raising money as the goal. Investor decks and term sheets are depth, not
  purpose.
- Becoming a founder or CEO. The seat we are aiming at is engineer number 1.
- Business-school strategy: five forces, TAM slides, market-sizing theatre.
- LeetCode and algorithm puzzles.
- Language and framework tutorials. This course decides *what* to build and
  *whether*, never *how to write a for loop*.
