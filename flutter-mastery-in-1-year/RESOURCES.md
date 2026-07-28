# Flutter Resources

All versions below were checked against the official sources on **2026-07-28**:
Flutter **3.44** stable (released 18 May 2026), Dart SDK **3.12.2**.

## Knowledge

### Primary — the official docs (trust these first)
- [Flutter documentation](https://docs.flutter.dev/)
  The single most reliable source. Use for: anything at all, first.
- [Flutter learning pathway](https://docs.flutter.dev/learn)
  The official ordered path for newcomers (added in Flutter 3.41). Use for: checking I have not skipped a foundation.
- [Flutter official glossary](https://docs.flutter.dev/resources/glossary)
  Flutter's own definitions of its nomenclature. Use for: settling "what does this word really mean" arguments. My own [glossary](reference/glossary.html) follows its wording.
- [Understanding constraints](https://docs.flutter.dev/ui/layout/constraints)
  The layout rule: "Constraints go down. Sizes go up. Parent sets position." Use for: every layout confusion, all year.
- [Flutter architectural overview](https://docs.flutter.dev/resources/architectural-overview)
  How the framework, engine, and embedder fit together. Use for: senior interview answers about rendering.
- [Inside Flutter](https://docs.flutter.dev/resources/inside-flutter)
  How Flutter keeps layout linear-time: the three trees, sublinear rebuilds. Use for: the deepest "how does Flutter work" questions.
- [Performance best practices](https://docs.flutter.dev/perf/best-practices) and [Flutter DevTools](https://docs.flutter.dev/tools/devtools)
  Use for: Month 8, and any jank complaint.
- [Testing Flutter apps](https://docs.flutter.dev/testing/overview)
  Unit, widget, and integration testing from the source. Use for: Month 7.
- [Deployment: iOS](https://docs.flutter.dev/deployment/ios) and [Android](https://docs.flutter.dev/deployment/android)
  Use for: Month 10, shipping to the stores.
- [Writing platform-specific code](https://docs.flutter.dev/platform-integration/platform-channels)
  Platform channels and Pigeon. Use for: Month 9.

### The language
- [Dart language tour](https://dart.dev/language)
  Complete and current (Dart 3.12.2). Use for: syntax, null safety, records, patterns, mixins, async.
- [Effective Dart](https://dart.dev/effective-dart)
  The official style and design guide. Use for: writing Dart that a senior reviewer respects.
- [DartPad](https://dartpad.dev/)
  Run Dart in the browser, no install. Use for: practising language exercises before Flutter is set up.

### The libraries this course commits to
- [Riverpod](https://riverpod.dev/) — **Riverpod 3.0**; `flutter_riverpod: ^3.4.1`, `riverpod_annotation: ^4.0.5`, `riverpod_generator: ^4.0.6`.
  The daily driver for state. Use for: Months 4, 6–12.
- [Bloc library](https://bloclibrary.dev/) — `flutter_bloc: 9.1.1` (on top of `bloc: ^9.0.0`).
  The enterprise pattern most senior job ads still name. Use for: Month 5, and any interview that asks for it.
- [go_router](https://pub.dev/packages/go_router) — **17.3.0**, maintained by the Flutter team in `flutter/packages`.
  Declarative routing, deep links, guards. Use for: Month 6.
- [pub.dev](https://pub.dev/)
  Always check a package's publisher, last publish date, and popularity before depending on it.

### Video and long-form
- [Flutter YouTube channel](https://www.youtube.com/@flutterdev)
  Official. The "Decoding Flutter" and "Widget of the Week" series are high value.
- [Flutter release notes / What's new](https://docs.flutter.dev/release/whats-new)
  Use for: staying current. Check it each month; this course records versions so I can spot drift.

## Wisdom (Communities)

- [r/FlutterDev](https://www.reddit.com/r/FlutterDev/)
  The largest Flutter community. Use for: architecture critique, package opinions, job-market reality checks.
- [Flutter Community on Discord](https://discord.gg/flutter)
  Real-time help. Use for: being unstuck in minutes rather than hours.
- [Stack Overflow — flutter tag](https://stackoverflow.com/questions/tagged/flutter)
  Use for: exact error messages. Search before asking.
- [flutter/flutter GitHub issues](https://github.com/flutter/flutter/issues)
  Use for: confirming a bug is real and not mine. Reading good issue threads is senior-level training in itself.
- [Flutter Meetup groups](https://www.meetup.com/topics/flutter/)
  Use for: in-person practice, local contract leads, and mock interviews with real developers.

Community note: no opt-out recorded. Communities matter twice over here — once for
unsticking, and once because **freelance work usually comes from people, not job boards**.

## Gaps

- **Senior Flutter interview question banks** are mostly low quality (scraped listicles, out of
  date answers). This course builds its own bank inside each lesson instead.
- **Mobile system design** material is far thinner than the web equivalent. Plan for Month 12:
  adapt general system-design method and write my own mobile-specific cases (offline sync, push,
  auth, caching).
- **Freelance pricing and contracts for mobile** — no single trusted source found yet. Look for
  practitioner writing, and ask in the communities above during Month 12.
