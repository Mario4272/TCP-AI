# TCP/AI Token Count Tool

This is a lightweight offline tool designed to establish baseline token counts for the TCP/AI benchmark corpus.

## Requirements
- Python 3.8+
- `tiktoken` (used to count OpenAI tokens offline)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
The tool reads a benchmark corpus in JSONL format, validates the structure, counts tokens for both natural and TCP/AI prompts, and outputs the baseline results to a CSV file.

```bash
python count_tokens.py \
  --input ../../corpus/seed/prompts_v0.1.jsonl \
  --output ../../benchmarks/results/seed_v0.1_token_counts.sample.csv \
  --tokenizer o200k_base
```

### Arguments
- `--input`: Path to the input JSONL corpus (e.g., `corpus/seed/prompts_v0.1.jsonl`).
- `--output`: Path where the results CSV should be saved.
- `--tokenizer`: The `tiktoken` encoding to use (default: `o200k_base`). Supported encodings include `cl100k_base` and `o200k_base`.
