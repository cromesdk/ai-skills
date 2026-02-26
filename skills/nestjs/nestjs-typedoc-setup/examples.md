# NestJS TypeDoc examples

## 1. App-level config (`typedoc.json`)

Document controllers, services, DTOs, and modules from `src`.
When Prisma is installed, keep `"**/prisma/generated/**"` excluded.

```json
{
  "entryPoints": ["src"],
  "out": "docs",
  "tsconfig": "tsconfig.json",
  "plugin": ["typedoc-material-theme"],
  "entryPointStrategy": "expand",
  "exclude": [
    "**/*.spec.ts",
    "**/*.test.ts",
    "dist/**",
    "node_modules/**",
    "**/prisma/generated/**"
  ],
  "excludePrivate": true,
  "excludeProtected": true,
  "cleanOutputDir": true
}
```

## 2. Smaller public surface config

Use this when a backend has many internal modules and docs should focus on bootstrap-exposed API paths.

```json
{
  "entryPoints": ["src/main.ts"],
  "out": "docs",
  "tsconfig": "tsconfig.json",
  "plugin": ["typedoc-material-theme"],
  "entryPointStrategy": "resolve",
  "exclude": ["**/*.spec.ts", "**/*.test.ts", "dist/**", "node_modules/**"],
  "excludePrivate": true,
  "excludeProtected": true
}
```

## 3. Service method JSDoc

```typescript
/**
 * Find a user by id.
 * @param id Unique user identifier.
 * @returns User entity when found, otherwise undefined.
 * @example
 * const user = await usersService.findOne('usr_123')
 */
async findOne(id: string): Promise<User | undefined> {
  return this.userRepo.findById(id)
}
```

## 4. Controller endpoint JSDoc

```typescript
/**
 * Return the profile for a user.
 * @param id Unique user identifier from route params.
 * @returns Public user profile.
 */
@Get(':id/profile')
getProfile(@Param('id') id: string): Promise<UserProfileDto> {
  return this.usersService.getProfile(id)
}
```

## 5. Class-level remarks

```typescript
/**
 * Handle authentication and token validation.
 * @remarks
 * Use JWT for access tokens and support refresh token rotation.
 */
@Injectable()
export class AuthService {
  // ...
}
```

## 6. Module-level package docs

```typescript
/**
 * @packageDocumentation
 * Public API for users: controller endpoints, DTOs, and service contracts.
 */
```
