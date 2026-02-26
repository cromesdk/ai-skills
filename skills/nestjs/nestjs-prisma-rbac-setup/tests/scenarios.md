# Scenarios: prisma-rbac

## Easy: Add RBAC to existing NestJS + Prisma backend

**Given**
- A NestJS backend already uses Prisma and has a working `PrismaService`.
- Auth endpoints are minimal or missing refresh-session handling.

**When**
- The agent applies `$prisma-rbac`.

**Then**
- RBAC schema entities and relation tables are present in Prisma schema.
- JWT auth plus refresh-session rotation behavior is implemented.
- Protected controllers use guard + permission metadata consistently.

## Hard: Repair broken permission traversal and refresh reuse handling

**Given**
- Existing RBAC code checks only direct user roles and ignores group-linked role permissions.
- Refresh endpoint reissues access tokens without revoking/replacing prior refresh session rows.

**When**
- The agent remediates with `$prisma-rbac`.

**Then**
- Permission checks traverse `User -> Group -> Role -> Permission` through relation tables.
- Refresh flow rotates sessions and handles revoked/unknown token reuse defensively.
- Access to protected routes is denied when required permissions are missing.

## Edge: Missing required preconditions

**Given**
- Target project is not an existing NestJS + Prisma backend (missing Prisma module or bootstrap wiring).

**When**
- The agent is asked to run `$prisma-rbac`.

**Then**
- The agent stops before implementation edits.
- The agent reports the missing preconditions and asks for the correct project path.

## Edge: Sensitive token/password handling risk

**Given**
- Existing auth code stores plaintext refresh tokens or logs credential/token material.

**When**
- The agent applies `$prisma-rbac`.

**Then**
- Refresh tokens are stored as one-way hashes only.
- Passwords remain hashed and are never written in plaintext.
- Logs exclude raw tokens, passwords, and full sensitive payloads.
