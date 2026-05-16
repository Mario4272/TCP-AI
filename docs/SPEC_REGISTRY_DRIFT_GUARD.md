# Spec Registry Drift Guard

This document outlines the strategy for ensuring alignment between the human-readable specification (`SPEC.md`) and the machine-readable registry (`spec/tcpai-v0.3.json`).

## 1. The Drift Risk
As the TCP/AI protocol evolves, there is a significant risk that the human-readable documentation and the machine-readable JSON used by tooling will diverge. 

**Example from Phase 0009**: During the initial implementation of the spec registry, several marker meanings (e.g., `!`, `=`, `>`) were found to have drifted from the original `SPEC.md` definitions. These were corrected before the PR was merged, highlighting the need for automated guards.

## 2. Proposed Future Guard: `validate_spec_registry.py`

We propose implementing a lightweight validation script (likely in `tools/spec-check/`) to be run in CI.

### Verification Logic
- **JSON Integrity**: Ensure `spec/tcpai-v0.3.json` is valid JSON and follows the internal schema.
- **Marker Consistency**: Verify that the marker set in the registry matches the expected v0.3 set.
- **Category Consistency**: Verify that all categories used in the seed corpus are defined in the registry.
- **Schema Alignment**: Confirm that `corpus_schema.required_fields` matches the requirements documented in `corpus/schema.md`.

### Non-Goals
- The script will not attempt to verify natural-language equivalence (text descriptions) between `SPEC.md` and the JSON registry. This remains a human review task.

## 3. Recommended Workflow
1. **Single Source of Truth**: For all automated tooling (validators, counters), `spec/tcpai-v0.3.json` is the authoritative source.
2. **Dual Updates**: Any change to markers, categories, or schema must be reflected in both `SPEC.md` and the JSON registry in the same PR.
3. **PR Template**: Future PR templates should include a checklist item: *"Verified that SPEC.md and spec/tcpai-v0.3.json are aligned."*

## 4. Proposed Issue
We recommend creating a new issue to implement this guard:
- **Title**: Add spec registry drift guard
- **Labels**: `spec`, `tooling`, `ci`
- **Goal**: Implement a script to automate structural validation of the spec registry in CI.
