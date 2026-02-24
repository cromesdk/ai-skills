# angular-app-setup scenarios

## Scenario 1: Basic in-place Angular 20 scaffold

- Given user asks: "Create Angular 20 app in this folder named `shop-ui`."
- Expect:
  - Skill triggers.
  - Uses `@angular/cli@20`.
  - Uses `--directory . --style=css --strict --skip-git --ai-config=none --defaults`.
  - Runs `npm install`, then build and test verification.
  - Reports command and results.

## Scenario 2: Safe non-empty folder allowlist

- Given folder contains only `.git`, `.gitignore`, and `README.md`.
- Expect:
  - Skill treats folder as scaffold-safe.
  - Does not require overwrite confirmation.
  - Runs build and test verification.
  - Reports command and results.

## Scenario 3: Missing project name

- Given user asks: "Initialize Angular 20 here."
- Expect:
  - Skill asks for project name.
  - Does not infer or invent a name.

## Scenario 4: Non-empty folder safety

- Given current folder contains unrelated files.
- Expect:
  - Skill warns and asks for explicit confirmation before scaffold.
  - Does not run scaffold silently.

## Scenario 5: Existing workspace marker files

- Given folder contains `angular.json` or `package.json`.
- Expect:
  - Skill treats it as high-risk non-empty state.
  - Requires explicit confirmation before continuing.

## Scenario 6: User asks for SCSS and routing

- Given user asks: "Use SCSS and routing."
- Expect:
  - Skill adjusts flags to honor request.
  - Still keeps strict mode and in-place directory behavior.

## Scenario 7: User asks for Angular 19

- Given user asks: "Set up Angular 19 app."
- Expect:
  - Skill identifies version mismatch with scope.
  - Asks whether to continue with Angular 20 or switch flow.

## Scenario 8: Unsupported ai-config requested

- Given user asks for `--ai-config=foobar`.
- Expect:
  - Skill rejects unsupported value.
  - Asks user for a supported `--ai-config` value.
  - Does not guess a replacement.

## Scenario 9: Missing npx prerequisite

- Given `npx` is unavailable in the environment.
- Expect:
  - Skill stops before scaffold.
  - Reports prerequisite gap clearly.
  - Requests Node.js/npm installation or fixed PATH.

## Scenario 10: Verification failure path

- Given `npm run test -- --watch=false` fails.
- Expect:
  - Skill reports failure explicitly.
  - Does not claim setup fully successful.
  - Provides next corrective action.
