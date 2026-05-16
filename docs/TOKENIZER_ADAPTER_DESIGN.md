# Tokenizer Adapter Design

This document outlines the architectural design for supporting multiple tokenizer families in the TCP/AI benchmark tooling without introducing dependency bloat or implementation complexity.

## 1. Current State
The `count_tokens.py` script uses the `TokenCounter` dataclass abstraction (introduced in Phase 0015) to support both `tiktoken` and optional local Hugging Face tokenizers. The tool supports multiple encodings (e.g., `o200k_base`, `cl100k_base`) and any user-supplied local `tokenizer.json` file.

## 2. Implemented Abstraction: `TokenCounter` (Phase 0015)

The `TokenCounter` dataclass is now implemented in `tools/token-count/count_tokens.py`.

### Implementation
```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class TokenCounter:
    name: str
    family: str  # "tiktoken" or "hf-local"
    count: Callable[[str], int]
```

This replaces the previous conceptual class-based proposal. It is simpler, requires no inheritance or abstract base classes, and keeps the tool readable.

### Implemented Families
- **tiktoken** (`family="tiktoken"`): Built-in support for OpenAI encodings (`o200k_base`, `cl100k_base`).
- **hf-local** (`family="hf-local"`): Optional support for models via a user-supplied local `tokenizer.json`.

## 3. CLI Design (Implemented)

```bash
# Current (tiktoken baseline)
--tokenizer o200k_base
--tokenizer all

# HF-local only (Phase 0015)
--hf-tokenizer llama3=./path/to/tokenizer.json

# Combined tiktoken + HF-local
--tokenizer all --hf-tokenizer llama3=./path/to/tokenizer.json

# Future (SentencePiece - not yet implemented)
# --tokenizer-sp mistral=./models/mistral/tokenizer.model
```

## 4. Dependency Strategy

To keep the core project lightweight, non-tiktoken dependencies will be treated as "optional extras."

- **`requirements.txt`**: Remains limited to `tiktoken`.
- **`requirements-hf.txt`**: Contains `tokenizers`.
- **`requirements-sp.txt`**: Contains `sentencepiece`.

Tooling will use `try-import` blocks to check for these dependencies only when a non-tiktoken tokenizer is requested.

## 5. Output Strategy
- **Stability**: The CSV output schema (`id`, `category`, `tokenizer`, etc.) will remain stable.
- **Naming**: The `tokenizer` column will use the name provided in the CLI (e.g., `llama3` or `o200k_base`).
- **Reproducibility**: Sample results for non-tiktoken tokenizers will only be committed if the underlying assets are publicly accessible or standardized.

## 6. Non-Goals
- **No Automatic Downloads**: The tool will not download model files from the Hugging Face Hub or elsewhere.
- **No LLM APIs**: Token counting must remain local and offline.
- **No Heavy Frameworks**: `torch`, `tensorflow`, and `transformers` will not be added to the dependency tree.
- **No Binary Bloat**: Large model or tokenizer files will not be committed to the repository.
