# TCP/AI Corpus Contribution Guide

Thank you for your interest in contributing to the TCP/AI benchmark corpus! This document outlines the standards and processes for adding high-quality, synthetic prompt pairs to the benchmark.

## 1. Purpose
The corpus exists to provide a deterministic, reproducible baseline for measuring the efficiency of TCP/AI prompt compression across different model families.

## 2. Synthetic Data Policy
To ensure project sustainability and safety, we adhere to a strict **Synthetic Data Policy**:
- **Synthetic Examples Only**: All prompts must be generic or synthetically generated.
- **No PII**: Do not include names, addresses, phone numbers, or other personally identifiable information.
- **No Sensitive Real-World Data**: Do not include actual medical, legal, financial, immigration, or employment records.
- **No Private Conversations**: Do not contribute logs from private chats or emails.
- **No Licensed Scrapes**: Do not scrape external datasets without explicit license review.

## 3. Required JSONL Fields
Each record in the corpus must be a single JSON line with the following fields:
- `id`: A unique alphanumeric identifier.
- `category`: One of the valid categories from the [Spec Registry](spec/tcpai-v0.3.json).
- `natural_prompt`: The original, verbose natural language prompt.
- `tcp_prompt`: The compressed TCP/AI version.
- `markers`: A space-separated list of the markers used.
- `expected_response_shape`: A brief description of the intended output.
- `risk_notes`: Potential failure modes or ambiguity introduced by compression.
- `compression_notes`: Rationale for specific compression choices.

## 4. Marker Usage Rules
- **Canonical Markers**: Use only v0.3 markers defined in [spec/tcpai-v0.3.json](spec/tcpai-v0.3.json).
- **No Custom Markers**: Do not invent new markers in a corpus PR. Proposals for new markers belong in the [Spec Issue Tracker](https://github.com/Mario4272/TCP-AI/issues).
- **Parentheses**: Allowed for grouping and context (e.g., `(in python)`) but are treated as syntax, not markers.
- **Resources**:
  - [Marker Heuristics](tools/corpus-validator/MARKER_HEURISTICS.md)
  - [TCP/AI Specification](SPEC.md)

## 5. Quality Expectations
- **Intent Preservation**: The `tcp_prompt` must preserve 100% of the core intent of the `natural_prompt`.
- **Honest Risk Assessment**: If compression introduces potential ambiguity, record it in `risk_notes`.
- **Meaning Over Reduction**: Do not sacrifice clarity or safety just to achieve a higher compression ratio.

## 6. Validation Steps
Before submitting a PR, you must run the following local checks:

### Validate Corpus Structure
```bash
python tools/corpus-validator/validate_corpus.py --input corpus/seed/prompts_v0.1.jsonl
```

### Regenerate Token Counts
If you have modified or added records, you must regenerate the multi-tokenizer baseline:
```bash
python tools/token-count/count_tokens.py --input corpus/seed/prompts_v0.1.jsonl --output benchmarks/results/seed_v0.1_token_counts.multi.sample.csv --tokenizer all
```

## 7. Pull Request Checklist
- [ ] Corpus validator passes with 0 errors.
- [ ] Token-count samples updated to reflect new/modified records.
- [ ] No private or sensitive real-world data included.
- [ ] No custom/invented markers.
- [ ] Category balance has been considered.
- [ ] `compression_notes` and `risk_notes` are meaningful.
