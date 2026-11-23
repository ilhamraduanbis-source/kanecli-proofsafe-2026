# ProofSafe QA — KaneCLI Hackathon 2026

A standalone, MIT licensed, local-first CSV data quality demonstration built after 12 Nov 2026. Source and browser testing are public. No paid service is needed to operate this application.

## Purpose
An evidence-first interface that checks the synthetic columns `invoice_id,amount,currency` and exports a local JSON report. A PASS is **not** invoice approval, customer acceptance or payment. Test with synthetic/non-sensitive data only.

## Reproduce
```sh
npm test
python3 -m http.server 8765
# open http://localhost:8765
```
CI tests run automatically. `scripts/browser_smoke.py` uses real Chromium but is **not KaneCLI**.

## Contest provenance
This repository was created on 23 Nov 2026 for the KaneCLI challenge. The work builds on a local-evidence ProofSafe idea in the earlier Toyol Digital repo. That precursor is **disclosed**, not represented as new intellectual property. An older ProofSafe frontend first passed [Toyol run 45093939279](https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45093939279). **This standalone app itself then passed authentic KaneCLI** in [one-shot evidence run 45212673247](https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45212673247). Kane reported PASS for the original sample (two records), FAIL for the invalid sample (three issues), and PASS after reset. An AI coding assistant used that real evidence to identify the unverified JSON export and strengthened provenance and Chromium export assertions in the next commit. This is a response to a coverage gap, not a bug falsely attributed to Kane. One human contestant; AI coding assistance. No prize, payout or contest submission yet.

## Genuine Kane workflow
The manual `kane-free.yml` workflow requires an owner-confirmed FREE TestMu balance, this app's actual HTTPS URL, and `LT_USERNAME` and `LT_ACCESS_KEY` saved as repository Actions Secrets. No credentials may enter source or chat. One bounded Kane run preserves unmodified output. `scripts/agent_feedback.sh` is a *prepared* feedback step, not proof it ran. Real agent patch, second Kane run, authentic video, public posts and official submission remain gates.

## Limits
Simple comma splitting only: quoted commas/multiline values are unsupported. No remote upload, data storage, bank/wallet interaction, financial advice, fees or deposits. See [submission checklist](docs/SUBMISSION.md).
