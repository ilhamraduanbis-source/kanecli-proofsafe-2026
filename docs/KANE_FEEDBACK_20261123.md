# Authenticated KaneCLI → AI coding-agent feedback, 23 Nov 2026

## Before-code-change evidence

1. **Original public app:** https://kanecli-proofsafe-2026.vercel.app
2. **Genuine KaneCLI run:** https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45212673247
3. **Original unmodified NDJSON artifact:** `proofsafe-standalone-genuine-kane-session`, artifact ID `14836742911`, preserved in that GitHub run.
4. **Official terminal result:** `REAL_STANDALONE_KANE_EXIT=0`, `AUTHENTIC_KANE_STATUS passed`.
5. **Actual `run_end` findings:** clean CSV PASS with 2 records, invalid CSV FAIL with 3 issues, reset CSV PASS.

The original Kane plan checked the **Export reproducible JSON** button was disabled *before* validation. It did **not** inspect the contents of the exported JSON after validation. That is an observable coverage gap, not a Kane-found software bug.

## AI-assisted iteration from real evidence

An AI coding assistant examined the unmodified result and changed:

- `src/app.mjs` to label exported JSON as `source: LOCAL_BROWSER`, `verifiedByKane: false`, and `transactionSettled: false`. Those explicit flags prevent local evidence from being misrepresented as a remote payment or verified contest state.
- `scripts/browser_smoke.py` to download the **actual** client-generated JSON after PASS, parse it, and assert the expected count, source, sensitive-input omission, and lack of payment/Kane claims.

**No false defect story:** Kane passed its instructed pre-change flow. The patch improves proof coverage in response to what the authentic Kane result had not verified.

## Still required for a fully evidenced closed loop

Re-deploy this commit, execute a **second original KaneCLI test** against the new deployment, preserve the full original transcript, and record both run links. A local test is not a Kane retest.

No credentials, payment, cash claim, or fabricated screenshot belongs in these records.

## Genuine post-agent retest — PASSED

- **Committed AI-assisted code change:** `489026de3d25265152d63d84054dd142c6d92d2a`.
- **Redeployment:** Vercel released the above commit, and the Kane runner first verified `LOCAL_BROWSER` and `transactionSettled:false` were live.
- **Authentic Kane after-agent run:** https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45214209632
- **Archive ID:** `14837054192`, `proofsafe-after-ai-genuine-kane-session`.
- **Terminal result:** `KANE_AFTER_AI_EXIT=0`, `GENUINE_AFTER_KANE_STATUS passed`.
- **What Kane actually did:** examined disabled Export before validation, checked clean PASS and enabled Export, clicked Export and confirmed a download was offered, checked invalid FAIL with exactly three issues, reset and verified PASS.
- **What Kane did NOT claim:** it did not read or assert the contents of that downloaded JSON file. Independent Chromium CI in run https://github.com/ilhamraduanbis-source/kanecli-proofsafe-2026/actions/runs/45213978552 performed that specific assertion after the code change.

The test sequence is **real Kane result → AI-assisted code/test change → Vercel redeploy → second real Kane result**. No bug was invented or disguised as a Kane discovery. No external payout is implied.
