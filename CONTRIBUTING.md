# Contributing to TCP/AI

TCP/AI is an open draft specification. Contributions are welcome, especially when they include concrete examples or benchmark data.

### Technical Contributions
- **Tooling**: Bug fixes or features for the validator, counter, or linter.
- **Specification**: Proposals for new markers or protocol updates (see [SPEC.md](SPEC.md)).
- **Corpus**: Adding new prompt pairs to the benchmark (see [CONTRIBUTING_CORPUS.md](CONTRIBUTING_CORPUS.md)).

## Useful contributions

- Empirical data from running token-reduction benchmarks
- Quality-preservation benchmark results
- Examples where compression fails or causes model misreads
- Proposed marker additions with justification
- Per-language variants
- Tokenizer-aware analysis
- Reference tooling, such as compressors, linters, browser extensions, or benchmark runners
- Critiques of design decisions with clear reasoning

## Less useful contributions

- Symbol-substitution proposals that have not been token-checked
- Vowel-dropping or txt-speak proposals without tokenizer evidence
- Proposals to compress AI output; this is an explicit non-goal for v0.x
- Claims about token savings without reproducible data

## Change process

1. Open an issue describing the problem.
2. Include examples and, where possible, token counts.
3. Propose a specific spec change.
4. For marker changes, describe collision risks and compatibility impact.
5. Submit a pull request against `SPEC.md` or related files.

## Versioning

TCP/AI uses semantic-ish versioning during the draft period:

- breaking changes to markers or core rules bump the minor version, e.g. `v0.3 → v0.4`
- additive examples, benchmark data, and clarifications may bump the patch version
- `v1.0` should not ship until benchmark data supports the core claims

## Benchmark-first principle

When in doubt, benchmark it. A shorthand that looks smaller may tokenize worse. A compression that saves tokens but causes a clarification round-trip is a net loss.
