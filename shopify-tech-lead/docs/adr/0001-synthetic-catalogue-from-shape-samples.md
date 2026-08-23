# Practise on a synthetic catalogue generated from shape samples, never on client data

**Status:** accepted · 2026-08-23

The learner has read-only access to a real client Shopify Plus store, with the
client's permission to download product data "to practise". This Course is
rsynced into a **public** GitHub Pages repo by `../deploy-site.sh`, which excludes
only `learning-records/`, PDFs, `.claude/`, `.github/`, the script and the gate
page — every `.md` and `.html` file is published.

Permission to practise is not permission to publish. Nobody granted the second
one. So: we read the Client store only for **structure and scale** (product and
variant counts, metafield namespaces and keys, tag conventions, location count,
collection organisation, and which installed app wrote which field), record that
as a **Shape sample**, and write a generator that produces a synthetic catalogue
of the same shape and scale. The Dev store and the Project are loaded with the
synthetic catalogue. No client title, SKU, price, vendor, customer or order ever
enters this repo or the Project repo.

## Considered options

- **Export the client catalogue into the Dev store.** Most realistic. Rejected:
  it puts client data on a machine that publishes, and the git history of the
  public repo cannot be un-published. `deploy-site.sh` already documents this
  hazard — the public repo was given a fresh history specifically so third-party
  PDFs in this repo's history would never be exposed.
- **Use a public sandbox catalogue.** Safe, but the wrong shape and the wrong
  scale, so it teaches none of the throttle and batching problems that matter.
- **Shape sample plus generator.** Chosen. Real structure, real scale, zero
  client data.

## Consequences

- Scale numbers quoted in Lessons are the *synthetic* numbers. Any figure
  traceable to the Client store is rounded to an order of magnitude and wrapped
  in this repo's privacy markers, so `../deploy-site.sh` drops it from the
  published copy. The marker pair is:

```
<!-- private:start -->  ...text that stays private...  <!-- private:end -->
```

  Keep those two tokens **inside a fenced code block** whenever you write about
  them, as above. `deploy-site.sh` matches them anywhere outside a fence: an
  unpaired mention aborts the deploy, and a paired mention silently deletes the
  prose between them.
- The generator is a deliverable, not a throwaway. It lives in the Project repo.
- Reading the Client store to see a **real integration in flight** — app
  attribution on products, which app owns which field, whether inventory is
  written by the store or by an app — stays allowed and is the highest-value use
  of that access. It is read-only and nothing is copied.
