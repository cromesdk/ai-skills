# Scenarios: nestjs-env-setup

Use these scenarios to evaluate trigger quality, deterministic execution, portability, and safety.

## Easy: baseline ConfigModule setup

- Prompt: `Set up .env support in my NestJS app using ConfigModule and ConfigService.`
- Assumptions:
  - NestJS app exists.
  - Root module is `src/app.module.ts`.
- Expected outcome:
  - `@nestjs/config` installed with compatible Nest version.
  - Root module imports `ConfigModule.forRoot({ isGlobal: true })`.
  - No unrelated rewrites.
- Non-goals:
  - No typed wrapper module unless requested.

## Hard: NodeNext runtime import compatibility

- Prompt: `My Nest app uses nodenext. Fix env module imports correctly.`
- Assumptions:
  - `tsconfig.json` uses `moduleResolution: "nodenext"`.
  - Environment wrappers are used across files.
- Expected outcome:
  - Relative runtime imports in TS use `.js` suffixes.
  - No CommonJS-specific fallback advice.
  - Build/runtime import resolution is consistent.
- Non-goals:
  - No conversion of project module system.

## Hard: typed environment wrapper with required-key errors

- Prompt: `Create a typed EnvironmentService so required keys fail fast.`
- Assumptions:
  - `ConfigModule` already globally configured.
- Expected outcome:
  - `EnvironmentModule` and `EnvironmentService` added or updated.
  - Typed getters expose required keys.
  - Missing required key throws explicit error.
- Non-goals:
  - No schema validation framework unless requested.

## Edge: safe env-key sync preserving existing .env

- Prompt: `Sync my .env keys from ConfigService.get and process.env usage.`
- Assumptions:
  - `.env` already contains comments and existing values.
  - Source files contain additional env keys.
- Expected outcome:
  - Discovered keys are appended only when missing.
  - Existing values/comments/blank lines are preserved.
  - No existing key values are overwritten.
- Non-goals:
  - No secret value generation.

## Edge: ambiguous root module location

- Prompt: `Wire ConfigModule globally in this NestJS monorepo package.`
- Assumptions:
  - Multiple candidate modules exist.
- Expected outcome:
  - Assistant inspects project structure to identify the correct root module before editing.
  - If ambiguity remains, asks one precise clarification question with concrete candidates.
- Non-goals:
  - No broad monorepo restructuring.
