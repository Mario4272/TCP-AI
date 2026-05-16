# TCP/AI Token Count Tool

This tool establishes baseline token counts for the TCP/AI benchmark corpus. It supports tiktoken (OpenAI) encodings by default, and optional local Hugging Face tokenizer files.

## Requirements

### Core (required)
- Python 3.8+
- `tiktoken` — install via: `pip install -r requirements.txt`

### Optional — Local Hugging Face tokenizer support
- `tokenizers` — install via: `pip install -r requirements-hf.txt`

No transformers, torch, sentencepiece, or HuggingFace Hub connection required.

## Usage

### Basic tiktoken usage
```bash
python tools/token-count/count_tokens.py \
  --input corpus/seed/prompts_v0.2.jsonl \
  --output benchmarks/results/seed_v0.2_token_counts.sample.csv \
  --tokenizer o200k_base
```

### Multiple tiktoken encodings
```bash
python tools/token-count/count_tokens.py \
  --input corpus/seed/prompts_v0.2.jsonl \
  --output benchmarks/results/seed_v0.2_token_counts.multi.sample.csv \
  --tokenizer all
```
`--tokenizer all` means: `o200k_base` and `cl100k_base`.

### Optional: local Hugging Face tokenizer
First install the optional dependency:
```bash
pip install -r tools/token-count/requirements-hf.txt
```

Then run with `--hf-tokenizer NAME=PATH`:
```bash
python tools/token-count/count_tokens.py \
  --input corpus/seed/prompts_v0.2.jsonl \
  --output /tmp/hf_counts.csv \
  --hf-tokenizer local_llama3=/path/to/tokenizer.json
```

Multiple `--hf-tokenizer` flags are supported. `NAME` becomes the label in the CSV output.

### Combined tiktoken + HF
```bash
python tools/token-count/count_tokens.py \
  --input corpus/seed/prompts_v0.2.jsonl \
  --output /tmp/mixed_counts.csv \
  --tokenizer all \
  --hf-tokenizer local_llama3=/path/to/tokenizer.json
```

## Arguments

| Flag | Description |
|---|---|
| `--input` | Path to input JSONL corpus. |
| `--output` | Path to output CSV file. Directories created automatically. |
| `--tokenizer` | tiktoken encoding(s): `o200k_base`, `cl100k_base`, `all`, or comma-separated. Default: `o200k_base`. |
| `--hf-tokenizer NAME=PATH` | Optional local HF tokenizer. Repeatable. Requires `tokenizers` installed. |

## HF Tokenizer Constraints
- **Local files only**: `PATH` must be a local `tokenizer.json` file.
- **No downloads**: Remote URLs (`http://`, `https://`) are rejected.
- **No Hub calls**: HuggingFace Hub auto-downloads are not supported.
- **No model assets committed**: No real tokenizer/model files are included in this repo except the synthetic test fixture.

## Output Format (CSV)

| Column | Description |
|---|---|
| `id` | Record ID from corpus |
| `category` | Category from corpus |
| `tokenizer` | Tokenizer label (e.g., `o200k_base`, `tiny_hf`) |
| `natural_tokens` | Token count for natural prompt |
| `tcp_tokens` | Token count for TCP prompt |
| `tokens_saved` | `natural_tokens - tcp_tokens` |
| `token_reduction_percent` | Reduction as a percentage |

## Testing Fixture

A small **synthetic test-only** fixture is provided at:
```
tools/token-count/fixtures/tiny-tokenizer.json
```
This fixture is hand-authored for testing only. It is **NOT** derived from any real model provider and is **NOT** representative of real-world tokenizer performance.

```bash
# Test with the synthetic fixture (requires: pip install -r requirements-hf.txt)
python tools/token-count/count_tokens.py \
  --input corpus/seed/prompts_v0.2.jsonl \
  --output /tmp/fixture_test.csv \
  --hf-tokenizer tiny_hf=tools/token-count/fixtures/tiny-tokenizer.json
```
