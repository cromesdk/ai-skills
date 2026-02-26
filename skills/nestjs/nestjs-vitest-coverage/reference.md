# NestJS Vitest coverage reference

Quick reference for `nestjs-vitest-coverage`.

## Coverage block template

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
}
```

## Provider/package mapping

- `provider: 'v8'` -> `@vitest/coverage-v8`
- `provider: 'istanbul'` -> `@vitest/coverage-istanbul`
- Keep the same major version between `vitest` and the selected provider package.

## Common commands

```bash
npm ls vitest @vitest/coverage-v8 @vitest/coverage-istanbul
npm install -D vitest@latest @vitest/coverage-v8@latest
npm run test:cov
```

## Coverage repair order

1. Configure `include` and realistic `exclude` rules.
2. Run coverage and identify low files and uncovered branches.
3. Add tests for project logic first (services/controllers/handlers/libs).
4. Exclude only generated or framework wiring files.

## NestJS testing notes

- Use `Test.createTestingModule` for units and mocked dependencies.
- Cover both success and failure branches.
- For e2e tests, initialize and close `INestApplication` cleanly to avoid hanging workers.

## Links

- [Vitest coverage guide](https://vitest.dev/guide/coverage.html)
- [../nestjs-vitest-setup/SKILL.md](../nestjs-vitest-setup/SKILL.md)
