# Setup Winston reference implementation

Use these snippets for a Nest logger with:

- pretty console output in development
- JSON console output in production
- JSON file logs for `combined.log` and `error.log`
- exception and rejection logs

## logger.module.ts

```typescript
import { Global, Module } from "@nestjs/common";
import { LoggerService } from "./logger.service.js";

@Global()
@Module({
  providers: [LoggerService],
  exports: [LoggerService],
})
export class LoggerModule {}
```

## logger.service.ts

Required env: `LOGGER_LEVEL`, `LOGGER_SERVICE_NAME`, `LOGGER_PATH`.

```typescript
import {
  Injectable,
  LoggerService as NestLoggerService,
  OnModuleDestroy,
} from "@nestjs/common";
import { ConfigService } from "@nestjs/config";
import { mkdirSync } from "node:fs";
import * as winston from "winston";

type LogMeta = Record<string, unknown>;

@Injectable()
export class LoggerService implements NestLoggerService, OnModuleDestroy {
  private readonly logger: winston.Logger;

  constructor(private readonly configService: ConfigService) {
    this.ensureLogDirectory();
    this.logger = this.createLogger();

    this.logger.exceptions.handle(
      new winston.transports.File({
        filename: `${this.loggerPath}/exceptions.log`,
        format: this.jsonFormat,
      }),
    );

    this.logger.rejections.handle(
      new winston.transports.File({
        filename: `${this.loggerPath}/rejections.log`,
        format: this.jsonFormat,
      }),
    );
  }

  onModuleDestroy(): void {
    // Winston exception/rejection handlers attach process-level listeners.
    // Detach and close transports to avoid listener leaks in tests and module restarts.
    this.logger.exceptions.unhandle();
    this.logger.rejections.unhandle();
    this.logger.close();
  }

  private get loggerPath(): string {
    return this.getRequired("LOGGER_PATH");
  }

  private get logLevel(): string {
    return this.getRequired("LOGGER_LEVEL");
  }

  private get serviceName(): string {
    return this.getRequired("LOGGER_SERVICE_NAME");
  }

  private get isProduction(): boolean {
    return this.configService.get<string>("NODE_ENV") === "production";
  }

  private getRequired(key: string): string {
    const value = this.configService.get<string>(key);
    if (!value) {
      throw new Error(`${key} is not defined in the configuration`);
    }
    return value;
  }

  private ensureLogDirectory(): void {
    mkdirSync(this.loggerPath, { recursive: true });
  }

  private get jsonFormat(): winston.Logform.Format {
    return winston.format.combine(
      winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
      winston.format.errors({ stack: true }),
      winston.format.splat(),
      winston.format.json(),
    );
  }

  private get prettyConsoleFormat(): winston.Logform.Format {
    const levelPadding = 7;
    return winston.format.combine(
      winston.format.colorize(),
      winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
      winston.format.printf(({ timestamp, level, message, ...meta }) => {
        const paddedLevel = level.padEnd(levelPadding);
        let line = `${timestamp} ${paddedLevel} ${String(message)}`;

        const filteredMeta = Object.fromEntries(
          Object.entries(meta).filter(([, value]) => value !== undefined && value !== null),
        );

        if (Object.keys(filteredMeta).length > 0) {
          line += "\n  " + JSON.stringify(filteredMeta, null, 2).replace(/\n/g, "\n  ");
        }

        return line;
      }),
    );
  }

  private createLogger(): winston.Logger {
    const path = this.loggerPath;

    return winston.createLogger({
      level: this.logLevel,
      format: this.jsonFormat,
      defaultMeta: { service: this.serviceName },
      transports: [
        new winston.transports.Console({
          format: this.isProduction ? this.jsonFormat : this.prettyConsoleFormat,
        }),
        new winston.transports.File({
          filename: `${path}/error.log`,
          level: "error",
          format: this.jsonFormat,
        }),
        new winston.transports.File({
          filename: `${path}/combined.log`,
          format: this.jsonFormat,
        }),
      ],
    });
  }

  private withMeta(context?: string, meta?: LogMeta): LogMeta {
    return context ? { context, ...(meta ?? {}) } : { ...(meta ?? {}) };
  }

  log(message: string, context?: string, meta?: LogMeta): void {
    this.logger.info(message, this.withMeta(context, meta));
  }

  info(message: string, context?: string, meta?: LogMeta): void {
    this.logger.info(message, this.withMeta(context, meta));
  }

  warn(message: string, context?: string, meta?: LogMeta): void {
    this.logger.warn(message, this.withMeta(context, meta));
  }

  debug(message: string, context?: string, meta?: LogMeta): void {
    this.logger.debug(message, this.withMeta(context, meta));
  }

  verbose(message: string, context?: string, meta?: LogMeta): void {
    this.logger.verbose(message, this.withMeta(context, meta));
  }

  error(message: string, trace?: string, context?: string, meta?: LogMeta): void {
    this.logger.error(message, {
      trace,
      ...this.withMeta(context, meta),
    });
  }

  fatal(message: string, context?: string, meta?: LogMeta): void {
    this.logger.log("error", message, {
      fatal: true,
      ...this.withMeta(context, meta),
    });
  }
}
```

## AppModule wiring

```typescript
import { Module } from "@nestjs/common";
import { ConfigModule } from "@nestjs/config";
import { LoggerModule } from "./libs/logger/logger.module.js";

@Module({
  imports: [ConfigModule.forRoot({ isGlobal: true }), LoggerModule],
})
export class AppModule {}
```

## main.ts wiring

```typescript
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module.js";
import { LoggerService } from "./libs/logger/logger.service.js";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useLogger(app.get(LoggerService));
  await app.listen(process.env.PORT ?? 3000);
}

void bootstrap();
```

## .env snippet

```env
LOGGER_LEVEL=info
LOGGER_SERVICE_NAME=my-service
LOGGER_PATH=logs
```

