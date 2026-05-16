# Tokenizer Adapter Design

This document outlines the architectural design for supporting multiple tokenizer families in the TCP/AI benchmark tooling without introducing dependency bloat or implementation complexity.

## 1. Current State
The `count_tokens.py` script currently interacts directly with the `tiktoken` library. While it supports multiple encodings (e.g., `o200k_base`, `cl100k_base`), it is tightly coupled to the OpenAI-specific API.

## 2. Proposed Abstraction: `TokenCounter`

To support diverse families (tiktoken, HF, SentencePiece), we will introduce a lightweight internal abstraction.

### Conceptual Interface
```python
class TokenCounter:
    def __init__(self, name: str, family: str):
        self.name = name
        self.family = family

    def count(self, text: str) -> int:
        """Returns the number of tokens in the given text."""
        raise NotImplementedError
```

### Planned Families
- **tiktoken**: Built-in support for OpenAI encodings.
- **hf_tokenizers**: Support for models via a local `tokenizer.json`.
- **sentencepiece**: Support for models via a local `tokenizer.model`.

## 3. CLI Evolution

Future iterations of the token-count tool should support explicit paths to non-tiktoken assets to maintain an offline-first workflow.

### Proposed CLI Examples
```bash
# Current (tiktoken baseline)
--tokenizer all

# Future (Custom HF Tokenizer)
--tokenizer-hf llama3=./models/llama3/tokenizer.json

# Future (Custom SentencePiece)
--tokenizer-sp mistral=./models/mistral/tokenizer.model
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
