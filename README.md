# angular-skills

Single-purpose Codex skill workspace for Angular-focused agent workflows, currently centered on safe Angular 20 app scaffolding.

![Angular](https://img.shields.io/badge/Angular-20-DD0031?logo=angular&logoColor=white)
![Markdown](https://img.shields.io/badge/Docs-Markdown-000000?logo=markdown&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Features

- Defines a reusable `angular-app-setup` skill in `.agents/skills/angular-app-setup/SKILL.md`.
- Enforces safe preflight checks before in-place Angular scaffolding.
- Standardizes Angular 20 CLI defaults (`strict`, CSS, no nested directory).
- Includes scenario coverage in `.agents/skills/angular-app-setup/tests/scenarios.md`.

## Prerequisites

- Node.js 20+ (recommended for Angular 20 CLI workflows).
- `npm` available in terminal.
- A Codex-compatible environment that can read `SKILL.md` instructions.

## Quick Start

1. Clone the repository.
2. Open the repository root.
3. Reference the skill in your Codex prompt:

```text
[$angular-app-setup](.agents/skills/angular-app-setup/SKILL.md)
Create an Angular 20 app in this folder named "shop-ui".
```

## Usage

Use this repo as a local skill source. The main skill currently available in-repo is:

- `angular-app-setup`: scaffolds Angular 20 in the current directory with safety checks and verification.

Primary files:

- `.agents/skills/angular-app-setup/SKILL.md`
- `.agents/skills/angular-app-setup/reference.md`
- `.agents/skills/angular-app-setup/tests/scenarios.md`
- `.agents/skills/angular-app-setup/agents/openai.yaml`

## Configuration

The `angular-app-setup` skill documents:

- Required in-place scaffold flag: `--directory .`
- Baseline CLI flags: `--style=css --strict --skip-git --ai-config=none`
- Optional variants (routing, style extension, package manager, AI config)

See `.agents/skills/angular-app-setup/reference.md` for supported `--ai-config` values and official Angular docs links.

## Scripts / Commands

This repository does not currently define a root `package.json` or repository-level scripts.

The skill itself instructs downstream projects to run:

- `npm run build`
- `npm run test -- --watch=false`

after Angular app generation.

## Contributing

1. Update or add skills under `.agents/skills/...`.
2. Keep skill behavior explicit and testable (include scenario docs).
3. Prefer concrete commands and verification steps in each `SKILL.md`.
4. Validate all referenced paths and commands before opening a PR.

## License

MIT. See `LICENSE`.
