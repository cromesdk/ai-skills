---
name: angular-tailwind-theme-design
description: Implement a production-ready, Angular-compatible Tailwind CSS v4 theme system with explicit Light and Dark themes, using Light as the default. Use when users ask to add or refactor app theming, dark mode toggles, design tokens, or global color systems in Angular projects that use Tailwind v4 (or need to be aligned to it).
---

# Angular Tailwind Theme Design

## Goal

Create a single source of truth for theme tokens that works with Angular + Tailwind v4 and supports Light and Dark UI, while defaulting to Light on first load.

## Inputs

- `projectRoot` (default: current working directory)
- `themeTokenPrefix` (default: `--color-`)
- `useClassDarkMode` (default: `true`)
- `createThemeService` (default: `true`)
- `persistUserChoice` (default: `true`)

## Success Criteria

- Tailwind v4 is wired through global styles (`@import "tailwindcss";`).
- Light and Dark tokens exist in global styles via CSS variables.
- Light theme is active by default when no stored user preference exists.
- Dark mode is activated by class toggling (`.dark`) and mapped to Tailwind utilities.
- Angular code exposes a deterministic toggle API (service and/or UI control).

## Workflow

### 1) Validate Angular + Tailwind v4 context

- Confirm `angular.json` and `package.json` exist.
- Confirm Angular project context is valid.
- Confirm Tailwind v4 setup exists.
- If Tailwind v4 is missing or broken, fix setup first, then continue.

### 2) Define theme tokens in global styles

Edit the main global stylesheet (`src/styles.css` or `src/styles.scss`):

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));

:root {
  color-scheme: light;
  --color-bg: 255 255 255;
  --color-fg: 15 23 42;
  --color-surface: 248 250 252;
  --color-border: 226 232 240;
  --color-primary: 37 99 235;
}

.dark {
  color-scheme: dark;
  --color-bg: 2 6 23;
  --color-fg: 241 245 249;
  --color-surface: 15 23 42;
  --color-border: 51 65 85;
  --color-primary: 96 165 250;
}
```

Use RGB triplets for token values so opacity modifiers remain easy with Tailwind utilities.

### 3) Map tokens into reusable utility classes

Add app-level utility classes in the same global stylesheet:

```css
@layer utilities {
  .bg-app {
    background-color: rgb(var(--color-bg));
  }

  .text-app {
    color: rgb(var(--color-fg));
  }

  .bg-surface {
    background-color: rgb(var(--color-surface));
  }

  .border-app {
    border-color: rgb(var(--color-border));
  }

  .text-primary {
    color: rgb(var(--color-primary));
  }
}
```

Prefer these semantic classes in components over raw palette classes.

### 4) Implement light-by-default theme behavior in Angular

If `createThemeService` is enabled, create a minimal service to apply and persist theme:

```ts
import { Injectable } from '@angular/core';

type ThemeMode = 'light' | 'dark';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  private readonly storageKey = 'theme';

  initTheme(): void {
    const stored = localStorage.getItem(this.storageKey) as ThemeMode | null;
    const mode: ThemeMode = stored ?? 'light';
    this.applyTheme(mode);
  }

  toggleTheme(): void {
    const next: ThemeMode = this.isDark() ? 'light' : 'dark';
    this.applyTheme(next);
  }

  isDark(): boolean {
    return document.documentElement.classList.contains('dark');
  }

  private applyTheme(mode: ThemeMode): void {
    const root = document.documentElement;
    root.classList.toggle('dark', mode === 'dark');
    localStorage.setItem(this.storageKey, mode);
  }
}
```

Call `initTheme()` early (for example in app bootstrap path) to enforce Light as default when no explicit user choice exists.

### 5) Add a small toggle UI (optional but recommended)

- Add a toggle button in a shell or header component.
- Bind the click handler to `themeService.toggleTheme()`.
- Use semantic classes (`bg-app`, `text-app`, `bg-surface`) in the template to verify theme switching.

### 6) Verify behavior

- Load app in a clean browser profile with no `localStorage` entry and confirm Light is active.
- Toggle once and confirm `.dark` is added to `<html>`.
- Reload and confirm persisted mode is restored.
- Check at least one component in both modes for contrast and readability.

## Guardrails

- Keep Light as default unless user explicitly requests a different default.
- Use class-based dark mode; do not rely on implicit system preference for initial mode.
- Avoid hard-coding colors in components; route through theme tokens.
- Preserve existing project style conventions (`css` vs `scss`, formatting rules, naming style).
- Minimize scope: implement tokens and wiring first, then expand theme palette only as needed.
