# Angular i18n Maintenance — Examples

## Example 1: New button label

**Before (hardcoded):**
```html
<button type="submit">Save changes</button>
```

**After:**

Template:
```html
<button type="submit">{{ 'settings.saveChanges' | translate }}</button>
```

`public/i18n/en.json`:
```json
{
  "app.title": "My App",
  "settings.saveChanges": "Save changes"
}
```

`public/i18n/de.json`:
```json
{
  "app.title": "Meine App",
  "settings.saveChanges": "Änderungen speichern"
}
```

---

## Example 2: New heading

**Before:**
```html
<h2>Dashboard</h2>
```

**After:**

Template:
```html
<h2>{{ 'dashboard.title' | translate }}</h2>
```

Add `"dashboard.title": "Dashboard"` to `en.json` and the same key with translated text to every other locale file.

---

## Example 3: Interpolation

**Before:**
```html
<p>Welcome, {{ user.name }}</p>
```

**After:**

Template:
```html
<p>{{ 'dashboard.welcome' | translate:{ name: user.name } }}</p>
```

`en.json`:
```json
"dashboard.welcome": "Welcome, {{ name }}"
```

`de.json`:
```json
"dashboard.welcome": "Willkommen, {{ name }}"
```

---

## Example 4: Attribute (e.g. placeholder)

**Before:**
```html
<input placeholder="Search..." />
```

**After:**

Template:
```html
<input [placeholder]="'common.search' | translate" />
```

Add `"common.search": "Search..."` (and equivalents) to all locale files.
