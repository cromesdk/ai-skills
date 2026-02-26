# scenarios.md - typescript-winston-setup

## Easy: Fresh Winston install in a standard Nest app

### Input
User asks to add Winston logging to an existing NestJS TypeScript backend that has `src/app.module.ts` and `src/main.ts`.

### Expected behavior
- Detects active package manager and installs `winston` (and `@nestjs/config` only if missing).
- Adds `src/libs/logger/logger.module.ts` and `src/libs/logger/logger.service.ts` using `reference.md`.
- Wires `LoggerModule` in `AppModule` and `app.useLogger(app.get(LoggerService))` in `main.ts`.
- Adds/updates `.env` keys: `LOGGER_LEVEL`, `LOGGER_SERVICE_NAME`, `LOGGER_PATH`.
- Reports deterministic verification checks for development and production outputs.

## Hard: Repair broken Winston setup in NodeNext project

### Input
User reports existing Winston setup is broken: runtime import errors under `moduleResolution: nodenext`, missing exception/rejection logs, and missing required env values.

### Expected behavior
- Detects NodeNext/Node16 context and uses `.js` runtime import extensions where required.
- Ensures required env validation exists for `LOGGER_LEVEL`, `LOGGER_SERVICE_NAME`, and `LOGGER_PATH`.
- Ensures exception/rejection transports are configured and `OnModuleDestroy` cleanup detaches handlers.
- Preserves unrelated app behavior and avoids broad refactors.
- Verifies that `combined.log`, `error.log`, `exceptions.log`, and `rejections.log` are produced in expected conditions.

## Edge: Missing Nest entry files or wrong target path

### Input
User asks to set up Winston, but repository root does not contain `src/app.module.ts` and `src/main.ts`.

### Expected behavior
- Fails fast during preflight.
- Does not apply speculative edits in unknown paths.
- Asks for the correct Nest app directory or monorepo package target.
- Leaves repository unchanged until target is confirmed.

## Edge: Config package absent and install should be minimal

### Input
User already has `winston` installed but not `@nestjs/config`.

### Expected behavior
- Installs only `@nestjs/config`.
- Avoids reinstalling or changing unrelated dependencies.
- Proceeds with logger wiring and verification checklist.

## Edge: Production log-format mismatch

### Input
User says logs are still pretty-printed in production.

### Expected behavior
- Checks `NODE_ENV` handling and ensures production branch uses JSON console format.
- Confirms file transports always use JSON format regardless of environment.
- Provides concrete verification steps to reproduce and validate fix.

## Regression guard: Handler leak across test/module lifecycle

### Input
User observes listener leak warnings after repeated module initialization in tests.

### Expected behavior
- Ensures logger implements `OnModuleDestroy` and calls `exceptions.unhandle()`, `rejections.unhandle()`, and `logger.close()`.
- Confirms change specifically targets lifecycle cleanup without altering logging API contracts.