---
name: nestjs-swagger-setup
description: Install and configure OpenAPI docs in NestJS using @nestjs/swagger with environment-driven SWAGGER_* settings, optional bearer auth, and safe defaults for UI/raw docs exposure. Include an explicit OpenAPI JSON endpoint (default `openapi.json`) and an automatic Swagger UI "Download OpenAPI" button. Use when the user asks to install Swagger, add API documentation endpoints, or wire OpenAPI in a Nest backend.
---

# NestJS Swagger Install

Use this workflow to add Swagger UI and OpenAPI JSON endpoints in a Nest app.

## Prerequisites

- Have a NestJS app with a root module (`AppModule`) and `main.ts`.
- Use Node.js >= 20 (Nest 11 baseline).
- Keep Nest and `@nestjs/swagger` major versions aligned.

## Install steps

1. Install packages from project root:

   ```bash
   npm install @nestjs/swagger @nestjs/config
   ```

2. Verify version alignment:
   - Nest 11 -> `@nestjs/swagger` ^11
   - Nest 10 -> `@nestjs/swagger` ^10
   - `@nestjs/config` should match supported Nest peer ranges.
3. Resolve any peer dependency warnings before wiring docs.

## ConfigModule

Import `ConfigModule` in `AppModule` so `ConfigService` is available at bootstrap:

- Add `ConfigModule.forRoot({ isGlobal: true })` to the `imports` array of `AppModule`.
- Keep `.env` loading global unless the project already has a different config strategy.

## Swagger wiring

1. Create a reusable setup function using [reference.md](reference.md):
   - `src/libs/swagger/setup-swagger.ts`
2. In `main.ts`, call `setupSwagger(app)` after app creation and before `app.listen(...)`.
3. Prefer bootstrap-level setup over creating an extra global Swagger module/service unless the project architecture explicitly needs it.

## .env setup

Create or update `.env` in the project root. Do not commit secrets; ensure `.env` is in `.gitignore`.

Use this template (defaults match the reference implementation):

```env
PORT=3000

# Swagger (OpenAPI)
SWAGGER_ENABLED=true
SWAGGER_PATH=api/docs
SWAGGER_TITLE=API
SWAGGER_DESCRIPTION=HTTP API documentation
SWAGGER_VERSION=1.0.0
SWAGGER_UI_ENABLED=true
SWAGGER_RAW_ENABLED=true
SWAGGER_JSON_URL=openapi.json
SWAGGER_USE_GLOBAL_PREFIX=false

# Optional: enable bearer auth scheme in docs
SWAGGER_BEARER_AUTH=false
```

UI default:
- The Swagger setup includes an automatic top-bar `Download OpenAPI` button that points to the generated JSON schema route.

Security defaults:
- Set `SWAGGER_ENABLED=false` in production unless docs must be public.
- If docs stay enabled in production, protect the route (gateway auth, app guard, or IP allowlist).
- Do not use JWT secrets as feature flags for Swagger behavior.

## Optional: CLI plugin

For larger projects, enable the Swagger CLI plugin to reduce DTO decorator boilerplate:
- Add `@nestjs/swagger` plugin under `compilerOptions.plugins` in `nest-cli.json`.
- Keep runtime validators (`class-validator`) in DTOs.
- Import mapped type utilities from `@nestjs/swagger` so schemas are generated correctly.

## Verification

1. Run the app (e.g. `npm run start:dev`).
2. Open docs route:
   - `http://localhost:PORT/SWAGGER_PATH`
3. Open raw JSON:
   - `http://localhost:PORT/SWAGGER_JSON_URL` (when `SWAGGER_RAW_ENABLED=true` and `SWAGGER_USE_GLOBAL_PREFIX=false`)
   - `http://localhost:PORT/<global-prefix>/SWAGGER_JSON_URL` (when `SWAGGER_USE_GLOBAL_PREFIX=true`)
4. Confirm UI and/or raw endpoints match toggles (`SWAGGER_UI_ENABLED`, `SWAGGER_RAW_ENABLED`).
5. If `SWAGGER_BEARER_AUTH=true`, confirm "Authorize" is shown.
6. Confirm the automatic `Download OpenAPI` button is visible in the Swagger UI top bar.

## Checklist

- [ ] Install `@nestjs/swagger` and `@nestjs/config`; align major versions
- [ ] Enable `ConfigModule.forRoot({ isGlobal: true })`
- [ ] Add `setupSwagger(app)` from [reference.md](reference.md) and call it in `main.ts`
- [ ] Create or update `.env` with `SWAGGER_*` keys
- [ ] Ensure `.env` is listed in `.gitignore`
- [ ] Verify UI and JSON endpoints at configured routes
- [ ] Verify automatic `Download OpenAPI` button appears in Swagger UI

## Additional resources

- Full implementation with env toggles: [reference.md](reference.md)
- Minimal AppModule/main.ts snippets: [examples.md](examples.md)

