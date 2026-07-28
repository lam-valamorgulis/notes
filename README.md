# Study notes

Personal, self-taught course notes, published as a static site so they can be read
on any device.

**Read them here: https://lam-valamorgulis.github.io/notes/**

Seven courses, each opening on a "Map" page that tells the whole journey and links
to every lesson:

| Course | What it covers |
| --- | --- |
| React Mastery in 1 Year | `UI = f(state)`, then the hard parts, in TypeScript |
| Node.js Mastery in 1 Year | The event loop, async, and non-blocking servers |
| Flutter Mastery in 1 Year | Dart from zero, the rebuild loop, layout, Riverpod and BLoC |
| Engineering Manager in 1 Year | The move to leading people (+ a Front-End Tech Lead sub-course) |
| Shopify Backend Interview Prep | The largest course here (+ an omnichannel sub-course) |
| Claude Certified Architect: Foundations | The six exam areas, plus strategy and a mock |
| Vibe Coding Platform: Architecture in 30 Days | One real open-source AI agent product, end to end |

These are study notes written to teach one reader. They are shared because a public
link is the simplest way to read them anywhere — not because they are finished or
authoritative. Some courses are only a month or two in. Each Map page says which
parts are live.

## Publishing

**Normally you do nothing.** Push to `master` and the site updates itself, through
`.github/workflows/deploy-site.yml`. A run takes about a minute. You can watch it in
the repo's Actions tab, or re-run it by hand from there without making a new commit.

The workflow checks every internal link *before* it publishes. If a link is broken
the run fails and the live site keeps its last good version, so a typo can never
put a 404 on the site. The failed run names the file and the bad link.

To publish from your own machine instead, run `./deploy-site.sh`. It does the same
work: stages the publishable files into `.site/`, checks the links, then commits and
pushes. `./deploy-site.sh --check-only` checks the links and publishes nothing —
useful before you commit.

Two repos are involved on purpose:

| Repo | Visibility | Holds |
| --- | --- | --- |
| `lam-valamorgulis/learn` | private | the source: third-party PDFs and `learning-records/` |
| `lam-valamorgulis/notes` | public | only the publishable site, fresh history |

The split exists because two third-party PDFs sit in this repo's **git history**.
Making this repo public would expose them through that history even if they were
deleted today. The public repo starts from a clean history and never receives them,
so nothing published here redistributes someone else's material.

The workflow cannot use the built-in `GITHUB_TOKEN`, because that token only works on
the repo it runs in. Instead it authenticates with an SSH deploy key kept in the
repository secret `SITE_DEPLOY_KEY`. That key can write to `notes` and to nothing
else — it cannot even read this repo.

## Keeping something out of the public site

`learning-records/` never leaves this repo. Those files hold baselines, self-rated
weak spots, and career goals, and the public site has no reason to carry them.

Excluding the files is not enough on its own, because some course maps describe those
notes inline and that text is personal too. So anything wrapped in these two comments
is cut out of the published pages:

```html
<!-- private:start -->
  ...anything here stays on this machine...
<!-- private:end -->
```

Your local copy keeps everything, so reading the courses here still shows the full
page. Use the same markers for any future content you want kept back.

Two checks run before publishing and fail the build rather than leak:

- no file under `learning-records/` may be staged;
- no published page may still link to one.

If the second one fires, wrap the offending block in the markers above.

Four details that matter if you change the setup:

- `.nojekyll` must stay in the published site. Without it GitHub Pages runs Jekyll,
  which converts the `.md` files into `.html` and breaks every link that points at
  them (for example `href="MISSION.md"`).
- `.github/` must stay excluded from the published files. If the workflow were copied
  into the public repo, GitHub would run it there too, where the secret does not
  exist, so every run would fail.
- Keep `*.pdf` excluded, so the two third-party PDFs never reach the public repo.
- `robots.txt` asks search engines not to index the site. That is a request, not a
  lock. Anyone with the link can read it.

Actions minutes are metered on private repos (the free plan includes 2,000 per month).
A deploy run is about one minute, so normal use costs very little.
