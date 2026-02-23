# Figma Make Export Baseline Heuristics

Use this checklist when analyzing a `figma_make_corpus_root` before implementation.

## 1) Route and page structure
- Identify repeated top-level route layout patterns.
- Capture where navigation, shell wrappers, and page containers are defined.
- Note route-specific overrides that should not be promoted globally.

## 2) Component family mapping
- Group repeated UI into component families (cards, lists, forms, nav, dialogs).
- Record prop/state differences across exports.
- Prefer mapping to existing Angular shared components before creating new ones.

## 3) Token and theme usage
- Extract recurring spacing, typography, radius, shadow, and color conventions.
- Distinguish true design tokens from one-off visual exceptions.
- Reuse repository token variables/classes when available.

## 4) State and interaction behavior
- Capture hover/focus/active/disabled/loading/empty/error states.
- Document keyboard/focus behavior when visible in export patterns.
- Keep semantics accessible when mapping to Angular templates.

## 5) Responsive behavior
- Infer breakpoint behavior from container changes, stacking rules, and truncation.
- Record which elements are hidden, reordered, or resized per viewport.
- Preserve stable interaction hierarchy across breakpoints.

## 6) Risk flags
- Mark any hard-coded values that conflict with repository tokens.
- Mark patterns that require data contracts not present in target project.
- Mark any architecture assumptions that would force broad rewrites.

## Output format suggestion
- Write findings to `<project_root>/figma-make-export-analysis.md`.
- Use sections:
  - `Stable Patterns`
  - `Project-specific Deltas`
  - `Conversion Risks`
  - `Recommended Reuse Targets`
