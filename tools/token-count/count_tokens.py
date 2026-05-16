import argparse
import csv
import json
import pathlib
import statistics
import sys
import tiktoken

def calculate_reduction_percent(natural, tcp):
    if natural == 0:
        return 0.0
    return ((natural - tcp) / natural) * 100

def main():
    parser = argparse.ArgumentParser(description="Count tokens for TCP/AI prompt corpus")
    parser.add_argument("--input", required=True, help="Path to input JSONL corpus")
    parser.add_argument("--output", required=True, help="Path to output CSV")
    parser.add_argument("--tokenizer", default="o200k_base", help="Tokenizer(s) to use (comma-separated or 'all')")
    args = parser.parse_args()

    if args.tokenizer == "all":
        tokenizer_names = ["o200k_base", "cl100k_base"]
    else:
        raw_names = args.tokenizer.split(",")
        tokenizer_names = [name.strip() for name in raw_names]
        if any(not name for name in tokenizer_names):
            print("Error: Empty tokenizer name in comma-separated --tokenizer value.", file=sys.stderr)
            sys.exit(1)

    encodings = {}
    for name in tokenizer_names:
        try:
            encodings[name] = tiktoken.get_encoding(name)
        except ValueError as e:
            print(f"Error getting encoding for '{name}': {e}", file=sys.stderr)
            sys.exit(1)

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

                # Validate required fields
                required_fields = ["id", "category", "natural_prompt", "tcp_prompt"]
                for field in required_fields:
                    if field not in record:
                        print(f"Missing required field '{field}' on line {line_no}", file=sys.stderr)
                        sys.exit(1)

                for name, encoding in encodings.items():
                    nat_tokens = len(encoding.encode(record["natural_prompt"]))
                    tcp_tokens = len(encoding.encode(record["tcp_prompt"]))
                    saved = nat_tokens - tcp_tokens
                    reduction_pct = calculate_reduction_percent(nat_tokens, tcp_tokens)

                    reductions.append(reduction_pct)
                    
                    results.append({
                        "id": record["id"],
                        "category": record["category"],
                        "tokenizer": name,
                        "natural_tokens": nat_tokens,
                        "tcp_tokens": tcp_tokens,
                        "tokens_saved": saved,
                        "token_reduction_percent": f"{reduction_pct:.2f}"
                    })
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

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

    total_rows = len(results)
    if total_rows > 0:
        mean_reduction = statistics.mean(reductions)
        median_reduction = statistics.median(reductions)
        min_reduction = min(reductions)
        max_reduction = max(reductions)

        print("=== TCP/AI Token Count Summary ===")
        print(f"Input Records:    {len(results) // len(tokenizer_names)}")
        print(f"Tokenizers:       {', '.join(tokenizer_names)}")
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
