#!/usr/bin/env bash
#
# Publish ONLY this course — Claude Certified Architect: Foundations — to Vercel.
#
# This is separate from ../deploy-site.sh on purpose. That script publishes the
# whole library to GitHub Pages. This one publishes this single course folder to
# Vercel, and GitHub is not involved at any step.
#
# What it does, in order:
#   1. Copies this folder into .vercel-site/, leaving out the private files.
#   2. Cuts the private regions out of the copied pages, and takes the
#      Mission links off them.
#   3. Runs guards: nothing private and no PDF may survive in the copy.
#   4. Checks that every internal link points at a file that exists.
#   5. Uploads .vercel-site/ to Vercel as a production deploy.
#
# The source files on this machine are never changed. Everything is stripped in
# the .vercel-site/ copy only, so reading the course locally still shows all of
# it, Mission link included.
#
# What never reaches the internet:
#   - The two PDFs. They are third-party material (15 MB) and stay local.
#   - learning-records/ — personal notes: a baseline, self-ratings, weak spots.
#   - MISSION.md, NOTES.md, RESOURCES.md. No HTML page links to them, so
#     publishing them would only make personal text reachable by guessing a URL.
#     To publish one of them, delete its --exclude line below; the private
#     markers inside it will still be honoured.
#   - Anything wrapped in <!-- private:start --> / <!-- private:end -->.
#
# Usage:
#   ./deploy-vercel.sh                 # check, then publish
#   ./deploy-vercel.sh --check-only    # check only, publish nothing
#
# First run needs you to log in yourself, because the login step asks questions:
#   vercel login
#
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE="$SRC/.vercel-site"
PROJECT="claude-architect-foundations"
CHECK_ONLY="${1:-}"

# --- 1. Stage the publishable files -----------------------------------------
echo "==> 1. Staging the publishable files into .vercel-site/"

# A safety check before any rm -rf: SITE must really be the staging folder.
case "$SITE" in
  */.vercel-site) ;;
  *) echo "    ERROR refusing to delete '$SITE' — that is not the staging folder."; exit 1 ;;
esac

mkdir -p "$SITE"

# Empty the staging folder and build it again from scratch every run. That way a
# file deleted from the course, or a file an older run left behind, can never
# stay on the live site.
#
# .vercel/ is the one thing kept. It holds the id of the Vercel project this
# folder is linked to. Deleting it would make the next deploy create a second,
# brand-new project instead of updating the live one.
find "$SITE" -mindepth 1 -maxdepth 1 ! -name '.vercel' -exec rm -rf {} +

rsync -a \
  --exclude='.vercel-site/' \
  --exclude='.vercel/' \
  --exclude='.git/' \
  --exclude='.claude/' \
  --exclude='.DS_Store' \
  --exclude='.gitkeep' \
  --exclude='*.pdf' \
  --exclude='learning-records/' \
  --exclude='MISSION.md' \
  --exclude='NOTES.md' \
  --exclude='RESOURCES.md' \
  --exclude='deploy-vercel.sh' \
  "$SRC"/ "$SITE"/

# These are study notes for one reader, not something to be found by search.
# The X-Robots-Tag header in vercel.json says the same thing to crawlers that
# ignore robots.txt.
printf 'User-agent: *\nDisallow: /\n' > "$SITE/robots.txt"

# --- 2 & 3. Strip the private parts, then check the copy is safe -------------
echo "==> 2. Removing the private regions and the Mission links"
python3 - "$SITE" <<'PY'
import re
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()

# Anything between these two comments is cut out of the published copy.
region = re.compile(
    r'[ \t]*<!--\s*private:start\s*-->.*?<!--\s*private:end\s*-->[ \t]*\n?',
    re.S,
)

# The Mission links are handled in two different ways, because they appear in
# two different shapes.
#
# Shape 1 — the link sits alone on its own line. That is the footer nav item
# ("Mission" next to "Study Plan"). The whole line goes, so the nav row does
# not end up with a dead word in it.
mission_nav = re.compile(
    r'^[ \t]*<a\s[^>]*href="[^"]*MISSION\.md[^"]*"[^>]*>[^<]*</a>[ \t]*\n',
    re.I | re.M,
)
# Shape 2 — the link sits inside a sentence ("Ties to your mission: ..."). Here
# only the link is removed and its words are kept, so the sentence still reads
# normally. No page in this course uses shape 2 today, but other courses do, so
# the rule is here in case a lesson is copied over.
mission_inline = re.compile(
    r'<a\s[^>]*href="[^"]*MISSION\.md[^"]*"[^>]*>(.*?)</a>',
    re.I | re.S,
)


def pages():
    """Every page that could carry private text — HTML and Markdown both."""
    return sorted([*root.rglob('*.html'), *root.rglob('*.md')])


regions_cut = nav_removed = inline_unwrapped = 0

