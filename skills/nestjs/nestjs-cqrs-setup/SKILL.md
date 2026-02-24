---
name: nestjs-cqrs-setup
description: Install and configure @nestjs/cqrs in NestJS with environment-driven enable or disable using @nestjs/config and CQRS_ENABLED. Use when the user asks to add CQRS, CommandBus, QueryBus, EventBus, command or query handlers, or gate CQRS modules by environment.
---

# NestJS CQRS Setup

Use this workflow to add CQRS and keep it safely toggled by environment.

## Prerequisites

- NestJS backend with a root module (`AppModule`) and `main.ts`.
- Use Node.js 20+ for Nest 11 projects (or follow the repository's current runtime requirement).
- Keep Nest, `@nestjs/cqrs`, and `@nestjs/config` major versions aligned.

## Install steps

1. Install packages from project root:

   ```bash
   npm install @nestjs/cqrs @nestjs/config
   ```

2. Verify version alignment:
- Nest 11 -> `@nestjs/cqrs` ^11 and `@nestjs/config` ^4
- Nest 10 -> `@nestjs/cqrs` ^10 and `@nestjs/config` ^3
- Resolve peer dependency warnings before wiring CQRS.

## Env control

Single flag: `CQRS_ENABLED`

- `true` or unset: CQRS is enabled.
- `false`: CQRS is disabled.

Use `ConditionalModule.registerWhen(...)` from `@nestjs/config` to avoid reading `.env` at module load time.

## CQRS wiring (recommended)

1. In `AppModule`, add `ConfigModule.forRoot({ isGlobal: true })`.
2. In the same `imports` array, add:
   - `ConditionalModule.registerWhen(CqrsModule.forRoot(), 'CQRS_ENABLED')`
3. Keep CQRS handlers in feature modules as providers and import `CqrsModule` where those handlers are declared.
4. If CQRS is disabled, avoid loading modules that inject `CommandBus`, `QueryBus`, or `EventBus`. Gate those modules with the same `ConditionalModule.registerWhen(...)` pattern.

Full snippets are in [reference.md](reference.md) and [examples.md](examples.md).

## NodeNext / ESM

If the project uses `"moduleResolution": "nodenext"` or `"node16"`, use emitted `.js` extensions in relative TypeScript imports (for example, `./items/commands/create-item.command.js`).

## Verification

1. Set `CQRS_ENABLED=true` in `.env`, run the app, and confirm it boots without CQRS DI errors.
2. Execute a minimal command and query flow (see [examples.md](examples.md)); confirm handlers run.
3. Set `CQRS_ENABLED=false` and restart.
4. Confirm CQRS-gated modules are not loaded and the app still boots.

## Checklist

- [ ] Install `@nestjs/cqrs` and `@nestjs/config`
- [ ] Align package major versions with the Nest major version
- [ ] Add `ConfigModule.forRoot({ isGlobal: true })`
- [ ] Add `ConditionalModule.registerWhen(CqrsModule.forRoot(), 'CQRS_ENABLED')`
- [ ] Create or update `.env` with `CQRS_ENABLED=true|false`
- [ ] Gate CQRS-consuming modules when disabled
- [ ] Verify command and query execution with [examples.md](examples.md)

## Additional resources

- AppModule wiring and conditional imports: [reference.md](reference.md)
- `.env` and minimal command/query examples: [examples.md](examples.md)
