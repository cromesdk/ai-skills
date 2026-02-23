# AI-Skills & Rules

A curated repository of reusable agent skills and operational rules, with a strong Angular 20 focus.  
Each skill is a focused workflow with deterministic steps, agent metadata, and scenario tests.

![Language](https://img.shields.io/badge/language-Markdown-000000?logo=markdown)
![Framework](https://img.shields.io/badge/framework-Angular%2020-DD0031?logo=angular&logoColor=white)
![Skills](https://img.shields.io/badge/skills-12-0A7EA4)
[![License](https://img.shields.io/badge/license-MIT-2EA44F)](./LICENSE)

## What This Repo Provides

- A local skill catalog under `.agents/skills/`.
- Angular 20-focused setup, architecture, quality, and tooling workflows.
- Skill organization by domain under `.agents/skills/angular/` and `.agents/skills/figma/`.
- A consistent skill contract per package:
  - `SKILL.md`
  - `agents/openai.yaml`
  - `tests/scenarios.md`

## Prerequisites

- A coding-agent environment that can load and execute `SKILL.md` instructions.
- Node.js + npm for skills that run Angular CLI or package-manager commands.

## Quick Start

1. Open this repo as your working directory.
2. Reference a skill directly in your prompt.

```text
[$angular-app-setup](.agents/skills/angular/angular-app-setup/SKILL.md)
Create an Angular 20 app in this folder named "shop-ui".
```

## Skills

| Skill | Purpose | Path |
|---|---|---|
| `angular-app-setup` | Create Angular 20 apps in-place with deterministic, non-interactive defaults. | `.agents/skills/angular/angular-app-setup/SKILL.md` |
| `angular-capacitor-setup` | Add or repair Capacitor integration for Angular projects. | `.agents/skills/angular/angular-capacitor-setup/SKILL.md` |
| `angular-component-rule` | Enforce companion-file and structure rules for Angular components. | `.agents/skills/angular/angular-component-rule/SKILL.md` |
| `angular-folder-structure` | Define and enforce feature-first Angular app architecture. | `.agents/skills/angular/angular-folder-structure/SKILL.md` |
| `angular-json-server-setup` | Add or repair local `json-server` mock API flows for Angular. | `.agents/skills/angular/angular-json-server-setup/SKILL.md` |
| `angular-lucide-icons-setup` | Install and verify `lucide-angular` icon wiring. | `.agents/skills/angular/angular-lucide-icons-setup/SKILL.md` |
| `angular-pwa-setup` | Add or repair Angular PWA support and service worker validation. | `.agents/skills/angular/angular-pwa-setup/SKILL.md` |
| `angular-runtime-i18n-setup` | Add or repair runtime language switching with persisted preference support. | `.agents/skills/angular/angular-runtime-i18n-setup/SKILL.md` |
| `angular-storybook-setup` | Install and align Storybook for Angular 20 + Tailwind workflows. | `.agents/skills/angular/angular-storybook-setup/SKILL.md` |
| `angular-supabase-connector-setup` | Create DI-first Supabase connector wiring with optional API adapter bridge. | `.agents/skills/angular/angular-supabase-connector-setup/SKILL.md` |
| `angular-tailwind-setup` | Install or repair Tailwind CSS v4 setup in Angular 20 workspaces. | `.agents/skills/angular/angular-tailwind-setup/SKILL.md` |
| `angular-vitest-setup` | Migrate Angular unit tests from Karma/Jasmine to Vitest. | `.agents/skills/angular/angular-vitest-setup/SKILL.md` |

## Repository Layout

```text
.agents/skills/
  angular/
    <skill-name>/
      SKILL.md
      agents/openai.yaml
      tests/scenarios.md
  figma/
    <skill-name>/
      SKILL.md
      agents/openai.yaml
      tests/scenarios.md
```

## Authoring Rules

- Keep each skill single-purpose and deterministic.
- Include explicit preflight checks before file edits.
- Keep instructions non-destructive by default.
- Update `tests/scenarios.md` whenever behavior changes.
- Keep `agents/openai.yaml` aligned with the current trigger intent and workflow.

## Contributing

1. Add or update skills in `.agents/skills/<domain>/<skill-name>/`.
2. Validate command/path accuracy in `SKILL.md`.
3. Add or revise `tests/scenarios.md` to cover easy, hard, and edge cases.
4. Update `agents/openai.yaml` so interface metadata matches behavior.
5. Open a PR with behavior deltas and verification notes.

## License

MIT. See `LICENSE`.
