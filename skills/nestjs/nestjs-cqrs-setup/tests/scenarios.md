# Scenario Tests

## Easy: Fresh CQRS setup in existing Nest app

- Given a NestJS project with `src/main.ts`, `src/app.module.ts`, and no CQRS wiring
- When the assistant applies this skill with default `CQRS_ENABLED=true`
- Then it installs `@nestjs/cqrs` and `@nestjs/config`, adds `ConfigModule.forRoot({ isGlobal: true })`, and gates `CqrsModule.forRoot()` via `ConditionalModule.registerWhen(..., 'CQRS_ENABLED')`
- And it verifies the app boots and a minimal command/query handler path executes without DI errors

## Hard: Repair partial CQRS wiring with existing modules

- Given a project where `@nestjs/cqrs` is installed but feature modules inject `CommandBus` without consistent conditional imports
- When the assistant is asked to fix startup failures when CQRS is disabled
- Then it performs minimal edits to gate both CQRS infrastructure and CQRS-dependent modules with the same `CQRS_ENABLED` flag
- And it preserves unrelated module architecture and existing business logic

## Edge: Missing required Nest entry files

- Given a target directory that lacks `src/main.ts` or root module file
- When the assistant starts the workflow
- Then it stops before editing, reports the exact missing file blocker, and asks for the correct project path
- And it does not claim CQRS setup verification passed

## Edge: Dependency install failure

- Given package installation fails due to registry, auth, or network errors
- When the assistant runs dependency installation
- Then it reports the exact failing command and error context and stops before partial CQRS wiring
- And it provides deterministic retry commands from project root

## Edge: CQRS disabled boot verification

- Given CQRS modules and handlers are wired behind `CQRS_ENABLED`
- When `.env` sets `CQRS_ENABLED=false`
- Then the app still boots without `CommandBus`/`QueryBus`/`EventBus` injection failures
- And CQRS-dependent modules are not loaded unless alternative non-CQRS providers are intentionally configured