# NestJS CQRS Setup - Examples

Minimal `.env`, command/query handlers, and a controller using buses.

## .env

```env
PORT=3000

# CQRS feature flag
# true or unset: enable CQRS
# false: disable CQRS
CQRS_ENABLED=true
```

## Command and handler

**Command:** `src/items/commands/create-item.command.ts`

```typescript
import { Command } from '@nestjs/cqrs';

export class CreateItemCommand extends Command<void> {
  constructor(public readonly label: string) {
    super();
  }
}
```

**Handler:** `src/items/commands/handlers/create-item.handler.ts`

```typescript
import { CommandHandler, ICommandHandler } from '@nestjs/cqrs';
import { CreateItemCommand } from '../create-item.command.js';

@CommandHandler(CreateItemCommand)
export class CreateItemHandler implements ICommandHandler<CreateItemCommand> {
  async execute(command: CreateItemCommand): Promise<void> {
    const { label } = command;
    console.log('CreateItem', label);
  }
}
```

## Query and handler

**Query:** `src/items/queries/get-item.query.ts`

```typescript
import { Query } from '@nestjs/cqrs';

export class GetItemQuery extends Query<{ id: string; label: string } | null> {
  constructor(public readonly id: string) {
    super();
  }
}
```

**Handler:** `src/items/queries/handlers/get-item.handler.ts`

```typescript
import { IQueryHandler, QueryHandler } from '@nestjs/cqrs';
import { GetItemQuery } from '../get-item.query.js';

@QueryHandler(GetItemQuery)
export class GetItemHandler implements IQueryHandler<GetItemQuery> {
  async execute(query: GetItemQuery): Promise<{ id: string; label: string } | null> {
    const { id } = query;
    return { id, label: `Item ${id}` };
  }
}
```

## Controller using CommandBus and QueryBus

**Controller:** `src/items/items.controller.ts`

```typescript
import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { CommandBus, QueryBus } from '@nestjs/cqrs';
import { CreateItemCommand } from './commands/create-item.command.js';
import { GetItemQuery } from './queries/get-item.query.js';

@Controller('items')
export class ItemsController {
  constructor(
    private readonly commandBus: CommandBus,
    private readonly queryBus: QueryBus,
  ) {}

  @Post()
  async create(@Body('label') label: string): Promise<void> {
    await this.commandBus.execute(new CreateItemCommand(label));
  }

  @Get(':id')
  async get(@Param('id') id: string) {
    return this.queryBus.execute(new GetItemQuery(id));
  }
}
```

## AppModule toggle

Use the same `CQRS_ENABLED` flag for both the CQRS infra and CQRS-dependent feature modules.

```typescript
import { Module } from '@nestjs/common';
import { ConditionalModule, ConfigModule } from '@nestjs/config';
import { CqrsModule } from '@nestjs/cqrs';
import { ItemsModule } from './items/items.module.js';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    ConditionalModule.registerWhen(CqrsModule.forRoot(), 'CQRS_ENABLED'),
    ConditionalModule.registerWhen(ItemsModule, 'CQRS_ENABLED'),
  ],
})
export class AppModule {}
```

When `CQRS_ENABLED=false`, do not load modules that require CQRS buses unless you intentionally provide alternative non-CQRS implementations.
