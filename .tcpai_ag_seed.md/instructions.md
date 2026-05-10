AG — process update for TCP-AI.

Before proceeding with Phase 1 implementation, update your operating process for this repo.

You must follow the standard Mario + Val development workflow used in prior projects.

Reference operating contract:
Use the attached AG safety/process seed as binding guidance. Key rules include:
- Mario is final authority.
- Val and Mario both provide instructions.
- If instructions conflict, ask to resolve.
- Read all instructions fully before acting.
- Translate work into explicit ordered tasks before changing files.
- Make only requested changes.
- Keep diffs minimal and scoped.
- Do not assume missing details.
- If ambiguous, risky, or irreversible: STOP and ASK.
- Do not run destructive commands.
- Do not touch anything outside the repo root.
- Do not bypass tests/checks or fake success.

Project tracking convention:
Create a repo-local project tracking structure:

.project_tracking/
  implementation_plans/
  walkthroughs/

Phase naming convention:
Use zero-padded phase identifiers:

phase_0001
phase_0002
phase_0003
...

For every phase, create both:

.project_tracking/implementation_plans/implementation_plan_phase_####.md
.project_tracking/walkthroughs/walkthrough_phase_####.md

For this current work, use:

phase_0001

Phase 0001 files should be:

.project_tracking/implementation_plans/implementation_plan_phase_0001.md
.project_tracking/walkthroughs/walkthrough_phase_0001.md

Implementation plan process:
1. Before making implementation changes, create the implementation plan file for the phase.
2. The plan must include:
   - phase name and number
   - goal
   - scope
   - files proposed for creation
   - files proposed for modification
   - ordered task list
   - verification plan
   - risks / open questions
   - explicit “awaiting approval” note
3. After creating the implementation plan, STOP.
4. Wait for Mario/Val review and approval.
5. Do not implement until approved.

Walkthrough process:
After the approved implementation is complete, create the walkthrough file for the phase.

The walkthrough must include:
- phase name and number
- summary of completed work
- files created
- files modified
- commands run
- verification results
- intentionally deferred items
- risks / follow-ups
- git status / diff summary

Important:
The implementation plan and walkthrough must live under:

.project_tracking/implementation_plans/
.project_tracking/walkthroughs/

Do not place phase plans only at the repo root going forward.

Current Phase 1 instruction:
Convert the existing Phase 1 plan into:

.project_tracking/implementation_plans/implementation_plan_phase_0001.md

Then stop and report that the plan is ready for review.

Do not implement the Phase 1 repo hardening changes yet.