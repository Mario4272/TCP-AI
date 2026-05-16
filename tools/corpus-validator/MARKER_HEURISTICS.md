# Marker-Detection Heuristics

The TCP/AI corpus validator employs both strict validation and conservative heuristic warnings to ensure the integrity of prompt pairs.

## 1. Strict Validation
The validator strictly enforces that the `markers` array in each JSONL record contains only valid TCP/AI v0.3 markers:
`?`, `!`, `~`, `=`, `>`, `+`, `*`, `.b`, `.m`, `.l`, `.opt`, `.rec`, `.why`, `.ans`, `.blunt`, `.soft`

## 2. Heuristic Warning Logic
To help catch missing declarations, the validator identifies **apparent markers** in the `tcp_prompt` text and compares them against the `markers` array. If an apparent marker is found in the text but not declared in the array, a warning is emitted.

## 3. Conservative Detection Rules
Because single-character markers can appear naturally as punctuation in natural language or code, the validator uses conservative rules to avoid false positives:

### Single-Character Markers (`?`, `!`, `~`, `=`, `>`, `+`, `*`)
A single-character marker is only flagged as an "apparent marker" if it appears as a **standalone token** at the **beginning or end** of the `tcp_prompt` string.

Inline standalone punctuation-like tokens are intentionally ignored to reduce false positives. For example, `Next.js + NestJS` and `1 + 1 = 2` do not trigger marker-mismatch warnings.

### Multi-Character Markers (`.b`, `.ans`, etc.)
These markers are more specific and are flagged as apparent markers whenever they appear as standalone tokens anywhere in the `tcp_prompt`.

## 4. Exclusion Examples (Valid Usage)
The following common patterns are **intentionally excluded** from warnings to reduce noise:

- **Technology Operands**: `Next.js + NestJS` (The `+` is not a standalone token at the start/end).
- **Mathematical Operators**: `1 + 1 = 2` (Inside the prompt text, these are treated as content).
- **Punctuation in context**: Parentheses `(like this)` or quotes `"this"` are allowed for clarity in the shorthand and do not trigger marker-mismatch warnings.

## 5. Best Practices
- **Explicit Declaration**: Always include all used markers in the `markers` array.
- **Spacing**: Use spaces to separate markers from prompt text to ensure the validator (and future automated parsers) can distinguish them clearly.
- **Punctuation**: Favor parentheses `()` for providing conversational context that is not a functional TCP/AI marker.
