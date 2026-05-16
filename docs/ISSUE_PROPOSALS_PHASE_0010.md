# Phase 0010: Issue Proposals

This document outlines proposed future issues derived from the research and design work in Phase 0010. 

> [!IMPORTANT]
> **These are proposals only.** No live GitHub issues or labels should be created until these are explicitly reviewed and approved by Mario/Val.

---

### 1. Add spec registry drift guard
- **Goal**: Implement an automated CI check to ensure `spec/tcpai-v0.3.json` remains structurally sound and aligned with schema expectations.
- **Proposed Labels**: `spec`, `tooling`, `ci`
- **Acceptance Criteria**:
  - Script `tools/spec-check/validate_spec_registry.py` created.
  - Script validates JSON schema-like constraints (keys, types).
  - Script added to GitHub Actions workflow.

### 2. Expand seed corpus to 100 prompt pairs
- **Goal**: Scale the benchmark to improve statistical significance.
- **Proposed Labels**: `corpus`, `benchmark`
- **Acceptance Criteria**:
  - `corpus/seed/prompts_v0.1.jsonl` contains 100+ valid records.
  - All records pass the corpus validator.
  - Token-count samples updated for the new records.

### 3. Add corpus category distribution report
- **Goal**: Improve transparency regarding benchmark balance.
- **Proposed Labels**: `corpus`, `tooling`, `benchmark`
- **Acceptance Criteria**:
  - Validator or separate tool generates a summary report (text or JSON) of category counts and percentages.

### 4. Create corpus contribution guide
- **Goal**: Facilitate community contributions while maintaining quality.
- **Proposed Labels**: `documentation`, `corpus`, `good-first-issue`
- **Acceptance Criteria**:
  - `CONTRIBUTING_CORPUS.md` created.
  - Documents synthetic data policy, marker usage, and local validation steps.

### 5. Implement optional Hugging Face tokenizers support
- **Goal**: First step toward non-tiktoken support (Issue #10).
- **Proposed Labels**: `benchmark`, `tooling`
- **Acceptance Criteria**:
  - `count_tokens.py` supports `--tokenizer-hf` using a local `tokenizer.json`.
  - Dependencies are optional (`requirements-extra.txt`).
  - No automatic network downloads or large binary commits.
