# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
