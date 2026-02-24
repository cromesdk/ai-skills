# angular-docker-compose-env-coverage scenario tests

## Easy: First-time Angular 20 dockerization with env coverage

### Input
User asks: "Dockerize this Angular 20 app with docker-compose and make sure `.env` variables are covered."

### Expected behavior
- Validates Angular workspace files and confirms `@angular/core` major version `20`.
- Creates or repairs `Dockerfile` using a multi-stage build.
- Creates or repairs a compose file with coherent service, build, and port settings.
- Runs coverage script in referenced mode and reports result.
- Runs compose model validation (`docker compose config`) before runtime startup.

## Hard: Existing compose stack with missing env mappings in strict mode

### Input
User asks: "Fix my compose setup and enforce strict coverage for all `.env` variables."

### Expected behavior
- Preserves unrelated compose services and user configuration.
- Runs coverage check in strict mode.
- Adds explicit environment mappings for missing keys rather than relying only on implicit loading.
- Re-runs strict coverage check until it passes.
- Reports exactly which variables were fixed and where.

## Hard: Multiple env files with exclusions and custom compose file

### Input
User asks: "Use `compose.yaml`, include `.env.local`, exclude `.env.example`, and verify coverage."

### Expected behavior
- Uses provided compose filename instead of auto-detection.
- Includes requested env files and respects exclusions.
- Applies coverage logic per selected mode and reports per-file pass/fail.
- Fails clearly when any selected key is not covered.

## Edge case: Not an Angular 20 workspace

### Input
User asks for dockerization, but `@angular/core` major version is not `20` or Angular workspace files are missing.

### Expected behavior
- Stops before Dockerfile/compose edits and before docker commands.
- Reports exact blocker (`package.json`/`angular.json` missing or version mismatch).
- Leaves existing files unchanged.

## Edge case: Docker engine unavailable

### Input
User asks for full verification, but Docker daemon is not running.

### Expected behavior
- Completes static checks and coverage verification.
- Attempts compose config/runtime validation and captures the Docker error.
- Reports verification as partially blocked with explicit next action to rerun runtime checks.
