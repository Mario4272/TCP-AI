# TCP/AI Corpus Validator

This is a lightweight offline utility to strictly validate a TCP/AI JSONL benchmark corpus against the v0.3 spec.

## Requirements
- Python 3.8+
- No external dependencies required.

## Usage
The tool reads a benchmark corpus in JSONL format, validates the schema, checks IDs, enforces the 12 primary categories, validates marker usage, and generates a report.

```bash
python validate_corpus.py \
  --input ../../corpus/seed/prompts_v0.1.jsonl \
  --output ../../benchmarks/validation/seed_v0.1_validation.sample.txt
```

### Validation Logic
1.  **Schema**: Checks for the 8 required fields per record.
2.  **Categories**: Enforces the 12 canonical TCP/AI categories.
3.  **Markers**: 
    - Validates the `markers` array against the v0.3 specification.
    - Warns on apparent markers in prompt text that aren't declared in the array.
    - Uses conservative heuristics for punctuation-like markers (see [MARKER_HEURISTICS.md](MARKER_HEURISTICS.md)).
4.  **Compression**: Warns if the TCP prompt is longer than the natural prompt.

### Arguments
- `--input`: Path to the input JSONL corpus (e.g., `corpus/seed/prompts_v0.1.jsonl`).
- `--output` (Optional): Path where the validation report TXT should be saved. If omitted, the report is printed to `stdout`.

### Exit Codes
- `0`: Validation passed (warnings may exist).
- `1`: Validation failed due to syntax errors or invalid schema/markers.
