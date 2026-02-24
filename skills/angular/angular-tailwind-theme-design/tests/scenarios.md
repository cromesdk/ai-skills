# angular-tailwind-theme-design scenario tests

## Easy: Add first light/dark theme system to valid Angular 20 + Tailwind v4 app

### Input
User asks: "Add light/dark theming with light as default and a toggle."

### Expected behavior
- Validates Angular workspace files and confirms `@angular/core` major version `20`.
- Confirms Tailwind v4 is already wired with `@import "tailwindcss";`.
- Adds or repairs root and `.dark` token variables in the configured global stylesheet.
- Adds semantic utility classes (`bg-app`, `text-app`, `bg-surface`, `border-app`, `text-primary`).
- Implements theme initialization and toggle wiring with Light as default.
- Reports changed files and verification command outcomes.

## Hard: Existing custom styles and partial dark mode setup require non-destructive repair

### Input
User asks: "Refactor our current dark mode setup to token-based Tailwind v4 theme design."
Project state:
- Global stylesheet already contains unrelated custom rules.
- `.dark` exists but token names are inconsistent.
- A theme toggle exists but default mode behavior is incorrect.

### Expected behavior
- Preserves unrelated styles and component-specific CSS.
- Normalizes token naming to semantic variables while keeping style-file conventions.
- Enforces Light as default when no stored preference exists.
- Repairs toggle logic without introducing framework-specific lock-in wording.
- Verifies at least build status and reports results.

## Hard: Multiple style entries in angular.json

### Input
User asks: "Implement app-wide theme tokens."
Project state:
- `angular.json` includes multiple style entries (app styles + vendor styles).

### Expected behavior
- Resolves and edits only the primary application global stylesheet.
- Avoids destructive edits to vendor/third-party stylesheets.
- Reports which style file was selected and why.

## Edge case: Tailwind v4 not configured

### Input
User asks to implement theme design, but project has no working Tailwind v4 wiring.

### Expected behavior
- Detects missing or broken Tailwind v4 setup before theme edits.
- Routes to `angular-tailwind-setup` prerequisite workflow first.
- Stops with an explicit blocker if prerequisite cannot be completed safely.

## Edge case: Unsupported Angular version or missing workspace files

### Input
User asks to implement theme design in a non-Angular folder or unsupported Angular major.

### Expected behavior
- Stops before editing any files.
- Reports exact blocker (`angular.json`/`package.json` missing or Angular major not `20`).
- Leaves repository state unchanged.

## Edge case: Persistence disabled by user preference

### Input
User asks: "Add toggle, but do not store theme preference."

### Expected behavior
- Implements class-based runtime toggle behavior.
- Skips `localStorage` writes.
- Keeps Light as default on clean load unless user explicitly requests otherwise.
