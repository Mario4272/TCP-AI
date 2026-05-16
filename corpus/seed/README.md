# Benchmark Seed Corpus (v0.1)

This directory contains the initial seed corpus for the TCP/AI benchmark. 

## Purpose
The seed dataset (`prompts_v0.1.jsonl`) provides 36 high-quality, paired examples of natural language prompts and their corresponding TCP/AI shorthand translations. It spans 12 practical categories and is intended to establish the foundation for testing prompt compression ratios, quality preservation, and marker fidelity.

## Design Constraints
- **Fictional & Generic**: All examples are synthetic. They do not contain real private user data, real medical/legal/financial records, or personally identifiable information.
- **Structured Data Lane**: Structured data examples (e.g., JSON/YAML) are intentionally simple and obviously fictional payloads designed for testing parsing fidelity.
- **No Executable Tooling**: This directory contains only the dataset. Tooling to ingest, run, and measure this dataset will be introduced in future phases.

## File Format
The dataset is in JSONL format, conforming to the schema defined in `corpus/schema.md`.
