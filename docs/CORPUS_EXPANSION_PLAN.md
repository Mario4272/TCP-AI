# Corpus Expansion Plan

This document outlines the strategy for expanding the TCP/AI benchmark corpus from the current 36 seed records to a more robust set of 100+ prompt pairs.

## 1. Target Size & Scope
- **Version**: v0.2 Corpus.
- **Target Count**: 100+ prompt pairs.
- **Content Policy**: All prompts must remain synthetic, generic, and free of PII or sensitive real-world data (medical, legal, financial).

## 2. Category Strategy
We will maintain the current balanced distribution across existing categories while evaluating new domains.

### Existing Categories
- `general_qna`, `brief_explanation`, `technical_explanation`, `coding_request`, `debugging_request`, `writing_editing`, `brainstorming`, `architecture`, `decision_recommendation`, `skeptical_review`, `personal_important`, `structured_data_wrapper`.

### Potential Candidate Domains
- **Summarization**: Condensing long context while preserving specific nuances.
- **Extraction**: Retrieving specific data points into structured formats.
- **Constrained Output**: Adhering to strict length or formatting requirements.
- **Planning**: Multi-step reasoning and logistics.

## 3. Quality Rules for New Records
Each record added to the corpus must adhere to the following:
1. **Valid Markers**: Use only v0.3 markers defined in the canonical spec registry.
2. **Schema Compliance**: Include all required fields (`id`, `category`, `natural_prompt`, `tcp_prompt`, etc.).
3. **Compression Quality**: `tcp_prompt` must represent a meaningful reduction while preserving the intent of the `natural_prompt`.
4. **Detailed Notes**: Provide clear `compression_notes` and realistic `risk_notes`.
5. **Tooling Validation**: Must pass the `validate_corpus.py` script with zero errors.

## 4. Acceptance Criteria for Expansion PRs
- **Validator**: 100% pass rate.
- **Benchmarks**: Token-count samples regenerated and verified.
- **Distribution**: Category distribution remains balanced or justification is provided for skew.
- **Hygiene**: No benchmark claims are made beyond the measured token reduction counts.

## 5. Proposed Milestone Issues
1. **Expand seed corpus to 100 prompt pairs**: Focus on pure data entry and validation.
2. **Add corpus category distribution report**: Enhance validator to output a detailed balance report.
3. **Create corpus contribution guide**: Document the synthetic data policy and validation steps for community contributors.
