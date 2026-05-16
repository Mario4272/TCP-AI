# TCP/AI Benchmark Summary Report

## 1. Dataset Information
- **Corpus**: `corpus/seed/prompts_v0.2.jsonl`
- **Records**: 100
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
| `cl100k_base` | 41.20% | 6.25% | 76.00% | 42.87% |
| `o200k_base` | 40.44% | 6.25% | 72.00% | 42.23% |

## 4. Performance by Category
| Category | Records | Mean Reduction | Min | Max |
|---|---|---|---|---|
| `architecture` | 16 | 34.69% | 19.05% | 46.67% |
| `brainstorming` | 16 | 47.33% | 26.67% | 62.50% |
| `brief_explanation` | 16 | 53.37% | 30.00% | 76.00% |
| `coding_request` | 18 | 47.59% | 30.77% | 66.67% |
| `debugging_request` | 18 | 41.05% | 12.50% | 60.71% |
| `decision_recommendation` | 16 | 46.65% | 26.67% | 61.11% |
| `general_qna` | 16 | 44.29% | 6.25% | 70.00% |
| `personal_important` | 16 | 38.55% | 26.67% | 70.00% |
| `skeptical_review` | 16 | 35.64% | 12.50% | 61.90% |
| `structured_data_wrapper` | 18 | 32.25% | 14.29% | 50.00% |
| `technical_explanation` | 18 | 42.93% | 14.29% | 70.00% |
| `writing_editing` | 16 | 25.40% | 7.14% | 46.67% |

## 5. Implementation Notes
- This report was generated automatically by `tools/benchmark-report/summarize_token_counts.py`.
- All metrics are derived from token-count samples in `benchmarks/results/`.