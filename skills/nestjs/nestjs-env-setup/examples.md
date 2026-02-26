# Examples: .env template and env-sync output

## .env template

Use this template when creating or documenting .env. It matches common Nest backends (logger, Swagger, port).

```env
PORT=3000
NODE_ENV=development

# Logger
LOGGER_LEVEL=info
LOGGER_SERVICE_NAME=new-backend-application
LOGGER_PATH=logs

# Swagger (OpenAPI)
SWAGGER_TITLE=NEST API
SWAGGER_DESCRIPTION=The NEST API documentation
SWAGGER_VERSION=1.0
SWAGGER_PATH=api/docs

# Optional: enable "Authorize" in Swagger UI for JWT
# JWT_SECRET=your-secret
```

## Example output of env-sync (manual)

When the AI performs the env-sync command and finds keys in code that are missing from .env, it can report something like:

```
Env sync: found 9 keys in source (PORT, NODE_ENV, LOGGER_LEVEL, LOGGER_SERVICE_NAME, LOGGER_PATH, SWAGGER_TITLE, SWAGGER_DESCRIPTION, SWAGGER_VERSION, SWAGGER_PATH, JWT_SECRET).
Updated .env: added LOGGER_PATH=, JWT_SECRET=.
```

Or simpler:

```
Env sync complete. .env updated with missing keys from src/.
```

The sync should not overwrite existing values; it only appends new keys with an empty value so the user can fill them in.
