# Angular i18n Maintenance Scenarios

## Easy

### 1) Add one static button label
- Prompt: "Add translation for a new Save button label in settings template."
- Expected:
  - New key created using existing naming style.
  - Template uses `{{ 'settings.saveChanges' | translate }}`.
  - Key added to all locale JSON files.

## Hard

### 2) Add interpolated message used in two templates
- Prompt: "Add a translated welcome message with user name on dashboard and profile pages."
- Expected:
  - Single shared key defined (for example `dashboard.welcome`).
  - Both templates use `translate:{ name: ... }`.
  - Parameter token name (`name`) is consistent across all locales.

## Edge Cases

### 3) Mixed flat and nested key conventions
- Setup: Locale set contains both flat and nested entries.
- Prompt: "Add translation key for notifications empty state."
- Expected:
  - Dominant project convention is detected and used.
  - Inconsistency is noted without broad refactor.

### 4) Missing locale file
- Setup: One configured locale file is absent.
- Prompt: "Add a new translated heading for reports page."
- Expected:
  - Missing file is reported explicitly.
  - Workflow stops with deterministic blocker message (or explicit create-path requirement).

### 5) Malformed locale JSON
- Setup: One locale JSON has invalid syntax.
- Prompt: "Add translated tooltip text for refresh button."
- Expected:
  - Exact file and parse issue reported.
  - No blind rewrite of malformed file.

### 6) Regression guard: no new hardcoded copy
- Prompt: "Add translation for new checkout confirm label."
- Expected:
  - Newly added user-facing copy is translated.
  - Unrelated locale keys remain unchanged.
