# Validation Linking Criteria

Use this reference when converting a validation plan into repository-specific checks.

The goal is to tie each proposed validation step to a real mechanism in the repository, not to a generic best-practice placeholder.

The language-specific sections below are discovery cues, not requirements.
Use only the cues that match the repository under analysis.

The language-specific sections below are discovery cues, not requirements.
Use only the cues that match the repository under analysis.

## Selection order

Prefer validation sources in this order:

1. Existing repository task runners or scripts
2. Existing CI workflow commands
3. Native language or framework validation commands already implied by the repo
4. Narrow manual scenarios when no deterministic check exists

## Repository cues

Look for these files and map them to likely validation entry points.

### JavaScript and TypeScript
- `package.json`: use `scripts` such as `lint`, `typecheck`, `test`, `build`, `check`
- `pnpm-workspace.yaml`, `turbo.json`, `nx.json`: prefer workspace-native commands
- `eslint.config.*` or `.eslintrc*`: lint likely exists
- `tsconfig.json`: typecheck may exist
- `vitest.config.*`, `jest.config.*`, `playwright.config.*`: test families likely exist

### Python
- `pyproject.toml`, `requirements*.txt`, `tox.ini`, `noxfile.py`
- tool sections for `pytest`, `ruff`, `mypy`, `pyright`, `coverage`

### Go
- `go.mod`
- likely checks include `go test`, `go vet`, and project wrappers around them

### Rust
- `Cargo.toml`
- likely checks include `cargo test`, `cargo clippy`, and `cargo fmt --check`

### JVM
- `pom.xml`, `build.gradle`, `build.gradle.kts`
- prefer `mvn` or `gradle` tasks already used in the repo

### General build systems
- `Makefile`, `justfile`, `Taskfile.yml`, shell scripts under `scripts/`
- prefer the highest-level stable entry point that the repo already uses

### CI and delivery
- `.github/workflows/*.yml`
- mirror the verification surface already enforced in CI when practical

## Mapping risks to checks

Map each major risk or invariant to one or more checks.

Examples:

- API contract risk -> contract tests, integration tests, schema validation, manual request-response scenario
- type or interface drift -> typecheck, compile, generated client checks
- architecture drift -> structural tests, lint rules, import boundary checks
- regression risk -> targeted unit or integration tests for impacted paths
- build or packaging risk -> build step, bundle check, artifact generation
- config or docs drift -> config review, generated docs check, manual startup scenario

## When a check is unavailable

If a useful check does not exist:

- say that it is unavailable
- explain what risk remains
- propose the smallest manual validation that still gives signal

Do not pretend the repository has stronger harnesses than it actually has.

## Output rule

For each validation line in the clarification summary, prefer this format:

- check type
- repository mechanism or command family
- reason it covers the identified risk

Example:

- tests: targeted repository test command for the changed authentication flow or equivalent repo wrapper; covers regression risk in token refresh behavior
- typecheck: repository typecheck or compile command if available; covers interface drift in changed modules
- manual validation: create session, expire token, retry protected route; covers behavior not fully exercised by automated checks
