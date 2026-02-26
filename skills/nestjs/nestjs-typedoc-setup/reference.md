# NestJS TypeDoc reference

Extended options and optional features for NestJS API documentation.
Official docs: https://typedoc.org

## Default theme (typedoc-material-theme)

- Install: `npm install --save-dev typedoc-material-theme` (alongside `typedoc`).
- Configure: add `"typedoc-material-theme"` to the `plugin` array.
- `themeColor`: optional Material 3 source color hex (for example `"#cb9820"`).
- Links: [npm](https://www.npmjs.com/package/typedoc-material-theme), [GitHub](https://github.com/dmnsgn/typedoc-material-theme).

Use built-in themes (`default`, `minimal`) only when not using the material theme.

## Markdown plugin

- Install: `npm install --save-dev typedoc-plugin-markdown`.
- Configure: add `"typedoc-plugin-markdown"` to `plugin`.
- Use when markdown output is needed for wikis or static-site pipelines.
- Plugin options: https://typedoc-plugin-markdown.org/docs/options

## CI

- Build docs with `npx typedoc` or `npm run docs:api`.
- Use `"cleanOutputDir": true` so each build starts from a clean output folder.
- Publish `docs/` (or custom `out`) via GitHub Pages or another static host.

## NestJS-oriented excludes

Use these defaults for Nest backends:

- `"**/*.spec.ts"`
- `"**/*.test.ts"`
- `"dist/**"`
- `"node_modules/**"`

When Prisma is installed, always add:

- `"**/prisma/generated/**"`

## Options summary

| Option | Purpose |
|--------|---------|
| `entryPoints` | Entry file(s) or directories, for example `["src"]` or `["src/main.ts"]`. |
| `entryPointStrategy` | `"expand"` for full source expansion or `"resolve"` for merged entry behavior. |
| `out` | Output directory for generated docs (for example `"docs"`). |
| `tsconfig` | Path to tsconfig (for example `"tsconfig.json"`). |
| `plugin` | TypeDoc plugins, including `"typedoc-material-theme"`. |
| `themeColor` | Material 3 source color hex when using `typedoc-material-theme`. |
| `exclude` | Glob patterns to exclude test/build/generated code. |
| `excludePrivate` | Omit private members from docs. |
| `excludeProtected` | Omit protected members from docs. |
| `cleanOutputDir` | Remove output directory before generation. |

For the full option list, see: https://typedoc.org/documents/Options.html
