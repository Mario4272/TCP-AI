# TCP/AI v0.3

**Token Compression Protocol for AI** — an open shorthand profile for token-efficient human → AI communication.

TCP/AI reduces unnecessary user-input tokens by removing low-value conversational scaffolding while preserving meaning, tone, certainty, register, and requested response shape. It is designed to work today with current LLMs through a short system-prompt primer and to evolve later toward tooling, benchmark validation, and native model/tokenizer support.

The name intentionally echoes TCP/IP: the goal is boring, unowned infrastructure — a small standard, not a product.

**Status:** Draft for community feedback. Empirical benchmarks pending.

## Table of contents

- [Quick start](#quick-start)
- [Scope](#scope)
- [Why TCP/AI](#why-tcpai)
- [Design principles](#design-principles)
- [Compression rules](#compression-rules)
- [Marker system](#marker-system)
- [Worked examples](#worked-examples)
- [Edge cases](#edge-cases)
- [Related work and adjacent formats](#related-work-and-adjacent-formats)
- [Maturity levels](#maturity-levels)
- [Reserved namespace](#reserved-namespace)
- [Non-goals](#non-goals)
- [FAQ](#faq)
- [System prompt primer](#system-prompt-primer)
- [Benchmark methodology](#benchmark-methodology)
- [Roadmap](#roadmap)
- [Open issues](#open-issues)

## Quick start

1. Copy [`primer/system-prompt.txt`](primer/system-prompt.txt) into your AI chat.
2. Write messages by:
   - dropping greetings, hedges, and self-narration;
   - keeping content words intact;
   - adding a leading marker for tone, such as `?`, `!`, `=`, `>`, or `~`;
   - adding a trailing marker for reply shape, such as `.b`, `.l`, `.rec`, `.why`, or `.ans`.
3. The AI replies in natural language, matching the modality and shape signaled.

Example:

```text
?.b how transformers work
```

instead of:

```text
Hi Claude, I was wondering if you could give me a quick explanation of how transformers work?
```

## Scope

TCP/AI is a **human-writable shorthand profile** for conversational LLM input. It is not a general-purpose data format, a tokenizer, or a model compression technique.

The practical aim for v0.x is simple:

```text
same user intent + fewer input tokens + no meaningful quality loss
```

## Why TCP/AI

Natural English contains redundancy that helps humans maintain warmth, politeness, and conversational flow. In LLM input, much of that scaffolding costs tokens without materially changing the answer.

Ad hoc concise prompting already works, but it varies wildly by user. A shared profile enables:

- repeatable examples;
- tokenizer-aware tooling;
- benchmarkable claims;
- auto-compressors and linters;
- future model or tokenizer support;
- interoperability with structured-data formats and agent systems.

TCP/AI avoids meta-prompting such as "compress this prompt and then answer it," because that costs extra tokens and adds latency before the real request begins.

## Design principles

1. **Tokenizer-friendly, not character-friendly.** Preserve whole words. Vowel-dropping, camel-mashing, and symbol soup often tokenize worse.
2. **Drop scaffolding, keep skeleton.** Remove greetings, hedges, filler, and self-narration. Keep content words, constraints, and load-bearing modality.
3. **Asymmetric.** Humans may compress input; AI replies in normal natural language.
4. **Meaning-safe.** Negation, quantifiers, technical terms, names, identifiers, paths, URLs, numbers, and units survive compression.
5. **Round-trip-safe.** A compression that causes a clarification question may cost more tokens than it saves.
6. **Readable first.** TCP/AI should remain readable by humans without a decoder ring. We are not building prompt Klingon. Yet.

## Compression rules

### Tier 1 — Always drop when safe

- Greetings and sign-offs: "Hi Claude," / "Thanks!"
- Self-narration: "I'm trying to..." / "I was wondering if..." / "Can you help me..."
- Hedges: "kind of" / "sort of" / "I think maybe" / "just" / "basically"
- Meta-restatement: "As you know" / "To clarify my question"

### Tier 2 — Drop when unambiguous

- Articles: `the`, `a`, `an`
- Complementizer `that`: "I think that X" → "I think X"
- Auxiliary `do/does` in questions: "How does X work" → "How X work"
- Full sentences → fragments when context remains clear

### Tier 3 — Substitute with common cheap equivalents

| Natural | TCP/AI |
|---|---|
| for example | `e.g.` |
| that is | `i.e.` |
| versus / compared to | `vs` |
| and | `&` |
| with | `w/` |
| without | `w/o` |
| leads to / produces | `→` |

Use substitutions only when they are readable and tokenizer-sensible.

### Tier 4 — Never compress

- Negations: `not`, `never`, `no`, `without`
- Quantifiers: `all`, `some`, `only`, `every`, `any`
- Technical terms
- Names, identifiers, file paths, URLs
- Numbers and units
- Code
- Verbatim quotes
- Anything where ambiguity could trigger a clarification round-trip

### Anti-patterns

- Vowel-dropping: `trnsfrmr`
- Camel-mashing: `ImTryng2cm`
- Symbol soup: `^>~@`
- Emoji-for-words
- Most txt-speak: `u`, `ur`, `2`, `4`

These may look short to humans but often tokenize poorly and reduce model reliability.

## Marker system

Markers restore tone and response-shape cues that compression removes.

### Modality markers

| Marker | Meaning | Replaces |
|---|---|---|
| `?` | curious / open-ended | "I was wondering..." |
| `!` | urgent / important | "This is important..." |
| `~` | casual / brainstorming | "Just thinking out loud..." |
| `=` | precise / definitive answer wanted | "I need the exact..." |
| `>` | skeptical / push back | "I'm not convinced..." |
| `+` | follow-up / continue prior | "Building on that..." |
| `*` | personally important | "This matters because..." |

### Response-shape markers

| Marker | Meaning | Replaces |
|---|---|---|
| `.b` | brief, 1–3 sentences | "Quick answer..." |
| `.m` | medium/default | default response |
| `.l` | long/full treatment | "Go in depth..." |
| `.opt` | options, do not pick | "What are my choices..." |
| `.rec` | recommendation | "What should I do..." |
| `.why` | show reasoning | "Walk me through..." |
| `.ans` | answer only | "Just tell me..." |
| `.blunt` | direct, less diplomacy | "Be honest..." |
| `.soft` | diplomatic framing | "Tactfully..." |

### Stacking

Markers combine left-to-right, with modality first and response shape second.

| TCP/AI | Meaning |
|---|---|
| `?.b` | curious + brief |
| `!=.ans` | urgent + precise + answer only |
| `>.blunt` | skeptical + blunt |
| `~.opt` | casual + options |

## Worked examples

Token-reduction figures are heuristic until benchmarked.

| Natural | TCP/AI | Est. reduction |
|---|---|---|
| "Hi Claude, I was wondering if you could help me understand how transformers work?" | `? how transformers work` | ~70% |
| "Could you please write me a Python function that takes a list and returns the unique values, preserving order?" | `=Python fn: list → unique values, preserve order` | ~45% |
| "I'm trying to figure out the difference between supervised and unsupervised learning. Can you give me a quick breakdown?" | `?.b supervised vs unsupervised learning` | ~70% |
| "I'm not really sure about this, but it seems like maybe transformers might be overrated for small datasets?" | `> transformers overrated small datasets` | ~65% |
| "Can you give me a quick brainstorm of names for a coffee shop with a vintage aesthetic?" | `~.opt coffee shop names, vintage aesthetic` | ~55% |
| "I need you to be really direct with me — is my business plan actually viable or am I fooling myself?" | `=.blunt business plan viable, or fooling myself?` | ~55% |

More examples live in [`EXAMPLES.md`](EXAMPLES.md).

## Edge cases

### Code blocks

Code is never compressed. Compress only prose around it.

````text
=.b fix bug in fn:
```python
def add(a, b): return a - b
```
````

### Quotes

Verbatim quotes are never compressed. The reader needs the original text intact.

### Multi-paragraph messages

Markers apply to the whole message. For different modalities, prefer separate messages.

### Mixed natural + TCP/AI

Allowed. Users can mix normal language and TCP/AI shorthand when precision matters.

### Names, identifiers, file paths, URLs

Never compressed. Treat as opaque tokens.

### Negation

Always preserved literally.

```text
not viable ≠ viable
```

### Numbers and units

Preserve as-is unless the original already used an abbreviation.

### Languages other than English

v0.3 is English-only. Per-language variants need separate function-word and marker testing.

## Related work and adjacent formats

TCP/AI belongs to a broader token-efficiency landscape, but it targets a specific lane: human-authored conversational input.

- **TOON** optimizes JSON-like structured data for LLM prompts. TCP/AI should interoperate with TOON rather than compete with it.
- **JSON compact, YAML, XML, and CSV** remain required baselines for structured-data benchmarks.
- **LLMLingua, LongLLMLingua, and LLMLingua-2** are algorithmic prompt-compression systems. They are important benchmark comparators, but their compressed prompts are generally machine-generated rather than manually writable.
- **Selective Context, gist tokens, soft prompts, and prompt tuning** are adjacent approaches for context pruning or learned/native prompt compression.

TCP/AI should not claim to invent prompt compression. Its claim is narrower: a readable, manually writable, tokenizer-aware shorthand convention for user-side conversational prompts.

## Maturity levels

| Level | Name | Meaning |
|---|---|---|
| L0 | Informal shorthand | User writes concise fragments without a formal primer. |
| L1 | Primer-aware TCP/AI | Model is given the system prompt primer and interprets markers. |
| L2 | Tool-assisted TCP/AI | A compressor or linter validates shorthand against tokenizers. |
| L3 | Benchmark-validated TCP/AI | Compression, quality, marker fidelity, and clarification-rate benchmarks are published. |
| L4 | Native TCP/AI support | Models/tokenizers understand TCP/AI markers and merges directly. |

## Reserved namespace

To preserve future compatibility:

- Leading single-character markers are reserved for TCP/AI core modality markers.
- Dot-suffix markers are reserved for response shape and register.
- Slash markers are reserved for future domain packs.
- Double-colon `::` is reserved for explicit field labels.

## Non-goals

TCP/AI is not:

- a replacement for natural language;
- a compression scheme for AI output;
- a new tokenizer;
- a model fine-tune;
- a v0.x protocol for agent-to-agent communication;
- a solution for already-dense technical input;
- a claim that compression always improves quality.

## FAQ

### Won't models misread compressed input?

Sometimes, if compression is too aggressive. That is why TCP/AI keeps load-bearing terms and uses markers. Benchmarking should measure misread and clarification rates.

### Is this just prompt engineering?

It overlaps with prompt engineering, but the goal is standardization: shared rules, examples, tooling, and benchmarks.

### Why bother if tokens are getting cheaper?

Cost is only one axis. Context window, latency, and retrieved-context capacity still matter.

### Why not let the model compress prompts?

Meta-prompting costs tokens and adds latency. TCP/AI compresses before the request reaches the model.

### What happens when compression fails?

Move that pattern to Tier 4 or document a safer form. The standard should evolve from failures, not hand-wave them away.

### Is this compatible with TOON?

Yes. TCP/AI can compress the human instruction around a TOON payload. TOON and TCP/AI solve different problems.

## System prompt primer

```text
The user may write in TCP/AI — a compressed shorthand. Rules:
- Greetings, self-narration, hedges, and articles may be dropped.
- "&" = and, "w/" = with, "w/o" = without, "vs" = versus, "→" = leads to / produces.
- Leading modality markers set tone: ? curious, ! urgent, ~ casual, = precise, > skeptical, + follow-up, * personal.
- Trailing shape markers set reply form: .b brief, .l long, .opt options, .rec recommend, .why show reasoning, .ans answer only, .blunt direct, .soft diplomatic.
- Stack markers (e.g. ?.b = curious + brief, !=.ans = urgent + precise + answer only).
- Negations and quantifiers are never dropped — read them literally.
- Reply in natural language, matching the modality and shape the user signaled.
```

## Benchmark methodology

See [`BENCHMARKS.md`](BENCHMARKS.md) for the full benchmark plan.

Minimum benchmark tracks:

1. token reduction;
2. quality preservation;
3. round-trip safety;
4. marker fidelity;
5. structured-data compression, including TOON;
6. algorithmic prompt-compression comparison.

## Roadmap

| Version | Mechanism | Expected savings | Status |
|---|---|---|---|
| v0 | concise prompting / informal shorthand | 30–40%* | works today |
| v1 | system-prompt primer | 40–50%* | works today |
| v2 | tooling / linter / auto-compressor | 45–60%* | future |
| v3 | tokenizer-aware merges | 60–70%* | requires tokenizer support |
| v4 | bidirectional / agent-to-agent | 70%+* | future research |

\* Estimates pending benchmark data.

## Open issues

1. Empirical token reduction.
2. Quality preservation.
3. Clarification-rate delta.
4. Marker collisions.
5. Multilingual extension.
6. Standardization vs flexibility.
7. Auto-compressor UX.
8. Compatibility with XML-style prompts, function-calling JSON, TOON, and agent tool results.
9. Formal grammar for a future TCS — Token Compression Spec.
10. Domain packs such as TCP/AI-Code, TCP/AI-Architecture, TCP/AI-Legal, and TCP/AI-Med.
