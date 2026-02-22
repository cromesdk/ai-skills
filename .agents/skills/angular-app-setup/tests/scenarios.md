# angular-app-setup scenarios

## Scenario 1: Basic in-place Angular 20 scaffold

- Given user asks: "Create Angular 20 app in this folder named `shop-ui`."
- Expect:
  - Skill triggers.
  - Uses `@angular/cli@20`.
  - Uses `--directory . --style=css --strict --skip-git --ai-config=none`.
  - Runs build and test verification.
  - Reports command and results.

## Scenario 2: Missing project name

- Given user asks: "Initialize Angular 20 here."
- Expect:
  - Skill asks for project name.
  - Does not infer or invent a name.

## Scenario 3: Non-empty folder safety

- Given current folder contains unrelated files.
- Expect:
  - Skill warns and asks for explicit confirmation before scaffold.
  - Does not run scaffold silently.

## Scenario 4: User asks for SCSS and routing

- Given user asks: "Use SCSS and routing."
- Expect:
  - Skill adjusts flags to honor request.
  - Still keeps strict mode and in-place directory behavior.

## Scenario 5: User asks for Angular 19

- Given user asks: "Set up Angular 19 app."
- Expect:
  - Skill identifies version mismatch with scope.
  - Asks whether to continue with Angular 20 or switch flow.

## Scenario 6: Verification failure path

- Given `npm run test -- --watch=false` fails.
- Expect:
  - Skill reports failure explicitly.
  - Does not claim setup fully successful.
  - Provides next corrective action.
