# JSDoc Examples

## JavaScript function with destructured options

Before:

```js
export function listUsers({ limit = 25, cursor } = {}) {
  return api.get('/users', { params: { limit, cursor } });
}
```

After:

```js
/**
 * Lists users with optional pagination controls.
 * @param {Object} [options] - Query options
 * @param {number} [options.limit=25] - Maximum users to fetch
 * @param {string} [options.cursor] - Cursor for next page
 * @returns {Promise<User[]>} Resolved user list
 */
export function listUsers({ limit = 25, cursor } = {}) {
  return api.get('/users', { params: { limit, cursor } });
}
```

## TypeScript function updated after signature change

Before:

```ts
/**
 * Builds a slug.
 * @param input - Raw string
 */
export function toSlug(input: string, separator = '-'): string {
  return input.toLowerCase().replace(/\s+/g, separator);
}
```

After:

```ts
/**
 * Builds a URL slug from input text.
 * @param input - Raw string to normalize
 * @param separator - Character inserted between words (default '-')
 * @returns Normalized slug string
 */
export function toSlug(input: string, separator = '-'): string {
  return input.toLowerCase().replace(/\s+/g, separator);
}
```

## Async TypeScript function with throws

Before:

```ts
export async function readConfig(path: string): Promise<Config> {
  const text = await fs.promises.readFile(path, 'utf8');
  return JSON.parse(text) as Config;
}
```

After:

```ts
/**
 * Reads and parses the application config file.
 * @param path - Absolute or workspace-relative config path
 * @returns Parsed configuration object
 * @throws {Error} When the file cannot be read or JSON parsing fails
 */
export async function readConfig(path: string): Promise<Config> {
  const text = await fs.promises.readFile(path, 'utf8');
  return JSON.parse(text) as Config;
}
```

## React component in TSX

Before:

```tsx
interface BadgeProps {
  label: string;
  tone?: 'neutral' | 'success' | 'danger';
}

export function Badge({ label, tone = 'neutral' }: BadgeProps) {
  return <span data-tone={tone}>{label}</span>;
}
```

After:

```tsx
interface BadgeProps {
  label: string;
  tone?: 'neutral' | 'success' | 'danger';
}

/**
 * Displays a small status badge for short labels.
 * @param props - Badge rendering options (see BadgeProps)
 * @returns Rendered badge element
 */
export function Badge({ label, tone = 'neutral' }: BadgeProps) {
  return <span data-tone={tone}>{label}</span>;
}
```
