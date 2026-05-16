# Non-tiktoken Tokenizer Support Research

This document evaluates implementation paths for supporting tokenizer families beyond the OpenAI `tiktoken` baseline, aiming to fulfill the goals of Issue #10.

## 1. Candidate Approaches

### A. Hugging Face `tokenizers` library
- **Dependency**: `tokenizers`
- **Pros**:
  - Rust-backed and extremely fast.
  - Significantly lighter than the full `transformers` library.
  - Native support for `tokenizer.json` files.
- **Cons**:
  - Requires specific configuration/JSON files per model.
  - Managing different model versions can lead to UX complexity.
  - May require users to download or provide assets separately to avoid repo bloat.

### B. SentencePiece
- **Dependency**: `sentencepiece`
- **Pros**:
  - Industry standard for older and many local-first models (e.g., Llama 2, T5).
  - Relatively lightweight compared to full deep learning frameworks.
- **Cons**:
  - Requires `.model` binary files.
  - Version-specific and sometimes brittle regarding environment setup.
  - Binary assets are not suitable for version control.

### C. Transformers `AutoTokenizer`
- **Dependency**: `transformers`, `tokenizers`, and often `torch` or `tensorflow`.
- **Pros**:
  - Excellent developer UX (`AutoTokenizer.from_pretrained("model-name")`).
  - Broadest coverage of model families.
- **Cons**:
  - **Heavyweight**: Extremely large dependency tree.
  - **Network-Dependent**: Frequently triggers automatic model downloads.
  - **Unsuitable for Core**: Violates the project's "offline-first" and "lightweight" constraints.

### D. Pre-supplied Local Tokenizer Files
- **Approach**: Users provide paths to local `tokenizer.json` (HF) or `tokenizer.model` (SentencePiece) files.
- **Pros**:
  - **Offline**: No network access required during benchmark execution.
  - **Reproducible**: Ensures the exact same encoding is used regardless of Hugging Face Hub status.
  - **Lightweight Repo**: Keeps binary assets out of the project repository.
- **Cons**:
  - Higher documentation burden on how to obtain and path these files.
  - UX complexity in the CLI.

## 2. Recommendation

**The recommended path for the first non-tiktoken implementation is Option D (Local Files) using the HF `tokenizers` library.**

- **Core Tooling**: Maintain `tiktoken` as the only hard requirement for the baseline.
- **Optional Extras**: Implement non-tiktoken support as an optional "extra" (e.g., `pip install -r requirements-extra.txt`).
- **Safety First**:
  - Do **not** use `transformers` or `torch` in core tooling.
  - Do **not** download models in CI.
  - Do **not** commit large tokenizer/model files to the repository.

## 3. Issue #10 Closure Criteria

Issue #10 ("Add multi-tokenizer support beyond tiktoken baseline") will be considered ready for closure when:
1. At least one non-tiktoken tokenizer path (e.g., HF `tokenizers`) is implemented.
2. The implementation works entirely offline once dependencies are met.
3. No secrets or LLM API keys are required.
4. No model assets are downloaded during CI execution.
5. Setup instructions are clearly documented.
6. Sample output for a non-tiktoken baseline (e.g., Llama 3 via local `tokenizer.json`) is committed and passes reproducibility checks.
7. Core project dependencies remain lightweight.

## 4. Decision Table

| Approach | Dependency Weight | Offline Support | CI Suitability | Setup Complexity | Recommended Phase |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **tiktoken** | Low | Native | High | Low | Phase 0001 (Done) |
| **HF tokenizers** | Medium | via Local File | High | Medium | Phase 0011 |
| **SentencePiece** | Medium | via Local File | High | Medium | Phase 0012+ |
| **Transformers** | Very High | Poor (Default) | Low | Low | Not Recommended |
| **Local File API** | Low | Native | High | Medium | Phase 0011 |
