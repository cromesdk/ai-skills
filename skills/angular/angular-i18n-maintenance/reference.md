# Angular i18n Maintenance Reference

## Translation Key Naming

- Follow existing project convention first.
- Typical format: `scope.context.name` (for example `auth.login.submitButton`, `dashboard.title`, `common.cancel`).
- Keep keys stable and descriptive; avoid one-off abbreviations.

## Locale File Discovery Heuristics

1. Find `@ngx-translate/core` usage in the workspace.
2. Locate JSON loader configuration and prefix/suffix paths.
3. Confirm locale directory contents and language set.
4. Identify default/reference locale (commonly `en.json`).

Common paths include:
- `public/i18n/*.json`
- `assets/i18n/*.json`

## TranslatePipe Patterns

- Static content:
```html
{{ 'feature.section.label' | translate }}
```

- Interpolation:
```html
{{ 'dashboard.welcome' | translate:{ name: user.name } }}
```

- Attribute bindings:
```html
<input [placeholder]="'common.search' | translate" />
<button [title]="'common.refresh' | translate"></button>
```

Ensure `TranslatePipe` is available in the component context (directly or via imported/provided module setup).

## JSON Validity and Key Parity

- Add each new key to all locale JSON files in the set.
- Preserve existing structure style (flat or nested).
- Keep valid JSON: double-quoted keys/values, no trailing commas.
- If a translation is pending, use default-locale text temporarily and track follow-up outside JSON.
