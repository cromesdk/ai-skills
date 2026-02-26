---
name: nestjs-typedoc-setup
description: Install and configure TypeDoc for NestJS backends using typedoc-material-theme, build docs from src entry points, and document public controllers/services/DTOs with JSDoc. Use when the user asks to add TypeDoc, generate API docs, update docs build scripts, or improve NestJS backend documentation quality.
---

# NestJS TypeDoc Install

Use this workflow to add TypeDoc documentation to a NestJS application.

## Prerequisites

- Use a NestJS backend with `src/main.ts` and a project `tsconfig.json`.
- Run commands from the Nest app root.
- Keep Node.js compatible with the Nest version in use (Nest 11 baseline is Node.js 20+).

## Install steps

1. Install TypeDoc and the default Material theme:

```bash
npm install --save-dev typedoc typedoc-material-theme
```

2. Create `typedoc.json` in the project root:

```json
{
  "entryPoints": ["src"],
  "out": "docs",
  "tsconfig": "tsconfig.json",
  "plugin": ["typedoc-material-theme"],
  "entryPointStrategy": "expand",
  "exclude": [
    "**/*.spec.ts",
    "**/*.test.ts",
    "dist/**",
    "node_modules/**"
  ],
  "excludePrivate": true,
  "excludeProtected": true,
  "cleanOutputDir": true
}
```

When Prisma is installed, always add `"**/prisma/generated/**"` to `exclude`.

3. Add scripts in `package.json`:

```json
"docs:api": "typedoc",
"docs:api:watch": "typedoc --watch"
```

4. Update `.gitignore` so generated docs are not committed unintentionally:

```gitignore
docs/
```

## Entry points

- Use `["src"]` for a full Nest app (controllers, services, DTOs, modules).
- Use `["src/main.ts"]` for a tighter surface when large internal folders should stay undocumented.
- Use `entryPointStrategy: "expand"` to include all matching files under each entry point.
- Use `exclude`, `excludePrivate`, and `excludeProtected` to keep internal code out of the docs.

## JSDoc conventions

- Use `@param` for parameter descriptions.
- Use `@returns` for return behavior.
- Use `@example` for realistic Nest usage snippets.
- Use `@remarks` for module/service context that is not obvious from types.
- Describe public API behavior, not type syntax.

See [examples.md](examples.md) for sample JSDoc and configs.

## Optional

- Add `themeColor` when using `typedoc-material-theme` to align docs branding.
- Add `typedoc-plugin-markdown` when markdown output is needed.
- Build docs in CI and optionally publish from `docs/`.

See [reference.md](reference.md) for full options and examples.

## Verification

1. Run `npm run docs:api`.
2. Confirm docs output exists in `docs/`.
3. Open `docs/index.html` and verify controllers/services/DTOs are rendered.
4. Confirm excluded test/build/generated files are absent.

## Checklist

- [ ] Install `typedoc` and `typedoc-material-theme`
- [ ] Add `typedoc.json` with Nest-focused entry points and excludes
- [ ] Add docs scripts to `package.json`
- [ ] Add `docs/` to `.gitignore`
- [ ] Run docs generation and verify output

## Additional resources

- TypeDoc options and CI notes: [reference.md](reference.md)
- NestJS-focused config and JSDoc examples: [examples.md](examples.md)
