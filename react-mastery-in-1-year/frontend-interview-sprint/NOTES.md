# Notes — how to teach this sprint

## Learner
- Senior-level frontend dev, Vietnamese, reads code fluently, reads English prose slowly.
- Real production React: React 18 + TypeScript, webpack 5, Emotion + MUI,
  jotai + zustand + react-query, STOMP over WebSocket, WebRTC media engine.
- Weak spot by self-report: **can use Redux, cannot explain it**.
- Strong material available: a real-time virtual-office product (video call,
  screen share, chat, presence, device management). This is the interview's
  best weapon — most candidates have CRUD apps.

## Teaching rules for this workspace
1. **Every lesson ends in a spoken answer.** Reading is not the deliverable —
   saying it out loud is. Use `renderRecall` for the spoken drills.
2. **Short sentences.** One idea per sentence. The learner is a non-native
   English reader. Never simplify a real technical name.
3. **No new theory without an interview question attached.** If a topic will
   not be asked, it is out of scope this week.
4. **Link, do not repeat.** 26 React lessons already exist in `../lessons/`.
   Point at them; write new material only where the sprint needs a different
   angle (interview framing, drills, gap topics).
5. **Timed katas.** Live coding is a performance skill. Every kata has a clock.
6. **Company names stay wrapped** in ``
   markers so `deploy-site.sh` strips them. In lesson prose, the real-time
   product is "the case-study app", matching lesson 0006 of the parent course.

## Preferences recorded
- Wants links to every already-built lesson so they can go back later —
  see `reference/coverage-map.html`.
- Wants soft-skill lessons about *working* (code review, agile, distributed
  teams, English), not personality-test fluff.
