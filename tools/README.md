# TCP/AI Tools

This directory contains executable tooling to support the TCP/AI specification.

## Available Tools

- [**token-count**](token-count/): A lightweight offline utility to count and compare tokens between natural language and TCP/AI shorthand using `tiktoken`.
- [**corpus-validator**](corpus-validator/): A dependency-free Python script to strictly validate the integrity and syntax of TCP/AI JSONL benchmark corpora.

## Automated Validation (CI)

This repository uses GitHub Actions to ensure the integrity of the benchmark corpus and the reproducibility of tokenizer results. The [Validate Corpus](.github/workflows/validate-corpus.yml) workflow runs on every pull request and push to `main`, executing both the `corpus-validator` and a smoke test of the `token-count` tool.

## Planned Tools
In the future, we plan to implement the following tools to support the ecosystem:

1. **Prompt Pair Validator**: A CI tool to validate the structure and syntax of submissions to the prompt corpus.
3. **Benchmark Runner**: An automated script to run corpus pairs against live LLM APIs and measure response quality and token usage.
4. **TCP/AI Linter**: A static analysis tool to enforce TCP/AI syntax conventions in IDEs and editors.
5. **Auto-Compressor (Optional)**: An algorithmic tool to automatically convert natural language into valid TCP/AI shorthand.
