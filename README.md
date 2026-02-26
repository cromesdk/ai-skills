# CromeSDK AI Skills Repository

<p align="center">
  <img src="assets/logo.svg" alt="Project logo" />
</p>

Deterministic, reusable agent skills for engineering workflows across Angular, Figma, NestJS, TypeScript, Codex, and project operations.

## Overview and Scope

This repository is a skill catalog for coding assistants. Each skill package is organized under `skills/<domain>/<skill-name>/` and is expected to include:

- `SKILL.md` (workflow and rules)
- `agents/openai.yaml` (assistant interface metadata)
- `tests/scenarios.md` (evaluation scenarios)

Repository scope includes skill authoring, maintenance, and scenario coverage for assistant behavior and delivery workflows.

## Architecture at a Glance

Domain-first layout under `skills/`:

| Domain | Skill Count (`SKILL.md`) | Path | Notes |
|---|---:|---|---|
| `angular` | 15 | `skills/angular` | Angular application/tooling workflows |
| `codex` | 1 | `skills/codex` | Assistant behavior hardening workflows |
| `figma` | 6 | `skills/figma` | Figma-to-code and design workflows |
| `nestjs` | 14 | `skills/nestjs` | NestJS backend setup, maintenance, and tooling workflows |
| `project` | 7 | `skills/project` | Repository/process and documentation workflows |
| `python` | 0 | `skills/python` | Domain folder present; no `SKILL.md` currently |
| `typescript` | 8 | `skills/typescript` | TypeScript tooling workflows |

Companion-file integrity status: all discovered skills currently include both `agents/openai.yaml` and `tests/scenarios.md`.

## Prerequisites

- Git
- A coding-assistant runtime capable of executing skill instructions from `SKILL.md`
- Node.js and npm only when an individual skill requires Node-based tooling

## Quick Start

1. Open this repository as your active workspace.
2. Invoke a skill by name in your assistant prompt.
3. Review changed files and scenario coverage for the touched skill.

Example invocations:

```text
$readme-updater update root readme
$changelog-keepachangelog-update update changelog from current repository changes
```

## Configuration and Environment Variables

Not applicable at repository root: no root `.env`/`.env.example` contract is defined.

## Development Workflow (Test/Lint/Build)

Not applicable at repository root: no root `package.json` command catalog is present.

Skill-level quality workflow:

1. Keep each skill scoped to one primary responsibility.
2. Keep `agents/openai.yaml` aligned with `SKILL.md` behavior.
3. Keep `tests/scenarios.md` updated when workflow behavior changes.

## Operations and Troubleshooting

Basic runbook checks:

1. Confirm target skill path exists under `skills/<domain>/<skill-name>/`.
2. Confirm required companion files exist:
   - `SKILL.md`
   - `agents/openai.yaml`
   - `tests/scenarios.md`
3. If an update target file is missing, clarify creation intent before writing.

Common failure mode:

- Skill discovery mismatch: verify `name` and `description` frontmatter in `SKILL.md` are accurate and trigger-friendly.

## Deployment and Release

Release documentation is maintained in [CHANGELOG.md](./CHANGELOG.md) (Keep a Changelog format).

Deployment automation/pipeline guidance at repository root: `TBD (owner needed)`.

## Security and Compliance

- License file is present and project is MIT-licensed ([LICENSE](./LICENSE)).
- No repository-level secrets-management workflow is documented.
- No repository-level compliance framework documentation is declared.
- Security/compliance ownership model: `TBD (owner needed)`.

## Contributing and Code Standards

1. Add or update a skill under `skills/<domain>/<skill-name>/`.
2. Keep instructions deterministic and non-destructive by default.
3. Update `tests/scenarios.md` when behavior changes.
4. Keep `agents/openai.yaml` synchronized with skill workflow changes.
5. Validate companion-file completeness before merge.

## License and Legal Notices

This project is licensed under MIT. See [LICENSE](./LICENSE).
