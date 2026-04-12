# task-clarification-harness

[![Install](https://img.shields.io/badge/install-npx%20skills-0f766e)](https://skills.sh/)
[![Harness role](https://img.shields.io/badge/role-guide-111827)](#what-this-skill-does)
[![Language](https://img.shields.io/badge/language-agnostic-1f2937)](#language-agnostic)

A pre-implementation harness skill for ambiguous or risky coding tasks. It forces
the agent to slow down, inspect the repository, surface ambiguities, map impact,
set boundaries, and produce an implementation contract before any code changes begin.

## Why this skill exists

Coding agents fail most often when they implement too early, assume hidden
behavior, or choose generic validation steps that do not match the repository.

This skill exists to reduce those failure modes by turning an underspecified
request into a constrained engineering artifact:

- task restatement
- repository evidence
- ambiguities
- impacted areas
- risks and invariants
- scope boundaries
- implementation contract
- validation plan
- readiness decision

In harness-engineering terms, this skill is primarily a `guide`.

## What this skill does

When triggered, the skill makes the agent:

1. restate the task in engineering terms
2. inspect the repository before making claims
3. identify ambiguities and assumptions
4. map likely impact surface
5. define risks, invariants, and boundaries
6. produce a structured clarification artifact
7. decide whether implementation is safe to start

## Language agnostic

This skill is intentionally language-agnostic.

It does not assume JavaScript, Python, Go, Rust, or any specific framework.
Instead, it teaches the agent to inspect the repository and link validation to
whatever mechanisms already exist there.

The references include multi-language repository cues only to help the agent
discover likely validation entry points in different stacks.

## When to use

Use this skill when the task is:

- broad
- ambiguous
- cross-cutting
- risky
- likely to drift without explicit boundaries

Typical cases:

- "Add support for X"
- "Refactor this flow"
- "Make this production-ready"
- "Update the auth logic"
- "Fix this across the project"

## When not to use

Do not use this skill when the task is extremely small, explicit, isolated, and
low risk, unless you still want a formal clarification artifact.

## Output

The main output is a structured `Clarification Summary` based on
`output-template.md`.

If the summary is written to disk, validate it with:

```bash
python scripts/validate_clarification_summary.py <path-to-summary.md>
```

## What To Do Next

After running this skill, use the `Clarification Summary` as an execution
artifact, not as disposable notes.

- If the decision is `ready-for-implementation`, use the summary as the working
  contract for the coding step.
- If the decision is `needs-user-clarification`, resolve the open decisions
  before coding.
- If the decision is `needs-codebase-investigation`, inspect the missing
  repository areas and refresh the summary.
- If the decision is `not-safe-to-proceed`, do not implement until the artifact
  is tightened.

For important tasks, persist the artifact in the repository so later agent runs
can reuse the same intent, scope boundaries, and validation logic.

If you want a stronger gate before coding, pass the artifact to
`implementation-contract-review-harness`.

## How to use

Example request:

```text
Use task-clarification-harness before implementation. Inspect the repo, surface ambiguities, map impacted areas, define scope boundaries, and give me a readiness decision.
```

Typical outcome:

- `ready-for-implementation`
- `needs-user-clarification`
- `needs-codebase-investigation`
- `not-safe-to-proceed`

## Relationship to the other harness skills

This skill can be used on its own.

Recommended composition when you want stronger pre-implementation control:

1. `task-clarification-harness`
2. `implementation-contract-review-harness`
3. `implementation-readiness-gate`

That sequence is recommended, not mandatory.
Each skill has its own role:

- `task-clarification-harness`: produce the artifact
- `implementation-contract-review-harness`: review the artifact
- `implementation-readiness-gate`: issue the final go or no-go decision

## File structure

```text
task-clarification-harness/
  SKILL.md
  README.md
  ambiguity-checklist.md
  scope-boundaries.md
  output-template.md
  references/
    harness-patterns.md
    validation-linking-criteria.md
    contract-review-handoff-template.md
    example-clarification-summary.md
  scripts/
    validate_clarification_summary.py
  evals/
    evals.json
```

## Evals

This skill includes eval prompts in `evals/evals.json` covering:

- correct pre-implementation clarification behavior
- refusal to invent repository facts
- refusal to use generic validation placeholders
- handoff to the contract review skill

---

[← Back to skills catalog](../README.md)
