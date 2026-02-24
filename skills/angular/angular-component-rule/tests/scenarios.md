# Scenarios: angular-component-rule

## Easy

### 1) Missing companions, Storybook not installed
User request:
"Run `$angular-component-rule` and fix missing component companion files."

Setup:
- `src/app/button/button.component.ts` exists
- Missing `button.component.html`, `button.component.spec.ts`, and any style file
- No `@storybook/angular` dependency, no `.storybook/`, no storybook scripts
- `angular.json` component style configured as `scss`

Expected:
- Creates `button.component.html`, `button.component.spec.ts`, and `button.component.scss`
- Does not create `button.component.stories.ts`
- Reports Storybook as `not installed` with reason
- Reports style decision as `scss` with reason
- Reports created file paths as absolute or workspace-root-resolved concrete paths

### 2) Existing compatibility style preserved
User request:
"Audit components and add only what is missing."

Setup:
- `src/app/card/card.component.ts` exists
- `card.component.css` already exists
- Preferred style resolved to `scss`

Expected:
- Keeps `card.component.css` as valid (no forced conversion)
- Creates only missing files (`.html`, `.spec.ts`, conditional `.stories.ts`)
- Report explicitly references compatibility rule

### 3) No components in scope
User request:
"Run `$angular-component-rule`."

Setup:
- `src/app/**` exists but contains no `*.component.ts` files

Expected:
- Makes no file changes
- Reports `Total components scanned: 0`
- Provides a complete report with zeroed summaries (not placeholders)

## Hard

### 4) Multi-project style ownership
User request:
"Apply the component rule across this workspace."

Setup:
- Two Angular projects in `angular.json` with different style defaults
- `apps/admin/src/app/a.component.ts` belongs to project style `scss`
- `apps/portal/src/app/b.component.ts` belongs to project style `css`
- Both components missing style companions

Expected:
- Creates `a.component.scss` and `b.component.css`
- Uses project path ownership (`root`/`sourceRoot`) before global fallback
- Report includes reason for each style decision path

### 5) Storybook installed by script only
User request:
"Repair component companions and story files."

Setup:
- No `.storybook/` directory
- No direct `@storybook/angular` package
- `package.json` includes `storybook` script
- `src/app/tag/tag.component.ts` missing `tag.component.stories.ts`

Expected:
- Detects Storybook as installed via script condition
- Creates `tag.component.stories.ts`
- Report includes detection reason

## Edge Cases

### 6) Multiple `@Component` classes in one file
User request:
"Fix all component issues automatically."

Setup:
- `src/app/bad/bad.component.ts` contains two `@Component` classes

Expected:
- Does not auto-split the file
- Marks item as unfixable automatically with manual follow-up steps
- No destructive edits

### 7) Inline template/styles and host class migration ambiguity
User request:
"Externalize inline metadata and enforce rules."

Setup:
- `src/app/legacy/legacy.component.ts` uses inline `template`, inline `styles`, and `host.class`
- Template has multiple candidate root nodes; safe host-class migration target is ambiguous

Expected:
- Performs deterministic extraction only when safe
- Creates companions when needed and updates metadata links where unambiguous
- Leaves ambiguous host-class migration as manual follow-up with exact file location

### 8) Variant declarations inline with ambiguous extraction
User request:
"Move variants into `.component.variants.ts`."

Setup:
- `src/app/chip/chip.component.ts` contains variant constants/types intertwined with unrelated logic

Expected:
- Creates `chip.component.variants.ts` only when safe extraction is clear
- If ambiguous, does not rewrite; reports exact declarations needing manual extraction
- Preserves runtime behavior and public API naming for any moved symbols

## Failure Handling

### 9) Missing `package.json` or malformed `angular.json`
User request:
"Run the component rule."

Setup:
- `package.json` missing or unreadable
- `angular.json` malformed JSON

Expected:
- Continues with best available fallback rules where possible
- Reports detection limitations clearly
- Does not fabricate environment assumptions

### 10) Both config files unreadable
User request:
"Apply the component rule and auto-fix what you can."

Setup:
- `package.json` unreadable
- `angular.json` unreadable
- Repository style counts unavailable (permission or I/O failure)

Expected:
- Uses safe default `styleExt = css`
- Continues scanning and companion-file creation
- Reports explicit fallback path used (`primary` -> `secondary` -> `tertiary` -> default `css`)
