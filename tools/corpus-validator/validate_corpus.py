import argparse
import collections
import json
import pathlib
import sys

def load_spec(spec_path):
    try:
        with open(spec_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Spec file not found at {spec_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in spec file {spec_path} - {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Validate TCP/AI corpus JSONL")
    parser.add_argument("--input", required=True, help="Path to input JSONL corpus")
    parser.add_argument("--output", help="Path to save output report (prints to stdout if omitted)")
    parser.add_argument("--spec", help="Path to TCP/AI spec JSON (default: spec/tcpai-v0.3.json)")
    args = parser.parse_args()

    # Resolve spec path
    if args.spec:
        spec_path = pathlib.Path(args.spec)
    else:
        # Default to spec/tcpai-v0.3.json relative to repo root
        # Script is in tools/corpus-validator/validate_corpus.py
        # Root is ../../
        script_dir = pathlib.Path(__file__).parent
        spec_path = script_dir.parent.parent / "spec" / "tcpai-v0.3.json"

    spec = load_spec(spec_path)
    
    # Core spec validation
    if not isinstance(spec.get("version"), str):
        print(f"Error: Spec file {spec_path} is missing a 'version' string.", file=sys.stderr)
        sys.exit(1)
    if not isinstance(spec.get("markers"), dict):
        print(f"Error: Spec file {spec_path} is missing a 'markers' object.", file=sys.stderr)
        sys.exit(1)
    if not isinstance(spec.get("categories"), dict):
        print(f"Error: Spec file {spec_path} is missing a 'categories' object.", file=sys.stderr)
        sys.exit(1)
    if not isinstance(spec.get("corpus_schema"), dict) or not isinstance(spec["corpus_schema"].get("required_fields"), list):
        print(f"Error: Spec file {spec_path} is missing a valid 'corpus_schema.required_fields' array.", file=sys.stderr)
        sys.exit(1)

    valid_categories = set(spec.get("categories", {}).keys())
    valid_markers = set(spec.get("markers", {}).keys())
    required_fields = spec.get("corpus_schema", {}).get("required_fields", [])

    errors = []
    warnings = []
    
    seen_ids = set()
    category_counts = collections.Counter()
    marker_counts = collections.Counter()
    total_records = 0

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                if not line.strip():
                    continue
                total_records += 1
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    errors.append(f"Line {line_no}: Invalid JSON - {e}")
                    continue
                
                # Check required fields
                missing_fields = [f for f in required_fields if f not in record]
                if missing_fields:
                    errors.append(f"Line {line_no}: Missing required fields: {', '.join(missing_fields)}")
                    continue
                
                rec_id = record.get("id")
                category = record.get("category")
                natural_prompt = record.get("natural_prompt")
                tcp_prompt = record.get("tcp_prompt")
                markers = record.get("markers")

                if rec_id in seen_ids:
                    errors.append(f"Line {line_no}: Duplicate ID '{rec_id}'")
                seen_ids.add(rec_id)

                if category not in valid_categories:
                    errors.append(f"Line {line_no}: Invalid category '{category}'")
                category_counts[category] += 1

                if not isinstance(markers, list):
                    errors.append(f"Line {line_no}: 'markers' must be an array")
                else:
                    for m in markers:
                        if m not in valid_markers:
                            errors.append(f"Line {line_no}: Invalid marker '{m}'")
                        marker_counts[m] += 1
                    
                    # Warnings checks
                    if tcp_prompt and isinstance(tcp_prompt, str):
                        for m in markers:
                            if m not in tcp_prompt:
                                warnings.append(f"Line {line_no}: Declared marker '{m}' not visibly found in tcp_prompt string.")
                        
                        # Find apparent markers in tcp_prompt
                        tokens = tcp_prompt.split()
                        for i, token in enumerate(tokens):
                            if token in valid_markers and token not in markers:
                                # Be conservative with single-char punctuation-like markers
                                if len(token) == 1 and token in {"?", "!", "~", "=", ">", "+", "*"}:
                                    if i == 0 or i == len(tokens) - 1:
                                        warnings.append(f"Line {line_no}: Apparent marker '{token}' in tcp_prompt but not in markers array.")
                                else:
                                    warnings.append(f"Line {line_no}: Apparent marker '{token}' in tcp_prompt but not in markers array.")
                
                if not isinstance(natural_prompt, str) or not natural_prompt.strip():
                    errors.append(f"Line {line_no}: 'natural_prompt' must be a non-empty string")
                if not isinstance(tcp_prompt, str) or not tcp_prompt.strip():
                    errors.append(f"Line {line_no}: 'tcp_prompt' must be a non-empty string")
                
                if isinstance(natural_prompt, str) and isinstance(tcp_prompt, str):
                    if len(tcp_prompt) > len(natural_prompt):
                        warnings.append(f"Line {line_no}: tcp_prompt ({len(tcp_prompt)} chars) is longer than natural_prompt ({len(natural_prompt)} chars).")

    except FileNotFoundError:
        print(f"Error: Could not open {args.input}")
        sys.exit(1)

    # Generate Report
    report_lines = []
    report_lines.append("=== TCP/AI Corpus Validation Report ===")
    report_lines.append(f"Total Records: {total_records}")
    report_lines.append(f"Errors Found:  {len(errors)}")
    report_lines.append(f"Warnings:      {len(warnings)}")
    report_lines.append(f"Final Status:  {'FAIL' if errors else 'PASS'}")
    
    report_lines.append("\n-- Category Distribution --")
    for cat in sorted(valid_categories):
        count = category_counts.get(cat, 0)
        percentage = (count / total_records * 100) if total_records > 0 else 0
        report_lines.append(f"  {cat}: {count} ({percentage:.2f}%)")
    
    report_lines.append("\n-- Marker Distribution --")
    # Sort markers by frequency (descending), then alphabetically
    sorted_markers = sorted(marker_counts.items(), key=lambda x: (-x[1], x[0]))
    for marker, count in sorted_markers:
        report_lines.append(f"  {marker}: {count}")

    if errors:
        report_lines.append("\n-- Errors --")
        for e in errors:
            report_lines.append(f"  [ERROR] {e}")

    if warnings:
        report_lines.append("\n-- Warnings --")
        for w in warnings:
            report_lines.append(f"  [WARN]  {w}")

    report_text = "\n".join(report_lines)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out_f:
            out_f.write(report_text + "\n")
        print(f"Validation complete. Report written to {args.output}")
        if errors:
            print("Status: FAIL (Errors encountered)")
        else:
            print("Status: PASS")
    else:
        print(report_text)

    if errors:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
