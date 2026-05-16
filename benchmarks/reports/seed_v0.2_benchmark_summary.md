# TCP/AI Benchmark Summary Report

## 1. Dataset Information
- **Corpus**: `corpus/seed/prompts_v0.2.jsonl`
- **Unique Prompt Records**: 100
- **Tokenizers**: `o200k_base`, `cl100k_base`
- **Total Tokenizer Samples**: 200
- **Categories**: 12

## 2. Overall Performance
| Metric | Value |
|---|---|
| Total Natural Tokens | 3342 |
| Total TCP/AI Tokens | 1920 |
| Total Tokens Saved | 1422 |
| Overall Reduction % | 42.55% |
| Mean Reduction % | 40.82% |
| Median Reduction % | 40.00% |
| Min Reduction % | 6.25% |
| Max Reduction % | 76.00% |

## 3. Performance by Tokenizer
| Tokenizer | Mean Reduction | Min | Max | Overall Reduction |
|---|---|---|---|---|
| `o200k_base` | 40.44% | 6.25% | 72.00% | 42.23% |
| `cl100k_base` | 41.20% | 6.25% | 76.00% | 42.87% |

## 4. Performance by Category
| Category | Records | Samples | Mean Reduction | Min | Max | Total Saved |
|---|---|---|---|---|---|---|
| `architecture` | 8 | 16 | 34.69% | 19.05% | 46.67% | 91 |
| `brainstorming` | 8 | 16 | 47.33% | 26.67% | 62.50% | 122 |
| `brief_explanation` | 8 | 16 | 53.37% | 30.00% | 76.00% | 132 |
| `coding_request` | 9 | 18 | 47.59% | 30.77% | 66.67% | 191 |
| `debugging_request` | 9 | 18 | 41.05% | 12.50% | 60.71% | 165 |
| `decision_recommendation` | 8 | 16 | 46.65% | 26.67% | 61.11% | 126 |
| `general_qna` | 8 | 16 | 44.29% | 6.25% | 70.00% | 124 |
| `personal_important` | 8 | 16 | 38.55% | 26.67% | 70.00% | 100 |
| `skeptical_review` | 8 | 16 | 35.64% | 12.50% | 61.90% | 93 |
| `structured_data_wrapper` | 9 | 18 | 32.25% | 14.29% | 50.00% | 86 |
| `technical_explanation` | 9 | 18 | 42.93% | 14.29% | 70.00% | 134 |
| `writing_editing` | 8 | 16 | 25.40% | 7.14% | 46.67% | 58 |

## 5. Benchmark Limitations
- **Semantic Fidelity**: This benchmark measures token reduction only, not meaning preservation.
- **Synthetic Data**: The corpus is 100% synthetic for privacy and safety.
- **Limited Scope**: The 100-record seed represents a narrow subset of real-world conversational variety.

## 6. Safe vs. Unsafe Claims
- **Safe**: "TCP/AI v0.2 shows ~40% token reduction on this 100-record synthetic baseline."
- **Unsafe**: "TCP/AI preserves meaning perfectly for all workloads."

## 7. Implementation Notes
- This report was generated automatically by `tools/benchmark-report/summarize_token_counts.py`.
- All metrics are derived from token-count samples in `benchmarks/results/`.
