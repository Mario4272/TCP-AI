# Issue Proposals — Phase 0014

These issues are proposed for future phases to build upon the semantic fidelity evaluation design established in Phase 0014.

---

## Issue Proposal 1: Apply semantic fidelity rubric to v0.2 corpus

**Labels**: `benchmark`, `corpus`, `evaluation`

**Body**:
Run a full human semantic fidelity review against the 100-record v0.2 corpus using the Phase 0014 rubric. Document all scores, identify failures, and propose corrections for the v0.3 corpus milestone.

**Acceptance Criteria**:
- Review artifacts (completed templates) created for all 100 records.
- Failures and "suggested corrections" captured in a summary document.
- Benchmark documentation updated to report the baseline semantic fidelity score for v0.2.

---

## Issue Proposal 2: Add semantic fidelity report format to reporting tool

**Labels**: `benchmark`, `documentation`, `evaluation`, `tooling`

**Body**:
Update the `summarize_token_counts.py` tool (or create a companion tool) to aggregate and report semantic fidelity scores from review artifacts.

**Acceptance Criteria**:
- Tool can parse completed review templates/CSV.
- Report includes aggregate scores by category.
- Report clearly distinguishes between token reduction (quantitative) and semantic fidelity (qualitative).

---

## Issue Proposal 3: Design optional LLM-assisted semantic review prompt

**Labels**: `benchmark`, `evaluation`, `tooling`

**Body**:
Design and test a stable prompt for using one or more frontier or locally hosted LLMs as optional review assistants to provide preliminary semantic fidelity scores. This is intended to supplement, not replace, human review.

**Acceptance Criteria**:
- Evaluation prompt is documented and versioned.
- Deterministic settings (temperature 0) recommended.
- "LLM vs Human" calibration check performed on a sample of records.
- Clearly documented as an optional, non-CI tool.

---

**Note**: These are proposals only. Do not create live GitHub issues until explicitly approved by Mario/Val.
