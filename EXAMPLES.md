# TCP/AI Examples

This file expands the worked examples from the specification. Examples are provisional until empirical benchmarks replace heuristic estimates.

## Reading markers

| Marker | Meaning |
|---|---|
| `?` | curious / open-ended |
| `!` | urgent / important |
| `~` | casual / brainstorming |
| `=` | precise / definitive |
| `>` | skeptical / push back |
| `+` | follow-up / continue prior |
| `*` | personally important |
| `.b` | brief |
| `.l` | long / full treatment |
| `.opt` | options |
| `.rec` | recommendation |
| `.why` | show reasoning |
| `.ans` | answer only |
| `.blunt` | direct |
| `.soft` | diplomatic |

## General Q&A

| Natural | TCP/AI |
|---|---|
| Hi Claude, I was wondering if you could help me understand how transformers work? | `? how transformers work` |
| Could you give me a quick breakdown of supervised versus unsupervised learning? | `?.b supervised vs unsupervised learning` |
| Walk me through your reasoning on why GPUs beat CPUs for deep learning, in detail. | `.l.why GPU vs CPU deep learning` |
| I am not convinced that transformers are always the right choice for small datasets. | `> transformers not always right choice small datasets` |

## Writing and editing

| Natural | TCP/AI |
|---|---|
| Please rewrite this so it sounds professional but not too stiff. | `=.soft rewrite professional, not stiff:` |
| Can you make this more concise while preserving the meaning? | `=.b tighten, preserve meaning:` |
| I need a blunt critique of this proposal. | `>.blunt critique proposal:` |
| Give me three options for a title. | `.opt 3 title options:` |

## Code and technical work

Code blocks are not compressed. Only the prose wrapper is compressed.

````text
=.b fix bug in fn:
```python
def add(a, b):
    return a - b
```
````

| Natural | TCP/AI |
|---|---|
| Could you please write me a Python function that takes a list and returns the unique values, preserving order? | `=Python fn: list → unique values, preserve order` |
| Can you review this TypeScript error and tell me the likely root cause? | `=.why review TS error, likely root cause:` |
| Give me a test plan for this change. | `=test plan for change:` |
| I need the shortest safe fix, not a full refactor. | `=.ans shortest safe fix, not full refactor` |

## Architecture and planning

| Natural | TCP/AI |
|---|---|
| Help me compare these two architecture options and recommend one. | `=.rec compare architecture options:` |
| Give me options, but do not pick yet. | `.opt options only, do not pick:` |
| I want a direct answer on whether this is over-engineered. | `=.blunt over-engineered?` |
| Build a phased implementation plan. | `=phased implementation plan:` |

## Structured data pairing

TCP/AI can wrap structured data formats. For structured payloads, compare TOON, compact JSON, YAML, CSV, and XML in benchmarks.

```text
=.why analyze churn drivers using TOON payload:
<toon>
customers[3]{id,plan,months,churned}:
  c1,basic,2,true
  c2,pro,18,false
  c3,basic,4,true
</toon>
```

## Safety rules in examples

Do not compress away:

- `not`, `never`, `no`, `without`
- `all`, `some`, `only`, `every`, `any`
- names, identifiers, file paths, URLs
- numbers and units
- quoted source text
- code

Bad:

```text
viable business plan?
```

Better:

```text
=.blunt business plan not viable?
```

The negation is load-bearing. Dropping it reverses the question. Tiny little footgun. Classic.
