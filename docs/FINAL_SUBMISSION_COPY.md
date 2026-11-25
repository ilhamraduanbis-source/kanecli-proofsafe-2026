# KaneCLI Online Hackathon — submission received (owner-confirmed)

## GitHub project URL
https://github.com/ilhamraduanbis-source/kanecli-proofsafe-2026

## Project title
ProofSafe QA — Evidence-first CSV validation, verified with KaneCLI

## Live demo
https://kanecli-proofsafe-2026.vercel.app/

## About the app and AI/Kane loop

ProofSafe QA is a small, original local-first web application that validates simple invoice-like CSV examples and exports reproducible JSON evidence, without uploading records or contacting paid services. It explicitly distinguishes a local validation pass from a customer acceptance, settled payment, or official regulatory result.

Built with JavaScript/HTML/CSS and AI coding assistance, with ten deterministic unit tests and an independent Chromium acceptance suite. One genuine KaneCLI agent test verified the baseline on the deployed website: clean two-row PASS, three-issue invalid FAIL, and reset PASS (run 45212673247). The AI coding assistant read its unmodified result, observed that exported JSON contents had not been inspected, added clear local-provenance and payment-not-settled flags, and extended the browser test to parse that downloaded JSON. After publishing the patch, a second authentic KaneCLI agent run verified the revised export flow and the pass/fail/reset scenarios (run 45214209632). Both original Kane sessions are preserved as GitHub Actions artifacts.

Code and evidence:
- https://github.com/ilhamraduanbis-source/kanecli-proofsafe-2026/blob/main/docs/KANE_FEEDBACK_20261123.md
- https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45212673247
- https://github.com/ilhamraduanbis-source/toyol-digital/actions/runs/45214209632

Technology: standards-based browser JavaScript, GitHub Actions, Playwright/Chromium, TestMu AI KaneCLI. This is a prototype with a narrow CSV parser, not a production regulatory or payment service.

## YouTube demo URL
https://youtu.be/p0rKEJ4f3T0

## Public post URLs
1. https://kanecli-proofsafe-2026.vercel.app/blog/introducing-proofsafe.html
2. https://kanecli-proofsafe-2026.vercel.app/blog/kanecli-feedback-loop.html

These are the two prepared project articles; the organizer's receipt confirms submission, not independent acceptance of each judging criterion.

## Official submission receipt

Owner provided a screenshot of the competition portal showing SUBMISSION RECEIVED, receipt KH-JP4SU3, first submitted 25 November 2026 at 8:55 PM IST (11:25 PM MYT). The submission was made through the official portal by the owner. The prize decision and payment remain unverified.
