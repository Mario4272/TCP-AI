# TCP/AI

**Token Compression Protocol for AI** — an open shorthand profile for token-efficient human → AI communication.

TCP/AI is intended to reduce unnecessary user-input tokens while preserving meaning, tone, certainty, register, and requested response shape. It is a lightweight convention that works today through a short system-prompt primer and can later evolve toward tooling and native model support.

> Status: **v0.3 draft** for community feedback. Empirical benchmarks are currently pending.

## Why this exists

As context windows grow and API requests scale, the token overhead of polite, conversational scaffolding adds up in both cost and latency. TCP/AI provides a standardized, human-readable shorthand to remove low-value scaffolding, allowing power users to communicate their exact intent to models in a fraction of the tokens.

## What TCP/AI is not

- **Not a structured data format:** Unlike TOON, JSON, or YAML, TCP/AI is designed for conversational, human-writable input.
- **Not an algorithmic compressor:** Unlike LLMLingua or other algorithmic compressors, it requires no pre-processing scripts or API middleware.
- **Not a replacement for natural language:** It is an optional power-user shorthand.
- **Not a model fine-tune or learned compression:** It uses standard English vocabulary in a condensed grammar.

## 30-second quick start

Paste [`primer/system-prompt.txt`](primer/system-prompt.txt) at the start of an AI conversation, then write:

```text
?.b how transformers work
```

instead of:

```text
Hi, I was wondering if you could give me a quick explanation of how transformers work?
```

The model should reply naturally, using the tone and response shape signaled by the marker.

## Core idea

TCP/AI preserves whole content words and removes low-value conversational scaffolding:

- Drop greetings, hedges, self-narration, and obvious filler.
- Keep technical terms, names, identifiers, file paths, URLs, numbers, units, negations, and quantifiers.
- Use compact markers for tone and response shape.
- Reply in natural language; only the human input is compressed.

## Example

| Natural                                                                                                          | TCP/AI                                             |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| "Could you please write me a Python function that takes a list and returns the unique values, preserving order?" | `=Python fn: list → unique values, preserve order` |
| "I need you to be really direct with me — is my business plan actually viable or am I fooling myself?"           | `=.blunt business plan viable, or fooling myself?` |
| "Can you give me a quick brainstorm of names for a coffee shop with a vintage aesthetic?"                        | `~.opt coffee shop names, vintage aesthetic`       |

## Repository layout

- [`ROADMAP.md`](ROADMAP.md) — project roadmap and upcoming phases
- [`SPEC.md`](SPEC.md) — canonical TCP/AI v0.3 draft specification
- [`EXAMPLES.md`](EXAMPLES.md) — expanded examples and patterns
- [`BENCHMARKS.md`](BENCHMARKS.md) — benchmark methodology and comparison matrix
- [`primer/system-prompt.txt`](primer/system-prompt.txt) — copy-pasteable primer for current LLMs
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to propose changes
- [`SECURITY.md`](SECURITY.md) — security policy
- [`GOVERNANCE.md`](GOVERNANCE.md) — project governance
- [`CHANGELOG.md`](CHANGELOG.md) — version history
- [`LICENSE`](LICENSE) — CC0 / public domain dedication

## License

TCP/AI is released under CC0 / public domain. Use, fork, implement, benchmark, and extend freely.
