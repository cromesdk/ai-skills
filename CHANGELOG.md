# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-24-02

### Changed

- Updated repository documentation to reflect the current `skills/...` directory layout instead of legacy `.agents/skills/...` paths.
- Updated root `README.md` architecture and contribution path examples to use `skills/<domain>/<skill-name>/`.

## [1.0.0] - 2026-24-02

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
