# TCP/AI Roadmap

TCP/AI is currently in **Phase 3: Tooling Development**. 
The goal is to evolve from a draft specification into a fully benchmarked protocol with robust community tooling.

## Phase 1: Repo Hardening (Completed)
- Establish repository structure and open-source hygiene.
- Finalize issue templates, pull request processes, and governance.
- Clean up documentation and outline future benchmark schemas.

## Phase 2: Empirical Benchmarking (Completed)
- Build out the initial prompt corpus (JSONL).
- Gather community benchmark submissions across different models (frontier, open-weight, and local models).
- Validate tokenizer counts and compression ratios.
- Identify edge cases, failure modes, and areas needing specification updates.
- **Seed Corpus expanded to 100+ records (v0.2).**

## Phase 3: Tooling Development (Current)
- Build a tokenizer counter for accurate metrics.
- Develop a prompt-pair validator for CI pipelines.
- **Automated CI, Backlog Tracking, and Spec Registry (Completed/Hardened).**
- **Governance Tooling and Corpus Contribution Guides (Completed).**
- **Tokenizer Strategy and Corpus Expansion (Completed - v0.2).**
- **Benchmark Reporting and v0.2 Snapshot (Phase 0013 Completed).**
- **Semantic Fidelity Evaluation Layer (Phase 0014 Design Completed).**
- Create a local benchmark runner for automated testing.
- Begin work on a TCP/AI linter for IDEs and text editors.

## Phase 4: Auto-Compression
- Research algorithmic approaches to auto-compress natural language into TCP/AI shorthand.
- Provide a CLI tool or extension for automatic conversion.

## Phase 5: Native Model Integration
- Long-term goal: Encourage native recognition and optimization for TCP/AI in major LLM providers to further reduce token costs and latency without sacrificing output quality.
