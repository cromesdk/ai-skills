# Reference: bcryptjs setup for NestJS

## SALT_ROUNDS guidance

- Use `10-12` in production for stronger hashes.
- Use lower values (`4-8`) in tests and local development for speed.
- Keep `SALT_ROUNDS` as an integer string in `.env` (example: `SALT_ROUNDS=10`).

---

## `encryption.service.ts`

```ts
import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import * as bcrypt from 'bcryptjs';

const MIN_SALT_ROUNDS = 4;
const MAX_SALT_ROUNDS = 31;

/**
 * Provides one-way hashing and verification for secrets using bcryptjs.
 */
@Injectable()
export class EncryptionService {
  private readonly saltRounds: number;

  constructor(private readonly configService: ConfigService) {
    this.saltRounds = this.parseSaltRounds(
      this.configService.get<string>('SALT_ROUNDS'),
    );
  }

  /**
   * Hash a plain string (password, token, API key).
   */
  async hash(plain: string): Promise<string> {
    return bcrypt.hash(plain, this.saltRounds);
  }

  /**
   * Verify plain input against an existing bcrypt hash.
   */
  async verify(plain: string, hashed: string): Promise<boolean> {
    return bcrypt.compare(plain, hashed);
  }

  private parseSaltRounds(raw: string | undefined): number {
    if (raw === undefined) {
      throw new Error('SALT_ROUNDS is not set');
    }

    const parsed = Number(raw);
    if (
      !Number.isInteger(parsed) ||
      parsed < MIN_SALT_ROUNDS ||
      parsed > MAX_SALT_ROUNDS
    ) {
      throw new Error(
        `SALT_ROUNDS must be an integer between ${MIN_SALT_ROUNDS} and ${MAX_SALT_ROUNDS}`,
      );
    }

    return parsed;
  }
}
```

---

## `encryption.module.ts`

```ts
import { Global, Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { EncryptionService } from './encryption.service';

@Global()
@Module({
  imports: [ConfigModule],
  providers: [EncryptionService],
  exports: [EncryptionService],
})
export class EncryptionModule {}
```

---

## `app.module.ts` wiring example

```ts
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { EncryptionModule } from './libs/encryption/encryption.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    EncryptionModule,
  ],
})
export class AppModule {}
```

---

## `encryption.utils.ts` (optional)

```ts
const DEFAULT_SALT_ROUNDS = 10;

/**
 * Append encryption env lines to an array used to build .env templates.
 */
export function addEncryptionEnvVariables(
  values: Array<string>,
  saltRounds: number = DEFAULT_SALT_ROUNDS,
): void {
  values.push('# Encryption (bcrypt)');
  values.push(`SALT_ROUNDS=${saltRounds}`);
  values.push('');
}
```

---

## `index.ts`

```ts
export * from './encryption.service';
export * from './encryption.module';
export * from './encryption.utils';
```
