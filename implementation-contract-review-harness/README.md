# implementation-contract-review-harness

[![Install](https://img.shields.io/badge/install-npx%20skills-0f766e)](https://skills.sh/)
[![Harness role](https://img.shields.io/badge/role-sensor-111827)](#what-this-skill-does)
[![Language](https://img.shields.io/badge/language-agnostic-1f2937)](#language-agnostic)

A pre-implementation review skill that acts as a feedback sensor for a
clarification artifact or implementation contract. Its purpose is to challenge
whether the artifact is actually tight enough to guide coding safely.

## Why this skill exists

A clarification summary can look good while still being too loose to use as an
implementation handoff. Common failure modes include:

- vague validation lines
- unresolved product decisions
- invented repository facts
- hidden scope expansion
- missing approval edges

This skill exists to review the artifact before coding starts and return a clear
verdict instead of letting the agent drift into implementation.

## What this skill does

The skill reviews an existing clarification artifact and checks:

- repository grounding
- scope tightness
- ambiguity leakage
- risk and invariant coverage
- validation quality
- approval-required edges

It then returns exactly one verdict:

- `contract-approved`
- `contract-needs-tightening`
- `contract-needs-user-decision`
- `contract-not-safe`

In harness-engineering terms, this skill is an inferential `sensor`.

## Language agnostic

This skill is language-agnostic.

It does not care what stack the repository uses. It cares whether the artifact
is grounded in the actual repository and whether the validation plan is linked
to real repository mechanisms.

## When to use

Use this skill when you already have:

- a `Clarification Summary`
- an implementation contract
- or another pre-implementation planning artifact

and you want a second-pass review before coding starts.

## What To Do Next

After running this skill, treat the verdict as a real gate.

- If the verdict is `contract-approved`, implementation can begin using the
  reviewed artifact as the contract.
- If the verdict is `contract-needs-tightening`, revise the weak sections and
  review again before coding.
- If the verdict is `contract-needs-user-decision`, resolve the missing product
  or behavior decisions with the user first.
- If the verdict is `contract-not-safe`, do not implement from the current
  artifact.

If you want one final execution decision after review, pass the clarification
artifact and the review verdict to `implementation-readiness-gate`.

## How to use

Example request:

```text
Use implementation-contract-review-harness on this clarification artifact before implementation starts. Review repository grounding, scope boundaries, validation quality, and approval edges. Return one verdict only.
```

## Relationship to the other harness skills

This skill can be used independently whenever an existing artifact needs review.

Recommended composition when building a stronger harness:

1. `task-clarification-harness` creates the artifact
2. `implementation-contract-review-harness` reviews the artifact
3. `implementation-readiness-gate` consolidates the final execution decision

## File structure

```text
implementation-contract-review-harness/
  SKILL.md
  README.md
  contract-review-checklist.md
  review-output-template.md
  example-contract-review.md
  evals/
    evals.json
```

## Evals

This skill includes eval prompts in `evals/evals.json` covering:

- approval of strong contracts
- rejection of generic validation placeholders
- handling of unresolved product decisions
- staying in review mode instead of rewriting the plan from scratch
