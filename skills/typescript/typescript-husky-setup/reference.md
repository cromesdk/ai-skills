# TypeScript Husky Setup Reference

## Optional: run tests in pre-commit

Add tests only when explicitly requested and keep the hook fast:

```sh
npx lint-staged
npm run test
```

Prefer `npm run test` over `npm run test:cov` in pre-commit.

## CI coverage enforcement

When coverage is not part of pre-commit, enforce it in CI.

Example (GitHub Actions):

```yaml
- name: Install
  run: npm ci
- name: Lint
  run: npm run lint
- name: Test with coverage
  run: npm run test:cov
```

## Monorepo note

If the repository is a monorepo, run hooks from the repo root and scope lint-staged globs/commands to the affected packages.
