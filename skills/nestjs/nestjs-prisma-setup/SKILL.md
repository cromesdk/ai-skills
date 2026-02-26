---
name: nestjs-prisma-setup
description: Install and configure Prisma ORM in a NestJS backend with a generated client, prisma.config.ts, PrismaService, PrismaModule, and migrations. Default workflow targets SQLite with @prisma/adapter-better-sqlite3, plus NodeNext/ESM import guidance and Prisma v7 generator settings. Use when the user asks to add Prisma, initialize schema and migrations, or wire Prisma client access into Nest services.
---

# NestJS Prisma Setup

Use this workflow to add Prisma to a Nest app with a reusable service and module.

## Prerequisites

- NestJS backend with `AppModule` and `main.ts`
- Node.js 20+ for Nest 11 projects (or the runtime already pinned by the repository)
- Keep `prisma` and `@prisma/client` on the same major version

## Install steps

1. Install base packages from project root:

   ```bash
   npm install --save-dev prisma dotenv
   npm install @prisma/client
   npm install @prisma/adapter-better-sqlite3 better-sqlite3
   ```

2. If the app does not already use `@nestjs/config`, install it:

   ```bash
   npm install @nestjs/config
   ```

3. Resolve peer dependency warnings before wiring Prisma.

## Initialize Prisma

Run from project root:

```bash
npx prisma init --datasource-provider sqlite --output ../src/libs/prisma/generated
```

This creates `prisma/schema.prisma`, `prisma.config.ts`, and `.env`.

If `.env` already exists, merge the Prisma entries instead of replacing the file.

## Configure schema and config

Use generator and datasource blocks from [reference.md](reference.md), then add your models.

- Keep datasource URL in `prisma.config.ts` when using adapters.
- For Nest CommonJS projects, set `moduleFormat = "cjs"` in the generator block.
- For NodeNext/ESM projects, keep generator and module settings aligned with your TypeScript module strategy.

## Add PrismaService and PrismaModule

1. Add files from [reference.md](reference.md):
   - `src/libs/prisma/prisma.service.ts`
   - `src/libs/prisma/prisma.module.ts`
2. In `PrismaService`:
   - inject `ConfigService`
   - build `PrismaBetterSqlite3` from the constructor parameter
   - call `super({ adapter })`
   - implement `OnModuleInit` and `OnModuleDestroy`
   - run `VACUUM` on startup after `$connect()` (recommended for local SQLite file compaction after heavy deletes)
3. Do not access `this` before `super()`.
4. Do not use `this.$on('beforeExit', ...)` with driver adapters; Prisma client engine throws at runtime.

## Wire AppModule

- Add `ConfigModule.forRoot({ isGlobal: true })` if not already configured.
- Add `PrismaModule` to `AppModule.imports`.
- Keep `PrismaModule` global so feature modules can inject `PrismaService` without re-importing the module.

## .env setup

For SQLite:

```env
DATABASE_URL="file:./dev.db"
```

Use an absolute file path if app startup does not run from project root.

## Usage pattern

Inject `PrismaService` into services/controllers and call model delegates from your schema. See [examples.md](examples.md).

## Migrations and client generation

After adding or changing models:

```bash
npx prisma migrate dev --name init
npx prisma generate
```

Optional package scripts:

```json
"prisma:generate": "prisma generate",
"prisma:migrate": "prisma migrate dev"
```

## Verification

1. Run app (for example `npm run start:dev`).
2. Confirm startup has no Prisma connection errors.
3. Call one read and one write endpoint that use `PrismaService`.
4. Confirm migration artifacts and the SQLite database file are created.

## Checklist

- [ ] Install `prisma`, `dotenv`, `@prisma/client`, `@prisma/adapter-better-sqlite3`, and `better-sqlite3`
- [ ] Install `@nestjs/config` if not already present
- [ ] Run `npx prisma init --datasource-provider sqlite --output ../src/libs/prisma/generated`
- [ ] Configure `prisma/schema.prisma` and `prisma.config.ts`
- [ ] Add `PrismaService` and `PrismaModule` from [reference.md](reference.md)
- [ ] Wire `ConfigModule.forRoot({ isGlobal: true })` and `PrismaModule` in `AppModule`
- [ ] Run `npx prisma migrate dev --name init` and `npx prisma generate`
- [ ] Ensure `.env` is listed in `.gitignore`
- [ ] Verify runtime reads and writes through Prisma

## Additional resources

- Full implementation snippets: [reference.md](reference.md)
- Usage pattern: [examples.md](examples.md)
- [NestJS Prisma recipe](https://docs.nestjs.com/recipes/prisma)
- [Prisma init command](https://www.prisma.io/docs/orm/reference/prisma-cli-reference#init)
- [Prisma driver adapters](https://www.prisma.io/docs/orm/overview/databases/database-drivers)
