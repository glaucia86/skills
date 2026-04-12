# Agent Skills by Glaucia

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-111827)](https://agentskills.io/)
[![Directory](https://img.shields.io/badge/Directory-skills.sh-0f766e)](https://skills.sh/)
[![License: MIT](https://img.shields.io/badge/License-MIT-1f2937.svg)](LICENSE)

A growing collection of reusable skills for coding agents — focused on safe
delivery workflows, Human in the Loop decisions, and explicit release gates.

## Why this collection exists

Most teams ship faster when they are strict about process, but process often
lives in scattered docs and tribal knowledge. These skills turn those rules into
portable, executable playbooks that any coding agent can follow.

## Quick Start

Install all skills from this repository:

```bash
npx skills@latest add glaucia86/skills
```

Install a specific skill by name:

```bash
npx skills@latest add glaucia86/skills --skill <skill-name>
```

List all available skills:

```bash
npx skills add ./ --list
```

## Skill Catalog

Each skill has its own `README.md` with installation instructions, workflow details, and examples.

| Skill | Category | What it does | HITL |
|---|---|---|---|
| [`review-to-release-workflow`](review-to-release-workflow/README.md) | Engineering Workflow | Four-phase workflow: discovery → implementation → verification → release readiness | Required at key decision points |

## Add a New Skill

Use this repo as a scalable catalog. For every new skill:

1. Create a folder at repo root using kebab-case.
2. Add `SKILL.md` with valid frontmatter (`name`, `description`).
3. Add a `README.md` inside the skill folder with full documentation.
4. Add `evals/evals.json` with at least 2 realistic prompts.
5. Add one row to the Skill Catalog table above.

Starter layout:

```text
my-new-skill/
  SKILL.md
  README.md
  evals/
    evals.json
  references/
  scripts/
```

## Quality Bar for New Skills

- Clear trigger description (when to use, when not to use)
- Explicit scope boundaries and stop conditions
- Deterministic outputs or documented decision points
- At least 2 realistic eval prompts before publish
- Install test passes locally:

```bash
npx skills add ./ --list
```

## Publishing Checklist

Before pushing a new skill:

1. Skill folder is at repo root and not ignored by Git.
2. `SKILL.md` has valid `name` and `description` frontmatter.
3. `README.md` inside the skill folder covers usage and examples.
4. Skill Catalog table in this file links to the skill README.
5. Install command works locally and from the remote repo.

## Roadmap

- More workflow skills: architecture reviews, incident response, migration playbooks.
- Stronger eval coverage with negative tests and artifact-gating checks.
- Benchmark automation for iteration reports.
