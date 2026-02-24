# NestJS + Vitest reference

## Jest to Vitest mapping

| Jest | Vitest |
|------|--------|
| `jest.fn()` | `vi.fn()` |
| `jest.spyOn()` | `vi.spyOn()` |
| `jest.mock()` | `vi.mock()` |
| `jest.clearAllMocks()` | `vi.clearAllMocks()` |
| `jest.restoreAllMocks()` | `vi.restoreAllMocks()` |
| `jest.useFakeTimers()` | `vi.useFakeTimers()` |
| `jest.useRealTimers()` | `vi.useRealTimers()` |
| `jest.setSystemTime()` | `vi.setSystemTime()` |

## Nest provider mocking pattern

Use `useValue` providers and keep mocks explicit:

```typescript
const usersRepo = {
  findById: vi.fn(),
  save: vi.fn(),
}

const moduleRef = await Test.createTestingModule({
  providers: [
    UsersService,
    { provide: UsersRepository, useValue: usersRepo },
  ],
}).compile()
```

Reset mock state after each test:

```typescript
afterEach(() => {
  vi.clearAllMocks()
  vi.restoreAllMocks()
})
```

## Hoisted module mocks

`vi.mock()` is hoisted. If the factory needs test-file variables, define them with `vi.hoisted`:

```typescript
const mockedToken = vi.hoisted(() => 'token-123')

vi.mock('./auth.service', () => ({
  issueToken: vi.fn(() => mockedToken),
}))
```

Use `vi.doMock` only when a non-hoisted mock is required.

## E2E bootstrap pattern

```typescript
let app: INestApplication

beforeAll(async () => {
  const moduleRef = await Test.createTestingModule({
    imports: [AppModule],
  }).compile()

  app = moduleRef.createNestApplication()
  await app.init()
})

afterAll(async () => {
  await app.close()
})
```

Always close the Nest app in `afterAll` to avoid hanging workers.

## Coverage thresholds example

Use thresholds to prevent silent test quality regressions:

```typescript
coverage: {
  provider: 'v8',
  reporter: ['text', 'html'],
  reportsDirectory: 'coverage',
  thresholds: {
    lines: 80,
    functions: 80,
    branches: 70,
    statements: 80,
  },
}
```

## Useful CLI commands

- `vitest run` - one-shot run
- `vitest` - watch mode
- `vitest run -t "UsersService"` - run tests by name
- `vitest run src/users/users.service.spec.ts` - run a single file
- `vitest run --coverage` - coverage output

## Links

- [Vitest API](https://vitest.dev/api/)
- [Vitest config](https://vitest.dev/config/)
- [Vitest mocking guide](https://vitest.dev/guide/mocking.html)
- [Vitest coverage](https://vitest.dev/guide/coverage.html)
- [Nest testing fundamentals](https://docs.nestjs.com/fundamentals/testing)