for page in pages():
    original = page.read_text(encoding='utf-8')
    text, n = region.subn('', original)
    regions_cut += n
    if page.suffix == '.html':
        text, k = mission_nav.subn('', text)
        nav_removed += k
        text, j = mission_inline.subn(lambda m: m.group(1), text)
        inline_unwrapped += j
    if text != original:
        page.write_text(text, encoding='utf-8')

print(f"    private regions cut:            {regions_cut}")
print(f"    Mission nav links removed:      {nav_removed}")
print(f"    Mission links made plain text:  {inline_unwrapped}")

# --- Guards ---------------------------------------------------------------
# Each guard answers one question: "could something private still go out?"
print("==> 3. Checking the staged copy is safe to publish")
problems = []

# Guard 1: a marker left on its own means the pair was not closed, and
# everything after it would be published by mistake.
for page in pages():
    text = page.read_text(encoding='utf-8')
    if 'private:start' in text or 'private:end' in text:
        problems.append(f"unclosed private marker in {page.relative_to(root)}")

# Guard 2: no private file may survive in the copy.
private_names = {'MISSION.md', 'NOTES.md', 'RESOURCES.md'}
for path in sorted(root.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(root)
    if path.name in private_names:
        problems.append(f"file that must stay private is staged: {rel}")
    if path.suffix.lower() == '.pdf':
        problems.append(f"third-party PDF is staged: {rel}")
    if 'learning-records' in rel.parts:
        problems.append(f"personal note is staged: {rel}")

# Guard 3: no published page may still LINK to a private file. A link like that
# would be both a dead link and a pointer at something meant to stay private.
private_link = re.compile(
    r'(?:href|src)\s*=\s*"[^"]*'
    r'(?:learning-records/|MISSION\.md|NOTES\.md|RESOURCES\.md)'
    r'[^"]*"',
    re.I,
)
for page in pages():
    text = page.read_text(encoding='utf-8', errors='replace')
    for hit in private_link.findall(text):
        problems.append(f"{page.relative_to(root)} still links to: {hit}")

if problems:
    print("    ERROR this copy is not safe to publish:")
    for problem in problems:
        print(f"      {problem}")
    print("    Fix the source, or wrap the block in"
          " <!-- private:start --> / <!-- private:end -->.")
    sys.exit(1)

print("    passed: no private file, no PDF, and no link to either")
PY

echo "    staged: $(find "$SITE" -name '*.html' | wc -l | tr -d ' ') html," \
     "$(du -sh "$SITE" | cut -f1) total"

# --- 4. Check every internal link -------------------------------------------
# This runs before the upload, so a dead link leaves the live site on its last
# good version instead of shipping a 404.
echo "==> 4. Checking every internal link"
python3 - "$SITE" <<'PY'
import re
import sys
import urllib.parse
from pathlib import Path

root = Path(sys.argv[1]).resolve()
href_re = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.I)
skip = ('http://', 'https://', 'mailto:', '#', 'data:', '//', 'javascript:')
checked, broken = 0, []

for html in sorted(root.rglob('*.html')):
    text = html.read_text(encoding='utf-8', errors='replace')
    for raw in href_re.findall(text):
        if raw.startswith(skip):
            continue
        rel = urllib.parse.unquote(raw.split('#')[0].split('?')[0])
        if not rel:
            continue
        target = (root if rel.startswith('/') else html.parent) / rel.lstrip('/')
        checked += 1
        if not target.exists():
            broken.append((str(html.relative_to(root)), raw))

print(f"    {checked} internal links checked, {len(broken)} broken")
for src, link in broken:
    print(f"    BROKEN  {src}  ->  {link}")
if broken:
    sys.exit(1)
PY

if [ "$CHECK_ONLY" = "--check-only" ]; then
  echo "==> --check-only given, stopping before the upload."
  exit 0
fi

# --- 5. Upload to Vercel -----------------------------------------------------
echo "==> 5. Publishing to Vercel"

# Use the installed CLI if there is one, otherwise fetch it for this run only.
if command -v vercel >/dev/null 2>&1; then
  VERCEL=(vercel)
else
  echo "    vercel is not installed — using 'npx vercel@latest' for this run."
  VERCEL=(npx --yes vercel@latest)
fi

# Logging in asks questions, so it cannot happen inside this script.
if ! "${VERCEL[@]}" whoami >/dev/null 2>&1; then
  cat <<'MSG'
    ERROR not logged in to Vercel.
    Run this once, answer the prompts, then run this script again:

        vercel login

    (Or set VERCEL_TOKEN in your shell if you would rather use a token.)
MSG
  exit 1
fi

cd "$SITE"

# First run only: create the Vercel project and remember its id in .vercel/.
# --project is given explicitly because the folder is named ".vercel-site",
# which would be a poor project name.
if [ ! -f .vercel/project.json ]; then
  echo "    First run — linking this folder to the Vercel project '$PROJECT'"
  "${VERCEL[@]}" link --yes --project "$PROJECT"
fi

# There is no build step. The folder is plain HTML, CSS, and JS, so Vercel
# serves the files exactly as they are.
"${VERCEL[@]}" deploy --prod --yes

echo "==> Done. The URL printed just above is the live site."
