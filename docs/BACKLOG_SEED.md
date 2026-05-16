# Backlog Seed

This document contains a seed/index of proposed initial issues to be added to the GitHub Issue tracker. Once created in GitHub, the live issue tracker becomes the primary source of truth, and this document will serve as a historical reference.

## Proposed Initial Issues

### Issue 1: Add CI workflow for corpus validation and token-count smoke test
- **Labels**: `ci`, `tooling`
- **Goal**: Implement GitHub Actions to run the corpus validator and token-count script on every PR and push to `main`.
- **Status**: (Implemented in Phase 0005)

### Issue 2: Create single source of truth for TCP/AI markers and corpus categories
- **Labels**: `tech-debt`, `spec`, `tooling`
- **Body**: Valid markers and corpus categories are currently duplicated across `SPEC.md`, `corpus/schema.md`, and `tools/corpus-validator/validate_corpus.py`. Create a shared machine-readable source later (e.g., `spec/tcpai-v0.3.json`) and update tooling to consume it.

### Issue 3: Harden token-count tool to create output directories automatically
- **Labels**: `tech-debt`, `tooling`
- **Body**: `tools/token-count/count_tokens.py` assumes the output parent directory exists. Update the script to ensure the path is created automatically if missing.

### Issue 4: Add reproducibility check for `seed_v0.1_token_counts.sample.csv`
- **Labels**: `benchmark`, `tooling`, `ci`
- **Body**: Implement a CI step that regenerates token counts from the seed corpus and compares the output against the committed sample CSV to ensure results are deterministic and reproducible.

### Issue 5: Document marker-detection heuristic rules
- **Labels**: `spec`, `tooling`, `documentation`
- **Body**: The corpus validator uses specific conservative rules for marker detection. Formally document how this logic works and how it avoids false positives.

### Issue 6: Add multi-tokenizer support beyond tiktoken baseline
- **Labels**: `benchmark`, `tooling`
- **Body**: Research and implement support for additional tokenizer families beyond OpenAI (e.g., Llama/SentencePiece) in the baseline measurement scripts.

---

*Note: Do not create these issues manually yet. Await formal approval to use the GitHub CLI or UI for backlog initialization.*
