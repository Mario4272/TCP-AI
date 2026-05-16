# Benchmark Methodology

This document outlines the conceptual methodology for the TCP/AI benchmark. Formal executable tooling to automatically measure these metrics will be developed in future phases.

## 1. Token Reduction Measurement
The primary efficiency metric is the compression ratio, defined as the token count of the TCP/AI shorthand prompt divided by the token count of the original natural language prompt.
- **Metric**: `Compression Ratio = TCP_Tokens / Natural_Tokens`
- **Goal**: Measure the raw input efficiency gain without degrading the quality of the model's response.
- **Note**: Exact token counts depend on the tokenizer used (e.g., tiktoken for OpenAI models, Llama tokenizer).

## 2. Clarification-Rate Tracking
A key risk in shorthand communication is ambiguity that forces the AI to ask clarifying questions instead of providing a direct answer.
- **Metric**: `Clarification Rate = Clarification_Responses / Total_Responses`
- **Goal**: Ensure the clarification rate for TCP/AI prompts is equivalent to or lower than the natural language baseline.

## 3. Comparison Lanes (Conceptual)
To properly evaluate TCP/AI, it must be compared against established baselines.

### A. Structured-Data Lane
- **Baselines**: TOON (Task-Oriented Object Notation), JSON, YAML, CSV, XML.
- **Purpose**: Compare the authoring ergonomics and token efficiency of TCP/AI against standard structured data formats for specific, highly structured tasks.

### B. Algorithmic Compressor Lane
- **Baselines**: LLMLingua-family tools.
- **Purpose**: Compare human-writable TCP/AI shorthand against algorithmic prompt compression tools that remove tokens mathematically post-authoring.

*Note: As of Phase 0002, this methodology is strictly conceptual. No benchmark results, claims of measured performance, or testing tools are currently implemented.*
