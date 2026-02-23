# Scenarios: figma-make-angular20-tailwind4-implementation

## Easy

### 1) Single-page implementation with complete input
- Input:
  - `project_root` provided
  - `figma_make_base` provided
  - `design_source` includes Figma URL and node
  - `target_scope` is one route
- Expected:
  - Uses existing project structure/components/tokens.
  - Implements direct code changes (not planning-only).
  - Returns file paths, reused patterns, assumptions, and verification commands.

## Hard

### 2) Corpus-based implementation with missing extraction script
- Input:
  - `figma_make_corpus_root` provided with multiple exports
  - `scripts/extract_figma_make_exports.ps1` missing
  - `target_scope` is a complex page with repeated component families
- Expected:
  - Detects missing script and uses manual fallback to create an analysis markdown.
  - Extracts stable/variable patterns before coding.
  - Reuses shared components and avoids architecture rewrites.

### 3) Tailwind version mismatch
- Input:
  - Project uses Angular 20 but Tailwind v3
  - User requests immediate implementation
- Expected:
  - Asks one blocking compatibility question before proceeding.
  - Does not silently mix v4-only patterns into a v3 setup.
  - Continues once compatibility direction is confirmed.

### 4) Missing or invalid project path
- Input:
  - `project_root` provided but path is invalid
  - `figma_make_base` points to an existing path in the current repo
- Expected:
  - States the missing path once.
  - Applies ordered fallback (`absolute` -> `workspace-relative` -> `closest matching path`).
  - Continues implementation without repeated clarification loops.

### 5) No resolvable safe path
- Input:
  - `project_root` invalid
  - `figma_make_base` invalid
  - no close path match in repository
- Expected:
  - Tries ordered fallback and fails safely.
  - Asks exactly one blocking question.
  - Makes no edits before path confirmation.

## Edge Cases

### 6) Ambiguous design details and tight scope
- Input:
  - `design_source` is screenshot plus short brief
  - Missing typography/state details
  - `target_scope` limited to one component
- Expected:
  - Makes conservative assumptions and proceeds.
  - Documents assumptions in final output.
  - Avoids repeated clarification loops.

### 7) Conflicting Figma detail vs project system
- Input:
  - Figma specifies spacing/colors that conflict with repo tokens
- Expected:
  - Prioritizes repository tokens/patterns.
  - Notes design delta explicitly in output.
  - Preserves accessibility semantics.

### 8) Verification command failure
- Input:
  - Implementation done, but targeted tests fail
- Expected:
  - Reports exact failing command and scope.
  - Does not claim successful validation.
  - Identifies likely regression surface in touched shared components.

### 9) Missing target scope with broad design input
- Input:
  - `design_source` provided
  - `target_scope` missing
  - Multiple routes/components are plausible targets
- Expected:
  - Asks one concise blocking question to resolve scope.
  - Does not edit unrelated routes/components before scope is clarified.

### 10) Unrelated-file safety during shared component update
- Input:
  - `target_scope` is one route
  - shared component change is required
  - formatter would touch many unrelated files
- Expected:
  - Limits edits to target scope and direct shared dependencies only.
  - Avoids mass formatting/refactors unrelated to the request.
  - Reports exact files changed.

### 11) Verification availability gap
- Input:
  - Implementation complete
  - project has no runnable test script, but has `build`
- Expected:
  - Runs at least one targeted check if available; otherwise states why unavailable.
  - Runs one integration check (`build`, `typecheck`, or `lint`) when available.
  - Clearly reports what was not run and why.
