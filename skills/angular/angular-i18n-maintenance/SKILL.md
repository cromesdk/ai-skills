---
name: angular-i18n-maintenance
description: When new static text is added in Angular apps that use embedded i18n (@ngx-translate), create a new translation ID, use TranslatePipe in the template, and add the key and default translation to all locale JSON files. Use when adding labels, buttons, messages, or any user-facing copy in projects with runtime i18n.
---

# Angular i18n Maintenance

When adding new static text in an Angular app that already has runtime i18n (e.g. `@ngx-translate/core` with JSON locale files), always: (1) define a new translation ID, (2) use the translation pipe in the template, and (3) add the key and wording to every locale file.

## When to Apply

- New labels, buttons, headings, messages, or any user-facing copy is added.
- The project uses `TranslatePipe` and JSON locale files (e.g. `public/i18n/*.json` or `assets/i18n/*.json`).
- Do **not** hardcode user-facing strings in templates or components.

## Workflow

### 1) Choose or detect translation location

- Locate the project’s locale JSON files (commonly `public/i18n/` or `assets/i18n/`).
- Use existing key patterns (e.g. `feature.section.label`, `nav.home`, `common.save`).
- If the app has a `reference`/default locale (e.g. `en.json`), use it as the source of truth for key structure.

### 2) Create a new translation ID

- Use dot-notation: `scope.context.name` (e.g. `dashboard.welcome`, `auth.loginButton`, `errors.required`).
- Prefer one key per phrase; avoid concatenating multiple keys for a single sentence.
- Keep IDs stable: same key in every locale file.

### 3) Use TranslatePipe in the template

- Prefer: `{{ 'key' | translate }}` for static text.
- For attributes: `[title]="'key' | translate"` or `placeholder="key"` only if the project uses a custom attribute directive; otherwise use the pipe in the template where the value is bound.
- Ensure the component imports `TranslateModule` (or the pipe is provided globally) so `translate` is available.

### 4) Add the key to all locale files

- Add the **same key** to every locale JSON file (e.g. `en.json`, `de.json`).
- Set the **default language** value to the new wording (e.g. English).
- Set other locales to the correct translation; if unknown, use the default wording and optionally add a `// TODO: translate` comment in a separate doc, not inside JSON.
- Keep JSON valid (no trailing commas, quoted keys).

## Checklist

- [ ] New translation ID follows dot-notation and existing project patterns.
- [ ] Template uses `{{ 'key' | translate }}` (or equivalent) for the new text.
- [ ] Key added to default/reference locale (e.g. `en.json`) with the new word/phrase.
- [ ] Key added to every other locale file with translation or temporary default.
- [ ] No user-facing string left hardcoded for that text.

## Optional: Interpolation

If the string has placeholders (e.g. "Welcome, {{ name }}"):

- In JSON: `"dashboard.welcome": "Welcome, {{ name }}"`
- In template: `{{ 'dashboard.welcome' | translate:{ name: user.name } }}`
- Use the same parameter names in every locale.

## References

- Key naming and locale paths: [reference.md](reference.md)
- Before/after examples: [examples.md](examples.md)
