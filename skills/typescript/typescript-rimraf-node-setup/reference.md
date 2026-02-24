# Rimraf reference

## Official documentation

- GitHub: https://github.com/isaacs/rimraf
- API and manual: https://isaacs.github.io/rimraf/

## CLI

```bash
rimraf <path> [path...]
```

- Remove each provided path recursively.
- Pass multiple paths to remove several outputs in one command.
- Quote glob arguments when used, for example `rimraf "dist/**" "*.tsbuildinfo"`.
- Use `--no-glob` when paths should be treated literally.

## package.json scripts

- In `package.json` scripts, call `rimraf` directly.
- For one-off terminal usage outside scripts, run `npx rimraf <path>`.

## Programmatic API

```javascript
import { rimraf, rimrafSync } from 'rimraf'

await rimraf('dist')
rimrafSync('dist')
```

- Use `rimraf` for async cleanup and `rimrafSync` for synchronous cleanup.
- Pass options as the second argument (`glob`, `preserveRoot`, `filter`, `signal`, and platform-specific retry options).
- Review the official docs for full option semantics and edge cases.

## Common cleanup targets

- `dist`
- `build`
- `coverage`
- `.cache`
- `.turbo`
- `*.tsbuildinfo`
