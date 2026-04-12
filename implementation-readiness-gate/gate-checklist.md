# Gate Checklist

Use this checklist to decide whether implementation should begin.

## Artifact quality
- Is there a clarification artifact?
- If a contract review exists, is its verdict compatible with implementation?
- Are the artifacts internally consistent?

## Ambiguity
- Are remaining ambiguities small enough to tolerate during implementation?
- Do any unresolved items still require explicit user choice?

## Scope and approval
- Are scope boundaries clear?
- Are approval-required edges named explicitly?
- Would implementation risk silent scope expansion?

## Validation
- Is the validation plan linked to real repository mechanisms or explicitly marked unavailable?
- Does the validation plan cover the main risks and invariants?

## Decision rule

Use `go` only when the artifacts support safe execution now.
Use `go-with-caveats` when implementation may start but with named limits and follow-up obligations.
Use `no-go` when coding should wait for stronger inputs.
