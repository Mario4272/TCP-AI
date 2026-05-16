import csv
import argparse
import sys
from collections import defaultdict

def calculate_metrics(rows):
    total_natural = sum(int(row['natural_tokens']) for row in rows)
    total_tcp = sum(int(row['tcp_tokens']) for row in rows)
    total_saved = sum(int(row['tokens_saved']) for row in rows)
    
    if total_natural == 0:
        overall_reduction = 0.0
    else:
        overall_reduction = (total_saved / total_natural) * 100
        
    reductions = [float(row['token_reduction_percent']) for row in rows]
    
    return {
        "count": len(rows),
        "total_natural": total_natural,
        "total_tcp": total_tcp,
        "total_saved": total_saved,
        "overall_reduction": overall_reduction,
        "mean_reduction": sum(reductions) / len(reductions) if reductions else 0.0,
        "median_reduction": sorted(reductions)[len(reductions)//2] if reductions else 0.0,
        "min_reduction": min(reductions) if reductions else 0.0,
        "max_reduction": max(reductions) if reductions else 0.0
    }

def format_markdown(summary, category_summaries, tokenizer_summaries, corpus_info):
    lines = []
    lines.append("# TCP/AI Benchmark Summary Report")
    lines.append("")
    lines.append("## 1. Dataset Information")
    lines.append(f"- **Corpus**: `{corpus_info['path']}`")
    lines.append(f"- **Unique Prompt Records**: {corpus_info['record_count']}")
    lines.append(f"- **Total Tokenizer Samples**: {summary['count']}")
    lines.append(f"- **Categories**: {len(category_summaries)}")
    lines.append("")
    
    lines.append("## 2. Overall Performance")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Total Natural Tokens | {summary['total_natural']} |")
    lines.append(f"| Total TCP/AI Tokens | {summary['total_tcp']} |")
    lines.append(f"| Total Tokens Saved | {summary['total_saved']} |")
    lines.append(f"| Overall Reduction % | {summary['overall_reduction']:.2f}% |")
    lines.append(f"| Mean Reduction % | {summary['mean_reduction']:.2f}% |")
    lines.append(f"| Median Reduction % | {summary['median_reduction']:.2f}% |")
    lines.append(f"| Min Reduction % | {summary['min_reduction']:.2f}% |")
    lines.append(f"| Max Reduction % | {summary['max_reduction']:.2f}% |")
    lines.append("")
    
    lines.append("## 3. Performance by Tokenizer")
    lines.append("| Tokenizer | Mean Reduction | Min | Max | Overall Reduction |")
    lines.append("|---|---|---|---|---|")
    for tok in sorted(tokenizer_summaries.keys()):
        s = tokenizer_summaries[tok]
        lines.append(f"| `{tok}` | {s['mean_reduction']:.2f}% | {s['min_reduction']:.2f}% | {s['max_reduction']:.2f}% | {s['overall_reduction']:.2f}% |")
    lines.append("")
    
    lines.append("## 4. Performance by Category")
    lines.append("| Category | Samples | Mean Reduction | Min | Max | Total Saved |")
    lines.append("|---|---|---|---|---|---|")
    for cat in sorted(category_summaries.keys()):
        s = category_summaries[cat]
        lines.append(f"| `{cat}` | {s['count']} | {s['mean_reduction']:.2f}% | {s['min_reduction']:.2f}% | {s['max_reduction']:.2f}% | {s['total_saved']} |")
    lines.append("")

    lines.append("## 5. Benchmark Limitations")
    lines.append("- **Semantic Fidelity**: This benchmark measures token reduction only, not meaning preservation.")
    lines.append("- **Synthetic Data**: The corpus is 100% synthetic for privacy and safety.")
    lines.append("- **Limited Scope**: The 100-record seed represents a narrow subset of real-world conversational variety.")
    lines.append("")

    lines.append("## 6. Safe vs. Unsafe Claims")
    lines.append("- **Safe**: \"TCP/AI v0.2 shows ~40% token reduction on this 100-record synthetic baseline.\"")
    lines.append("- **Unsafe**: \"TCP/AI preserves meaning perfectly for all workloads.\"")
    lines.append("")
    
    lines.append("## 7. Implementation Notes")
    lines.append("- This report was generated automatically by `tools/benchmark-report/summarize_token_counts.py`.")
    lines.append("- All metrics are derived from token-count samples in `benchmarks/results/`.")
    lines.append("") # Final newline
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Summarize TCP/AI token-count benchmarks.")
    parser.add_argument("--input", required=True, help="Input CSV file from count_tokens.py")
    parser.add_argument("--output", help="Optional output Markdown file")
    args = parser.parse_args()
    
    rows = []
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except Exception as e:
        print(f"Error reading {args.input}: {e}", file=sys.stderr)
        sys.exit(1)
        
    if not rows:
        print("No data found in input file.", file=sys.stderr)
        sys.exit(1)
        
    # Grouping
    by_tokenizer = defaultdict(list)
    by_category = defaultdict(list)
    unique_ids = set()
    
    for row in rows:
        by_tokenizer[row['tokenizer']].append(row)
        by_category[row['category']].append(row)
        unique_ids.add(row['id'])
        
    # Summaries
    overall = calculate_metrics(rows)
    tokenizer_summaries = {tok: calculate_metrics(r) for tok, r in by_tokenizer.items()}
    category_summaries = {cat: calculate_metrics(r) for cat, r in by_category.items()}
    
    corpus_info = {
        "path": "corpus/seed/prompts_v0.2.jsonl", # Hardcoded for now as per phase requirements
        "record_count": len(unique_ids)
    }
    
    # Text Output
    print("=== TCP/AI Benchmark Summary ===")
    print(f"Unique Records: {corpus_info['record_count']}")
    print(f"Tokenizers:     {', '.join(sorted(tokenizer_summaries.keys()))}")
    print(f"Overall Reduction: {overall['overall_reduction']:.2f}%")
    print(f"Mean Reduction:    {overall['mean_reduction']:.2f}%")
    print(f"Median Reduction:  {overall['median_reduction']:.2f}%")
    print(f"Min/Max:           {overall['min_reduction']:.2f}% / {overall['max_reduction']:.2f}%")
    
    if args.output:
        md_content = format_markdown(overall, category_summaries, tokenizer_summaries, corpus_info)
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(md_content)
            print(f"Markdown report saved to: {args.output}")
        except Exception as e:
            print(f"Error writing to {args.output}: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
