# Scenario Tests

## Easy: Fresh bcryptjs setup in existing NestJS app

- Given a NestJS backend with `src/main.ts`, `src/app.module.ts`, and no encryption utility
- When the assistant applies this skill
- Then it installs `bcryptjs` and `@types/bcryptjs`, ensures `ConfigModule.forRoot({ isGlobal: true })`, and adds `EncryptionService` plus global `EncryptionModule`
- And it verifies `hash` and `verify` behavior with passing build and test commands

## Hard: Repair partial hashing implementation

- Given a project with `bcryptjs` installed but ad hoc hashing logic spread across services and no centralized module export
- When the assistant is asked to standardize hashing
- Then it performs minimal edits to introduce a reusable `EncryptionService` and `EncryptionModule` without breaking unrelated module wiring
- And it preserves existing business logic while replacing duplicate hash/compare snippets with service usage

## Edge: Missing NestJS entry files

- Given the target path lacks `src/main.ts` or `src/app.module.ts`
- When the workflow starts
- Then the assistant stops before editing, reports the exact missing file path, and asks for the correct backend root
- And it does not claim setup or verification success

## Edge: Invalid SALT_ROUNDS value

- Given `.env` has `SALT_ROUNDS` missing, non-numeric, or out of accepted range
- When the app boots and the service parses configuration
- Then startup fails fast with a clear error from `EncryptionService`
- And the assistant reports the required valid range and corrective `.env` value format

## Edge: Dependency installation failure

- Given package installation fails due to registry/network/auth issues
- When dependency install commands are executed
- Then the assistant reports the exact failing command and error context
- And it stops before partial code wiring and provides deterministic retry commands from project root
