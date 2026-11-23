# KaneCLI hackathon — two optional public launch posts (NOT PUBLISHED)

**Important:** Official rules require two separate authentic public posts on Hacker News, X, Reddit or LinkedIn. These are drafts ONLY. Do not represent them as posted or counted until the owner intentionally publishes each and preserves the public URL. No post buying, bots, engagement gaming, affiliate marketing, or misleading prize claim.

## Post 1 — LinkedIn or X

**ProofSafe QA, an evidence-first CSV preflight tested by real KaneCLI**

I built an independent, MIT-licensed browser app for the KaneCLI Online Hackathon. ProofSafe QA checks simple synthetic CSV invoice rows locally, highlights duplicates and invalid amounts, and exports machine-readable evidence without uploading data.

A genuine TestMu KaneCLI run checked the passing, failing and reset flows. An AI coding assistant then reviewed the real run and improved JSON provenance and test coverage. We redeployed and ran KaneCLI again successfully.

Code: https://github.com/ilhamraduanbis-source/kanecli-proofsafe-2026

Live demo: https://kanecli-proofsafe-2026.vercel.app/

Genuine Kane logs (before/after): https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45212673247 and https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45214209632

The app is a simple local preflight, not a production invoice validator, regulatory approval or proof of payment. Feedback on evidence quality and QA design is welcome.

## Post 2 — Hacker News or Reddit

**Show HN: ProofSafe QA — local CSV preflight with a real KaneCLI feedback loop**

I made a small MIT-licensed app to explore a specific problem: how can we keep validation evidence honest when coding agents move quickly?

The app runs entirely in the browser and checks three CSV columns. The original KaneCLI flow passed its requirements (valid data PASS with 2 rows; invalid data FAIL with 3 findings; reset PASS). Reviewing that real log revealed a coverage gap: it didn't inspect the exported JSON after validation. An AI coding assistant added explicit source/settlement flags and a Chromium test that opens the downloaded JSON. A second authentic Kane test then passed and confirmed the export could be triggered.

Repo: https://github.com/ilhamraduanbis-source/kanecli-proofsafe-2026

Demo: https://kanecli-proofsafe-2026.vercel.app/

Before and after Kane evidence:
- https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45212673247
- https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45214209632

This parser is intentionally narrow: it doesn't handle quoted commas or multiline CSV. I welcome critiques of the test design or suggestions for the next meaningful assertion.

## Owner's final checklist

- [ ] Publish post 1 from the owner's real account; copy public post URL
- [ ] Publish a **different** post 2 from a real account; copy public post URL
- [ ] Supply both URLs in the competition form
- [ ] Never invent publication dates, engagement or endorsements
