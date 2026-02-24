# Scenarios: figma-make-always-check

## 1) Basic routing with reachable OMS Figma Make (easy)
### Input
User asks: "Implement the OMS order summary page from Figma Make in Angular."

### Expected behavior
- Opens `references/oms-figma-make.md` first.
- Checks `https://www.figma.com/make/VQeYDTGteluPfiNKq1ZaQC/OMS?t=j4sIRnOerI7uoUG0-1` before other implementation work.
- Routes to the minimal relevant skills (for example `figma-make-angular20-tailwind4-implementation`).
- Completes requested implementation work end-to-end, not planning-only output.
- Final report states Figma Make check status, selected helper skills, and changed files.

## 2) URL check unavailable but delivery continues (edge)
### Input
User asks: "Refactor the OMS product list to match the design baseline."

Environment constraint:
- Figma Make URL is inaccessible (network/tool failure).

### Expected behavior
- Attempts the mandatory URL check first.
- Explicitly reports that Figma Make validation could not be completed.
- Continues with local repository context instead of blocking.
- Keeps assumptions explicit where design details are uncertain.
- Still returns concrete edits and validation outcomes when possible.

## 3) Non-UI request still enforces first check (hard)
### Input
User asks: "Update README and changelog for the latest skill changes."

### Expected behavior
- Performs OMS Figma Make check first (or reports inability).
- Routes to documentation-focused skills only (for example `readme-updater`, `changelog-keepachangelog-update`).
- Avoids unnecessary UI implementation skills.
- Produces deterministic documentation updates with evidence-based summaries.

## 4) Overlapping-skill request uses minimal set (hard)
### Input
User asks: "Implement this OMS screen, enforce component companion files, and align folder structure."

### Expected behavior
- Performs OMS Figma Make check first.
- Selects only necessary helpers for scope (for example Figma implementation + `angular-component-rule` + `angular-folder-structure`).
- Applies skills in deterministic order (setup/architecture -> design translation -> enforcement).
- Avoids redundant or overlapping skills that do not add coverage.

## 5) Ambiguous design details with explicit gap reporting (edge)
### Input
User asks: "Make this dashboard like OMS design" with no node IDs or screenshot.

### Expected behavior
- Checks OMS Figma Make first.
- Proceeds with best-available context and minimal assumptions.
- Explicitly reports design-context gaps in the output contract.
- Delivers the closest valid implementation/refactor without stalling on repeated clarification loops.
