# Contract Review Handoff Template

Use this template when handing a clarification artifact to `implementation-contract-review-harness`.

The goal is to make the review target explicit and prevent the second-pass review from drifting into a fresh discovery exercise.

## Handoff message

Use a message shaped like this:

```text
Use $implementation-contract-review-harness on this clarification artifact before implementation starts.

Artifact path: <path-to-summary.md>
Task summary: <one or two lines>
Review focus:
- repository grounding
- scope boundaries
- validation quality
- approval-required edges

Return:
- the key gaps that matter
- the tightening required before coding
- exactly one verdict: contract-approved / contract-needs-tightening / contract-needs-user-decision / contract-not-safe
```

## Handoff rules

- Pass the artifact path or full artifact content
- Do not pre-solve the review for the sister skill
- Keep the task summary short
- Name the review focus explicitly
- Require one verdict only
