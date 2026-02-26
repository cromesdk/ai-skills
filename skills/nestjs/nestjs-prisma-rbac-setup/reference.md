# RBAC reference

## Full Prisma schema (RBAC models)

Add these models to the project's `prisma/schema.prisma` (keep existing generator and datasource). Adjust `output` if your Prisma client lives elsewhere.

```prisma
model User {
  id           Int           @id @default(autoincrement())
  username     String        @unique
  password     String
  createdAt    DateTime      @default(now())
  updatedAt    DateTime      @updatedAt
  userGroups   UserGroup[]
  authSessions AuthSession[]

  @@map("users")
}

model Group {
  id          Int         @id @default(autoincrement())
  name        String      @unique
  description String?
  createdAt   DateTime    @default(now())
  updatedAt   DateTime    @updatedAt
  users       UserGroup[]
  groupRoles  GroupRole[]

  @@map("groups")
}

model UserGroup {
  userId  Int
  groupId Int
  user    User  @relation(fields: [userId], references: [id], onDelete: Cascade)
  group   Group @relation(fields: [groupId], references: [id], onDelete: Cascade)

  @@id([userId, groupId])
  @@map("user_groups")
}

model Permission {
  id              Int              @id @default(autoincrement())
  name            String           @unique
  description     String?
  createdAt       DateTime         @default(now())
  updatedAt       DateTime         @updatedAt
  rolePermissions RolePermission[]

  @@map("permissions")
}

model Role {
  id              Int              @id @default(autoincrement())
  name            String           @unique
  description     String?
  createdAt       DateTime         @default(now())
  updatedAt       DateTime         @updatedAt
  groupRoles      GroupRole[]
  rolePermissions RolePermission[]

  @@map("roles")
}

model RolePermission {
  roleId       Int
  permissionId Int
  role         Role       @relation(fields: [roleId], references: [id], onDelete: Cascade)
  permission   Permission @relation(fields: [permissionId], references: [id], onDelete: Cascade)

  @@id([roleId, permissionId])
  @@map("role_permissions")
}

model GroupRole {
  groupId Int
  roleId  Int
  group   Group @relation(fields: [groupId], references: [id], onDelete: Cascade)
  role    Role  @relation(fields: [roleId], references: [id], onDelete: Cascade)

  @@id([groupId, roleId])
  @@map("group_roles")
}

model AuthSession {
  id               String    @id @default(cuid())
  userId           Int
  refreshTokenHash String    @unique
  expiresAt        DateTime
  revokedAt        DateTime?
  replacedById     String?
  userAgent        String?
  ip               String?
  createdAt        DateTime  @default(now())
  updatedAt        DateTime  @updatedAt

  user       User         @relation(fields: [userId], references: [id], onDelete: Cascade)
  replacedBy AuthSession? @relation("SessionReplacement", fields: [replacedById], references: [id])
  replaced   AuthSession? @relation("SessionReplacement")

  @@index([userId])
  @@index([expiresAt])
  @@index([revokedAt])
  @@map("auth_sessions")
}
```

## Refresh-token flow standard (recommended)

1. Generate an access JWT (short TTL) and an opaque refresh token (long TTL) at login.
2. Hash refresh token before persistence (`refreshTokenHash`).
3. On `/auth/refresh`, find active session by hash + expiry + revoked check.
4. Rotate refresh token on every successful refresh:
   - revoke old session (`revokedAt = now`)
   - create successor session with a new hash and expiry
   - optionally set `replacedById`
5. Reuse detection: if an already-revoked refresh token is used, revoke all active sessions for that user.
6. Revoke current session on logout; provide logout-all endpoint for all devices if needed.

Use HttpOnly + Secure + SameSite cookies for browser refresh tokens whenever possible.

## Inspiration file paths

Reference project root: `c:\Users\Jsiem\Downloads\nestjs-backend-main\nestjs-backend-main`.

Use these paths to open and adapt concrete implementations:

| Purpose | Path under `src/libs/rbac/` |
|--------|------------------------------|
| Module | `rbac.module.ts` |
| Guard | `guards/auth.guard.ts` |
| Auth service | `services/auth.service.ts` |
| Token or session service | `services/token.service.ts` |
| User service | `services/user.service.ts` |
| User-groups service | `services/user-groups.service.ts` |
| Group service | `services/group.service.ts` |
| Role service | `services/role.service.ts` |
| Permission service | `services/permission.service.ts` |
| Auth controller | `controllers/auth.controller.ts` |
| User controller | `controllers/user.controller.ts` |
| Group controller | `controllers/group.controller.ts` |
| Role controller | `controllers/role.controller.ts` |
| Permission controller | `controllers/permission.controller.ts` |
| Auth context util | `utils/auth-context.utils.ts` |
| Auth decorator | `utils/auth-decorator.ts` |
| Responses decorator | `utils/responses-decorator.ts` |
| Session interface | `interfaces/session.interface.ts` |
| DTOs (create/patch/get/delete/replace) | `dtos/create-user.dto.ts`, `dtos/patch-user.dto.ts`, `dtos/get-user.dto.ts`, `dtos/delete-user.dto.ts`, `dtos/change-password.dto.ts`, `dtos/replace-user-groups.dto.ts`, and analogous files for group, role, permission |

Prisma schema with RBAC models: `prisma/schema.prisma` in the same reference project.

