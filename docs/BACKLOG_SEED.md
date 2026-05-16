# Backlog Seed

This document contains a seed/index of proposed initial issues to be added to the GitHub Issue tracker. 

> [!IMPORTANT]
> **GitHub Issues are now the active source of truth for all backlog items.**
> This file is maintained as historical seed/index documentation only. Please refer to the [live GitHub Issue tracker](https://github.com/Mario4272/TCP-AI/issues) for the current status and discussion of these items.

## Seed Issues Index

### 1. Add CI workflow for corpus validation and token-count smoke test
- **Status**: **Completed** (Phase 0005)
- **Description**: Implemented GitHub Actions to run the corpus validator and token-count script on every PR and push to `main`.

### 2. Create single source of truth for TCP/AI markers and corpus categories
- **Live Issue**: [#6](https://github.com/Mario4272/TCP-AI/issues/6)
- **Status**: **Completed** (Phase 0009)
- **Description**: Created `spec/tcpai-v0.3.json` as the canonical registry and refactored the validator to consume it.
- **Labels**: `tech-debt`, `spec`, `tooling`

### 3. Harden token-count tool to create output directories automatically
- **Live Issue**: [#7](https://github.com/Mario4272/TCP-AI/issues/7)
- **Labels**: `tech-debt`, `tooling`, `good-first-issue`

### 4. Add reproducibility check for `seed_v0.1_token_counts.sample.csv`
- **Live Issue**: [#8](https://github.com/Mario4272/TCP-AI/issues/8)
- **Status**: **Completed** (Phase 0008)
- **Labels**: `benchmark`, `tooling`, `ci`

### 5. Document marker-detection heuristic rules
- **Live Issue**: [#9](https://github.com/Mario4272/TCP-AI/issues/9)
- **Status**: **Completed** (Phase 0008)
- **Labels**: `spec`, `tooling`, `documentation`

### 6. Add multi-tokenizer support beyond tiktoken baseline
- **Live Issue**: [#10](https://github.com/Mario4272/TCP-AI/issues/10)
- **Status**: **Advanced** (Phase 0009)
- **Description**: Expanded `count_tokens.py` to support multiple tiktoken encodings and documented the long-term [Tokenizer Strategy](../docs/TOKENIZER_STRATEGY.md).
- **Labels**: `benchmark`, `tooling`
