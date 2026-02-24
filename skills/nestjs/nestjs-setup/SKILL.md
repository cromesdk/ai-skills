---
name: nestjs-typescript-setup
description: Installs and scaffolds NestJS with TypeScript using the Nest CLI with project-root-safe workflow, package-manager selection, strict TypeScript mode, optional SWC, and live version/runtime checks. Use when the user asks to install NestJS, bootstrap a new Nest backend, add Nest to a repository, or set up Nest with TypeScript.
---

# NestJS + TypeScript Install (Best Practice)

## Confirm inputs first

- Require a `project-name` when not explicitly provided. Do not assume one.
- Confirm package manager preference (`npm`, `pnpm`, `yarn`) when not explicit.
- If creating inside an existing git repository, add `--skip-git` to avoid nested repositories.

## Root directory

Installation must end in the Nest app root. Scaffold from the intended parent directory, then run all install and run commands from the generated project root.

## Prerequisites

- Node.js baseline from docs: `>= 20` ([First Steps - Prerequisites](https://docs.nestjs.com/first-steps#prerequisites)).
- Current `@nestjs/cli` runtime floor is `>= 20.11` (verify with `npm view @nestjs/cli engines --json`).

## Recommended path (default)

Use `npx` so you do not depend on a preinstalled global CLI:

1. Scaffold:
   - `npx @nestjs/cli@latest new project-name --package-manager npm --strict`
2. Enter project root:
   - `cd project-name`
3. Run in watch mode:
   - `npm run start:dev`
4. Verify:
   - open `http://localhost:3000` and confirm `Hello World!`

If the user chose `pnpm` or `yarn`, set `--package-manager` accordingly and use matching script commands.

## Existing repository integration

When adding Nest to a repository that already has git initialized:

1. Scaffold from the target parent directory.
2. Use `--skip-git` so `nest new` does not initialize another repository.
3. Keep all subsequent commands in the Nest app root.

Example:
- `npx @nestjs/cli@latest new services/api --package-manager pnpm --strict --skip-git`

## Alternatives

- Global CLI install:
  1. `npm i -g @nestjs/cli@latest`
  2. `nest new project-name --package-manager npm --strict`
- Git starter:
  1. `git clone https://github.com/nestjs/typescript-starter.git project-name`
  2. `cd project-name`
  3. `npm install`
  4. `npm run start:dev`

## Live version checks

Use these commands when version certainty matters:

- `npm view @nestjs/core version`
- `npm view @nestjs/cli version`
- `npm view @nestjs/cli engines --json`

Interpretation:
- Keep Nest packages on the same major version.
- Ensure local Node satisfies `@nestjs/cli` `engines.node` (currently `>= 20.11`).

## Run scripts

From project root:
- `npm run start` for one-shot run
- `npm run start:dev` for watch mode
- `npm run test` for unit tests
- `npm run lint` for lint checks

## Optional SWC builder (faster builds)

Follow [SWC docs](https://docs.nestjs.com/recipes/swc). From project root:

1. Install:
   - `npm i --save-dev @swc/cli @swc/core`
2. Set default builder in `nest-cli.json`:

```json
{
  "compilerOptions": {
    "builder": "swc",
    "typeCheck": true
  }
}
```

3. For one-off runs:
   - `nest start -b swc`
   - `nest start -b swc -w`
   - `nest start -b swc --type-check` when you need explicit type-check + plugin metadata behavior

## .gitignore

Ensure project root `.gitignore` includes at minimum:
- `dist/`
- `node_modules/`

Recommended additions:
- `.env`
- `.env.local`
- `*.log`
- `coverage/`
- `.DS_Store`
- `.idea/`
- `.vscode/`

See [reference.md](reference.md) for links and a minimal template.

## Verification checklist

- [ ] Scaffold succeeds with chosen package manager
- [ ] Commands run from Nest app root
- [ ] `npm run start:dev` starts successfully
- [ ] `http://localhost:3000` returns `Hello World!`
- [ ] Optional SWC path compiles and runs as expected

## Additional resources

For official docs and command references, see [reference.md](reference.md).
