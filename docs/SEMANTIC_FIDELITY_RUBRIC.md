# TCP/AI Semantic Fidelity Rubric

This document defines the criteria for evaluating whether a TCP/AI compressed prompt preserves the meaning and intent of its natural language source.

## Overview

TCP/AI aims to reduce token usage while preserving semantic fidelity. This rubric provides a standardized way to measure that preservation across eight critical dimensions.

### Scoring Scale
Each dimension is scored on a scale of **0 to 2**:

- **0: Failed**: The meaning has changed materially, a critical constraint is lost, or the prompt is now nonsensical.
- **1: Partial**: The core intent is preserved, but there is noticeable ambiguity, lost nuance, or minor constraint distortion.
- **2: Preserved**: The prompt is semantically equivalent for the purpose of the task; any loss is negligible.

---

## Scoring Dimensions

### 1. Intent Preservation
Does the TCP prompt preserve the primary task?
- **2**: The AI will perform the exact same task.
- **1**: The task is slightly different or more generic.
- **0**: The AI will perform a different task entirely.

### 2. Constraint Preservation
Are explicit negative and positive constraints retained? (e.g., "no code", "Python only", "limit to 3 bullets").
- **2**: All constraints are clearly present.
- **1**: One or more minor constraints are implied rather than explicit.
- **0**: A major constraint is lost.

### 3. Response-Shape Preservation
Does the TCP prompt preserve the requested output format? (e.g., list, table, code, JSON).
- **2**: Format is unmistakable.
- **1**: Format is implied or simplified.
- **0**: Format is lost.

### 4. Tone/Register Preservation
Does the TCP prompt preserve the requested persona or tone? (e.g., blunt, soft, skeptical).
- **2**: Tone is explicitly signaled via markers or concise language.
- **1**: Tone is neutral when it should have been specific.
- **0**: Tone is distorted or contradictory.

### 5. Context Preservation
Does the TCP prompt retain necessary background information, variables, or identifiers?
- **2**: All load-bearing details are present.
- **1**: Some secondary context is removed, requiring minor AI inference.
- **0**: Critical context is missing.

### 6. Ambiguity Introduced
Does the compression introduce new confusion not present in the original?
- **2**: No new ambiguity.
- **1**: Slightly harder to parse but clear for an LLM.
- **0**: Materially confusing or "word salad."

### 7. Safety/Privacy Preservation
Does the compression avoid distorting sensitive context or amplifying risks?
- **2**: Safe and matches natural intent.
- **1**: Minor distortion of risk profile.
- **0**: Compression makes the prompt appears to violate safety or privacy in a way the original did not.

### 8. Marker Correctness
Are TCP/AI markers used consistently with the specification?
- **2**: Markers are used correctly per `spec/tcpai-v0.3.json`.
- **1**: Marker is used but technically redundant or slightly misapplied.
- **0**: Wrong marker for the intent or broken marker syntax.

---

## Total Score Interpretation

The maximum score is **16**.

| Total Score | Interpretation |
|---|---|
| **14–16** | **Strong Preservation**: High confidence in compression quality. |
| **10–13** | **Usable**: Acceptable for most cases, but nuance may be lost. |
| **6–9** | **Weak**: Likely to produce inconsistent or incorrect AI results. |
| **0–5** | **Failed**: Compression is unusable. |

### Provisional Pass/Fail Threshold
A prompt pair is considered a **Pass** if:
1.  Total Score is **13 or higher**.
2.  No score of **0** in Intent, Constraints, or Marker Correctness.

*Note: These thresholds are provisional and may be updated after initial reviewer calibration.*

---

## Implementation Notes
- **Human Review First**: This rubric is designed for human expert review.
- **LLM-Assisted Scoring**: Automated scoring may be used for preliminary screening, but human validation remains the source of truth.
- **Metrics**: Token reduction and Semantic Fidelity are separate and complementary metrics.
