# Phase 0001: Repo Hardening

## Goal
Prepare the TCP-AI repository for public-facing early collaboration and benchmark development without overbuilding implementation tooling.

## Scope
Repository hygiene, open-source governance templates, benchmark scaffolding, and README polish.

## Files Proposed for Creation
- `.gitignore`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/spec_proposal.md`
- `.github/ISSUE_TEMPLATE/benchmark_result.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `ROADMAP.md`
- `GOVERNANCE.md`
- `SECURITY.md`
- `benchmarks/README.md`
- `corpus/README.md`
- `corpus/schema.md`
- `tools/README.md`

## Files Proposed for Modification
- `README.md`

## Ordered Task List
1. Create `.gitignore` to ignore standard Node, Python, and OS files.
2. Create GitHub collaboration templates in `.github/ISSUE_TEMPLATE/` and `.github/`.
3. Create `ROADMAP.md`, `GOVERNANCE.md`, and `SECURITY.md` in the repo root.
4. Create benchmark scaffolding READMEs and schemas in `benchmarks/`, `corpus/`, and `tools/`.
5. Update `README.md` to refine intro, add "Why this exists", add "What TCP/AI is not", and add a "Roadmap" pointer.

## Verification Plan
- Validate that no executables or heavy dependencies were added.
- Review the modified `README.md` for tone, credibility, and accuracy of claims.
- Confirm all new markdown files render correctly.

## Risks / Open Questions
- **Security Doc:** Defaulting to `SECURITY.md` as it is the GitHub standard, unless `SECURITY-NOTES.md` is preferred.
- **Benchmark Formats:** Should specific baseline metrics or target models be pre-filled in the `benchmark_result.md` template, or should it be left generic for now?

## Awaiting Approval
> [!IMPORTANT]
> Awaiting approval from Mario/Val. Do not proceed to implementation until this plan is explicitly approved.
