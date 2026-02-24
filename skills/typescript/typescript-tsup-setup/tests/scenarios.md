# Scenario Tests

## Easy: Add tsup to a basic library

- Given a TypeScript library with `package.json`, `src/index.ts`, and no tsup config
- When the assistant applies this skill with defaults for `targetKind=library`
- Then it installs `tsup` as a dev dependency, creates `tsup.config.ts`, adds `build` (and optional `build:watch`) scripts, and verifies `dist` artifacts are produced
- And `package.json` library entry fields (`main`, `module`, `types`, `exports`) align with emitted files

## Hard: Repair existing dual-format library without destructive rewrite

- Given a project that already has a non-trivial `tsup.config.ts` plus custom scripts
- When the assistant is asked to fix broken CJS/ESM exports and keep advanced options
- Then it performs minimal edits, preserves unrelated options/scripts, and only updates fields required to restore deterministic output and runtime resolution
- And it verifies that generated files match declared `exports` paths

## Edge: Monorepo package-level execution and missing entry

- Given a monorepo where tsup must be configured inside a package subdirectory
- And the package's requested entry file does not exist
- When the assistant runs this skill
- Then it works from the package directory, reports the missing entry as a blocking precondition, and avoids writing an invalid config
- And it does not modify module system (`package.json.type`) unless explicitly requested
