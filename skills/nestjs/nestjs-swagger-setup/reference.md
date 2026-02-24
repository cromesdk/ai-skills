# NestJS Swagger Install - Reference

Use this implementation as the default for modern NestJS Swagger setup.

## Package and version checks

Run from project root:

```bash
npm install @nestjs/swagger @nestjs/config
npm ls @nestjs/core @nestjs/swagger @nestjs/config
```

Version guidance:
- Nest 11 -> `@nestjs/swagger` ^11
- Nest 10 -> `@nestjs/swagger` ^10

## File placement

- `src/libs/swagger/setup-swagger.ts`

Keep Swagger setup as a bootstrap helper so it stays close to app startup and is easy to gate by environment.

## setup-swagger.ts

**File:** `src/libs/swagger/setup-swagger.ts`

```typescript
import { INestApplication } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import {
  DocumentBuilder,
  SwaggerCustomOptions,
  SwaggerDocumentOptions,
  SwaggerModule,
} from '@nestjs/swagger';

const TRUE_VALUES = new Set(['1', 'true', 'yes', 'on']);

function readBoolean(value: string | undefined, fallback: boolean): boolean {
  if (value === undefined) {
    return fallback;
  }

  return TRUE_VALUES.has(value.toLowerCase());
}

function createDownloadOpenApiButtonScript(jsonDocumentUrl: string): string {
  return `
    (() => {
      const BUTTON_ID = 'download-openapi-json-btn';
      const addButton = () => {
        if (document.getElementById(BUTTON_ID)) return;

        const topbar =
          document.querySelector('.topbar .topbar-wrapper') ??
          document.querySelector('.topbar');
        if (!topbar) return;

        const docsPath = window.location.pathname.replace(/\\/+$/, '');
        const jsonPath = ${JSON.stringify(jsonDocumentUrl)};
        const normalizedJsonPath = jsonPath.startsWith('/')
          ? jsonPath
          : '/' + jsonPath;
        const openApiJsonUrl = docsPath + normalizedJsonPath;

        const button = document.createElement('a');
        button.id = BUTTON_ID;
        button.href = openApiJsonUrl;
        button.download = 'openapi.json';
        button.target = '_blank';
        button.rel = 'noopener noreferrer';
        button.textContent = 'Download OpenAPI';
        button.style.marginLeft = '8px';
        button.style.padding = '6px 12px';
        button.style.borderRadius = '4px';
        button.style.background = '#85ea2d';
        button.style.color = '#111';
        button.style.fontSize = '12px';
        button.style.fontWeight = '600';
        button.style.textDecoration = 'none';
        button.style.whiteSpace = 'nowrap';

        topbar.appendChild(button);
      };

      const interval = window.setInterval(() => {
        addButton();
        if (document.getElementById(BUTTON_ID)) {
          window.clearInterval(interval);
        }
      }, 300);

      addButton();
    })();
  `;
}

export function setupSwagger(app: INestApplication): void {
  const configService = app.get(ConfigService);

  const swaggerEnabled = readBoolean(
    configService.get<string>('SWAGGER_ENABLED'),
    true,
  );

  if (!swaggerEnabled) {
    return;
  }

  const path = configService.get<string>('SWAGGER_PATH') ?? 'api/docs';
  const title = configService.get<string>('SWAGGER_TITLE') ?? 'API';
  const description =
    configService.get<string>('SWAGGER_DESCRIPTION') ??
    'HTTP API documentation';
  const version = configService.get<string>('SWAGGER_VERSION') ?? '1.0.0';

  const uiEnabled = readBoolean(
    configService.get<string>('SWAGGER_UI_ENABLED'),
    true,
  );
  const rawEnabled = readBoolean(
    configService.get<string>('SWAGGER_RAW_ENABLED'),
    true,
  );
  const jsonDocumentUrl =
    configService.get<string>('SWAGGER_JSON_URL') ?? 'openapi.json';
  const useGlobalPrefix = readBoolean(
    configService.get<string>('SWAGGER_USE_GLOBAL_PREFIX'),
    false,
  );
  const useBearerAuth = readBoolean(
    configService.get<string>('SWAGGER_BEARER_AUTH'),
    false,
  );

  let builder = new DocumentBuilder()
    .setTitle(title)
    .setDescription(description)
    .setVersion(version);

  if (useBearerAuth) {
    builder = builder.addBearerAuth();
  }

  const documentOptions: SwaggerDocumentOptions = {
    deepScanRoutes: true,
    autoTagControllers: true,
  };

  const documentFactory = () =>
    SwaggerModule.createDocument(app, builder.build(), documentOptions);

  const customOptions: SwaggerCustomOptions = {
    useGlobalPrefix,
    ui: uiEnabled,
    raw: rawEnabled ? ['json'] : false,
    jsonDocumentUrl,
    swaggerOptions: {
      persistAuthorization: true,
      tagsSorter: 'alpha',
      operationsSorter: 'alpha',
    },
    customJsStr: createDownloadOpenApiButtonScript(jsonDocumentUrl),
  };

  SwaggerModule.setup(path, app, documentFactory, customOptions);
}
```

Behavior:
- Adds an automatic `Download OpenAPI` button to the Swagger UI top bar.
- Button color default is `#85ea2d`.

## AppModule

Add `ConfigModule.forRoot({ isGlobal: true })`:

```typescript
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';

@Module({
  imports: [ConfigModule.forRoot({ isGlobal: true })],
})
export class AppModule {}
```

## main.ts

Register Swagger after app creation and before `listen`:

```typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { setupSwagger } from './libs/swagger/setup-swagger';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  setupSwagger(app);

  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

## .env template

```env
PORT=3000
SWAGGER_ENABLED=true
SWAGGER_PATH=api/docs
SWAGGER_TITLE=API
SWAGGER_DESCRIPTION=HTTP API documentation
SWAGGER_VERSION=1.0.0
SWAGGER_UI_ENABLED=true
SWAGGER_RAW_ENABLED=true
SWAGGER_JSON_URL=openapi.json
SWAGGER_USE_GLOBAL_PREFIX=false
SWAGGER_BEARER_AUTH=false
```

## Production guidance

- Prefer `SWAGGER_ENABLED=false` in production by default.
- If documentation must be live in production, protect it with authentication and network controls.
- Keep secrets out of Swagger toggles (for example, do not use `JWT_SECRET` to decide whether Swagger should be enabled).

## Optional: CLI plugin

Use the Swagger CLI plugin to reduce repetitive decorators in DTOs.

`nest-cli.json`:

```json
{
  "compilerOptions": {
    "plugins": ["@nestjs/swagger"]
  }
}
```

Notes:
- Keep `class-validator` decorators for runtime validation.
- For mapped types (`PartialType`, `PickType`, `OmitType`, `IntersectionType`), import from `@nestjs/swagger`.
- If using SWC, enable type checking (for example `"typeCheck": true`) so plugin metadata generation remains reliable.
