---
name: review-to-release-workflow
description: Run a structured four-phase engineering workflow (discovery, implementation, verification, release-readiness) with Human in the Loop checkpoints and explicit go/no-go gates. Use this whenever the user asks for full codebase review before changes, wants QUESTIONS.md-driven implementation, requests validation against approved decisions, or needs a final release gate verdict (Ready, Ready with caveats, Not ready).
---

# Review to Release Workflow

## Purpose

Use this skill to run a complete engineering workflow from technical discovery through implementation, verification, and final release-readiness assessment.

This workflow is designed for situations where a project needs more than isolated code changes. It should be used when the goal is to understand the codebase first, clarify unresolved questions, implement only approved decisions, verify correctness, and then determine whether the result is actually ready for merge, handoff, staging, or production.

This skill coordinates a four-phase process:

1. Discovery
2. Implementation
3. Verification
4. Release Readiness

---

## When to use

Use this skill when the user wants to:

- review a codebase before making broad changes
- identify ambiguities, missing decisions, and technical risks
- generate a structured `QUESTIONS.md` file before implementation
- implement only after questions have been answered
- verify whether approved changes were applied correctly
- perform a final release gate before merge or deployment
- run a staff/principal-engineer-style review workflow

Do not use this skill when the user wants a quick isolated fix with no need for structured discovery, decision capture, verification, or release assessment.

---

## Workflow files

This skill relies on the following workflow documents in the same folder:

- `01-codebase-review-question-audit.md`
- `02-questions-md-resolution-implementation.md`
- `03-implementation-verification-pass.md`
- `04-release-readiness-pass.md`

Read and apply them in order.

---

## Pre-workflow checkpoint: confirm release target

Before starting Phase 1, explicitly confirm the intended release target with the user.

Allowed targets:

- local demo
- internal prototype
- team handoff
- staging
- production
- open-source release

This target defines the level of rigor expected in discovery, implementation, verification, and release-readiness decisions.

If the user did not provide a target but requests immediate discovery, infer a provisional target, mark that inference as a caveat, and continue with Phase 1 in the same response.

---

## Execution order

### Phase 1 — Discovery

First, read:

`01-codebase-review-question-audit.md`

Goal:
- perform a broad and deep review of the codebase
- identify ambiguities, risks, missing decisions, suspicious areas, and architectural concerns
- generate `QUESTIONS.md`

Expected output:
- `QUESTIONS.md`

Do not proceed automatically if:
- `QUESTIONS.md` still needs human answers
- major ambiguities remain unresolved
- the user wants to review the questions first

---

### Phase 2 — Implementation

Only after `QUESTIONS.md` has been answered, read:

`02-questions-md-resolution-implementation.md`

Goal:
- read the answered `QUESTIONS.md`
- classify decisions
- convert approved answers into a scoped implementation plan
- apply approved changes safely
- generate `IMPLEMENTATION_NOTES.md`

Expected output:
- approved code changes
- `IMPLEMENTATION_NOTES.md`

Do not proceed automatically if:
- `QUESTIONS.md` is unanswered
- answers are contradictory or too vague
- major blockers remain unresolved

---

### Phase 3 — Verification

After implementation is complete, read:

`03-implementation-verification-pass.md`

Goal:
- verify that approved changes were implemented correctly
- check alignment with `QUESTIONS.md`
- assess regressions, consistency, tests, docs, and integration quality
- generate `VERIFICATION.md`

Expected output:
- `VERIFICATION.md`

Do not proceed automatically if:
- implementation is incomplete
- verification cannot be done confidently
- must-fix findings remain unresolved

---

### Phase 4 — Release Readiness

After verification is complete, read:

`04-release-readiness-pass.md`

Goal:
- determine whether the project is actually ready for merge, handoff, staging, demo, or production
- assess build readiness, configuration, tests, deployment assumptions, observability, operational posture, and documentation
- generate `RELEASE_READINESS.md`

Expected output:
- `RELEASE_READINESS.md`

Final verdict must be one of:
- `Ready`
- `Ready with caveats`
- `Not ready`

Do not mark the project ready if verification still contains unresolved must-fix findings.

---

## Required workflow behavior

Follow these rules strictly:

- Do not skip phases.
- Do not start discovery without either a confirmed target or a documented provisional target inference.
- Do not implement before discovery has produced `QUESTIONS.md`.
- Do not proceed to implementation unless `QUESTIONS.md` has answers.
- Do not apply implementation changes in Phase 2 before explicit user approval of the scoped plan.
- Do not treat vague answers as approval for broad changes.
- Do not mark work verified without checking related areas, tests, and docs.
- Do not mark the project release-ready without making an explicit verdict.
- Preserve scope boundaries throughout the workflow.

---

## Output summary

This workflow should produce the following artifacts over time:

1. `QUESTIONS.md`
2. `IMPLEMENTATION_NOTES.md`
3. `VERIFICATION.md`
4. `RELEASE_READINESS.md`

Each artifact should reflect the outcome of its corresponding phase and should be used as input for the next phase where applicable.

---

## Operating mindset

Act as:

- a staff or principal engineer
- a technical lead performing structured engineering review
- a release gate reviewer focused on evidence, not assumptions

Understand first.  
Clarify second.  
Implement third.  
Verify fourth.  
Release only when justified.

---

## Stop conditions

Stop the workflow when any of the following is true:

- `QUESTIONS.md` is still unanswered
- key decisions remain blocked
- implementation is incomplete
- verification finds unresolved must-fix issues
- release readiness cannot be assessed honestly with confidence

If a stop condition is reached, report the current state clearly and do not pretend the workflow is complete.