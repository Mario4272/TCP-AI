# Corpus Schema

The intended format for the TCP/AI prompt-pair corpus is JSONL (JSON Lines). Each line represents a single prompt pair.

## Schema Definition

```json
{
  "id": "string (unique identifier)",
  "category": "string (e.g., 'coding', 'brainstorming', 'analysis')",
  "natural_prompt": "string (the original verbose prompt)",
  "tcp_prompt": "string (the TCP/AI shorthand equivalent)",
  "expected_response_shape": "string (optional description of the expected output)",
  "metadata": {
    "natural_token_estimate": "integer (optional)",
    "tcp_token_estimate": "integer (optional)",
    "author": "string (optional)"
  }
}
```

*Note: This schema is a draft and is subject to change as the project evolves into the benchmarking phase.*
