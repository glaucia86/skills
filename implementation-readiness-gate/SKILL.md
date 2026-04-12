---
name: implementation-readiness-gate
description: "Run a final pre-implementation go or no-go gate after clarification and contract review. Use when a task already has a clarification artifact and, optionally, a contract review verdict, and you want one explicit execution decision: go, go-with-caveats, or no-go before any code changes begin."
---

# Implementation Readiness Gate

## Purpose

Use this skill as the final decision layer before implementation starts.

This skill does not replace clarification.
This skill does not replace contract review.
It consolidates the current evidence into a single execution decision.

Its job is to answer:

- Is the task clear enough to implement now?
- Are the scope boundaries tight enough?
- Are the approval edges visible?
- Is the validation path credible?
- Should coding start, wait, or proceed only with explicit caveats?

## Inputs

This skill expects one or both of the following:

- a clarification artifact such as a `Clarification Summary`
- a contract review result from `implementation-contract-review-harness`

If both are available, use both.
If only one is available, say what evidence is missing and lower confidence accordingly.

## Workflow files

This skill relies on the following files in the same folder:

- `gate-checklist.md`
- `gate-output-template.md`
- `example-gate-decision.md`

Read and apply them during the gate decision.

## Required behavior

Before implementation begins, the gate must:

1. inspect the available artifacts
2. confirm whether key ambiguities are resolved enough
3. confirm whether the contract review verdict permits safe execution
4. assess whether the validation plan is linked to real repository mechanisms
5. return one explicit gate decision

Do not implement during the gate.
Do not silently upgrade a weak contract into approval.

## Gate workflow

### Step 1 - Read the artifacts

Read the clarification artifact first.
If a contract review exists, read that too.

Treat the existing artifacts as the source of truth for the gate.

### Step 2 - Apply the checklist

Read `gate-checklist.md`.

Look for:

- unresolved behavioral ambiguity
- missing repository grounding
- weak validation linkage
- approval-required edges that are still open
- contradictions between the clarification artifact and the contract review verdict

### Step 3 - Decide execution readiness

Use `gate-output-template.md`.

Return exactly one decision:

- `go`
- `go-with-caveats`
- `no-go`

Use:

### `go`
when the task is clear enough, the scope is bounded, and the validation path is credible enough to begin implementation.

### `go-with-caveats`
when implementation can begin, but only with explicitly named limits, assumptions, or follow-up obligations.

### `no-go`
when coding should not begin yet because the artifacts are too weak, too contradictory, or too risky.

## Constraints

Do not:

- implement during the gate
- ignore a negative contract review verdict
- treat generic validation placeholders as sufficient evidence
- hide caveats inside a `go` decision

Do:

- consolidate the current evidence
- make blockers and caveats explicit
- tie the decision to artifact quality, not optimism
- preserve narrow scope

## Operating mindset

Act as:

- a final pre-implementation gate
- a conservative decision layer in the harness
- an engineer reducing avoidable execution thrash

Only say `go` when the current artifacts genuinely support implementation.
