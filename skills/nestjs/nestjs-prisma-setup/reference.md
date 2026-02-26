# NestJS Prisma Setup Reference

Copy or adapt this implementation for NestJS + Prisma with SQLite and `better-sqlite3`.

## File placement

- `src/libs/prisma/prisma.service.ts`
- `src/libs/prisma/prisma.module.ts`
- `prisma/schema.prisma`
- `prisma.config.ts`

## schema.prisma

**File:** `prisma/schema.prisma`

```prisma
generator client {
  provider     = "prisma-client"
  output       = "../src/libs/prisma/generated"
  moduleFormat = "cjs"
}

datasource db {
  provider = "sqlite"
}
```

Notes:
- `moduleFormat = "cjs"` matches Nest CommonJS defaults.
- For NodeNext/ESM projects, align generator settings with your module strategy.
- Keep datasource URL in `prisma.config.ts` when using adapters.

## prisma.config.ts

**File:** `prisma.config.ts`

```typescript
import 'dotenv/config';
import { defineConfig } from 'prisma/config';

export default defineConfig({
  schema: 'prisma/schema.prisma',
  migrations: {
    path: 'prisma/migrations',
  },
  datasource: {
    url: process.env['DATABASE_URL'],
  },
});
```

## PrismaService

**File:** `src/libs/prisma/prisma.service.ts`

```typescript
import { Injectable, OnModuleDestroy, OnModuleInit } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { PrismaBetterSqlite3 } from '@prisma/adapter-better-sqlite3';
import { PrismaClient } from './generated/client';

@Injectable()
export class PrismaService
  extends PrismaClient
  implements OnModuleInit, OnModuleDestroy
{
  constructor(configService: ConfigService) {
    const url = configService.getOrThrow<string>('DATABASE_URL');
    const adapter = new PrismaBetterSqlite3({ url });
    super({ adapter });
  }

  async onModuleInit(): Promise<void> {
    await this.$connect();
    await this.vacuumOnStartup();
  }

  async onModuleDestroy(): Promise<void> {
    await this.$disconnect();
  }

  private async vacuumOnStartup(): Promise<void> {
    try {
      await this.$executeRawUnsafe('VACUUM');
    } catch (error) {
      const reason = error instanceof Error ? error.message : String(error);
      console.warn(`Prisma startup VACUUM failed: ${reason}`);
    }
  }
}
```

Notes:
- Do not use `this` before `super()`.
- Do not wire `this.$on('beforeExit', ...)` with driver adapters; it is not supported by Prisma client engine.
- For NodeNext/ESM, use `./generated/client.js` in relative imports.
- Running `VACUUM` on startup is useful for SQLite when files grow after deletions; keep failure non-fatal.

## PrismaModule

**File:** `src/libs/prisma/prisma.module.ts`

```typescript
import { Global, Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { PrismaService } from './prisma.service';

@Global()
@Module({
  imports: [ConfigModule],
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
```

For NodeNext/ESM, use `./prisma.service.js` in relative imports.

## AppModule wiring

```typescript
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { PrismaModule } from './libs/prisma/prisma.module';

@Module({
  imports: [ConfigModule.forRoot({ isGlobal: true }), PrismaModule],
})
export class AppModule {}
```

For NodeNext/ESM, use emitted `.js` extensions in relative imports.

## main.ts

No Prisma-specific shutdown hook is required for this adapter setup:

```typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(process.env.PORT ?? 3000);
}

void bootstrap();
```
