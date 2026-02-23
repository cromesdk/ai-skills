# Figma Atomic Design Implementation - Scenario Tests

## Easy

### 1. Decompose simple login card from Figma
- Input: User asks to implement a login card from one Figma node into an Angular feature.
- Expected behavior:
  - Assistant identifies atoms first (label, input, button).
  - Assistant composes molecule(s) (form row) and organism (login panel) before template/page.
  - Companion files are created/updated for all touched components.
  - Output reports component tree and quality-gate status.

## Hard

### 2. Refactor an existing page with mixed concerns
- Input: Existing Angular page has large inline markup and duplicated controls; user asks to align with atomic design.
- Expected behavior:
  - Assistant audits reusable components before creating new ones.
  - Assistant extracts page-specific primitives into reusable atoms/molecules without breaking orchestration boundaries.
  - Assistant keeps business/data orchestration at page level.
  - Output documents reuse decisions and remaining gaps.

### 3. Multi-state dashboard section implementation
- Input: Figma section includes loading, empty, error, and populated states with shared controls.
- Expected behavior:
  - Assistant maps states at each atomic level and includes them in stories.
  - Specs verify rendering and key state-dependent behavior.
  - No skipped levels for newly introduced patterns.

## Edge Cases

### 4. Missing target path context
- Input: User provides Figma URL but no target Angular folder/path.
- Expected behavior:
  - Assistant asks one focused clarification question for destination path.
  - Assistant proceeds with atomic decomposition guidance once context is provided.

### 5. Missing companion files in existing components
- Input: User asks for a small UI tweak, but touched components are missing `.stories.ts` and `.spec.ts`.
- Expected behavior:
  - Assistant creates missing companion files before marking task complete.
  - Assistant reports file completeness remediation explicitly.

### 6. Ambiguous request to jump directly to page implementation
- Input: User asks to "just build the page quickly" from Figma.
- Expected behavior:
  - Assistant still follows atomic order and does not skip lower levels when missing.
  - Assistant explains reuse-first decision and quality-gate compliance in output.
