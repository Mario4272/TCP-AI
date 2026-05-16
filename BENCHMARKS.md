# TCP/AI Benchmark Methodology

This document describes how we measure the performance of the TCP/AI shorthand protocol.

## Evaluation Layers

The TCP/AI benchmark consists of two primary evaluation layers:

1.  **Token Reduction (Quantitative)**: Measuring the raw token savings using various tokenizers. This is currently fully implemented.
    - tiktoken (`o200k_base`, `cl100k_base`) — default baseline.
    - Optional local Hugging Face tokenizers via `--hf-tokenizer NAME=PATH` (requires `pip install -r tools/token-count/requirements-hf.txt`).
2.  **Semantic Fidelity (Qualitative)**: Measuring how well the compressed prompt preserves meaning, intent, and constraints. This is currently in the **Design & Scaffolding** phase.

## Current Baseline (v0.2)

TCP/AI's claims should be validated empirically. Heuristic token-reduction estimates are useful for early discussion, but benchmark data is the source of truth.

## Benchmark goals

*See [methodology.md](benchmarks/methodology.md) for detailed evaluation strategies and [rubric.md](benchmarks/rubric.md) for quality preservation rubrics.*

Measure whether TCP/AI reduces user-input tokens **without materially degrading answer quality, tone fidelity, or round-trip safety**. 

Corpus integrity and token-count reproducibility are ensured through automated CI validation (see [`.github/workflows/`](.github/workflows/)).

Core questions:

1. How many input tokens does TCP/AI save by prompt category?
2. Does response quality change compared with natural prompts?
3. Does the clarification-question rate increase?
4. Do modality and response-shape markers work reliably?
5. How does TCP/AI interoperate with structured data formats such as TOON?
6. How does TCP/AI compare with algorithmic prompt compressors such as LLMLingua and LongLLMLingua?

## Benchmark matrix

| Category | Baselines | TCP/AI candidate | External candidates |
|---|---|---|---|
| Conversational prompt | Natural English, concise English | TCP/AI | N/A |
| Short task request | Natural English | TCP/AI | N/A |
| Code request | Natural wrapper + unchanged code | TCP/AI wrapper + unchanged code | N/A |
| Structured data | JSON pretty, JSON compact, YAML, XML, CSV | TCP/AI instruction + structured payload | TOON, TONL |
| Tool results | JSON compact | TCP/AI summary + structured payload | TOON |
| RAG context | Raw chunks | TCP/AI summary profile | LLMLingua, LongLLMLingua, LLMLingua-2, Selective Context |
| Agent handoff | Natural instructions | TCP/AI + structured fields | XML-style prompts, JSON schemas |

## Track 1 — Token reduction

Corpus:

- 100+ real conversational prompts, anonymized
- categories: Q&A, brainstorming, code, writing/editing, planning, technical troubleshooting, follow-up prompts

Procedure:

1. Write natural prompt.
2. Write TCP/AI compressed prompt.
3. Tokenize both with multiple tokenizers where possible.
4. Report mean, median, p25, p75, min, max, and distribution by category.

Tokenizers to include:

- OpenAI `cl100k_base`
- OpenAI `o200k_base`
- available Anthropic-compatible tokenizer if accessible
- SentencePiece/BPE tokenizer for at least one open-weight model, where practical

Report:

```text
reduction = (natural_tokens - compressed_tokens) / natural_tokens
```

## Track 2 — Quality preservation

Corpus:

- Same paired natural/TCP prompts as Track 1.

Procedure:

1. Run natural and compressed prompts against the same model with identical settings.
2. Randomize output order.
3. Blind-rate each output.

Rating dimensions:

- correctness
- completeness
- usefulness
- tone match
- instruction following
- whether a clarification was needed

Hypothesis:

```text
TCP/AI should show no statistically meaningful quality degradation at normal compression levels.
```

## Track 3 — Round-trip safety

Measure how often a compressed prompt causes the model to ask a clarification question when the natural prompt produced a direct answer.

Key metric:

```text
clarification_rate_delta = compressed_clarification_rate - natural_clarification_rate
```

