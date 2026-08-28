#!/usr/bin/env python3
"""Find prose that breaks the plain-English rules for this course.

The reader is a professional developer whose first language is not English.
Rule 0: one idea per sentence, 20 words maximum, no paragraph over 4 rendered lines.

    python3 check-prose.py                  # every lesson
    python3 check-prose.py 0009 0010        # only these
    python3 check-prose.py --max 24         # loosen the sentence limit while working

Code is not prose: <pre>, <svg>, <script> and <style> are skipped entirely, and a
<code> span counts as one word however long it is.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_WORDS = 20
# .wrap is 46rem = 736px at a 16px root. Body text is serif at 1.06rem (~17px);
# an average glyph is about 0.5em, so ~8.5px, giving ~86 characters per line.
# Callout boxes use .95rem sans (~15.2px), ~7.6px per glyph, so ~96 per line.
# These are estimates. When a paragraph is close to the limit, read it and judge.
CHARS_PER_LINE = 86
CHARS_PER_LINE_BOX = 96
MAX_LINES = 4

argv = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--max" in sys.argv:
    MAX_WORDS = int(sys.argv[sys.argv.index("--max") + 1])
    argv = [a for a in argv if not a.isdigit() or len(a) == 4]

BLOCK = re.compile(r"<(pre|svg|script|style)\b.*?</\1>", re.S | re.I)
CODE = re.compile(r"<code\b[^>]*>.*?</code>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")
# A sentence ends at . ? or ! followed by a space and a capital, or at the end.
SPLIT = re.compile("(?<=[.?!])[\"\u201d\u2019)\\]]?\\s+(?=[A-Z\u201c\"(]|\\d)")


# A Feynman part heading — <span class="h">1 · In plain words</span> — is a
# label, not prose. Left in, it merges into the first sentence and inflates its
# word count by four. Same for the .label heading on a callout box.
LABEL = re.compile(r'<span class="(h|label)"[^>]*>.*?</span>', re.S | re.I)


def strip(fragment: str) -> str:
    fragment = BLOCK.sub(" ", fragment)
    fragment = LABEL.sub(" ", fragment)
    fragment = CODE.sub(" CODE ", fragment)   # a code span is one word
    fragment = TAG.sub("", fragment)
    return re.sub(r"\s+", " ", html.unescape(fragment)).strip()


def sentences(text: str) -> list[str]:
    return [s.strip() for s in SPLIT.split(text) if s.strip()]


def words(sentence: str) -> int:
    return len([w for w in sentence.split() if any(c.isalnum() for c in w)])


targets = sorted(HERE.glob("lessons/[0-9][0-9][0-9][0-9]-*.html"))
if argv:
    # An argument may be a bare prefix ("0048") or a path ("lessons/0048-x.html").
    # Match on the basename either way, and REFUSE to run if an argument matches
    # nothing — a filter that silently selects zero files reports a false pass.
    wanted = [Path(a).name for a in argv]
    unmatched = [a for a in wanted if not any(p.name.startswith(a) for p in targets)]
    if unmatched:
        print("check-prose: these arguments matched no lesson: " + ", ".join(unmatched))
        raise SystemExit(2)
    targets = [p for p in targets if any(p.name.startswith(a) for a in wanted)]

long_sentences = 0
long_paras = 0

for path in targets:
    src = path.read_text(encoding="utf-8")
    lines = src.split("\n")
    hits: list[str] = []

    # Every paragraph-shaped block: <p>, <li>, and the loose text inside a callout.
    for m in re.finditer(r"<(p|li)\b[^>]*>(.*?)</\1>", src, re.S | re.I):
        line_no = src[: m.start()].count("\n") + 1
        text = strip(m.group(2))
        if not text:
            continue

        # A box uses a wider measure than body text.
        before = src[max(0, m.start() - 400):m.start()]
        wide = bool(re.search(r'class="(note|tip|trap|feynman|soundbite|drill|win|remember)', before))
        per = CHARS_PER_LINE_BOX if wide else CHARS_PER_LINE

        for s in sentences(text):
            n = words(s)
            if n > MAX_WORDS:
                hits.append(f"    L{line_no:<4} {n:>3}w  {s[:104]}")
                long_sentences += 1

        # The Sources line is a citation, scanned rather than read, so the
        # 4-line paragraph rule does not apply to it. Its SENTENCES are still
        # checked above — a citation may be long, but not hard to read.
        is_citation = 'id="src"' in m.group(0)

        est = len(text) / per
        if est > MAX_LINES and not is_citation:
            hits.append(f"    L{line_no:<4} {est:.1f} rendered lines ({len(text)} chars) — split it or make a list")
            long_paras += 1

    if hits:
        print(f"\n{path.name}")
        for h in hits:
            print(h)

print(f"\n{'=' * 60}")
print(f"sentences over {MAX_WORDS} words : {long_sentences}")
print(f"paragraphs over {MAX_LINES} lines  : {long_paras}")
sys.exit(1 if (long_sentences or long_paras) else 0)
