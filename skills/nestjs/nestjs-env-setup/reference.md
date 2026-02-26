# Reference: EnvironmentModule, env utilities, env-sync (manual)

## EnvironmentModule

Global module that provides EnvironmentService. Depends on ConfigModule (ConfigService).

**src/libs/environment/environment.module.ts**

```typescript
import { Global, Module } from "@nestjs/common";
import { EnvironmentService } from "./environment.service.js";

@Global()
@Module({
  providers: [EnvironmentService],
  exports: [EnvironmentService],
})
export class EnvironmentModule {}
```

## EnvironmentService

Thin wrapper around ConfigService with typed getters. Add more getters to mirror keys used in the app (for example `LOGGER_PATH`, `SWAGGER_TITLE`).

**src/libs/environment/environment.service.ts**

```typescript
import { Inject, Injectable } from "@nestjs/common";
import { ConfigService } from "@nestjs/config";

@Injectable()
export class EnvironmentService {
  constructor(@Inject(ConfigService) private configService: ConfigService) {}

  get port(): number {
    const tmpPort: number | undefined = this.configService.get<number>("PORT");
    if (tmpPort === undefined) {
      throw new Error("PORT is not defined in the configuration");
    }
    return tmpPort;
  }
}
```

## Env utilities

Uses Node `path` and `fs`: `path.resolve(process.cwd(), ...)` for `.env` path, `fs.mkdirSync(dir, { recursive: true })` before writes when `.env` is under a subdir, `fs.existsSync` for existence checks.

**src/libs/environment/environment.utils.ts**

```typescript
import * as fs from "fs";
import * as path from "path";

const DEFAULT_PORT = 5000;
const DEFAULT_ENV_FILE = ".env";

export function addBasicEnvVariables(values: string[]): void {
  values.push("# Basic Environment Variables");
  values.push(`PORT=${DEFAULT_PORT}`);
  values.push("NODE_ENV=development");
  values.push("");
}

export function regenerateEnvironment(values: string[] = []): void {
  const envPath = path.resolve(process.cwd(), DEFAULT_ENV_FILE);
  const dir = path.dirname(envPath);
  if (dir !== process.cwd()) {
    fs.mkdirSync(dir, { recursive: true });
  }
  fs.writeFileSync(envPath, values.join("\n"));
}

export function environmentFileExists(): boolean {
  const envPath = path.resolve(process.cwd(), DEFAULT_ENV_FILE);
  return fs.existsSync(envPath);
}
```

## Env-sync (manual): regex and merge algorithm

This algorithm is assistant-agnostic. If teams use command files (for example `.cursor/commands/env-sync.md`), they should encode the same rules below.

### Regex patterns

- **ConfigService.get key** (single or double quotes, optional type param):
  - `configService\.get\s*<[^>]*>\s*\(\s*['"]([^'"]+)['"]`
  - Or without type: `\.get\s*\(\s*['"]([^'"]+)['"]`
  - Capture group 1 = variable name (for example `PORT`, `LOGGER_LEVEL`).

- **process.env key**:
  - `process\.env\.([A-Za-z_][A-Za-z0-9_]*)`
  - Capture group 1 = variable name.

Scan all `.ts` files under `src` (and optionally `test`) with these regexes and collect unique keys into a Set.

### Parse existing .env

- Read `.env` with `fs.readFileSync('.env', 'utf8')` if it exists.
- Line by line:
  - If line is empty or trimmed starts with `#`: treat as comment and keep as-is in output.
  - If line matches `KEY=value` (key: `[A-Za-z_][A-Za-z0-9_]*`, value: rest after first `=`): keep line as-is and add `KEY` to the existing key set.

### Merge

- Preserve existing line order exactly.
- For each discovered key from code scan that is not in existing keys, append `KEY=`.
- Never overwrite existing key values.
- Write with `fs.writeFileSync('.env', output)`.

### Pseudocode

```
discoveredKeys = new Set()
for each file in glob('src/**/*.ts') (+ optional 'test/**/*.ts'):
  content = readFile(file)
  for each match of configService.get regex: discoveredKeys.add(capture1)
  for each match of process.env regex: discoveredKeys.add(capture1)

existingLines = []
existingKeys = new Set()
if existsSync('.env'):
  for each line in readFileSync('.env').split('\n'):
    if line is comment or blank: existingLines.push({ type: 'raw', line })
    else if line matches KEY=value: existingKeys.add(KEY); existingLines.push({ type: 'var', line })
  end
end

out = []
for each item in existingLines: out.push(item.line)
for each key in sorted(discoveredKeys):
  if key not in existingKeys: out.push(key + '=')
writeFileSync('.env', out.join('\n'))
```
