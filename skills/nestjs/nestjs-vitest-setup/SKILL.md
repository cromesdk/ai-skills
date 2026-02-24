---
name: nestjs-vitest-setup
description: Install and configure Vitest for NestJS backends, migrate Jest-based Nest tests, and write or fix unit and e2e tests with @nestjs/testing, vi mocks/spies, and coverage. Use when a user asks to add Vitest to a Nest project, convert Jest scripts/config/tests, debug failing Nest tests under Vitest, or improve Nest test speed and reliability.
---

# NestJS Vitest

Use this workflow to set up and maintain NestJS tests with Vitest.

## Prerequisites

- Run commands from the Nest app root.
- Use Node.js 20+ for modern Nest projects.
- Keep Nest package major versions aligned.
- Keep `@nestjs/testing` and `supertest` available for module and e2e tests.

## Install and baseline config

1. Install dev dependencies:

```bash
npm install --save-dev vitest @vitest/coverage-v8 vite-tsconfig-paths
```

2. Create `vitest.config.ts`:

```typescript
import { defineConfig } from 'vitest/config'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [tsconfigPaths()],
  test: {
    globals: true,
    environment: 'node',
    include: ['src/**/*.spec.ts', 'test/**/*.e2e-spec.ts'],
    exclude: ['dist', 'node_modules'],
    setupFiles: ['test/vitest.setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html'],
      reportsDirectory: 'coverage',
    },
  },
})
```

3. Create `test/vitest.setup.ts`:

```typescript
import { afterEach, vi } from 'vitest'

afterEach(() => {
  vi.restoreAllMocks()
  vi.clearAllMocks()
})
```

4. Update `package.json` scripts:

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "test:cov": "vitest run --coverage",
    "test:e2e": "vitest run test/**/*.e2e-spec.ts"
  }
}
```

If the repository already uses path aliases in `tsconfig.json`, keep `vite-tsconfig-paths`. If no aliases are used, the plugin is optional.

## Migrate from Jest

Apply these substitutions in tests and helper files:

- `jest.fn` -> `vi.fn`
- `jest.spyOn` -> `vi.spyOn`
- `jest.mock` -> `vi.mock`
- `jest.clearAllMocks` -> `vi.clearAllMocks`
- `jest.restoreAllMocks` -> `vi.restoreAllMocks`
- `jest.useFakeTimers` -> `vi.useFakeTimers`
- `jest.useRealTimers` -> `vi.useRealTimers`
- `jest.setSystemTime` -> `vi.setSystemTime`

Then remove Jest-only configuration and scripts when no longer needed (`jest.config.*`, `ts-jest` transforms, and scripts that call Jest directly).

## NestJS test patterns

### Unit tests for providers/services

- Build a `TestingModule` with `Test.createTestingModule`.
- Mock dependencies via `useValue` and `vi.fn`.
- Keep behavior-focused assertions at the service boundary.

### Controller tests

- Test delegation and response shaping.
- Stub service methods with `vi.fn` instead of calling external systems.

### e2e tests

- Compile module imports, create `INestApplication`, and call `await app.init()`.
- Use `supertest` against `app.getHttpServer()`.
- Always close the app in `afterAll` to avoid open-handle hangs.

See concrete snippets in [examples.md](examples.md).

## Common pitfalls

- Path alias imports fail:
  - Add `vite-tsconfig-paths` and ensure aliases exist in `tsconfig.json`.
- Tests hang after completion:
  - Ensure `await app.close()` runs and fake timers are restored.
- Module mocks do not apply:
  - `vi.mock` is hoisted. Use patterns in [reference.md](reference.md) for factory and hoisted values.
- Decorator or reflection issues:
  - Keep `experimentalDecorators` and `emitDecoratorMetadata` consistent with the app tsconfig.

## Verification checklist

- [ ] `npm run test` passes
- [ ] `npm run test:e2e` passes
- [ ] `npm run test:cov` creates `coverage/`
- [ ] Jest-only scripts and config were removed or intentionally retained
- [ ] At least one unit and one e2e spec run cleanly under Vitest

## Additional resources

- Advanced config and migration notes: [reference.md](reference.md)
- Nest-focused example tests: [examples.md](examples.md)
