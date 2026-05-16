# TCP/AI Tokenizer Strategy

This document outlines the project's strategy for evaluating tokenization efficiency across different models and encodings.

## 1. Current Baseline (tiktoken)
The current baseline uses the `tiktoken` library, which provides high-performance, offline, and deterministic tokenization for OpenAI models.

Supported encodings:
- `o200k_base` (GPT-4o)
- `cl100k_base` (GPT-4, GPT-3.5)

### Why tiktoken?
- **Lightweight**: Zero-dependency (except tiktoken itself).
- **Offline**: No network access required; suitable for private/secure environments.
- **Deterministic**: Guarantees bit-for-bit reproducibility in CI/CD pipelines.
- **Fast**: Efficiently processes large corpora.

## 2. Roadmap for Multi-Tokenizer Support (Issue #10)
Beyond the OpenAI baselines, we aim to support broader tokenizer families to evaluate TCP/AI efficiency across the industry.

### Candidate Tokenizer Families
- **Hugging Face Tokenizers**: Support for Llama 3, Mistral, and other open-weights models.
- **SentencePiece**: Support for older models (e.g., Llama 2, T5).
- **Model-Specific Encoders**: Custom BPE or WordPiece implementations.

### Strategic Constraints
To maintain the project's focus on transparency and reproducibility, adding new tokenizers must adhere to the following:
1. **Lightweight Dependencies**: Avoid pulling in heavy frameworks (e.g., `torch`, `transformers`) into the core repo unless strictly necessary for the benchmark.
2. **Offline-First**: Tooling must work without calling external APIs or downloading models during execution.
3. **Reproducibility**: Environment setup must be deterministic to ensure CI consistency.

## 3. Implementation Recommendations
- **Optional Extras**: Non-tiktoken tokenizers should likely be implemented as optional extras or separate scripts to avoid bloated dependencies in the main project.
- **Model Files**: If local model files (e.g., `.model` or `.json` files) are required, they should be clearly documented and handled outside of version control to avoid repo bloat.

## 4. Current Status
As of Phase 0009, the project supports multi-tokenizer baseline runs for all `tiktoken` encodings. Evaluation of non-tiktoken paths is ongoing.
