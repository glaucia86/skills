# Contract Review Checklist

Use this checklist to review an implementation contract before coding starts.

## Repository grounding
- Are the referenced files, modules, routes, or symbols real?
- Does the contract distinguish confirmed facts from inferences?
- Does it rely on repository evidence instead of hand-wavy architecture guesses?

## Scope quality
- Is the requested change narrowly bounded?
- Are adjacent improvements explicitly deferred?
- Are approval-required edges called out clearly?

## Behavior quality
- Are important product decisions already resolved?
- Are ambiguities small enough to tolerate during implementation?
- Are invariants explicit?

## Validation quality
- Are validation steps tied to real repository mechanisms?
- Are generic placeholders avoided?
- Is at least one manual scenario included when deterministic checks are weak or absent?

## Handoff quality
- Could another agent implement from this artifact without re-discovering the whole task?
- Does the contract reduce exploration rather than merely summarize the problem?

## Decision rule

If the contract still allows large implementation variance on behavior, scope, or verification, do not approve it as-is.
