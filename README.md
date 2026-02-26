# CromeSDK AI Skills Repository

<p align="center">
  <img src="assets/logo.svg" alt="Project logo" />
</p>

Curated, reusable agent skills for deterministic engineering workflows across Angular, Figma, NestJS, TypeScript, Codex, and project documentation operations.

## Overview and Scope

This repository is a skill catalog for coding assistants. Each skill package is organized under `skills/<domain>/<skill-name>/` and is expected to include:

- `SKILL.md` (workflow and rules)
- `agents/openai.yaml` (interface metadata)
- `tests/scenarios.md` (evaluation scenarios)

Repository scope includes skill authoring, maintenance, and scenario coverage for assistant behavior and delivery workflows.

## Architecture at a Glance

Domain-first layout under `skills/`:

| Domain | Skill Count (`SKILL.md`) | Path | Notes |
|---|---:|---|---|
| `angular` | 15 | `skills/angular` | Angular application/tooling workflows |
| `figma` | 6 | `skills/figma` | Figma-to-code and design workflows |
| `nestjs` | 7 | `skills/nestjs` | NestJS backend setup and tooling workflows |
| `typescript` | 2 | `skills/typescript` | TypeScript tooling workflows |
| `codex` | 1 | `skills/codex` | Assistant behavior hardening workflows |
| `project` | 5 | `skills/project` | Repository/project process workflows |
| `python` | 0 | `skills/python` | Domain folder present; no `SKILL.md` currently |

Companion-file integrity status: all discovered skills currently include both `agents/openai.yaml` and `tests/scenarios.md`.

## Prerequisites

- Git
- A coding-assistant runtime capable of executing skill instructions from `SKILL.md`
- Node.js/npm only when an individual skill requires Node-based tooling

## Quick Start

1. Open this repository as your active workspace.
2. Invoke a skill by name in your prompt.
3. Review changed files and scenario coverage for the touched skill.

Example invocations:

```text
$readme-updater recreate readme
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

- Skill discovery mismatch
  - Verify `name` and `description` frontmatter in `SKILL.md` are accurate and trigger-friendly.

## Deployment and Release

Release documentation is maintained in [CHANGELOG.md](./CHANGELOG.md) (Keep a Changelog format).

Deployment automation/pipeline guidance at repository root: `TBD (owner needed)`.

## Security and Compliance

- License file is present and project is MIT-licensed ([LICENSE](./LICENSE)).
- No repository-level secrets-management workflow is documented.
- Do not introduce unverifiable compliance claims in skill docs.
- Security/compliance ownership model: `TBD (owner needed)`.

## Contributing and Code Standards

1. Add or update a skill under `skills/<domain>/<skill-name>/`.
2. Keep instructions deterministic and non-destructive by default.
3. Update `tests/scenarios.md` when behavior changes.
4. Keep `agents/openai.yaml` synchronized with skill workflow changes.
5. Validate companion-file completeness before merge.

## Ownership, Support, and Escalation

- Repository owner: `TBD (owner needed)`
- Support channel: `TBD (owner needed)`
- Escalation path: `TBD (owner needed)`

## License and Legal Notices

This project is licensed under MIT. See [LICENSE](./LICENSE).