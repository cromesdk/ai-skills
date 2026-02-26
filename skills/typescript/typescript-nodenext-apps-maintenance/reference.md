# NodeNext Reference

## Official sources

- TypeScript TSConfig `moduleResolution`: https://www.typescriptlang.org/tsconfig/moduleResolution.html
- TypeScript TSConfig `module`: https://www.typescriptlang.org/tsconfig/module.html
- TypeScript 4.7 ESM in Node.js: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-7.html
- Node.js package system (`"type"` field): https://nodejs.org/api/packages.html#type

## tsconfig applicability

Treat this skill as applicable when either of these is set to `nodenext` or `node16`:

```json
{
  "compilerOptions": {
    "module": "nodenext",
    "moduleResolution": "nodenext"
  }
}
```

`node16` follows the same Node-integrated module resolution model for this use case.

## Relative import extension behavior

In Node ESM contexts, relative import specifiers must include the file extension at runtime. For TypeScript source in NodeNext/Node16 projects, rewrite relative imports to the emitted extension:

- `.ts` / `.tsx` -> `.js`
- `.mts` -> `.mjs`
- `.cts` -> `.cjs`

## package.json `type` nuance

- Without `"type"`, `.js` is treated as CommonJS by Node.
- With `"type": "module"`, `.js` is treated as ESM by Node.

This changes runtime interpretation of `.js` files, but not the need for explicit extensions in relative ESM-style import specifiers.

## Practical edge cases

- `index` imports: prefer explicit `./dir/index.js` when resolver behavior is ambiguous.
- Path separators: use forward slashes in import specifiers, including on Windows.
- Test files: apply the same rule only when test files compile under NodeNext/Node16 tsconfig settings.
