# Scenarios: universal-figma-skill

## Easy

### 1) Full Figma-to-code implementation with explicit scope
- Input:
  - Valid Angular project path
  - Figma URL with node ID
  - Scope is one route/page
- Expected:
  - Runs implementation branch with atomic sequence (atoms -> molecules -> organisms -> templates -> pages).
  - Reuses existing shared components before creating new ones.
  - Reports changed files, reuse decisions, verification commands, and outcomes.

### 2) Guidelines-only request
- Input:
  - User asks only to generate or standardize `guidelines/Guidelines.md`
  - No code implementation requested
- Expected:
  - Executes only guideline branch.
  - Does not modify route/component implementation files.
  - Returns a concise branch-limited report.

## Hard

### 3) Architecture refactor prioritized over deep UI edits
- Input:
  - Existing implementation request plus explicit folder-structure normalization
  - Current app has mixed/non-feature-first layout
- Expected:
  - Prioritizes folder-structure enforcement before deep UI edits.
  - Preserves behavior while relocating files to valid boundaries.
  - Reports structure changes and residual manual follow-ups.

### 4) Lucide not installed in project
- Input:
  - Figma includes icon set with partial Lucide likeness
  - `lucide-angular` dependency is absent
- Expected:
  - Does not install new packages.
  - Keeps normal asset/icon flow for unresolved or unavailable Lucide mapping.
  - States explicit reason for skipping Lucide bridging.

### 5) Conflicting Figma values vs repository tokens
- Input:
  - Figma colors/spacing differ from established project design tokens
- Expected:
  - Uses repository tokens/patterns instead of raw conflicting values.
  - Documents design deltas in output contract.
  - Avoids global visual regressions outside requested scope.

## Edge Cases

### 6) Missing required project path
- Input:
  - Design source provided
  - Project/workspace path missing or invalid
- Expected:
  - Asks exactly one blocking question for the missing/invalid required input.
  - Makes no edits before path is clarified.
  - Continues deterministically after clarification.

### 7) Ambiguous target scope across multiple routes
- Input:
  - Figma source provided
  - Multiple routes/components are plausible targets
  - User does not specify scope boundary
- Expected:
  - Asks one blocking scope question.
  - Avoids touching unrelated routes/components before scope is resolved.
  - Reports chosen branch execution after scope confirmation.

### 8) Storybook not detected while enforcing companions
- Input:
  - Component completeness enforcement is required
  - Storybook is not installed
- Expected:
  - Creates required companion files non-destructively, excluding stories.
  - Reports Storybook detection outcome explicitly.
  - Maintains one-component-per-file hygiene for touched components.

### 9) Verification command unavailable or failing
- Input:
  - Implementation completed
  - Test/typecheck scripts unavailable or build fails
- Expected:
  - Reports exact command outcomes (pass/fail/unavailable).
  - Does not claim successful validation when checks fail.
  - Identifies remaining follow-up actions.
