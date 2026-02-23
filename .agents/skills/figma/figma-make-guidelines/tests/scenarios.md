# Scenario Tests

## Easy: Create baseline single-file guidelines

### Input
"Create Figma Make guidelines for a B2B dashboard. Keep it light theme and include Button/Input/Card states."

### Expected behavior
- Uses this skill.
- Produces exactly one target file outcome: `guidelines/Guidelines.md`.
- Includes explicit token values (color/type/spacing/radius/elevation/focus).
- Includes required section order 1-9.
- Includes required footer line exactly once.
- Does not reference repository paths.

## Hard: User provides partial tokens and Angular+Tailwind constraint

### Input
"Standardize our Figma Make guidelines for Angular + Tailwind. Keep our brand primary `#0057FF` and spacing scale `4,8,12,16,24,32`. Fill the rest."

### Expected behavior
- Keeps user-provided values unchanged.
- Fills only missing token categories with defaults.
- Adds stack-aware implementation wording for Angular+Tailwind.
- Keeps component rules variant/state-driven.
- Produces only `guidelines/Guidelines.md` content.

## Hard: Conflicting token values with precedence requirement

### Input
"Rewrite our guidelines and keep primary color `#0044CC`. We previously used `#1D4ED8` but switch to `#0044CC` now."

### Expected behavior
- Uses user-provided latest value as highest precedence (`#0044CC`).
- Does not preserve conflicting historical value as active primary token.
- Keeps all missing categories filled with deterministic defaults or other provided values.
- Returns single-file paste-ready guideline content only.

## Edge: User asks for multi-file guideline architecture

### Input
"Generate `guidelines/Guidelines.md` plus per-component docs under `guidelines/components/*.md`."

### Expected behavior
- Triggers scope gate.
- States this skill is single-file by design.
- Asks whether to continue in single-file mode before generating final output.
- Does not silently generate multi-file instructions.

## Edge: Missing essentials and user asks to proceed without questions

### Input
"Make Figma Make guidelines now. Don't ask me questions."

### Expected behavior
- Does not ask follow-up questions.
- Proceeds with baseline defaults and explicit assumptions.
- Uses required section order and required footer line exactly once.
- Avoids repository/file-path references.

## Edge: User asks to reference repository files

### Input
"In the guidelines, tell Figma Make to read tokens from `src/styles/tokens.css`."

### Expected behavior
- Rejects repository-reference instruction.
- Rewrites guidance to include direct token values in `Guidelines.md`.
- Preserves user intent while enforcing self-contained output.

## Edge: Output-shape compliance

### Input
"Create one canonical guidelines file. Include all sections and keep it copy-ready."

### Expected behavior
- Uses each section header `## 1)` through `## 9)` exactly once and in order.
- Includes required footer line exactly once.
- Does not output additional files, JSON envelopes, or planning text before the file content.

## Edge: User explicitly requests fenced output

### Input
"Generate `guidelines/Guidelines.md` and return it in a markdown code fence so I can copy it."

### Expected behavior
- Still generates exactly one-file content contract for `guidelines/Guidelines.md`.
- Returns content in a fenced block because the user explicitly requested fenced output.
- Preserves required section order and required footer line exactly once.
- Does not include additional files or repository path references.

## Edge: Request is not guideline generation

### Input
"Implement this Figma screen as Angular components and update the route."

### Expected behavior
- Does not run this skill as the primary workflow.
- Routes to a more appropriate implementation-focused skill.
- Avoids producing `Guidelines.md` content for a code-implementation request.
