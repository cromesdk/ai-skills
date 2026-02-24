# Figma Lucide Angular Bridge - Scenario Tests

## Purpose

Validate deterministic substitution of Lucide assets to `lucide-angular` without breaking existing Angular conventions or non-Lucide asset handling.

## Scenario 1 - Easy: Known Lucide icon with package installed

### User prompt

Implement this Figma button in Angular and use Lucide icons where possible.

### Preconditions

- `package.json` includes `lucide-angular`.
- Figma icon name is `chevron-left`.

### Expected behavior

- Icon is mapped to `ChevronLeft`.
- Implementation uses `lucide-angular` instead of downloading an SVG for that icon.
- Accessibility label is present.

### Failure conditions

- Downloads a Lucide SVG even though mapping is available.
- Introduces bulk icon import.

## Scenario 2 - Hard: Mixed icon set with partial Lucide coverage

### User prompt

Build a card list from Figma with `circle-check`, a brand logo icon, and a custom illustration.

### Preconditions

- `package.json` includes `lucide-angular`.

### Expected behavior

- `circle-check` is mapped to `CircleCheck` and rendered via `lucide-angular`.
- Brand logo and illustration remain standard assets.
- Non-icon UI structure is unchanged.

### Failure conditions

- Converts non-Lucide brand/illustration assets to Lucide.
- Rewrites unrelated layout/styles during icon substitution.

## Scenario 3 - Edge: Package missing

### User prompt

Convert all possible icons from this Figma node to Lucide.

### Preconditions

- `package.json` does not include `lucide-angular`.

### Expected behavior

- No `lucide-angular` substitution occurs.
- Continues standard asset workflow.
- Does not install or request new package installation from this skill.

### Failure conditions

- Attempts Lucide conversion without package present.
- Adds package-install actions as part of this skill.

## Scenario 4 - Edge: Low-confidence icon identity

### User prompt

Use Lucide for icons in this section.

### Preconditions

- Icon layer names are ambiguous and do not clearly match Lucide patterns.

### Expected behavior

- Uses confidence rule and keeps ambiguous icon as asset when fewer than 2 indicators match.
- Applies conversion only to high-confidence icons.

### Failure conditions

- Forces Lucide mapping for uncertain icon identity.
- Replaces assets without clear mapping evidence.

## Scenario 5 - Convention preservation

### User prompt

Apply icon conversion but keep our existing icon pattern.

### Preconditions

- Existing project consistently uses `[img]` bindings for `lucide-icon`.

### Expected behavior

- New substitutions follow the existing `[img]` convention.
- No mixed inconsistent icon usage pattern is introduced unless already present.

### Failure conditions

- Introduces inconsistent icon usage style against established project pattern.

## Scenario 6 - Edge: Unmapped high-confidence icon

### User prompt

Implement this Figma toolbar and convert Lucide icons.

### Preconditions

- `package.json` includes `lucide-angular`.
- Icon label strongly suggests Lucide but no valid export can be resolved.

### Expected behavior

- Uses explicit fallback for that icon only (keeps downloaded asset).
- Continues Lucide substitution for other icons that are confidently mappable.

### Failure conditions

- Blocks the whole task because one icon is unmapped.
- Guesses a likely export name and ships broken icon code.

## Scenario 7 - Edge: Non-Figma request

### User prompt

Refactor our existing Angular icon system to Lucide.

### Preconditions

- No Figma implementation request or Figma node context is present.

### Expected behavior

- Skill is skipped because scope is Figma implementation bridging.
- No forced skill behavior is applied outside its scope.

### Failure conditions

- Applies Figma-specific workflow to a generic Angular refactor request.

## Scenario 8 - Hard: Deterministic per-icon mixed outcomes

### User prompt

Implement this Figma sidebar and bridge Lucide icons where appropriate.

### Preconditions

- `package.json` includes `lucide-angular`.
- Icon candidates in same screen: `chevron-left` (high confidence), `unknown-shape` (low confidence), `brand-mark` (non-Lucide).

### Expected behavior

- `chevron-left` is converted via `lucide-angular`.
- `unknown-shape` stays asset due to `low_confidence`.
- `brand-mark` stays asset due to `non_lucide_asset`.
- Processing continues for all icons; one fallback does not block others.

### Failure conditions

- Stops converting remaining icons after first fallback.
- Applies one global decision to all icons on the screen.

## Scenario 9 - Edge: Required conversion summary in final output

### User prompt

Implement icons from this Figma node with Lucide bridging.

### Preconditions

- `package.json` includes `lucide-angular`.
- At least one icon converts and at least one icon falls back.

### Expected behavior

- Final response includes:
  - Converted icons list.
  - Fallback icons list with reasons (`low_confidence`, `unresolved_export`, `package_missing`, `non_lucide_asset`).
  - Declared convention used (`[img]` or `name`).

### Failure conditions

- Omits fallback reasons.
- Reports conversion without convention declaration.

## Scenario 10 - Edge: Figma context evidence is explicit

### User prompt

Implement this node from https://figma.com/design/abc123/File?node-id=1-2 and bridge Lucide icons.

### Preconditions

- Angular project context exists.
- `package.json` includes `lucide-angular`.

### Expected behavior

- Skill treats URL/node-id as valid Figma context evidence.
- Per-icon decision flow executes without requiring extra trigger confirmation.

### Failure conditions

- Rejects the request due to missing MCP output even though URL/node-id is provided.

## Scenario 11 - Hard: Export candidate fails package symbol check

### User prompt

Implement this Figma toolbar and convert Lucide icons.

### Preconditions

- `package.json` includes `lucide-angular`.
- Icon name normalizes to a PascalCase candidate that is not a valid export in `lucide-angular`.

### Expected behavior

- Icon falls back with `unresolved_export`.
- Other resolvable icons continue converting.

### Failure conditions

- Ships code with a guessed import that is not exported by `lucide-angular`.
- Stops processing remaining icons after this failure.

## Scenario 12 - Edge: `package.json` missing or unreadable

### User prompt

Implement this Figma node and bridge Lucide icons where possible.

### Preconditions

- Angular project exists, but `package.json` is missing or unreadable.

### Expected behavior

- Skill does not assume `lucide-angular` availability.
- Keeps asset workflow for icons with fallback reason `package_missing`.
- Does not install packages or block unrelated implementation work.

### Failure conditions

- Proceeds with Lucide imports without package verification.
- Fails hard instead of applying deterministic fallback behavior.
