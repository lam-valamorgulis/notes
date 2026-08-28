# Mission: 7-Day Node.js Interview Sprint

## Why

A Node.js backend interview is close. The goal is not "learn Node".

The goal is to **walk out of a Node.js interview having said, out loud, what the
runtime was doing** — under a request, under load, and when it broke.


You already read code fluently. The gap this week closes is **retrieval under
pressure**, in English, in front of a stranger.

## Success looks like

- I can predict the print order of a mixed sync / `setTimeout` / `Promise` /
  `process.nextTick` program. On a whiteboard. In five minutes.
- I can write bounded concurrency from an empty file, live, in fifteen minutes.
  500 URLs, 10 at a time, with a retry and a timeout.
- I can explain backpressure with a number, not with the words "it just handles it".
- I can draw my own service on a whiteboard, and defend every box in it.
- I can tell two debugging stories with the mechanism, not just the symptom.
- I can shut a service down without dropping an in-flight request, and say why
  `process.exit()` is the wrong tool.
- I can sit in a system-design round and design a Node service end to end.
- I can say "I do not know, here is how I would find out" without losing the room.

## Domain expert goal

> "Give me any Node service. I can say what it is doing on the single thread,
> where it will break, and how to prove it."

The five abilities stay the same as the parent course:

- Explain it from first principles, with no jargon and no notes.
- Predict how it behaves in a case never seen before.
- Say why it was built this way, and what that choice gives up.
- Debug a problem in it that has no ready answer online.
- Judge someone else's work in it, and say what is wrong and why.

Every lesson here names **one** of those five. A lesson that cannot name one is
the wrong lesson.

## The seven days

| Day | Name | The question it answers |
|---|---|---|
| 1 | The runtime | What is Node actually doing on one thread? |
| 2 | Async under pressure | What happens when 500 things must happen at once? |
| 3 | Streams and memory | How do you move data bigger than RAM? |
| 4 | Your own service | What did *you* build, and why is it shaped that way? |
| 5 | Production | Will it survive real traffic, and can you prove it? |
| 6 | Scale and design | More than one core, and a system on a whiteboard. |
| 7 | The full mock | Nothing new. Everything out loud, on a clock. |

**Day 4 decides the interview.** Everyone else can talk about the event loop.
Only you can talk about your spine API.

## Constraints

- **Seven days, about eight hours each.** Full sprint.
- **NestJS, not Express.** The interview target is a structured backend team.
- **Node v24.14.0.** Every measured number in this sub-course came from that
  version, on 2026-08-28.
- English is a second language. Spoken answers are rehearsed, never improvised.
- Real Node knowledge exists but is **rusty in speech**. This is retrieval
  practice, not first teaching.

## Out of scope

- New Node features nobody asks about in an interview.
- Deno and Bun. Interesting, not the hiring target.
- LeetCode-style puzzles. The drills here are Node drills.
- Kubernetes and cloud platform work.
- Front-end JavaScript. The
  [React sprint](../../react-mastery-in-1-year/frontend-interview-sprint/index.html)
  covers that interview.
