# Spec Registry Drift Guard

This tool validates the structural integrity of the TCP/AI machine-readable specification registry.

## Purpose
To ensure that `spec/tcpai-v0.3.json` remains structurally sound and aligned with the protocol's requirements. This script is run in CI to catch breaking changes or accidental deletions in the spec registry.

## Usage

### Run Validation
```bash
python tools/spec-check/validate_spec_registry.py --spec spec/tcpai-v0.3.json
```

### Options
- `--spec`: Path to the spec JSON file (default: `spec/tcpai-v0.3.json`).

## Validation Logic
The script verifies:
1. **JSON Syntax**: The file must be valid JSON.
2. **Top-level Keys**: Presence of `version`, `markers`, `categories`, `corpus_schema`, and `syntax_notes`.
3. **Data Types**: Correct types for versions (string), markers (dict), categories (dict), and schema fields (list).
4. **Marker Integrity**: Each marker must have a valid `type` (`modality`, `response_shape`, or `register`) and a `meaning`.
5. **Category Integrity**: Each category must have a `description`.
6. **Syntax Notes**: Presence of notes regarding parentheses.

## Note on Natural Language
This script does **not** verify that the text descriptions in the JSON match `SPEC.md`. Natural-language alignment still requires manual review during Pull Requests.
