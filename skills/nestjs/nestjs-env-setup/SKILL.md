---
name: setup-nestjs-env
description: Configure NestJS environment handling with @nestjs/config and ConfigModule, including global config loading from .env, optional typed EnvironmentService wrappers, and optional AI-driven env key sync from source code. Use when users ask to add .env support, install ConfigModule/ConfigService, centralize env access, or keep .env keys aligned with code usage.
---

# NestJS env setup

Follow this workflow when applying environment configuration in an existing NestJS backend.

## Prerequisites

- Work in a NestJS project root that contains `src/` and a root module.
- Match package versions to the app's current Nest major version.
- Preserve existing user changes in `.env` and config files.

## 1) Install config package

Install `@nestjs/config` with the project's package manager.

```bash
npm install @nestjs/config
```

Install `@nestjs/common` only if the project is incomplete or missing core Nest packages.

## 2) Register ConfigModule globally

Update the root module (usually `src/app.module.ts`) to include:

```ts
ConfigModule.forRoot({ isGlobal: true })
```

Prefer this as the baseline. Add options only when needed by the user request or project pattern:

- `envFilePath` for non-default env file locations.
- `cache: true` for repeated config reads.
- `expandVariables: true` when values reference other env vars.

## 3) Keep env access centralized (optional but recommended)

If the project needs typed accessors, add a global `EnvironmentModule` and `EnvironmentService` wrapper around `ConfigService`.

Use `reference.md` for concrete implementation and file layout:

- `src/libs/environment/environment.module.ts`
- `src/libs/environment/environment.service.ts`
- `src/libs/environment/environment.utils.ts`

Expose typed getters (for example `port`) and throw explicit errors for required missing variables.

## 4) Handle NodeNext and ESM correctly

If `tsconfig.json` uses `moduleResolution: "nodenext"` or `"node16"`, use emitted `.js` extensions in relative TypeScript imports.

Examples:

- `./environment.service.js`
- `./libs/environment/environment.module.js`

Use the reference implementation as the source of truth for this case.

## 5) Add env-sync command (optional)

When the user asks to sync `.env` from code usage, create a Cursor command file (for example `.cursor/commands/env-sync.md`) that instructs the AI to:

- Scan `src/**/*.ts` (and optionally `test/**/*.ts`).
- Collect keys from `configService.get('KEY')` and `process.env.KEY`.
- Merge discovered keys into `.env` without overwriting existing values.

Use `reference.md` for regex patterns and merge behavior.

## 6) Protect secrets and verify behavior

- Ensure `.env` is in `.gitignore`.
- Never commit real secret values.
- Start the app and confirm required config values resolve at runtime.
- If env-sync is enabled, run it once and confirm only missing keys are appended.

## Validation checklist

- [ ] `@nestjs/config` is installed with matching Nest major version.
- [ ] Root module imports `ConfigModule.forRoot({ isGlobal: true })`.
- [ ] Optional EnvironmentModule/EnvironmentService are wired when typed access is needed.
- [ ] NodeNext/ESM projects use `.js` relative import extensions.
- [ ] `.env` is ignored by git and secrets are not committed.
- [ ] Env sync workflow (if requested) preserves existing `.env` values.

## References

- Environment module/service/utilities and env-sync algorithm: [reference.md](reference.md)
- Template `.env` and sample sync output: [examples.md](examples.md)
