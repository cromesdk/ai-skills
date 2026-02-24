# TSup Reference

## Official sources

- Repository and docs: https://github.com/egoist/tsup
- API/options index: https://www.jsdocs.io/package/tsup
- Successor project (migration context): https://tsdown.dev

## Practical option patterns

### Stable dual-format library outputs

Use explicit output extensions so `exports` paths stay deterministic:

```typescript
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['src/index.ts'],
  format: ['esm', 'cjs'],
  dts: true,
  outExtension({ format }) {
    return { js: format === 'cjs' ? '.cjs' : '.mjs' }
  },
})
```

### Multi-entry library

```typescript
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: {
    index: 'src/index.ts',
    cli: 'src/cli.ts',
  },
  format: ['esm', 'cjs'],
  dts: true,
})
```

Add matching subpath exports in `package.json` for each public entry.

### Dependency bundling behavior

- `external`: keep packages external.
- `noExternal`: force selected packages to be bundled.
- For Node apps, default to externalizing dependencies unless there is a deployment reason to inline them.

### Declaration generation

- Use `dts: true` for libraries.
- Keep declaration output aligned with `types` and `exports["."].types`.
- If declaration build fails, confirm TypeScript compiles cleanly and public entrypoints are valid.

## Troubleshooting

### Runtime cannot resolve built file

- Recheck generated filenames in `dist/`.
- Align `main`, `module`, and `exports` paths to actual output.
- If both CJS and ESM are emitted, prefer explicit `.cjs` and `.mjs` extensions.

### ESM/CJS mismatch

- Check `package.json.type`.
- If `type` is `module`, prefer ESM output for runtime entrypoints.
- If tooling expects CommonJS, keep `format: ['cjs']` or provide dual-format exports.

### Large bundles or unexpected inlining

- Audit `noExternal` and remove unnecessary entries.
- Disable minification until debugging is complete.
- Keep sourcemaps enabled while diagnosing production issues.

## Maintenance note

The tsup repository indicates maintenance mode and recommends tsdown for new long-term tooling decisions. Do not auto-migrate a user project; only propose migration when the user asks for it.
