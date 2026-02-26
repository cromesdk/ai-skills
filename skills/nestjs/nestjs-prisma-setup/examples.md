# NestJS Prisma Setup Examples

Minimal usage pattern after `PrismaModule` is added globally.

## Inject PrismaService

```typescript
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../libs/prisma/prisma.service';

@Injectable()
export class UsersService {
  constructor(private readonly prisma: PrismaService) {}

  findMany() {
    return this.prisma.user.findMany();
  }

  create(data: { email: string; name?: string }) {
    return this.prisma.user.create({ data });
  }
}
```

Notes:
- Replace `user` with model delegates generated from your own schema.
- After schema changes, run `npx prisma migrate dev` and `npx prisma generate`.
- For NodeNext/ESM projects, use `.js` in relative imports.
