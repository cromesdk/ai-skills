# NestJS Swagger Install - Examples

Minimal snippets for a modern bootstrap-based Swagger setup.

## AppModule

```typescript
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';

@Module({
  imports: [ConfigModule.forRoot({ isGlobal: true })],
})
export class AppModule {}
```

## main.ts

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

## .env (development)

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

With this configuration:
- Swagger UI: `http://localhost:3000/api/docs`
- OpenAPI JSON: `http://localhost:3000/openapi.json`
- Swagger UI top bar includes an automatic `Download OpenAPI` button (default background `#85ea2d`)

## Optional: with global prefix

If app bootstrap sets a global prefix such as `app.setGlobalPrefix('api')`, prefer:

```env
SWAGGER_PATH=docs
SWAGGER_USE_GLOBAL_PREFIX=true
```

Then docs are served under the global prefix (`/api/docs`, `/api/openapi.json`).

## Optional: enable bearer auth in docs

Set:

```env
SWAGGER_BEARER_AUTH=true
```

Swagger UI shows "Authorize" and sends bearer tokens when trying secured endpoints.
