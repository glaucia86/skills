---
name: implementation-contract-review-harness
description: Review a pre-implementation contract or clarification summary as a feedback harness before coding starts. Use when a task already has a clarification artifact and you want a second-pass review of scope boundaries, repository grounding, validation quality, risk coverage, and approval edges before implementation proceeds.
---

# Implementation Contract Review Harness

## Purpose

Use this skill after a clarification artifact already exists.

This skill acts as an inferential feedback sensor before implementation.
Its job is not to restate the task from scratch.
Its job is to challenge whether the implementation contract is tight enough, grounded enough, and safe enough to execute.

Use it to review artifacts produced by `task-clarification-harness` or any equivalent pre-implementation summary.
Its verdict can be used directly or passed into `implementation-readiness-gate` as part of a final pre-implementation go or no-go decision.

## Workflow files

This skill relies on the following files in the same folder:

- `contract-review-checklist.md`
- `review-output-template.md`
- `example-contract-review.md`

Read and apply them during the review pass.

## Required behavior

Before implementation begins, review the contract for:

1. repository grounding
2. scope tightness
3. ambiguity leakage
4. risk and invariant coverage
5. validation quality
6. approval-required edges

Do not rewrite the whole plan unless the artifact is fundamentally unusable.
Focus on finding weaknesses in the current contract.

## Review workflow

### Step 1 - Read the contract artifact

Read the full clarification summary or implementation contract.

Treat it as the object under review.
Do not assume missing details are acceptable.

### Step 2 - Check structural quality

Read `contract-review-checklist.md`.

Confirm that the artifact:

- is specific rather than narrative
- identifies real repository evidence
- distinguishes facts from inferences
- defines scope boundaries clearly
- contains executable validation lines

### Step 3 - Stress-test the contract

Ask whether another agent could implement safely from this artifact without:

- guessing architecture
- expanding scope silently
- inventing missing behavior
- choosing arbitrary validation steps

If the answer is no, identify the weakest sections precisely.

### Step 4 - Produce a review verdict

Use `review-output-template.md`.

Return exactly one verdict:

- `contract-approved`
- `contract-needs-tightening`
- `contract-needs-user-decision`
- `contract-not-safe`

Use:

### `contract-approved`
when the contract is specific enough to guide implementation safely.

### `contract-needs-tightening`
when the contract is promising but still too loose in one or more key areas.

### `contract-needs-user-decision`
when unresolved behavioral or product choices still require explicit human input.

### `contract-not-safe`
when the contract is too vague, too ungrounded, or too risky to use as an implementation handoff.

## Constraints

Do not:

- approve a contract with generic validation placeholders
- approve a contract that invents repository facts
- ignore missing approval edges
- silently fill in missing product decisions

Do:

- challenge weak assumptions
- point to the exact section that needs tightening
- preserve narrow scope
- prefer actionable feedback over general criticism

## Operating mindset

Act as:

- a pre-implementation reviewer
- a feedback sensor in the harness
- an engineer trying to prevent avoidable rework

Approve only when the contract can genuinely guide execution.
