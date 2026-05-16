import argparse
import collections
import json
import sys

VALID_CATEGORIES = {
    "general_qna",
    "brief_explanation",
    "technical_explanation",
    "coding_request",
    "debugging_request",
    "writing_editing",
    "brainstorming",
    "architecture",
    "decision_recommendation",
    "skeptical_review",
    "personal_important",
    "structured_data_wrapper"
}

VALID_MARKERS = {
    "?", "!", "~", "=", ">", "+", "*", ".b", ".m", ".l", ".opt", ".rec", ".why", ".ans", ".blunt", ".soft"
}

REQUIRED_FIELDS = [
    "id", "category", "natural_prompt", "tcp_prompt", 
    "markers", "expected_response_shape", "risk_notes", "compression_notes"
]

def main():
    parser = argparse.ArgumentParser(description="Validate TCP/AI corpus JSONL")
    parser.add_argument("--input", required=True, help="Path to input JSONL corpus")
    parser.add_argument("--output", help="Path to save output report (prints to stdout if omitted)")
    args = parser.parse_args()

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
                missing_fields = [f for f in REQUIRED_FIELDS if f not in record]
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

                if category not in VALID_CATEGORIES:
                    errors.append(f"Line {line_no}: Invalid category '{category}'")
                category_counts[category] += 1

                if not isinstance(markers, list):
                    errors.append(f"Line {line_no}: 'markers' must be an array")
                else:
                    for m in markers:
                        if m not in VALID_MARKERS:
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
                            if token in VALID_MARKERS and token not in markers:
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
    for cat, count in category_counts.most_common():
        report_lines.append(f"  {cat}: {count}")
    
    report_lines.append("\n-- Marker Distribution --")
    for m, count in marker_counts.most_common():
        report_lines.append(f"  {m}: {count}")

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
