You are working in the TCP-AI repository.

Goal:
Prepare the repo for public-facing early collaboration and benchmark development without overbuilding implementation tooling yet.

Current project:
TCP/AI is an open shorthand profile for token-efficient human → AI communication. It is currently documentation/spec-first. The repo already contains README.md, SPEC.md, EXAMPLES.md, BENCHMARKS.md, primer/system-prompt.txt, CONTRIBUTING.md, CHANGELOG.md, and LICENSE.

Branch:
Create and work on a new branch:

git checkout -b phase-1-repo-hardening

Task:
Create an implementation plan first. Do not modify files until the plan is reviewed.

The implementation plan should cover:

1. Repo hygiene
   - Add .gitignore suitable for a documentation-first repo that may later contain Node/Python benchmark tooling.
   - Avoid adding heavy dependencies.
   - Avoid adding generated files.

2. Public collaboration structure
   - Add .github/ISSUE_TEMPLATE/bug_report.md
   - Add .github/ISSUE_TEMPLATE/spec_proposal.md
   - Add .github/ISSUE_TEMPLATE/benchmark_result.md
   - Add .github/PULL_REQUEST_TEMPLATE.md

3. Additional project docs
   - Add ROADMAP.md
   - Add GOVERNANCE.md
   - Add SECURITY.md or SECURITY-NOTES.md

4. Benchmark scaffolding
   - Add benchmarks/README.md describing where benchmark result files will live.
   - Add corpus/README.md describing future corpus structure.
   - Add corpus/schema.md describing the intended JSONL prompt-pair format.
   - Add tools/README.md explaining that tooling will come later and listing planned tools:
     - tokenizer counter
     - prompt pair validator
     - benchmark runner
     - TCP/AI linter
     - optional auto-compressor

5. README polish
   - Improve the README intro if needed.
   - Add a “Why this exists” section.
   - Add a “What TCP/AI is not” section.
   - Add a “Roadmap” pointer.
   - Do not make exaggerated benchmark claims.

Constraints:
- Keep the repo documentation-first.
- Do not implement actual benchmark scripts yet.
- Do not add npm, Python, Rust, or other project tooling unless clearly justified.
- Do not invent benchmark results.
- Do not claim TCP/AI is proven until benchmarks exist.
- Keep language clean, credible, and attractive to open-source contributors.
- Preserve the distinction:
  TCP/AI = human-writable conversational shorthand.
  TOON/TONL = structured data compression baselines.
  LLMLingua-family = algorithmic prompt compression baselines.

Deliverable:
Append a concise implementation plan to a new file named IMPLEMENTATION_PLAN_PHASE_1.md.

After writing the plan, stop and report:
- files proposed for creation
- files proposed for modification
- risks or open questions
- recommended next action

Do not implement the plan until approved.