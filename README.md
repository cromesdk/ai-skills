# CromeSDK Angular Skills Repository

Curated, reusable agent skills for Angular- and Figma-centric engineering workflows, organized for deterministic execution and repeatable quality checks.

## Overview and Scope

This repository stores skill packages used by coding assistants.  
Each skill package is self-contained and follows a common contract:

- `SKILL.md` (workflow and rules)
- `agents/openai.yaml` (interface metadata)
- `tests/scenarios.md` (evaluation scenarios)

Scope includes skill authoring, skill maintenance, and scenario coverage for Angular, Figma, Codex, and project-level documentation workflows.

## Architecture at a Glance

The repository uses a domain-first folder model under `.agents/skills`.

| Domain | Purpose | Path |
|---|---|---|
| `angular` | Angular app/tooling workflows | `.agents/skills/angular` |
| `figma` | Figma-to-code workflows | `.agents/skills/figma` |
| `codex` | Assistant behavior hardening workflows | `.agents/skills/codex` |
| `project` | Project documentation maintenance workflows | `.agents/skills/project` |

## Prerequisites

- Git (to inspect and update repository changes).
- A coding-assistant runtime that can execute skill instructions from `SKILL.md`.
- Node.js/npm only when a specific skill requires Angular CLI/package commands.

## Quick Start

1. Open this repository as the active workspace.
2. Select a skill and invoke it by name in your prompt.
3. Review generated/updated files and scenario coverage.

Example invocations:

```text
$readme-updater Update the root README to enterprise quality.
$changelog-keepachangelog-update Update CHANGELOG.md from current git changes.
```

## Configuration and Environment Variables

Not applicable: no repository-level `.env` or `.env.example` files are present at this time.

## Development Workflow (Test/Lint/Build)

Not applicable at repository root: no root `package.json` is present, so no root build/lint/test command catalog exists.

Validation workflow used for skills:

- Keep each skill limited to one responsibility.
- Keep `agents/openai.yaml` aligned with `SKILL.md`.
- Keep `tests/scenarios.md` updated for easy/hard/edge cases.

## Operations and Troubleshooting

Operational checks:

- Confirm skill path exists before invocation.
- Confirm companion files exist:
  - `SKILL.md`
  - `agents/openai.yaml`
  - `tests/scenarios.md`
- If a target file is missing for an update request, ask one precise clarification question before creating new files.

Common issue:

- Skill not discoverable
  - Verify frontmatter `name` and `description` in `SKILL.md` are accurate and trigger-friendly.

## Deployment and Release

Not applicable: no deployment manifests, packaging pipeline, or release automation are defined in this repository.

## Security and Compliance

- Do not add unverifiable security/compliance claims to docs.
- Keep license metadata explicit (`LICENSE` is present; MIT).
- Do not commit secrets; no secrets-management workflow is defined in this repo.
- Compliance posture details are `TBD (owner needed)`.

## Contributing and Code Standards

1. Add or update a skill under `.agents/skills/<domain>/<skill-name>/`.
2. Keep instructions deterministic and non-destructive by default.
3. Update `tests/scenarios.md` when behavior changes.
4. Keep `agents/openai.yaml` metadata aligned with skill behavior.
5. Validate structural integrity before merge.

## Ownership, Support, and Escalation

- Primary owner: `TBD (owner needed)`.
- Support channel: `TBD (owner needed)`.
- Escalation path: `TBD (owner needed)`.

## License and Legal Notices

This project is licensed under MIT. See [LICENSE](./LICENSE).
