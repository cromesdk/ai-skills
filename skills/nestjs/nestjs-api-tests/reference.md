# API Tests Reference

## JWT detection checklist

Before generating API tests, check whether the project uses JWT auth. If any of the following are true, generate the JWT scenario (login, protected routes, invalid token):

- [ ] `JWT_SECRET` is referenced in `src/` (e.g. ConfigService.get('JWT_SECRET'), AuthService, RbacModule)
- [ ] `JwtModule` is imported and registered (e.g. in an auth or RBAC module)
- [ ] `AuthGuard` (or similar) is used with `@UseGuards()` on controller methods or classes
- [ ] A login route exists (e.g. `POST /auth/login`) that returns a token in the response body (e.g. `access_token`)

If all are absent, generate only public-endpoint tests. If any are present, include the JWT scenario and ensure `JWT_SECRET` is set for e2e.

---

## Example: app bootstrap with ValidationPipe

Use this pattern so e2e tests match production validation behavior:

```typescript
/// <reference types="vitest/globals" />
import { Test } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
import { ValidationPipe } from '@nestjs/common';
import request from 'supertest';
import { App } from 'supertest/types';
import { AppModule } from '../src/app.module';

describe('App (e2e)', () => {
  let app: INestApplication<App>;

  beforeEach(async () => {
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    app.useGlobalPipes(
      new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }),
    );
    await app.init();
  });

  afterEach(async () => {
    await app?.close();
  });

  it('GET / returns 200', () => {
    return request(app.getHttpServer()).get('/').expect(200);
  });
});
```

---

## Example: auth e2e (login, invalid credentials, logout)

Assumes login at `POST /auth/login` with body `{ username, password }` and response `{ access_token }`. Adjust path and DTO to match the project.

```typescript
describe('AuthController (e2e)', () => {
  let app: INestApplication<App>;

  beforeEach(async () => {
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = moduleFixture.createNestApplication();
    app.useGlobalPipes(
      new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }),
    );
    await app.init();
  });

  afterEach(async () => {
    await app?.close();
  });

  it('POST /auth/login with valid credentials returns 200 and access_token', async () => {
    const res = await request(app.getHttpServer())
      .post('/auth/login')
      .send({ username: 'admin', password: 'admin123' })
      .expect(200);
    expect(res.body).toHaveProperty('access_token');
    expect(typeof res.body.access_token).toBe('string');
  });

  it('POST /auth/login with invalid credentials returns 401', () => {
    return request(app.getHttpServer())
      .post('/auth/login')
      .send({ username: 'admin', password: 'wrong' })
      .expect(401);
  });

  it('POST /auth/logout with valid token returns 200', async () => {
    const login = await request(app.getHttpServer())
      .post('/auth/login')
      .send({ username: 'admin', password: 'admin123' })
      .expect(200);
    const token = login.body.access_token;
    return request(app.getHttpServer())
      .post('/auth/logout')
      .set('Authorization', 'Bearer ' + token)
      .expect(200);
  });
});
```

---

## Example: protected route (no token vs valid token)

Obtain token via login, then call a protected endpoint with and without the Bearer token.

```typescript
async function getToken(app: INestApplication<App>): Promise<string> {
  const res = await request(app.getHttpServer())
    .post('/auth/login')
    .send({ username: 'admin', password: 'admin123' })
    .expect(200);
  return res.body.access_token;
}

describe('UsersController (e2e)', () => {
  let app: INestApplication<App>;

  beforeEach(async () => {
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = moduleFixture.createNestApplication();
    app.useGlobalPipes(
      new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }),
    );
    await app.init();
  });

  afterEach(async () => {
    await app?.close();
  });

  it('GET /users without Authorization returns 401', () => {
    return request(app.getHttpServer()).get('/users').expect(401);
  });

  it('GET /users with valid Bearer token returns 200', async () => {
    const token = await getToken(app);
    return request(app.getHttpServer())
      .get('/users')
      .set('Authorization', 'Bearer ' + token)
      .expect(200);
  });

  it('GET /users with invalid token returns 401', () => {
    return request(app.getHttpServer())
      .get('/users')
      .set('Authorization', 'Bearer invalid')
      .expect(401);
  });
});
```

Use the same `getToken` (or inline login) and `.set('Authorization', 'Bearer ' + token)` for other protected methods (POST, PATCH, DELETE) as needed.
