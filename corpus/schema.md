# Corpus Schema

The intended format for the TCP/AI prompt-pair corpus is JSONL (JSON Lines). Each line represents a single prompt pair.

## Schema Definition

```json
{
  "id": "string (unique identifier)",
  "category": "string (one of the defined benchmark categories)",
  "natural_prompt": "string (the original verbose prompt)",
  "tcp_prompt": "string (the TCP/AI shorthand equivalent)",
  "markers": ["array of strings (TCP/AI markers used)"],
  "expected_response_shape": "string (optional description of the expected output)",
  "risk_notes": "string (optional, notes on potential risks or nuance loss)",
  "compression_notes": "string (optional, notes on the rationale behind the translation)",
  "metadata": {
    "natural_token_estimate": "integer (optional)",
    "tcp_token_estimate": "integer (optional)",
    "author": "string (optional)"
  }
}
```

*Note: This schema is currently used for the `v0.1` seed corpus and will evolve as formal tooling is introduced.*
