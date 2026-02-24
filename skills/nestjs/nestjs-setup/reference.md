# NestJS + TypeScript Reference

Use this file for official links and command details while applying the skill workflow.

## Official docs

- [First steps](https://docs.nestjs.com/first-steps)
- [Installation](https://docs.nestjs.com/#installation)
- [CLI overview](https://docs.nestjs.com/cli/overview)
- [Alternatives](https://docs.nestjs.com/#alternatives)
- [SWC builder recipe](https://docs.nestjs.com/recipes/swc)

## Live version checks

Use npm registry lookups to confirm current versions and runtime floor:

- `npm view @nestjs/core version`
- `npm view @nestjs/cli version`
- `npm view @nestjs/cli engines --json`

Interpretation:
- Keep Nest packages on the same major version.
- Docs baseline is Node `>= 20`.
- Enforce current CLI engine floor from `engines.node` (currently `>= 20.11`).

## Recommended scaffold command

Use this default command for new projects (no global CLI dependency):

- `npx @nestjs/cli@latest new project-name --package-manager npm --strict`

If scaffolding inside an already versioned repository, add:

- `--skip-git`

Example:

- `npx @nestjs/cli@latest new services/api --package-manager pnpm --strict --skip-git`

## Optional global CLI path

- `npm i -g @nestjs/cli@latest`
- `nest new project-name --package-manager npm --strict`

## SWC quick notes

- Install: `npm i --save-dev @swc/cli @swc/core`
- Set default in `nest-cli.json`:

```json
{
  "compilerOptions": {
    "builder": "swc",
    "typeCheck": true
  }
}
```

- One-off CLI usage: `nest start -b swc`, `nest start -b swc -w`
- Use `--type-check` when explicit type-check + plugin metadata behavior is needed.

## .gitignore

At minimum:
- `dist/`
- `node_modules/`

Recommended:
- `.env`
- `.env.local`
- `*.log`
- `coverage/`
- `.DS_Store`
- `.idea/`
- `.vscode/`
