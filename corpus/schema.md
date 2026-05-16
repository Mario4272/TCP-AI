# Corpus Schema

The intended format for the TCP/AI prompt-pair corpus is JSONL (JSON Lines). Each line represents a single prompt pair.

## Schema Definition

```json
{
  "id": "string (unique identifier)",
  "category": "string (one of the 12 strict benchmark categories)",
  "natural_prompt": "string (the original verbose prompt)",
  "tcp_prompt": "string (the TCP/AI shorthand equivalent)",
  "markers": ["array of strings (strict v0.3 TCP/AI markers)"],
  "expected_response_shape": "string (description of the expected output)",
  "risk_notes": "string (notes on potential risks or nuance loss)",
  "compression_notes": "string (notes on the rationale behind the translation)",
  "metadata": {
    "natural_token_estimate": "integer (optional)",
    "tcp_token_estimate": "integer (optional)",
    "author": "string (optional)"
  }
}
```

*Note: This schema is strictly enforced by the `tools/corpus-validator` script for all corpus contributions.*
