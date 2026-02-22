## Scenarios

### Easy: Fresh Angular 20 app, no Tailwind
- User asks: "Set up Tailwind v4 in this Angular 20 project."
- Expected behavior:
  - Validate Angular major version is 20.
  - Install missing dev dependencies: `tailwindcss`, `@tailwindcss/postcss`, `postcss`.
  - Create or update PostCSS config with `@tailwindcss/postcss`.
  - Add `@import "tailwindcss";` to the global stylesheet.
  - Run build and report success with changed file list.

### Hard: Existing Tailwind v3-era setup needs migration
- User asks: "Fix this project; Tailwind classes are not working after upgrade."
- Project state:
  - Has `@tailwind base; @tailwind components; @tailwind utilities;`
  - Has outdated PostCSS plugin usage.
- Expected behavior:
  - Replace v3 directives with v4 import style.
  - Ensure PostCSS uses `@tailwindcss/postcss`, not legacy plugin config.
  - Preserve unrelated CSS and existing repo conventions.
  - Build passes and assistant reports exactly what changed.

### Hard: Manual dark mode and preflight exclusion requested
- User asks: "Enable class-based dark mode and disable preflight."
- Expected behavior:
  - Keep v4 setup.
  - Add `@custom-variant dark (&:where(.dark, .dark *));`.
  - Use layered imports to omit preflight.
  - Explain how to toggle dark mode via `.dark` class.

### Edge: Unsupported Angular major version
- User asks: "Install Tailwind v4 here."
- Project state:
  - `@angular/core` major is not 20.
- Expected behavior:
  - Abort without mutating files.
  - Return clear incompatibility message with detected version.

### Edge: Ambiguous or non-standard stylesheet configuration
- User asks: "Set up Tailwind."
- Project state:
  - `angular.json` has multiple style entries or custom builder pathing.
- Expected behavior:
  - Do not guess target stylesheet.
  - Either select unambiguous configured global stylesheet or stop with explicit blocker details.
  - Avoid destructive edits to custom builder settings.
