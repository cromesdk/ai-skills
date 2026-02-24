# NestJS CQRS Setup - Reference

Use this reference to wire CQRS with a safe environment toggle.

## Env

| Key | Default | Purpose |
| --- | --- | --- |
| `CQRS_ENABLED` | enabled when unset | `true` or unset enables CQRS; `false` disables CQRS |

## Recommended AppModule wiring

Use `ConditionalModule.registerWhen(...)` from `@nestjs/config` so the CQRS module is toggled after env loading, not at top-level file evaluation.

**File:** `src/app.module.ts`

```typescript
import { Module } from '@nestjs/common';
import { ConditionalModule, ConfigModule } from '@nestjs/config';
import { CqrsModule } from '@nestjs/cqrs';
import { ItemsModule } from './items/items.module.js';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),

    // Enable CQRS only when CQRS_ENABLED is not false.
    ConditionalModule.registerWhen(CqrsModule.forRoot(), 'CQRS_ENABLED'),

    // Gate CQRS-dependent feature modules with the same flag.
    ConditionalModule.registerWhen(ItemsModule, 'CQRS_ENABLED'),
  ],
})
export class AppModule {}
```

## Why this pattern

- Avoids fragile `const enabled = process.env...` checks at module load time.
- Keeps one source of truth (`CQRS_ENABLED`) for both CQRS infra and CQRS-dependent feature modules.
- Prevents startup DI failures when CQRS is disabled.

## Feature module shape

CQRS handlers stay in feature modules as normal.

**File:** `src/items/items.module.ts`

```typescript
import { Module } from '@nestjs/common';
import { CqrsModule } from '@nestjs/cqrs';
import { CreateItemHandler } from './commands/handlers/create-item.handler.js';
import { GetItemHandler } from './queries/handlers/get-item.handler.js';
import { ItemsController } from './items.controller.js';

@Module({
  imports: [CqrsModule],
  controllers: [ItemsController],
  providers: [CreateItemHandler, GetItemHandler],
})
export class ItemsModule {}
```

## ESM / NodeNext note

If the project uses `"moduleResolution": "nodenext"` or `"node16"`, use `.js` in relative import specifiers inside `.ts` files.

## Legacy pattern warning

Avoid wrappers that read `process.env.CQRS_ENABLED` at file top level to decide module imports. They can evaluate before `.env` is loaded, causing inconsistent behavior across `start`, `start:dev`, and tests.
