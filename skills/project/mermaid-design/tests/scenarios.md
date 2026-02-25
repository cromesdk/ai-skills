# Mermaid Design Scenarios

## Easy

### 1) Generate flowchart using root tokens
- Prompt: "Create a flowchart for user signup."
- Expected:
  - Reads root `mermaid.tokens.json`.
  - Includes `%%{init: ...}%%` with root `themeVariables`.
  - Uses `flowchart` syntax.

## Hard

### 2) Restyle then regenerate sequence diagram
- Prompt: "Change primary color to #ffd166 and generate a sequence diagram for checkout."
- Expected:
  - Updates root `mermaid.tokens.json` first.
  - Diagram init uses updated root values.
  - Uses `sequenceDiagram` syntax.

## Edge cases

### 3) Missing root token file
- Setup: Delete root `mermaid.tokens.json`.
- Prompt: "Create a gantt chart for release plan."
- Expected:
  - Recreates root token file from skill default.
  - Generates `gantt` output with init block.

### 4) Invalid root JSON
- Setup: Corrupt root `mermaid.tokens.json`.
- Prompt: "Create a state diagram for deployment status."
- Expected:
  - Replaces invalid root with skill default.
  - Generates `stateDiagram` or `stateDiagram-v2` with init block.

### 5) Unsupported diagram request
- Prompt: "Generate a diagram type not in supported list."
- Expected:
  - Does not fabricate syntax.
  - Returns supported diagram list.
