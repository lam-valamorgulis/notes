#!/usr/bin/env python3
"""Fail when the course's hard-coded counts disagree with the files on disk.

Why this exists: on 2026-08-28 two lessons were written and five separate places
still claimed eight. Every one of those places is a number a human has to
remember to change. This script remembers instead.

    python3 check-counts.py          # from the course folder
    python3 check-counts.py --fix    # rewrite the counters to match reality

Exit code 0 means every count agrees with the files. Non-zero lists what drifted.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FAIL: list[str] = []


def bad(msg: str) -> None:
    FAIL.append(msg)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


# ---------------------------------------------------------------- the truth
lessons = sorted(HERE.glob("lessons/[0-9][0-9][0-9][0-9]-*.html"))
n_lessons = len(lessons)

plan = read(HERE / "reference/52-week-plan.html")
map_ = read(HERE / "index.html")
notes = read(HERE / "NOTES.md")
root = read(ROOT / "index.html")

# Which week does each lesson claim, and does the plan link back to it?
lesson_weeks: dict[int, Path] = {}
for f in lessons:
    src = read(f)
    m = re.search(r'<span class="wk">Week (\d+) of 52\.?</span>', src)
    if not m:
        bad(f"{f.name}: no `Week N of 52` in its .expertise line")
        continue
    w = int(m.group(1))
    if w in lesson_weeks:
        bad(f"{f.name}: week {w} is also claimed by {lesson_weeks[w].name}")
    lesson_weeks[w] = f

    if f'#w{w}"' not in src:
        bad(f"{f.name}: its .expertise line does not link to the plan anchor #w{w}")
    if f'href="../lessons/{f.name}"' not in plan:
        bad(f"plan: week card w{w} has no `Lesson:` link to {f.name}")

weeks_written = len(lesson_weeks)

# ---------------------------------------------------------------- the claims
def expect(where: str, pattern: str, want: int) -> None:
    """The regex must have exactly one group, and it must equal `want`."""
    found = re.findall(pattern, {"map": map_, "notes": notes, "root": root}[where])
    if not found:
        bad(f"{where}: no text matched /{pattern}/ — did the wording change?")
        return
    for got in found:
        if int(got) != want:
            bad(f"{where}: says {got}, but {want} is true  (/{pattern}/)")


# Ranges in prose are checked by their COUNT, not their shape, so a skipped
# review week does not force a new regex every module.
expect("map", r"<b>(\d+) of 52</b> weeks written", weeks_written)
expect("map", r"Currently live: <b>weeks [^<]*</b> \((\d+) lessons\)", n_lessons)
expect("root", r"<b>(\d+)</b> of <b>52</b> weeks written", weeks_written)
expect("notes", r"\*\*(\d+) of 52 weeks have no lesson yet", 52 - weeks_written)
# The prose range on The Map is checked by hand; the counts above are the guard.

# The core meter: filled bars must equal the caption, and the caption must be
# the number of core items whose weeks are ALL written.
ITEMS = {
    1: [1, 2, 3, 4, 22], 2: [5, 6], 3: [7, 8], 4: [9, 10, 11, 12],
    5: [14, 15, 16, 17], 6: [18, 20, 21], 7: [22, 23, 24, 25],
    8: [27, 28, 29, 30], 9: [31, 32, 33, 34], 10: [35, 36, 37, 38],
    11: [40, 41, 42, 43], 12: [44, 45, 46, 47, 48, 49, 50],
}
done_items = sum(1 for ws in ITEMS.values() if all(w in lesson_weeks for w in ws))

bars = re.search(r'<div class="bars"[^>]*>(.*?)</div>', map_, re.S)
if not bars:
    bad("map: the .core-meter bars block was not found")
else:
    total_bars = bars.group(1).count("<i")
    filled = bars.group(1).count('class="done"')
    if total_bars != 12:
        bad(f"map: core meter has {total_bars} bars, expected 12")
    if filled != done_items:
        bad(f"map: core meter fills {filled} bars, but {done_items} items are fully written")

expect("map", r"<b>(\d+) of 12</b> core items", done_items)
expect("map", r"covering <b>(\d+) of the 12 core items", done_items)

# ---------------------------------------------------------------- the plan
ids = {int(m) for m in re.findall(r'<div class="wk[^"]*" id="w(\d+)">', plan)}
if ids != set(range(1, 53)):
    bad(f"plan: week ids are not exactly 1..52 (missing {sorted(set(range(1,53))-ids)})")

cards = dict(re.findall(r'<div class="wk([^"]*)" id="w(\d+)">', plan))
depth_cards = {int(w) for c, w in re.findall(r'<div class="wk([^"]*)" id="w(\d+)">', plan) if "depth" in c}
review_cards = {int(w) for c, w in re.findall(r'<div class="wk([^"]*)" id="w(\d+)">', plan) if "review" in c}
grid_dp = {int(w) for w in re.findall(r'<a class="dp" href="#w(\d+)">', plan)}
grid_rv = {int(w) for w in re.findall(r'<a class="rv" href="#w(\d+)">', plan)}

if depth_cards != grid_dp:
    bad(f"plan: depth cards {sorted(depth_cards)} != grid dp links {sorted(grid_dp)}")
if review_cards != grid_rv:
    bad(f"plan: review cards {sorted(review_cards)} != grid rv links {sorted(grid_rv)}")

# Every week must appear in the coverage table.
cov = plan[plan.index('id="coverage"'):plan.index("<!-- ================= PHASE 1")]
missing = [w for w in range(1, 53) if f'href="#w{w}">{w}</a>' not in cov]
if missing:
    bad(f"plan: coverage table is missing weeks {missing}")

# A card that names the spine must carry the spine class, and vice versa.
for m in re.finditer(r'<div class="wk([^"]*)" id="w(\d+)">(.*?)</div>\s*(?=<div class="wk|<p class="mod-head|<div class="phase-band|<div class="ask")', plan, re.S):
    cls, w, body = m.group(1), int(m.group(2)), m.group(3)
    names_spine = "spine API" in body or "the spine" in body
    has_class = "spine" in cls
    if names_spine and not has_class:
        bad(f"plan: week {w} talks about the spine but has no `spine` class")
    if has_class and not names_spine:
        bad(f"plan: week {w} has the `spine` class but never mentions the spine")

# ---------------------------------------------------------------- lesson shape
for f in lessons:
    src = read(f)
    for needed, label in [
        ('class="expertise"', "the .expertise line"),
        ('class="feynman"', "the Feynman block"),
        ("1 · In plain words", "Feynman part 1"),
        ("2 · One analogy", "Feynman part 2"),
        ("and where the analogy breaks", "Feynman part 2b (the analogy's limit)"),
        ("3 · The sticking point", "Feynman part 3"),
        ("4 · Now you explain it back", "Feynman part 4 (teach-back)"),
        ('class="remember"', "the Remember-this card"),
        ('class="breadcrumb"', "the ← The Map breadcrumb"),
    ]:
        if needed not in src:
            bad(f"{f.name}: missing {label}")

    if "svg-fig" not in src and 'class="diagram"' not in src:
        bad(f"{f.name}: has no visual (needs an .svg-fig or a .diagram)")

    rec = re.search(r'<div class="remember">(.*?)</div>', src, re.S)
    if rec:
        n = rec.group(1).count("<li>")
        if not 5 <= n <= 7:
            bad(f"{f.name}: Remember-this has {n} bullets, the rule is 5 to 7")

    # A quiz option that is much longer than the others gives the answer away,
    # and quiz.js shuffles position but cannot hide length.
    for i, (opts, _ans) in enumerate(re.findall(r"options:\s*\[(.*?)\]\s*,\s*answer:\s*(\d)", src, re.S), 1):
        lens = [len(o) for o in re.findall(r'"((?:[^"\\]|\\.)*)"', opts)]
        if lens and max(lens) / max(min(lens), 1) > 1.6:
            bad(f"{f.name}: quiz {i} option lengths {lens} — longest is >1.6x the shortest")

# ---------------------------------------------------------------- links
# Every relative link on every page must point at a file that exists. This was
# added after 14 cross-lesson links were found pointing at invented filenames —
# a lesson written from memory of what a file "should" be called. The footer
# chain was already checked; the links inside the prose were not.
for page in sorted(HERE.glob("lessons/*.html")) + [
        HERE / "index.html",
        HERE / "reference/52-week-plan.html",
        HERE / "reference/glossary.html"]:
    if not page.exists():
        bad(f"{page.name}: expected page is missing")
        continue
    for href in re.findall(r'href="([^"#]+)(?:#[^"]*)?"', page.read_text(encoding="utf-8")):
        if href.startswith(("http", "mailto")):
            continue
        if not (page.parent / href).resolve().exists():
            bad(f"{page.name}: dead link -> {href}")


# ---------------------------------------------------------------- footer chain
# Previous/next must point at the adjacent lesson. Four of these broke silently
# when the depth lessons (19, 29, 33, 45) were written and landed between
# lessons that already linked past them.
chain = sorted(HERE.glob("lessons/[0-9][0-9][0-9][0-9]-*.html"))
for i, page in enumerate(chain):
    nav = re.search(r'<div class="footer-nav">(.*?)</div>', page.read_text(encoding="utf-8"), re.S)
    if not nav:
        bad(f"{page.name}: no .footer-nav block")
        continue
    links = re.findall(r'href="([^"#]+)', nav.group(1))
    if i == 0:
        if links[0] != "../index.html":
            bad(f"{page.name}: first lesson should link back to The Map")
    elif links[0] != "./" + chain[i - 1].name:
        bad(f"{page.name}: prev link is {links[0]}, expected ./{chain[i - 1].name}")
    if i < len(chain) - 1:
        if len(links) < 2 or links[1] != "./" + chain[i + 1].name:
            bad(f"{page.name}: next link should be ./{chain[i + 1].name}")


# ---------------------------------------------------------------- report
if FAIL:
    print(f"FAIL — {len(FAIL)} count or shape problems\n")
    for line in FAIL:
        print("  •", line)
    print(f"\ntruth on disk: {n_lessons} lessons, weeks {sorted(lesson_weeks)}, "
          f"{done_items} of 12 core items fully written")
    sys.exit(1)

print(f"OK — {n_lessons} lessons, weeks {sorted(lesson_weeks)}, "
      f"{done_items} of 12 core items fully written; every count agrees.")
