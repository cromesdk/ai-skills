# Scenarios: nestjs-prisma-setup

## Easy: Fresh SQLite Prisma setup in NestJS

**Given**
- A NestJS backend without Prisma installed.
- npm is the package manager.

**When**
- The agent runs `$nestjs-prisma-setup` and follows preflight, install, init, wiring, migration, and verification steps.

**Then**
- `prisma/schema.prisma` and `prisma.config.ts` exist.
- `src/libs/prisma/prisma.service.ts` and `src/libs/prisma/prisma.module.ts` are wired.
- Migration artifacts and generated client are present.
- App starts with no Prisma connection errors.

## Hard: Repair existing broken Prisma integration (ESM mismatch)

**Given**
- Project already has Prisma files.
- Runtime is NodeNext/ESM.
- Prisma imports incorrectly omit required emitted `.js` extensions.

**When**
- The agent runs `$nestjs-prisma-setup` in repair mode.

**Then**
- Existing schema models are preserved unless explicit rewrite requested.
- Generated-client imports are aligned to ESM rules.
- Prisma client regenerates successfully.
- Startup and read/write verification gates pass.

## Edge: Adapter-specific hook misuse and version drift

**Given**
- `prisma` and `@prisma/client` are on different major versions.
- `PrismaService` uses `this.$on('beforeExit', ...)` while using driver adapters.

**When**
- The agent applies `$nestjs-prisma-setup` remediation.

**Then**
- Prisma package majors are aligned.
- Unsupported `beforeExit` hook usage is removed.
- Adapter wiring uses `super({ adapter })` safely.
- Runtime initializes without adapter engine errors.

## Edge: Existing `.env` file with custom variables

**Given**
- `.env` already exists with unrelated keys.

**When**
- The agent initializes Prisma.

**Then**
- Existing `.env` keys are preserved.
- `DATABASE_URL` is merged or updated without destructive replacement.
- Verification confirms datasource resolution via `prisma.config.ts`.
