# Notes — how to teach this course

Working notes and stated preferences. Read before designing any lesson.

## Preferences stated by the learner

- **Interview prep goes inside every lesson.** Not a separate module at the end. Each lesson ends
  with an "Say it like an interviewer just asked" block using the shared `renderRecall` widget.
- **Aggressive pace: 15–20 hrs/week.** So each month carries a bigger build, an extra deep dive,
  and more drills than the sibling React / Node courses.
- **Two goals, equally weighted:** pass a senior interview, and be able to ship and sell work as
  a freelancer. Month 10 (release engineering) and Month 12 (system design + client work) exist
  because of the second goal.
- **Riverpod + BLoC both.** Riverpod is the daily driver. BLoC gets a full month because job ads
  ask for it. Teaching both side by side on the same feature is deliberate — the comparison is
  itself a strong interview answer.
- Plain English explanations. Simple vocabulary in docs. Keep real technical names exact
  (`BuildContext`, `RenderObject`, `setState`, `AsyncNotifier`) and explain each once in plain words.

## Teaching decisions made

- **Same design system as the sibling courses.** `assets/base.css` copies the structure of
  `../react-mastery-in-1-year/assets/base.css` and only changes the palette, so the shared
  `assets/quiz.js` works unchanged. Do not rename structural classes.
- **New CSS class added for this course:** `.interview` — the in-lesson interview block. It lives
  in `base.css`, not inline in lessons.
- **Every lesson must have:** a `← The Map` breadcrumb, one `.win` banner, at least one SVG
  visual in `.svg-fig`, a `.drill` scenario, a `renderQuiz` check, a `renderRecall` interview
  block, and a `.remember` recap card at the bottom.
- **Versions are written down on purpose.** Flutter moves fast. Every page that names a version
  says which date it was checked. When a version drifts, fix it and note it here.
  Checked 2026-07-28: Flutter **3.44** (18 May 2026), Dart **3.12.2**, `flutter_riverpod` **^3.4.1**,
  `flutter_bloc` **9.1.1**, `go_router` **17.3.0**.

## Environment facts (checked 2026-07-28)

- macOS. `xcodebuild` present → iOS builds possible after Xcode setup.
- **Flutter SDK not installed. Dart not installed. Android Studio not installed.**
  Lesson 0001 therefore includes a real setup section, and until it is done, Dart practice
  happens in [DartPad](https://dartpad.dev/) so learning is never blocked by tooling.

## Backlog — next sessions

1. **Month 2 lessons** — layout in depth (Flex, Stack, Slivers, responsive/adaptive) + build a
   pixel-accurate responsive screen from a design.
2. **`reference/interview-question-bank.html`** — a growing bank, tagged by month, so questions
   accumulate all year instead of living only inside lessons.
3. **`reference/widget-catalogue.html`** — the 40 widgets that cover 95% of real screens.
4. Consider a `reference/release-checklist.html` when Month 10 arrives (store submission, signing,
   flavors) — high value for the freelance goal.
5. Ask the learner to install Flutter and paste `flutter doctor -v` output, so lessons can assume
   a working toolchain from Month 1 Lesson 5 onward.
