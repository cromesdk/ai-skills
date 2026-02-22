---
name: angular-app-setup
description: Creates an Angular 20 app in the current root with strict TypeScript and CSS defaults. Use when the user asks to scaffold Angular 20 safely in place and verify build/test results.
metadata:
  clawdbot:
    emoji: "🅰️"
    requires:
      anyBins:
        - npx
        - npm
    os:
      - linux
      - darwin
      - win32
---

# Angular 20 App Setup
Create a production-ready Angular 20 app directly in the current directory with strict defaults and explicit safety checks.

## Purpose

Create a production-ready Angular 20 app directly in the current directory using strict defaults, while preventing unsafe scaffolding in the wrong folder.

## Use this skill when

- The user asks to create, initialize, or scaffold an Angular app.
- The user wants Angular 20 with strict TypeScript and minimal defaults.
- The user wants to scaffold in the current folder (no nested app directory).

## Do not use this skill when

- The user asks to add Angular into an existing non-empty project that should not be overwritten.
- The user asks for a different Angular major version.
- The user asks for a monorepo workspace strategy (Nx, multi-project workspace, custom builders).

## Required inputs

Ask the user for the project name when it is not explicitly provided.
Do not invent or infer a project name.

## Preflight safety checks (required)

Before running `ng new`:

1. Confirm current directory is the intended app root.
2. Check if folder is safe for in-place scaffolding using concrete rules:
   - Safe by default when only `.` and `..` are present.
   - Also safe when only expected scaffold-safe files exist (for example: `.git`, `.gitignore`, `README.md`, `LICENSE`).
   - Treat any existing app/workspace files (`angular.json`, `package.json`, `src/`) as non-empty and require explicit user confirmation before continuing.
3. If files already exist, explicitly confirm user wants in-place generation in this folder.
4. If target version is not 20, stop and ask whether to continue with this skill or use a version-specific flow.

Use one of these checks:

```bash
# Portable file listing for quick safety review
ls -la
```

```powershell
# Windows/PowerShell variant
Get-ChildItem -Force
```

## Root directory rule

Scaffold in the intended app root and keep all commands in that root.
Use `--directory .` so Angular CLI writes into the current folder instead of creating a nested subfolder.
If the current directory is not the intended app root, stop and ask the user to confirm or change directories before running scaffold commands.

## Scaffold command (baseline)

Use this command from the target root:

```bash
npx -y @angular/cli@20 new <project-name> --directory . --style=css --strict --skip-git --ai-config=none
```

Defaults:

- Package manager: `npm`
- Routing: Angular CLI prompt/default unless user specifies.
- Standalone: Angular CLI prompt/default unless user specifies.
- AI configuration: `none` unless user explicitly requests a supported value.

## Optional user-driven variants

Apply only when user explicitly asks:

- Change style extension (`--style=scss`, etc.).
- Force routing on/off (`--routing` or `--no-routing`).
- Change package manager (`--package-manager pnpm|yarn|bun|npm`).
- Set `--ai-config` to a supported value from `reference.md`.

## Verification

Run from app root:

```bash
npm run build
```

```bash
npm run test -- --watch=false
```

If tests are not configured yet, report that clearly and provide the next fix step instead of claiming success.
If build fails, report the exact failing command and first actionable error, then stop and ask user whether to debug now.
If tests fail, report failing suite/spec count and first actionable failure, then ask whether to proceed with fixes.

Optional checks for local confidence:

```bash
npx ng version
```

```bash
npx ng config cli.packageManager
```

## Output contract

After execution, report:

1. Exact command run.
2. Any prompts/flags chosen from defaults.
3. Build result.
4. Test result.
5. Files of interest created (for example: `angular.json`, `package.json`, `src/main.ts`).
6. Any follow-up action needed.

## Acceptance checklist

- Correctly triggers for Angular 20 setup requests.
- Does not assume a project name.
- Prevents unsafe generation in unintended folders.
- Uses in-place scaffolding (`--directory .`).
- Verifies with build and test commands.
- Reports outcomes with concrete command/results summary.

## Reference
[Angular 20 documentation](reference.md)

## Tips

- Prefer `npx -y @angular/cli@20` over global `ng` to avoid version drift.
- Always confirm folder intent when any non-scaffold files are present.
- Keep `--directory .` in every in-place scaffold command to avoid accidental nested folders.
- Do not infer project names from directory names; ask explicitly when missing.
- Keep `--ai-config=none` unless the user asks for a supported alternative.
- Use `npm run build` before tests to catch configuration issues faster.
- When `npm run test -- --watch=false` hangs in CI-like shells, add `--browsers=ChromeHeadless` only if the project already supports it.
