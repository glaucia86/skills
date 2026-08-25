# Agent Skills by Glaucia Lemos

<div align="center">

<img src="https://avatars.githubusercontent.com/u/1631477?v=4" width="96" style="border-radius:50%" alt="Glaucia Lemos"/>

<h3>Glaucia Lemos</h3>
<p>A.I Developer · Open Source Contributor · <a href="https://linktr.ee/glaucia_lemos86">linktr.ee/glaucia_lemos86</a></p>

<p>
  <a href="https://agentskills.io/"><img src="https://img.shields.io/badge/Agent%20Skills-Open%20Standard-111827?style=flat-square" alt="Agent Skills"/></a>
  <a href="https://skills.sh/"><img src="https://img.shields.io/badge/Listed%20on-skills.sh-0f766e?style=flat-square" alt="skills.sh"/></a>
  <a href="https://github.com/glaucia86"><img src="https://img.shields.io/github/followers/glaucia86?style=flat-square&label=Follow&color=1f2937" alt="GitHub followers"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-1f2937?style=flat-square" alt="License: MIT"/></a>
</p>

</div>

---

A growing collection of reusable skills for coding agents. Focused on safe delivery
workflows, Human in the Loop decisions, and explicit release gates.

Each skill is a portable, executable playbook that any coding agent can follow.
Most teams ship faster when they are strict about process. But process usually lives
in scattered docs and tribal knowledge. These skills change that.

## Quick Start

Install all skills from this repository:

```bash
npx skills@latest add glaucia86/skills
```

Install a specific skill by name:

```bash
npx skills@latest add glaucia86/skills --skill <skill-name>
```

List all available skills from a local clone:

```bash
npx skills add ./ --list
```

## Skill Catalog

Each skill has its own `README.md` with full installation instructions, workflow
diagrams, and usage examples.

| Skill | Category | What it does | HITL |
|---|---|---|---|
| [`task-clarification-harness`](task-clarification-harness/README.md) | Harness Engineering | Pre-implementation clarification guide that grounds the task in the repo, defines boundaries, and produces an implementation contract | Recommended when tasks are ambiguous or risky |
| [`implementation-contract-review-harness`](implementation-contract-review-harness/README.md) | Harness Engineering | Feedback sensor that reviews a clarification artifact before coding and returns a contract verdict | Recommended before coding when the contract matters |
| [`implementation-readiness-gate`](implementation-readiness-gate/README.md) | Harness Engineering | Final pre-implementation gate that returns `go`, `go-with-caveats`, or `no-go` from the current artifacts | Optional final decision layer |
| [`review-to-release-workflow`](review-to-release-workflow/README.md) | Engineering Workflow | Four-phase workflow: discovery → implementation → verification → release readiness | Required at key decision points |
| [`eli5`](eli5/README.md) | Learning and Education | Creates a self-contained beginner-friendly HTML visual explainer with minimal text and clear analogies | Recommended for visual beginner explanations |
| [`revealjs`](revealjs/SKILL.md) | Presentation | Creates reveal.js HTML presentations as single-file artifacts; covers slides, fragments, auto-animate, code highlighting, math, backgrounds, themes, transitions, speaker notes, PDF export, and the React wrapper | Not applicable |

## Recommended Harness Composition

The three harness skills can be used independently.
They do not have to run in a rigid sequence every time.

When you want stronger pre-implementation control, the recommended composition is:

1. [`task-clarification-harness`](task-clarification-harness/README.md)
2. [`implementation-contract-review-harness`](implementation-contract-review-harness/README.md)
3. [`implementation-readiness-gate`](implementation-readiness-gate/README.md)

Role of each:

- `task-clarification-harness`: creates the artifact
- `implementation-contract-review-harness`: reviews the artifact
- `implementation-readiness-gate`: consolidates the final execution decision

## Add a New Skill

Use this repo as a scalable catalog. For every new skill:

1. Create a folder at repo root using kebab-case.
2. Add `SKILL.md` with valid frontmatter (`name`, `description`).
3. Add `README.md` inside the folder with full documentation.
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
4. Skill Catalog table links to the skill README.
5. Install command works locally and from the remote repo.

## Roadmap

- More workflow skills: architecture reviews, incident response, migration playbooks.
- Stronger eval coverage with negative tests and artifact-gating checks.
- Benchmark automation for iteration reports.

---

<div align="center">

Made by [Glaucia Lemos](https://github.com/glaucia86) · Rio de Janeiro, Brazil
· [Twitter/X](https://twitter.com/glaucia_lemos86) · [LinkedIn](https://www.linkedin.com/in/glaucialemos/) · [YouTube](https://bit.ly/youtube-canal-glaucialemos) · [Linktree](https://linktr.ee/glaucia_lemos86)

</div>
