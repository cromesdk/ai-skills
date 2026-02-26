---
name: nestjs-vitest-coverage
description: Upgrade and maintain Vitest coverage for NestJS backends, including provider package alignment, coverage configuration, scripts, thresholds, and test updates to meet enforced coverage goals. Use when a user asks to update Vitest, fix or add coverage, configure coverage providers/reporters/thresholds, or raise test coverage in a NestJS project.
---

# NestJS Vitest Coverage

Use this workflow to keep NestJS Vitest coverage current and reliable.

## 1. Audit current state

1. Verify current versions and coverage package alignment:

```bash
npm ls vitest @vitest/coverage-v8 @vitest/coverage-istanbul
```

2. Confirm where test config lives:
- `vitest.config.ts`, or
- `vite.config.ts` with a `test` block.

3. Check whether `package.json` has `test:cov` and whether coverage output is cleaned.

## 2. Upgrade packages

Prefer `v8` coverage unless the project explicitly needs Istanbul.

`v8` provider:

```bash
npm install -D vitest@latest @vitest/coverage-v8@latest
```

`istanbul` provider:

```bash
npm install -D vitest@latest @vitest/coverage-istanbul@latest
```

Keep Vitest and the selected coverage package on the same major version.

## 3. Configure coverage

Add or update the `coverage` block:

```typescript
coverage: {
  provider: 'v8',
  reporter: ['text', 'html', 'lcov'],
  reportsDirectory: 'coverage',
  include: ['src/**/*.ts'],
  exclude: [
    'node_modules',
    'dist',
    '**/*.spec.ts',
    '**/*.test.ts',
    'src/main.ts',
    '**/*.module.ts',
    'test/**',
  ],
  thresholds: {
    lines: 80,
    functions: 80,
    branches: 80,
    statements: 80,
  },
},
```

Guidelines:
- Set `provider` to match the installed package.
- Keep `text` for terminal feedback and `html` for local inspection.
- Add `lcov` for CI tools such as Sonar and Codecov.
- Use `include` to measure real source files instead of only executed files.
- Exclude only entrypoints, modules, test files, generated code, and tooling.

## 4. Ensure scripts are correct

Update `package.json` scripts:

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "test:cov": "vitest run --coverage"
  }
}
```

If a cleanup script exists, ensure coverage output is removed (for example `rimraf dist coverage .cache`).

## 5. Run and inspect coverage

1. Run:

```bash
npm run test:cov
```

2. Inspect:
- Terminal summary for low files and uncovered lines.
- `coverage/index.html` for branch-level gaps.

3. Confirm thresholds are enforced and fail below target.

## 6. Raise coverage by improving tests

Preferred approach: add or improve tests for uncovered project code.

For NestJS:
- Use `Test.createTestingModule` and mock dependencies with `vi.fn`.
- Add branch tests for success, failure, and edge paths.
- Cover guards, pipes, interceptors, and service error handling.
- In e2e suites, always close the app in `afterAll`.

Do not make coverage pass by excluding maintained source files.

## 7. Apply exclusions responsibly

Allowed exclusions:
- Generated clients (for example Prisma generated output)
- Framework entrypoints (`src/main.ts`)
- Thin wiring modules (`**/*.module.ts`)
- Test/setup files

Avoid excluding controllers, services, handlers, domain logic, and shared libraries.

## 8. Validate completion

- [ ] `npm run test:cov` passes
- [ ] Coverage directory exists and includes expected reporters
- [ ] Provider package matches config (`v8` or `istanbul`)
- [ ] Thresholds are enforced in config
- [ ] Coverage gains came from tests, not broad source exclusions

## Additional resources

- [reference.md](reference.md) - quick config and troubleshooting reference
- [../nestjs-vitest-setup/SKILL.md](../nestjs-vitest-setup/SKILL.md) - full NestJS Vitest setup and migration
- Vitest coverage docs: https://vitest.dev/guide/coverage.html
