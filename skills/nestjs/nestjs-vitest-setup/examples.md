# NestJS + Vitest examples

## 1. Service unit test with mocked provider

```typescript
import { NotFoundException } from '@nestjs/common'
import { Test, TestingModule } from '@nestjs/testing'
import { beforeEach, describe, expect, it, vi } from 'vitest'

import { UsersRepository } from './users.repository'
import { UsersService } from './users.service'

describe('UsersService', () => {
  let service: UsersService
  const usersRepository = {
    findById: vi.fn(),
  }

  beforeEach(async () => {
    const moduleRef: TestingModule = await Test.createTestingModule({
      providers: [
        UsersService,
        { provide: UsersRepository, useValue: usersRepository },
      ],
    }).compile()

    service = moduleRef.get(UsersService)
    vi.clearAllMocks()
  })

  it('returns the user when found', async () => {
    usersRepository.findById.mockResolvedValue({ id: '1', email: 'dev@example.com' })

    await expect(service.findOne('1')).resolves.toEqual({
      id: '1',
      email: 'dev@example.com',
    })
    expect(usersRepository.findById).toHaveBeenCalledWith('1')
  })

  it('throws NotFoundException when user does not exist', async () => {
    usersRepository.findById.mockResolvedValue(null)

    await expect(service.findOne('404')).rejects.toBeInstanceOf(NotFoundException)
  })
})
```

## 2. Controller test that verifies delegation

```typescript
import { Test } from '@nestjs/testing'
import { beforeEach, describe, expect, it, vi } from 'vitest'

import { CreateUserDto } from './dto/create-user.dto'
import { UsersController } from './users.controller'
import { UsersService } from './users.service'

describe('UsersController', () => {
  let controller: UsersController
  const usersService = {
    create: vi.fn(),
  }

  beforeEach(async () => {
    const moduleRef = await Test.createTestingModule({
      controllers: [UsersController],
      providers: [{ provide: UsersService, useValue: usersService }],
    }).compile()

    controller = moduleRef.get(UsersController)
    vi.clearAllMocks()
  })

  it('calls UsersService.create and returns the result', async () => {
    const dto: CreateUserDto = { email: 'dev@example.com' }
    usersService.create.mockResolvedValue({ id: 'u1', ...dto })

    await expect(controller.create(dto)).resolves.toEqual({
      id: 'u1',
      email: 'dev@example.com',
    })
    expect(usersService.create).toHaveBeenCalledWith(dto)
  })
})
```

## 3. E2E test with INestApplication and supertest

```typescript
import { INestApplication } from '@nestjs/common'
import { Test } from '@nestjs/testing'
import request from 'supertest'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'

import { AppModule } from '../src/app.module'

describe('AppController (e2e)', () => {
  let app: INestApplication

  beforeAll(async () => {
    const moduleFixture = await Test.createTestingModule({
      imports: [AppModule],
    }).compile()

    app = moduleFixture.createNestApplication()
    await app.init()
  })

  afterAll(async () => {
    await app.close()
  })

  it('GET / should return 200', async () => {
    await request(app.getHttpServer())
      .get('/')
      .expect(200)
  })
})
```
