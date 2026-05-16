# TCP/AI Semantic Fidelity Evaluation Method

This document describes the process and methodology for conducting semantic fidelity reviews of TCP/AI prompt pairs.

## 1. Objectives
The primary goal is to ensure that TCP/AI compression preserves the "load-bearing" semantic elements of a prompt. This ensures that a model's output quality is not degraded by the use of shorthand.

## 2. Review Sample Selection
- **Full Corpus**: For stable milestones (like v0.2), a review of all 100 records is preferred.
- **Stratified Sample**: If time is limited, select a stratified sample (e.g., 2 records per category).
- **Edge Cases**: Include both high-compression (large savings) and low-compression (precision-focused) examples to test the boundaries of the protocol.

## 3. Evaluation Process

### Step 1: Automated Validation
Ensure the corpus/record is valid according to the `tools/corpus-validator/`. A record that fails technical validation cannot pass semantic review.

### Step 2: Side-by-Side Review
Compare the `natural_prompt` and `tcp_prompt` side-by-side. Use the [Review Template](../benchmarks/evaluation/semantic_fidelity_review_template.md) to record scores.

### Step 3: Scoring
Apply the [Semantic Fidelity Rubric](SEMANTIC_FIDELITY_RUBRIC.md). Score each of the 8 dimensions.

### Step 4: Resolution
- **Pass**: If the score meets the threshold (provisional >= 13) and has no critical zeros.
- **Fail**: If the score is below the threshold or has a critical zero. Failures should result in a "Suggested Correction" or a revision of the corpus record in a future phase.

## 4. Reviewer Calibration
- **Single Reviewer**: Acceptable for early development phases.
- **Double Reviewer**: Recommended for milestone snapshots. Two reviewers score independently, then resolve differences through discussion.
- **Disagreement Resolution**: If two reviewers cannot agree, a third "senior" reviewer (or the project lead) makes the final determination.

## 5. Artifact Management
- **Review Records**: Completed review templates should be stored (locally or in a dedicated branch) but should generally not include reviewer PII in public commits.
- **Anonymization**: Use handles or role-based identifiers (e.g., "Reviewer A") for public reporting.

## 6. Interpretation of Results
- **Prompt-Pair Quality**: A semantic fidelity score measures the quality of the *compression*, not the quality of the *AI model*.
- **Separation of Metrics**: Semantic fidelity should be reported alongside token reduction but never averaged with it. A prompt that saves 80% tokens but has a semantic score of 4 is a failure.

## 7. Future Directions: LLM-Assisted Review
Automated scoring via LLMs (e.g., using GPT-4 or Claude 3 as a judge) is a planned future capability.
- **Requirement**: Automated judges must use a stable, versioned evaluation prompt.
- **Constraint**: Automated scores must be periodically audited by human reviewers to ensure the "judge" has not drifted.
- **Availability**: LLM-assisted review will be an optional, non-CI tool to avoid API cost/secret requirements for standard contributors.
