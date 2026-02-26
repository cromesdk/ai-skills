# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2026-02-26

### Added

- Added new project-level skill `spec-kit-setup` for deterministic `github/spec-kit` install, safe reconcile updates, and workflow readiness validation:
  - `skills/project/spec-kit-setup/SKILL.md`
  - `skills/project/spec-kit-setup/agents/openai.yaml`
  - `skills/project/spec-kit-setup/tests/scenarios.md`
- Added new project-level skill `spec-kit-workflow` for strict, stage-gated spec-kit execution with command normalization, artifact verification, rollback routing, and execution-log reporting:
  - `skills/project/spec-kit-workflow/SKILL.md`
  - `skills/project/spec-kit-workflow/agents/openai.yaml`
  - `skills/project/spec-kit-workflow/tests/scenarios.md`
- Added new TypeScript skills for downloader, JWT secret generation, Husky hooks, JSDoc development, NodeNext maintenance, and Winston logging:
  - `skills/typescript/typescript-file-downloader-module/SKILL.md`
  - `skills/typescript/typescript-file-downloader-module/agents/openai.yaml`
  - `skills/typescript/typescript-file-downloader-module/references/error-codes.md`
  - `skills/typescript/typescript-file-downloader-module/references/implementation-spec.md`
  - `skills/typescript/typescript-file-downloader-module/references/test-plan.md`
  - `skills/typescript/typescript-file-downloader-module/tests/scenarios.md`
  - `skills/typescript/typescript-generate-jwt-secret-env-setup/SKILL.md`
  - `skills/typescript/typescript-generate-jwt-secret-env-setup/agents/openai.yaml`
  - `skills/typescript/typescript-generate-jwt-secret-env-setup/reference.md`
  - `skills/typescript/typescript-generate-jwt-secret-env-setup/tests/scenarios.md`
  - `skills/typescript/typescript-husky-setup/SKILL.md`
  - `skills/typescript/typescript-husky-setup/agents/openai.yaml`
  - `skills/typescript/typescript-husky-setup/reference.md`
  - `skills/typescript/typescript-husky-setup/tests/scenarios.md`
  - `skills/typescript/typescript-jsdoc-develop/SKILL.md`
  - `skills/typescript/typescript-jsdoc-develop/agents/openai.yaml`
  - `skills/typescript/typescript-jsdoc-develop/examples.md`
  - `skills/typescript/typescript-jsdoc-develop/reference.md`
  - `skills/typescript/typescript-jsdoc-develop/tests/scenarios.md`
  - `skills/typescript/typescript-nodenext-apps-maintenance/SKILL.md`
  - `skills/typescript/typescript-nodenext-apps-maintenance/agents/openai.yaml`
  - `skills/typescript/typescript-nodenext-apps-maintenance/reference.md`
  - `skills/typescript/typescript-nodenext-apps-maintenance/scripts/nodenext-audit-imports.js`
  - `skills/typescript/typescript-nodenext-apps-maintenance/tests/scenarios.md`
  - `skills/typescript/typescript-winston-setup/SKILL.md`
  - `skills/typescript/typescript-winston-setup/agents/openai.yaml`
  - `skills/typescript/typescript-winston-setup/reference.md`
  - `skills/typescript/typescript-winston-setup/tests/scenarios.md`

### Changed

- Strengthened `git-review-orchestrator` to enforce explicit preflight checks before Gate A, including git availability, git-repo validation, and scope evidence collection.
- Clarified fail-fast gate sequencing and output contract requirements, including mandatory `Preflight` row ordering in the gate matrix, explicit `no_changes` handling, mandatory Gate D file updates, and required failure-diagnostics reporting for failed gates.
- Updated `git-review-orchestrator` agent interface metadata to align prompt/description wording with fail-fast preflight-first behavior.
- Expanded orchestrator scenario coverage with Gate D execution expectations and preflight-failure diagnostics.
- Updated `spec-kit-setup` to remove `gh`/`uv` preflight dependency and standardize GitHub Releases API plus direct HTTP download commands.

## [1.0.2] - 2026-02-24

### Added

- Added new NestJS skill `nestjs-vitest-setup` with workflow, interface metadata, references, examples, and scenario tests:
  - `skills/nestjs/nestjs-vitest-setup/SKILL.md`
  - `skills/nestjs/nestjs-vitest-setup/agents/openai.yaml`
  - `skills/nestjs/nestjs-vitest-setup/reference.md`
  - `skills/nestjs/nestjs-vitest-setup/examples.md`
  - `skills/nestjs/nestjs-vitest-setup/tests/scenarios.md`

### Changed

- Enhanced NestJS setup skills with broader scenario coverage and workflow updates for:
  - `skills/nestjs/nestjs-swagger-setup`
  - `skills/nestjs/nestjs-cqrs-setup`
  - `skills/nestjs/nestjs-bcryptjs-setup`
  - `skills/nestjs/nestjs-vitest-setup`
- Updated root `README.md` to reflect current domain coverage, including `nestjs`, `typescript`, and `python`.

## [1.0.1] - 2026-02-24

### Changed

- Updated repository documentation to reflect the current `skills/...` directory layout instead of legacy `.agents/skills/...` paths.
- Updated root `README.md` architecture and contribution path examples to use `skills/<domain>/<skill-name>/`.

## [1.0.0] - 2026-02-24

### Added

- Added new project-level skill `changelog-keepachangelog-update` with workflow, interface metadata, and scenario tests:
  - `.agents/skills/project/changelog-keepachangelog-update/SKILL.md`
  - `.agents/skills/project/changelog-keepachangelog-update/agents/openai.yaml`
  - `.agents/skills/project/changelog-keepachangelog-update/tests/scenarios.md`
- Added new project-level skill `readme-updater` with workflow, interface metadata, references, and scenario tests:
  - `.agents/skills/project/readme-updater/SKILL.md`
  - `.agents/skills/project/readme-updater/agents/openai.yaml`
  - `.agents/skills/project/readme-updater/references/enterprise-readme-checklist.md`
  - `.agents/skills/project/readme-updater/tests/scenarios.md`
- Added missing scenario coverage for `figma-make-always-check` to complete required skill companion files:
  - `.agents/skills/figma/figma-make-always-check/tests/scenarios.md`

### Changed

- Rewrote root `README.md` to an evidence-based enterprise structure, including explicit applicability markers for missing root runtime/deployment metadata.
