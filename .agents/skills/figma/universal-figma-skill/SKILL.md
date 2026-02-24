---
name: universal-figma-skill
description: Execute an end-to-end Figma-to-Angular 20 implementation workflow in one skill by combining Atomic Design decomposition, Figma Make guidelines generation, Figma Make to Angular 20 + Tailwind v4 implementation, Lucide Angular icon bridging, feature-first Angular folder architecture enforcement, and component companion-file completeness enforcement. Use when a user wants one selectable skill to handle Figma-driven UI delivery from design intake through production-ready Angular structure and file hygiene.
---

# Universal Figma Skill

## Goal

Run a single coordinated workflow for Figma-driven Angular implementation without switching skills manually.

## Skill Composition

Load and apply these source skills in this order:

1. `../figma-make-guidelines/SKILL.md`
2. `../figma-make-angular20-tailwind4-implementation/SKILL.md`
3. `../figma-atomic-design-implementation/SKILL.md`
4. `../figma-lucide-angular-bridge/SKILL.md`
5. `../angular-folder-structure/SKILL.md`
6. `../angular-component-rule/SKILL.md`

If one source file is unavailable, continue with remaining sources and report the missing file.

## Execution Order

### Phase 1: Intake and baseline

1. Collect the minimum required design and project inputs.
2. Verify Angular and Tailwind versions and existing architecture quickly.
3. Infer missing non-blocking details and avoid long discovery chat.

### Phase 2: Guidelines and mapping

1. Generate or update `guidelines/Guidelines.md` only when the request includes Figma Make guideline creation or standardization.
2. Map Figma frames/components to Angular boundaries (route, page, template, organism, molecule, atom).
3. Plan reusable primitives before page-level implementation.

### Phase 3: Implementation

1. Implement in Atomic Design sequence: atoms, molecules, organisms, templates, pages.
2. Follow Angular 20 + Tailwind v4 project conventions and reuse existing components first.
3. Apply Lucide bridge rules: replace Lucide icon assets with `lucide-angular` only when confidently mapped and already installed.

### Phase 4: Structure and completeness enforcement

1. Enforce feature-first folder boundaries and pages/templates/components/data-access placement.
2. Enforce Angular component companion files and structural rules for all touched components.
3. Auto-create missing companions non-destructively, including stories only when Storybook is detected.

### Phase 5: Validation and report

1. Run targeted verification (tests/typecheck/build as appropriate).
2. Report implementation paths, reuse decisions, assumptions, and verification results.
3. Report component completeness metrics and any unfixable structural violations.

## Branching Rules

1. If the user asks only for guidelines output, run only the guideline branch and stop.
2. If the user asks only for code implementation, skip guideline generation unless explicitly requested.
3. If the user asks for architecture or folder refactor, prioritize folder-structure enforcement before deep UI edits.
4. If `lucide-angular` is not installed, do not install from this skill; keep normal asset flow.

## Guardrails

1. Preserve existing project architecture unless user requests wider refactor.
2. Do not introduce new UI/icon libraries.
3. Do not overwrite existing files when enforcing component completeness.
4. Ask at most one blocking question at a time; otherwise proceed with conservative assumptions.

## Required Output Contract

Return:

1. Workflow branches executed.
2. Files created or updated with paths.
3. Atomic component tree for implemented UI (when code was changed).
4. Reuse vs new-component decisions.
5. Style and Storybook detection outcomes.
6. Verification commands run and outcomes.
7. Remaining manual follow-ups, if any.