Target:

```text
clarification_rate_delta < 2 percentage points
```

## Track 4 — Marker fidelity

For each marker, test whether responses shift in the expected direction.

| Marker | Expected measurable effect |
|---|---|
| `.b` | shorter output |
| `.l` | longer, more detailed output |
| `.ans` | less reasoning / less explanation |
| `.why` | more reasoning / explanatory structure |
| `.blunt` | more direct language, less hedging |
| `.soft` | more diplomatic language |
| `.opt` | multiple options, less forced recommendation |
| `.rec` | explicit recommendation |

## Track 5 — Structured data compression

TCP/AI is not a structured-data serialization format. Structured data should be benchmarked separately.

Formats:

- JSON pretty
- JSON compact
- YAML
- XML
- CSV where applicable
- TOON
- TONL, if included

Datasets:

- uniform array of objects
- semi-uniform array
- deep nested object
- mixed object with arrays
- flat tabular data
- realistic API response
- RAG citation metadata payload
- agent tool-result payload

Metrics:

- token count
- reduction vs JSON pretty
- reduction vs JSON compact
- parse accuracy
- fact extraction accuracy
- malformed regeneration rate
- human readability score

Expected outcome:

TOON should be strong for uniform arrays. JSON may remain strong for deeply nested or irregular structures. TCP/AI should wrap the task instruction, not replace the structured data format.

## Track 6 — Algorithmic prompt compression comparison

External systems to compare where feasible:

- LLMLingua
- LongLLMLingua
- LLMLingua-2
- Selective Context

Benchmark dimensions:

- compression ratio
- quality preservation
- human readability
- authoring cost
- dependency/tooling complexity
- latency added by compression step
- suitability for short conversational prompts vs long-context/RAG payloads

Expected distinction:

```text
TCP/AI = manually writable, human-readable shorthand
LLMLingua family = machine-generated compression, stronger for long prompts/RAG, less human-readable
```

## Safe vs. Unsafe Claims

Before interpreting or publishing benchmark results, please review the [Safe vs. Unsafe Claims](docs/releases/v0.2-benchmark-snapshot.md#5-safe-vs-unsafe-claims) section in our latest snapshot. We prioritize empirical honesty over marketing.

## Minimum viable benchmark run

A credible first benchmark should include:

- 100 paired natural/TCP prompts
- at least 2 tokenizers
- at least 2 frontier LLMs
- at least 1 open-weight model
- blind output quality scoring
- public CSV/JSONL results

## Suggested result files

Future benchmark data and tooling outputs live under the `benchmarks/results/` and `benchmarks/validation/` directories:

```text
benchmarks/
├── reports/
│   └── seed_v0.2_benchmark_summary.md           # Current v0.2 summary report
├── results/
│   ├── seed_v0.1_token_counts.sample.csv        # Historical v0.1 baseline
│   ├── seed_v0.1_token_counts.multi.sample.csv  # Historical v0.1 multi-tokenizer baseline
│   ├── seed_v0.2_token_counts.sample.csv        # Current v0.2 baseline
│   └── seed_v0.2_token_counts.multi.sample.csv  # Current multi-tokenizer baseline
└── validation/
    ├── seed_v0.1_validation.sample.txt          # Historical v0.1 report
    └── seed_v0.2_validation.sample.txt          # Current v0.2 report
```

## Reporting Tool

We use a custom tool to generate summary reports from raw CSV results:
```bash
python tools/benchmark-report/summarize_token_counts.py \
  --input benchmarks/results/seed_v0.2_token_counts.multi.sample.csv \
  --output benchmarks/reports/seed_v0.2_benchmark_summary.md
```
See the [Reporting Tool README](tools/benchmark-report/README.md) for more details.

## Reporting template

```md
# Benchmark Run: YYYY-MM-DD

## Summary

- Corpus size:
- Models:
- Tokenizers:
- Median token reduction:
- Mean token reduction:
- Quality delta:
- Clarification-rate delta:

## Notes

- What worked:
- What failed:
- Patterns to move to Tier 4 / never compress:
- Proposed spec changes:
```
