"""
TCP/AI token counter.

Supports:
  - tiktoken encodings (o200k_base, cl100k_base, etc.)
  - Optional local Hugging Face tokenizer files via --hf-tokenizer NAME=PATH
    Requires: pip install -r tools/token-count/requirements-hf.txt
"""
import argparse
import csv
import json
import pathlib
import statistics
import sys
import tiktoken
from dataclasses import dataclass
from typing import Callable


@dataclass
class TokenCounter:
    name: str
    family: str  # "tiktoken" or "hf-local"
    count: Callable[[str], int]


def load_tiktoken_counter(name: str) -> TokenCounter:
    try:
        enc = tiktoken.get_encoding(name)
    except ValueError as e:
        print(f"Error getting tiktoken encoding for '{name}': {e}", file=sys.stderr)
        sys.exit(1)
    return TokenCounter(name=name, family="tiktoken", count=lambda text: len(enc.encode(text)))


def load_hf_counter(label: str, path_str: str) -> TokenCounter:
    # Reject remote URLs
    if path_str.startswith("http://") or path_str.startswith("https://"):
        print(
            f"Error: Remote URLs are not supported for --hf-tokenizer. "
            f"Provide a local tokenizer.json path (got: '{path_str}').",
            file=sys.stderr,
        )
        sys.exit(1)

    path = pathlib.Path(path_str)

    if not path.exists():
        print(f"Error: Tokenizer file not found: '{path}'", file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f"Error: Tokenizer path is not a file: '{path}'", file=sys.stderr)
        sys.exit(1)
    if path.suffix.lower() != ".json":
        print(
            f"Error: Tokenizer path must have a .json extension (got: '{path}'). "
            "Provide a valid tokenizer.json file.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        from tokenizers import Tokenizer  # noqa: PLC0415
    except ImportError:
        print(
            "Error: The 'tokenizers' package is required for --hf-tokenizer support.\n"
            "Install it with: pip install -r tools/token-count/requirements-hf.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        tok = Tokenizer.from_file(str(path))
    except Exception as e:  # noqa: BLE001
        print(f"Error loading tokenizer from '{path}': {e}", file=sys.stderr)
        sys.exit(1)

    return TokenCounter(name=label, family="hf-local", count=lambda text: len(tok.encode(text).ids))


def parse_hf_tokenizer_arg(raw: str) -> tuple[str, str]:
    """Parse 'NAME=PATH' into (name, path). Exits on error."""
    if "=" not in raw:
        print(
            f"Error: --hf-tokenizer must be in NAME=PATH format (got: '{raw}').",
            file=sys.stderr,
        )
        sys.exit(1)
    name, _, path = raw.partition("=")
    name = name.strip()
    path = path.strip()
    if not name:
        print(f"Error: Empty tokenizer name in --hf-tokenizer '{raw}'.", file=sys.stderr)
        sys.exit(1)
    if not path:
        print(f"Error: Empty path in --hf-tokenizer '{raw}'.", file=sys.stderr)
        sys.exit(1)
    return name, path


def calculate_reduction_percent(natural, tcp):
    if natural == 0:
        return 0.0
    return ((natural - tcp) / natural) * 100


def main():
    parser = argparse.ArgumentParser(description="Count tokens for TCP/AI prompt corpus")
    parser.add_argument("--input", required=True, help="Path to input JSONL corpus")
    parser.add_argument("--output", required=True, help="Path to output CSV")
    parser.add_argument(
        "--tokenizer",
        default="o200k_base",
        help="tiktoken tokenizer(s) to use (comma-separated or 'all'). Default: o200k_base",
    )
    parser.add_argument(
        "--hf-tokenizer",
        action="append",
        metavar="NAME=PATH",
        dest="hf_tokenizers",
        default=[],
        help=(
            "Optional local Hugging Face tokenizer in NAME=PATH format. "
            "Repeatable. Requires: pip install -r tools/token-count/requirements-hf.txt"
        ),
    )
    args = parser.parse_args()

    # --- Build tiktoken counters ---
    if args.tokenizer == "all":
        tiktoken_names = ["o200k_base", "cl100k_base"]
    else:
        raw_names = args.tokenizer.split(",")
        tiktoken_names = [name.strip() for name in raw_names]
        if any(not name for name in tiktoken_names):
            print("Error: Empty tokenizer name in comma-separated --tokenizer value.", file=sys.stderr)
            sys.exit(1)

    counters: list[TokenCounter] = [load_tiktoken_counter(n) for n in tiktoken_names]

    # --- Build HF counters ---
    for raw in args.hf_tokenizers:
        label, path_str = parse_hf_tokenizer_arg(raw)
        counters.append(load_hf_counter(label, path_str))

    if not counters:
        print("Error: No tokenizers selected. Provide --tokenizer or --hf-tokenizer.", file=sys.stderr)
        sys.exit(1)

    # --- Process corpus ---
    results = []
    reductions = []

    try:
        with open(args.input, "r", encoding="utf-8") as infile:
            for line_no, line in enumerate(infile, 1):
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON on line {line_no}", file=sys.stderr)
                    sys.exit(1)

                required_fields = ["id", "category", "natural_prompt", "tcp_prompt"]
                for field in required_fields:
                    if field not in record:
                        print(f"Missing required field '{field}' on line {line_no}", file=sys.stderr)
                        sys.exit(1)

                for counter in counters:
                    nat_tokens = counter.count(record["natural_prompt"])
                    tcp_tokens = counter.count(record["tcp_prompt"])
                    saved = nat_tokens - tcp_tokens
                    reduction_pct = calculate_reduction_percent(nat_tokens, tcp_tokens)

                    reductions.append(reduction_pct)
                    results.append({
                        "id": record["id"],
                        "category": record["category"],
                        "tokenizer": counter.name,
                        "natural_tokens": nat_tokens,
                        "tcp_tokens": tcp_tokens,
                        "tokens_saved": saved,
                        "token_reduction_percent": f"{reduction_pct:.2f}",
                    })
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

    # --- Write CSV ---
    try:
        output_path = pathlib.Path(args.output)
        if output_path.parent:
            output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(args.output, "w", encoding="utf-8", newline="") as outfile:
            fieldnames = ["id", "category", "tokenizer", "natural_tokens", "tcp_tokens", "tokens_saved", "token_reduction_percent"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for res in results:
                writer.writerow(res)
    except OSError as e:
        print(f"Error writing to output file '{args.output}': {e}", file=sys.stderr)
        sys.exit(1)

    # --- Summary ---
    total_rows = len(results)
    n_counters = len(counters)
    if total_rows > 0:
        mean_reduction = statistics.mean(reductions)
        median_reduction = statistics.median(reductions)
        min_reduction = min(reductions)
        max_reduction = max(reductions)

        print("=== TCP/AI Token Count Summary ===")
        print(f"Input Records:    {total_rows // n_counters}")
        print(f"Tokenizers:       {', '.join(c.name for c in counters)}")
        print(f"Total CSV Rows:   {total_rows}")
        print(f"Mean Reduction:   {mean_reduction:.2f}%")
        print(f"Median Reduction: {median_reduction:.2f}%")
        print(f"Min Reduction:    {min_reduction:.2f}%")
        print(f"Max Reduction:    {max_reduction:.2f}%")
        print(f"Results saved to: {args.output}")
    else:
        print("No records processed.")


if __name__ == "__main__":
    main()
