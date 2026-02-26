---
name: api-tests
description: Generate and maintain NestJS API end-to-end tests with Vitest and Supertest, including JWT login and protected-route coverage when authentication is configured. Use when adding or updating endpoint tests, creating e2e coverage for controllers, or implementing auth/JWT API test scenarios.
---

# NestJS API Tests (e2e)

## Workflow

1. Inspect project test setup (`package.json`, `vitest*.config.*`, `test/`).
2. Reuse the existing e2e runner and naming conventions.
3. Add or update `test/**/*.e2e-spec.ts` files by feature/controller.
4. Mirror production bootstrap behavior (global pipes/guards/interceptors that affect HTTP behavior).
5. Add JWT scenarios when auth is configured.
6. Run e2e tests and fix failures before finishing.

## Keep Existing Test Runner

- Reuse the repository's current test framework and config.
- Do not introduce a second e2e runner.
- Prefer one spec file per feature area:
  - `test/auth.e2e-spec.ts`
  - `test/users.e2e-spec.ts`
  - `test/<feature>.e2e-spec.ts`

## Mirror Production App Bootstrap

Apply the same app-level behavior as `src/main.ts` so tests match runtime behavior. At minimum, mirror `ValidationPipe` options and other global middleware that changes request/response behavior.

```typescript
import { ValidationPipe } from '@nestjs/common';
import { Test, TestingModule } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
import { AppModule } from '../src/app.module';

let app: INestApplication;

const moduleFixture: TestingModule = await Test.createTestingModule({
  imports: [AppModule],
}).compile();

app = moduleFixture.createNestApplication();
app.useGlobalPipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }));
await app.init();
```

Without this parity, DTO validation and status-code assertions can diverge from production.

## Detect JWT/Auth Usage

Treat auth as configured when at least one condition is true:
- `JWT_SECRET` (or equivalent token secret env key) is read by auth config/module code.
- A login endpoint returns an access token (for example `POST /auth/login`).
- One or more routes use auth guards (`AuthGuard`, passport guard, custom JWT guard).

If configured, include the JWT scenario matrix below.

## JWT Scenario Matrix

Add all of the following when JWT auth exists:

1. Valid login: send correct credentials, expect `200` and token field (`access_token` or project equivalent).
2. Invalid login: send wrong credentials, expect `401`.
3. Guarded route without token: expect `401`.
4. Guarded route with valid token: login first, send `Authorization: Bearer <token>`, expect success (`200`/`204` as applicable).
5. Guarded route with invalid or expired token: expect `401`.

## Token Handling Pattern

Use Supertest auth headers directly:

```typescript
const loginRes = await request(app.getHttpServer())
  .post('/auth/login')
  .send({ username: 'admin', password: 'admin123' })
  .expect(200);

const token = loginRes.body.access_token;

await request(app.getHttpServer())
  .get('/users/me')
  .set('Authorization', `Bearer ${token}`)
  .expect(200);
```

If login response keys differ (for example `token`), assert the real key used by the project.

## Environment and Data

- Ensure required auth env values exist for tests (`JWT_SECRET`, related expiry settings, DB URL).
- Use a dedicated test database when the app persists users/sessions.
- Run migrations (or schema push) before e2e when required by the stack.
- Use deterministic test credentials from seed/setup fixtures.

## Test Lifecycle and Assertions

- Initialize app in `beforeAll` (or `beforeEach` if isolation requires it).
- Always close app in `afterAll` (or `afterEach`) to avoid hanging handles.
- Assert both status code and response shape for each endpoint.
- Cover negative paths for validation and auth failures.

## Verification

- Run project e2e command (`npm run test:e2e` or repository equivalent).
- Ensure new tests pass with existing CI thresholds and lint rules.
- Keep tests stable (no hidden ordering dependencies, no real external calls).

## Additional Resources

- JWT detection rules and example snippets: [reference.md](reference.md)
