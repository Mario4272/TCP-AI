# Tokenizer Fixtures

This directory contains **synthetic test-only** tokenizer fixtures.

## `tiny-tokenizer.json`

- **Purpose**: Validate the optional Hugging Face `tokenizers` code path in `count_tokens.py`.
- **Origin**: Hand-authored from scratch using toy BPE vocabulary covering ASCII characters and common English bigrams.
- **Not from any model**: This fixture is **NOT** derived from any real model provider (e.g., LLaMA, Mistral, GPT).
- **Not for benchmarking**: Results produced with this fixture are **NOT** comparable to real-world tokenizer outputs.

To use it:
```bash
# Install optional dependency first
pip install -r tools/token-count/requirements-hf.txt

# Run
python tools/token-count/count_tokens.py \
  --input corpus/seed/prompts_v0.2.jsonl \
  --output /tmp/fixture_test.csv \
  --hf-tokenizer tiny_hf=tools/token-count/fixtures/tiny-tokenizer.json
```
