# angular-skills

Reusable Angular 20 skill workspace for Codex-style agents.  
Each skill is a focused workflow with deterministic instructions, scenario coverage, and agent config.

![Language](https://img.shields.io/badge/language-Markdown-000000?logo=markdown)
![Framework](https://img.shields.io/badge/framework-Angular%2020-DD0031?logo=angular&logoColor=white)
![Skills](https://img.shields.io/badge/skills-6-0A7EA4)
[![License](https://img.shields.io/badge/license-MIT-2EA44F)](./LICENSE)

## Features

- Maintains local, reusable skills under `.agents/skills/`.
- Targets common Angular 20 setup and architecture workflows.
- Includes scenario-based validation docs per skill.
- Supports direct skill invocation by linking `SKILL.md` in prompts.

## Prerequisites

- A Codex-compatible agent environment that can load `SKILL.md` instructions.
- Node.js and npm available for workflows that execute Angular CLI commands.

## Quick Start

1. Open this repository as your working directory.
2. Reference a skill file directly in your prompt.

Example:

```text
[$angular-app-setup](.agents/skills/angular-app-setup/SKILL.md)
Create an Angular 20 app in this folder named "shop-ui".
```

## Latest Changes (February 22, 2026)

- Expanded from a single-skill repo to a 6-skill Angular 20 skill workspace.
- Added new skills: `angular-component-rule`, `angular-folder-structure`, `angular-json-server-setup`, `angular-tailwind-setup`, and `angular-vitest-setup`.
- Updated `angular-app-setup` with clearer deterministic preflight and scaffold instructions.
- Standardized each skill to include `SKILL.md`, `agents/openai.yaml`, and `tests/scenarios.md`.

## Available Skills

| Skill | Purpose | Path |
|---|---|---|
| `angular-app-setup` | Scaffold Angular 20 app in-place with strict, non-interactive defaults and verification gates. | `.agents/skills/angular-app-setup/SKILL.md` |
| `angular-component-rule` | Enforce Angular 20 component companion-file and structure hygiene in `src/app/**`. | `.agents/skills/angular-component-rule/SKILL.md` |
| `angular-folder-structure` | Define and enforce feature-first Angular 20 architecture boundaries. | `.agents/skills/angular-folder-structure/SKILL.md` |
| `angular-json-server-setup` | Configure local `json-server` mocks with proxy wiring for Angular 20. | `.agents/skills/angular-json-server-setup/SKILL.md` |
| `angular-tailwind-setup` | Install or repair Tailwind CSS v4 setup in Angular 20 workspaces. | `.agents/skills/angular-tailwind-setup/SKILL.md` |
| `angular-vitest-setup` | Migrate Angular unit tests from Karma/Jasmine to Vitest deterministically. | `.agents/skills/angular-vitest-setup/SKILL.md` |

## Repository Layout

```text
.agents/skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    tests/scenarios.md
```

Notes:

- `angular-app-setup` also includes `.agents/skills/angular-app-setup/reference.md`.
- This repository currently has no root `package.json` and no repo-level npm scripts.

## Usage Notes

- Keep each skill single-purpose and deterministic.
- Prefer explicit preflight checks and non-destructive behavior.
- Add or update `tests/scenarios.md` whenever workflow behavior changes.
- Ensure every command and path in `SKILL.md` is valid before publishing.

## Contributing

1. Add or modify skills under `.agents/skills/`.
2. Keep workflows executable and tool-agnostic where possible.
3. Update scenario coverage and agent config alongside instruction changes.
4. Open a PR with clear behavior deltas and validation notes.

## License

MIT. See `LICENSE`.
