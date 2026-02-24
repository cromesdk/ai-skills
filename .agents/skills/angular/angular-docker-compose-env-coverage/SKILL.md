---
name: angular-docker-compose-env-coverage
description: Create, repair, and validate Dockerfile + docker-compose setups for Angular 20 applications, with explicit checks that variables declared in `.env` files are covered by compose configuration. Use when users ask to dockerize Angular 20, add or fix docker-compose, enforce `.env` variable coverage, or prevent missing runtime/build variables in containerized Angular environments.
---

# Angular 20 Docker Compose Env Coverage

## Goal

Build or fix a production-safe Angular 20 container setup and enforce that every variable defined in `.env` files is represented in `docker-compose` usage.

## Inputs

- `projectRoot` (default: current working directory)
- `composeFile` (optional, auto-detect when omitted)
- `envFiles` (optional, default: `.env` and `.env.*` except examples)
- `strictCoverage` (boolean, default: `false`)

## Success Criteria

- Angular 20 app has a valid Docker build path (`Dockerfile`).
- `docker-compose.yml` (or `.yaml`) exists and is valid.
- Every variable in targeted `.env` files is covered by compose.
- Coverage check is automated and repeatable.

## Workflow

1. Validate Angular workspace
- Confirm `package.json` and `angular.json` exist.
- Confirm `@angular/core` major version is `20`.
- Stop and report if the project is not Angular 20.

2. Create or repair Dockerfile for Angular 20
- Use multi-stage build by default.
- Stage 1: Node build (`npm ci`, `npm run build`).
- Stage 2: lightweight runtime (for example Nginx) serving built files.
- Keep build args and runtime environment handling explicit.

3. Create or repair `docker-compose`
- Ensure services, ports, build context, and image tags are coherent.
- Prefer explicit `environment` mappings for app-relevant variables.
- When `env_file` is used, keep file paths explicit and stable.

4. Enforce `.env` variable coverage
- Run:
```bash
python skills/custom/angular-docker-compose-env-coverage/scripts/check_env_compose_coverage.py --project-root .
```
- The script exits non-zero when variables are missing from compose coverage.
- In `strictCoverage` mode, require explicit environment wiring:
```bash
python skills/custom/angular-docker-compose-env-coverage/scripts/check_env_compose_coverage.py --project-root . --mode strict
```

5. Fix uncovered variables
- Add missing variables to compose `environment:` with explicit mapping (preferred), or ensure they are referenced via `${VAR}`.
- Re-run the script until it reports full coverage.

6. Verify container workflow
- Build and start services:
```bash
docker compose up --build
```
- Confirm containers start and Angular app is reachable.

## Guardrails

- Do not silently ignore missing variables.
- Do not rely on implicit assumptions about `.env` loading behavior.
- Keep variable names consistent across `.env`, compose, and any build args.
- Preserve unrelated compose services and existing user configuration.

## Script Behavior

`check_env_compose_coverage.py`:
- Detects compose file automatically unless overridden.
- Reads `.env` style files and extracts variable keys.
- Validates each key is covered in compose.
- Supports `referenced` mode (default) and `strict` mode.

Coverage definition:
- `referenced`: key is considered covered when compose references it (for example `${KEY}`), explicitly maps it in environment style lines, or includes the exact env file via `env_file`.
- `strict`: key is considered covered only when explicitly mapped in environment/argument style declarations.

## Definition of Done

- Dockerfile and compose are valid for Angular 20 deployment flow.
- Coverage script passes with requested mode.
- User can run one command to verify future changes.
