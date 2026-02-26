# Angular i18n Maintenance — Reference

## Translation key naming

- **Format**: `scope.context.name` (dot-notation, lowercase).
- **Scope**: Feature or area — e.g. `auth`, `dashboard`, `settings`, `nav`, `common`, `errors`.
- **Context**: Screen or block — e.g. `login`, `profile`, `sidebar`.
- **Name**: Purpose — e.g. `title`, `submitButton`, `requiredError`.

Examples: `auth.login.submitButton`, `nav.home`, `common.cancel`, `errors.required`.

## Locale file locations

| Setup              | Typical path              |
|--------------------|---------------------------|
| ngx-translate      | `public/i18n/*.json` or `assets/i18n/*.json` |
| Angular build i18n | `src/locale/*.json` or project-specific |

Detect by searching for `TranslateHttpLoader`, `prefix`/`suffix` for JSON, or existing `*.json` under `i18n`/`locale`.

## TranslatePipe usage

- **Static**: `{{ 'key' | translate }}`
- **With params**: `{{ 'key' | translate:{ param: value } }}`
- **In attributes**: `[title]="'key' | translate"` (ensure pipe is available in the component).

Standalone components must import `TranslateModule` (or the app provides the pipe globally).

## Adding to locale files

1. Open each locale file (e.g. `en.json`, `de.json`).
2. Add the key at the right level; use nested objects if the project uses them (e.g. `"dashboard": { "welcome": "..." }`) or flat keys (e.g. `"dashboard.welcome": "..."`) to match existing style.
3. Preserve JSON syntax (no trailing commas, double-quoted keys and string values).
