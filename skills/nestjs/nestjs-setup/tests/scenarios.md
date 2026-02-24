# Scenario Tests

## Easy: Scaffold a new NestJS app with npm

- Given an empty writable parent directory and Node compatible with current Nest CLI requirements
- When the assistant applies this skill with `projectPathOrName=api-service` and `packageManager=npm`
- Then it runs deterministic preflight checks, scaffolds with `npx @nestjs/cli@latest new api-service --package-manager npm --strict`, enters the generated root, and starts with `npm run start:dev`
- And it reports verification status for local HTTP response on `http://localhost:3000`

## Hard: Add NestJS inside an existing repository subpath using pnpm

- Given a git-initialized monorepo and a request to create `services/api`
- When the assistant applies this skill with `existingGitRepo=true` and `packageManager=pnpm`
- Then it includes `--skip-git`, scaffolds from the specified parent directory, keeps all follow-up commands in the generated Nest root, and uses pnpm-compatible scripts
- And it avoids destructive cleanup or repository reinitialization

## Edge: Block on missing required input and incompatible runtime

- Given no `projectPathOrName` is provided and local Node does not satisfy current CLI `engines.node`
- When the assistant starts the workflow
- Then it asks one precise clarification question for the missing project target and reports runtime incompatibility as a hard precondition failure
- And it does not run scaffold commands until both blockers are resolved

## Edge: SWC requested but partial install failure

- Given the project is scaffolded successfully and `useSwc=true`
- When SWC dependency installation fails due to registry/network issues
- Then the assistant reports the failure with exact command context, leaves existing non-SWC setup intact, and does not claim SWC verification passed
- And it provides the next deterministic retry command from project root