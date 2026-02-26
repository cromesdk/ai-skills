# Scenario Tests

## Easy: Fresh Husky + lint-staged setup in a TypeScript repo

- Given a Node.js TypeScript repository with `package.json`, Git initialized, and no `.husky` folder
- When the assistant applies this skill with default behavior
- Then it installs `husky` and `lint-staged`, initializes Husky, ensures a valid `prepare` script, and adds staged-file lint-staged rules for TypeScript files
- And `.husky/pre-commit` runs `npx lint-staged`

## Hard: Repair broken hook while preserving existing scripts

- Given a repository where `.husky/pre-commit` exists but runs invalid commands
- And `package.json` already has a complex `prepare` script and custom lint scripts
- When the assistant is asked to repair pre-commit behavior
- Then it performs minimal, non-destructive changes to restore working hook execution
- And it merges Husky prepare behavior without deleting existing script logic
- And it aligns lint-staged commands with tools already present in the repository

## Edge: Monorepo package mismatch and non-matching globs

- Given a monorepo where files are staged under `packages/*/src/**`
- And current lint-staged globs only match top-level `*.ts`
- When the assistant runs this skill
- Then it updates lint-staged patterns to match actual staged paths while keeping staged-file-only execution
- And it keeps pre-commit fast by avoiding full-project lint/test/coverage commands
- And if required tools are missing, it reports the blocking dependency explicitly instead of creating invalid commands
