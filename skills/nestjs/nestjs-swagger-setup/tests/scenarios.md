# Scenario Tests

## Easy: Fresh Swagger install with defaults

- Given a NestJS app with `main.ts`, `AppModule`, and no Swagger wiring
- When the assistant applies this skill with default `SWAGGER_*` values
- Then it installs `@nestjs/swagger` and `@nestjs/config`, enables `ConfigModule.forRoot({ isGlobal: true })`, adds `setupSwagger(app)` before `listen(...)`, and creates required env keys
- And it verifies `http://localhost:3000/api/docs` plus `http://localhost:3000/openapi.json`

## Hard: Repair existing setup with global prefix enabled

- Given a NestJS app that already sets `app.setGlobalPrefix('api')` and contains partial Swagger configuration
- When the assistant is asked to fix broken JSON route behavior without rewriting unrelated bootstrap code
- Then it performs minimal edits, keeps existing architecture, and sets `SWAGGER_USE_GLOBAL_PREFIX=true` with a valid `SWAGGER_JSON_URL`
- And it verifies docs and JSON are reachable at prefixed routes

## Edge: Production lockdown requested

- Given a request to keep Swagger disabled in production while retaining development access
- When the assistant applies this skill
- Then it configures environment-driven toggles so production can set `SWAGGER_ENABLED=false` without code edits
- And it reports that no Swagger UI/raw endpoints should be exposed when disabled

## Edge: Missing Nest entry files

- Given the provided target path does not contain required Nest bootstrap files (`main.ts` and root module)
- When the assistant starts the workflow
- Then it stops before making edits, reports the missing-file blocker precisely, and asks for the correct project path
- And it does not claim Swagger setup verification passed

## Edge: Dependency install failure

- Given package installation fails due to registry or network errors
- When the assistant runs the dependency install step
- Then it reports the exact failing command and error context, avoids partial Swagger wiring, and provides deterministic retry guidance from project root
- And it leaves existing project behavior unchanged
