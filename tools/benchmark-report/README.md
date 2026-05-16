# TCP/AI Benchmark Reporting Tool

This tool generates summary reports from the token-count CSV files produced by `tools/token-count/count_tokens.py`.

## Usage

### Basic Summary
To see a text summary in the console:
```bash
python tools/benchmark-report/summarize_token_counts.py --input benchmarks/results/seed_v0.2_token_counts.multi.sample.csv
```

### Markdown Report
To generate a formatted Markdown report:
```bash
python tools/benchmark-report/summarize_token_counts.py \
  --input benchmarks/results/seed_v0.2_token_counts.multi.sample.csv \
  --output benchmarks/reports/seed_v0.2_benchmark_summary.md
```

## Metrics
- **Mean Reduction**: Average of the reduction percentages for each record.
- **Median Reduction**: The middle value of the reduction percentages.
- **Overall Reduction**: Calculated as `(total_tokens_saved / total_natural_tokens) * 100`.
- **Min/Max**: The range of compression observed across the dataset.

## Requirements
- Python 3.x (Standard Library only)
