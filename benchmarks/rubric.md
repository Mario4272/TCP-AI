# Quality and Marker Fidelity Rubrics

This document outlines the evaluation rubrics for ensuring that the efficiency gains of TCP/AI do not come at the expense of response quality or accuracy.

## 1. Quality Preservation Rubric
When comparing a model's response to a TCP/AI shorthand prompt against its response to the original natural language prompt, the output must be evaluated on the following scale:

- **Score 5 (Identical or Better)**: The TCP/AI response contains all the necessary nuance, constraints, and information requested, matching or exceeding the baseline.
- **Score 4 (Minor Degradation)**: The TCP/AI response is fundamentally correct but misses a trivial detail or constraint that does not impact the overall utility.
- **Score 3 (Noticeable Nuance Loss)**: The core answer is present, but an important nuance, tone, or secondary constraint was missed.
- **Score 2 (Significant Failure)**: The response misses primary constraints or hallucinates due to lacking context.
- **Score 1 (Complete Failure)**: The model fails to understand the prompt, errors out, or asks for clarification on core concepts.

## 2. Marker Fidelity Rubric
TCP/AI relies on specific shorthand markers (e.g., `!` for urgency, `?` for uncertainty, `()` for context). This rubric evaluates how well the model adheres to the intent of these markers.

- **Pass**: The model's response explicitly or implicitly acknowledges the marker's intent (e.g., providing a concise answer when prompted with brevity markers, or adopting a specific persona).
- **Fail**: The model ignores the marker (e.g., providing a verbose answer despite brevity markers, or ignoring a requested output format).

*Note: These rubrics will guide human and LLM-as-a-judge evaluations in future executable benchmarking phases.*
