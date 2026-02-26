# Angular i18n Maintenance Examples

## Example 1: New Button Label

Before:
```html
<button type="submit">Save changes</button>
```

After:
```html
<button type="submit">{{ 'settings.saveChanges' | translate }}</button>
```

`en.json`:
```json
{
  "settings.saveChanges": "Save changes"
}
```

`de.json`:
```json
{
  "settings.saveChanges": "Änderungen speichern"
}
```

## Example 2: New Heading

Before:
```html
<h2>Dashboard</h2>
```

After:
```html
<h2>{{ 'dashboard.title' | translate }}</h2>
```

Add `dashboard.title` to every locale file.

## Example 3: Interpolation

Before:
```html
<p>Welcome, {{ user.name }}</p>
```

After:
```html
<p>{{ 'dashboard.welcome' | translate:{ name: user.name } }}</p>
```

`en.json`:
```json
{
  "dashboard.welcome": "Welcome, {{ name }}"
}
```

`de.json`:
```json
{
  "dashboard.welcome": "Willkommen, {{ name }}"
}
```

## Example 4: Attribute Binding

Before:
```html
<input placeholder="Search..." />
```

After:
```html
<input [placeholder]="'common.search' | translate" />
```

Add `common.search` to every locale file.
