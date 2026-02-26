# Scenario Tests

## Easy: Apply fixes in a NodeNext service with extensionless imports

- Given a TypeScript repository where `compilerOptions.module` is `nodenext`
- And `src/**/*.ts` contains extensionless relative imports like `./utils`
- When the assistant runs this skill
- Then it runs audit mode first and reports findings
- And in fix mode rewrites those relative imports to emitted `.js` specifiers
- And a follow-up audit reports zero remaining findings

## Hard: Mixed module file types with tests and path aliases

- Given a project using `moduleResolution: node16` with `.ts`, `.mts`, and `.cts` files
- And source files include relative imports, package imports, and TS path aliases
- When the assistant applies this skill
- Then it rewrites only relative imports to `.js`, `.mjs`, or `.cjs` based on file type
- And it does not alter package imports or non-relative alias specifiers
- And it includes test/spec directories when asked via multiple `--dir` flags

## Edge: Skill invoked on non-NodeNext project

- Given a repository where `module` and `moduleResolution` are not `nodenext|node16`
- When the assistant is asked to use this skill
- Then it stops at the detection gate
- And it reports that NodeNext/Node16 settings are required before this skill can run
- And it performs no import rewrites
