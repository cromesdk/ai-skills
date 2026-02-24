---
name: nestjs-bcryptjs-setup
description: Install and configure bcryptjs in a NestJS backend with ConfigModule-driven SALT_ROUNDS, a reusable one-way hashing service (`hash` and `verify`), and a global EncryptionModule. Use when the user asks to add password hashing, secret hashing, login credential verification, or bcrypt-based auth utilities.
---

# NestJS bcryptjs Setup

Use this workflow to add reusable one-way secret hashing with bcryptjs.

## Prerequisites

- NestJS backend with `AppModule` and `src`
- Node.js 20+ for modern Nest projects
- `@nestjs/config` available so `SALT_ROUNDS` can be read from environment

If `@nestjs/config` is missing:

```bash
npm install @nestjs/config
```

## Install packages

Run from project root:

```bash
npm install bcryptjs
npm install -D @types/bcryptjs
```

## Configure `SALT_ROUNDS`

Add `SALT_ROUNDS` to `.env`:

- Production: `10-12`
- Tests/local fast feedback: `4-8`

Example:

```env
SALT_ROUNDS=10
```

If not already present, wire global config in `AppModule`:

```ts
ConfigModule.forRoot({ isGlobal: true })
```

## Add `EncryptionService`

Implement `EncryptionService` from [reference.md](reference.md) with these rules:

1. Inject `ConfigService`.
2. Parse and validate `SALT_ROUNDS` once in the constructor.
3. Expose `hash(plain: string): Promise<string>`.
4. Expose `verify(plain: string, hashed: string): Promise<boolean>`.
5. Use only one-way terms (`hash` and `verify`), not encrypt/decrypt names.

## Add `EncryptionModule`

Create a global module from [reference.md](reference.md) that:

- imports `ConfigModule`
- provides `EncryptionService`
- exports `EncryptionService`

Register `EncryptionModule` in `AppModule.imports`.

## Optional env helper

Use `addEncryptionEnvVariables` from [reference.md](reference.md) if the project generates `.env` or `.env.example` files programmatically.

## Suggested file layout

- `src/libs/encryption/encryption.service.ts`
- `src/libs/encryption/encryption.module.ts`
- `src/libs/encryption/encryption.utils.ts` (optional)
- `src/libs/encryption/index.ts`

## Verification

1. App boots with `SALT_ROUNDS` set.
2. `verify(plain, await hash(plain))` returns `true`.
3. `verify('wrong', await hash('correct'))` returns `false`.
4. Invalid or missing `SALT_ROUNDS` fails fast with a clear startup error.

## Checklist

- [ ] Install `bcryptjs` and `@types/bcryptjs`
- [ ] Ensure `ConfigModule.forRoot({ isGlobal: true })` is configured
- [ ] Add `SALT_ROUNDS` to `.env`
- [ ] Add `EncryptionService` and `EncryptionModule` from [reference.md](reference.md)
- [ ] Import `EncryptionModule` in `AppModule`
- [ ] Verify hash and compare flow end to end

## Additional resources

- Full code snippets: [reference.md](reference.md)
