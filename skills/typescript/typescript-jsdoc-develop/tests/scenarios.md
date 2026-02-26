# Scenario Tests

## Easy: Add missing JSDoc to exported TypeScript function

- Given a `.ts` file with an exported function that has no JSDoc
- When the assistant applies this skill with default scope
- Then it adds a concise JSDoc block directly above the declaration
- And it includes accurate `@param` and `@returns` tags when applicable
- And it does not change runtime code

## Hard: Repair stale JSDoc after signature drift in React TSX

- Given a `.tsx` file where a component's props changed but JSDoc still references removed props
- When the assistant is asked to refresh documentation
- Then it updates summary text and tags to match current props and behavior
- And it removes stale parameter references and keeps valid existing wording
- And it preserves component logic and JSX output

## Hard: Document destructured parameters and optional defaults correctly

- Given a function signature using destructured object parameters with optional/default fields
- When this skill updates or creates JSDoc
- Then parameter names and optional/default behavior in tags match the actual signature
- And no inferred behavior is added beyond what the code implements

## Edge: Public-only default scope should skip private internals

- Given a file containing exported APIs and private helper functions
- When the user does not request full/internal coverage
- Then the assistant documents exported/public declarations only
- And it skips private helpers, trivial one-liners, and obvious getters/setters

## Edge: Missing or ambiguous target path handling

- Given a request to "document this code" without file or symbol targets
- When this skill is triggered
- Then the assistant asks one precise clarification question for the missing target
- And it avoids speculative edits until scope is clear
