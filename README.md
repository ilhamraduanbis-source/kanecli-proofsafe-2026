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
This repository was created on 23 Nov 2026 for the KaneCLI challenge. The work builds on a local-evidence ProofSafe idea in the earlier Toyol Digital repo. That precursor is **disclosed**, not represented as new intellectual property. A genuine KaneCLI run against a **different earlier frontend** passed in [Toyol run 45093939279](https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45093939279); it **does not prove** this new app was tested. One human contestant; AI coding assistance. No prize, payout or contest submission yet.

## Genuine Kane workflow
The manual `kane-free.yml` workflow requires an owner-confirmed FREE TestMu balance, this app's actual HTTPS URL, and `LT_USERNAME` and `LT_ACCESS_KEY` saved as repository Actions Secrets. No credentials may enter source or chat. One bounded Kane run preserves unmodified output. `scripts/agent_feedback.sh` is a *prepared* feedback step, not proof it ran. Real agent patch, second Kane run, authentic video, public posts and official submission remain gates.

## Limits
Simple comma splitting only: quoted commas/multiline values are unsupported. No remote upload, data storage, bank/wallet interaction, financial advice, fees or deposits. See [submission checklist](docs/SUBMISSION.md).
