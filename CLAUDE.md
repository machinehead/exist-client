# CLAUDE.md

This file provides guidance to Claude Code when working with the exist-client library.

## Project Overview

`exist-client` is a Python client library for the [Exist.io](https://exist.io) personal analytics API. It provides a clean, type-safe interface for interacting with Exist.io's REST API, including OAuth authentication, attribute management, and data updates.

**GitHub**: https://github.com/machinehead/exist-client
**PyPI Package**: `exist-client`
**Current Version**: 0.3.0
**Python Support**: >=3.10

## Architecture

### Code Generation

This library uses **auto-generation** from an OpenAPI specification:

- **OpenAPI Spec**: `codegen/exist.io.yaml` - Source of truth for API schema
- **Generator**: `openapi-python-client` - Generates Python client code
- **Generated Code**: `src/exist_client/_exist_io_client/` - Auto-generated API client (DO NOT EDIT DIRECTLY)
- **Custom Code**: `src/exist_client/client.py` - Hand-written wrapper around generated code

**IMPORTANT**: Never edit files in `_exist_io_client/` directly. Changes will be overwritten when regenerating.

### Project Structure

```
exist-client/
├── codegen/
│   ├── exist.io.yaml          # OpenAPI specification
│   ├── config.yaml            # Codegen configuration
│   ├── templates/             # Custom Jinja2 templates for generation
│   └── update-client.sh       # Script to regenerate client code
├── src/exist_client/
│   ├── __init__.py
│   ├── client.py              # Main ExistClient class (hand-written)
│   ├── models.py              # Re-exports from generated models
│   └── _exist_io_client/      # Auto-generated code (DO NOT EDIT)
│       ├── api/
│       ├── models/
│       └── client.py
├── tests/
│   ├── conftest.py            # Pytest fixtures
│   ├── test_client_mock.py   # Unit tests with mocked HTTP
│   └── test_client_simulator.py  # Integration tests with Flask simulator
├── use.py                     # Example usage script
└── pyproject.toml             # Poetry configuration
```

## Development Workflow

### Initial Setup

```bash
poetry install
pre-commit install
pre-commit autoupdate
```

### Common Tasks

#### Running Tests

```bash
# Run all tests with coverage
poetry run pytest

# Run specific test file
poetry run pytest tests/test_client_mock.py

# Run specific test
poetry run pytest tests/test_client_mock.py::test_refresh_token -v

# Run with verbose output
poetry run pytest -v
```

#### Type Checking

```bash
# Check specific file
poetry run mypy src/exist_client/client.py

# Check entire project
poetry run mypy src/
```

#### Code Formatting and Linting

Pre-commit hooks automatically run:
- **black** - Code formatting
- **isort** - Import sorting
- **flake8** - Linting
- **trailing-whitespace** - Removes trailing whitespace
- **end-of-file-fixer** - Ensures files end with newline

To run manually:
```bash
pre-commit run --all-files
```

#### Regenerating Client Code

**When to regenerate:**
- After modifying `codegen/exist.io.yaml`
- After updating API endpoints or models
- After changing request/response schemas

**How to regenerate:**
```bash
cd /path/to/exist-client
poetry run ./codegen/update-client.sh
```

This will:
1. Delete and recreate `src/exist_client/_exist_io_client/`
2. Generate new Python code from the OpenAPI spec
3. Apply custom templates from `codegen/templates/`

**After regenerating:**
- Review changes with `git diff`
- Run tests to ensure nothing broke
- Update `client.py` if new endpoints were added

### Versioning and Releases

This project uses:
- **Commitizen** for conventional commits and changelog management
- **poetry-dynamic-versioning** for automatic version management from git tags
- **GitHub Actions** for automated CI/CD and PyPI publishing

#### Creating a Release

Publishing is **automated via GitHub Actions**. When you push a tag, CI will build and publish to PyPI.

```bash
# Bump version and update CHANGELOG
poetry run cz bump

# Push tags (this triggers CI/CD)
git push --follow-tags
```

**What happens in CI:**
1. Tag push triggers `.github/workflows/publish-to-pypi.yml`
2. Runs full CI workflow (mypy, pytest, coverage)
3. Builds package with `poetry build`
4. Publishes to PyPI using trusted publishing (OIDC)

**Manual publish** (only if needed):
```bash
poetry build
poetry publish
```

Version format: `v{major}.{minor}.{patch}` (e.g., `v0.3.0`)

### CI/CD Pipeline

#### Continuous Integration (`.github/workflows/ci.yml`)

Runs on:
- Pull requests to `main`
- Called by publish workflow

Steps:
1. Set up Python 3.10
2. Install Poetry with poetry-dynamic-versioning plugin
3. Cache dependencies
4. Install project dependencies
5. Run mypy type checking
6. Run pytest with coverage
7. Upload coverage to Codecov
8. Build package artifacts
9. Upload build artifacts (retained for 3 days)

#### PyPI Publishing (`.github/workflows/publish-to-pypi.yml`)

Runs on:
- Push to `main` branch
- Push of tags matching `v*`
- Manual workflow dispatch

Steps:
1. Call CI workflow
2. Download build artifacts from CI
3. Publish to PyPI using trusted publishing (no API token needed)

**Note**: Uses OIDC trusted publishing, so no PyPI API token is stored in secrets.

## API Reference

### ExistClient

Main client class for interacting with Exist.io API.

#### Initialization

```python
from exist_client import ExistClient

# With access token
client = ExistClient(token="your_access_token")

# With custom base URL (for testing)
client = ExistClient(token="token", base_url="http://localhost:5000")
```

#### OAuth Methods (Static)

```python
# Exchange authorization code for tokens
tokens = ExistClient.get_tokens(
    code="authorization_code",
    client_id="your_client_id",
    client_secret="your_client_secret"
)

# Refresh expired tokens
new_tokens = ExistClient.refresh_tokens(
    refresh_token="old_refresh_token",
    client_id="your_client_id",
    client_secret="your_client_secret"
)
```

#### Instance Methods

```python
# Get user profile
profile = client.get_profile()

# Get attributes
attributes = client.get_attributes(
    groups=["custom"],      # Filter by group
    manual=True,            # Only manual attributes
    owned=True              # Only owned attributes
)

# Get attribute values (historical data)
values = client.get_attribute_values(attribute="steps")

# Acquire attributes (claim ownership)
result = client.acquire_attributes(
    acquisitions=[
        AttributeByName(name="custom_attribute"),
        AttributeByTemplate(template="mood")
    ]
)

# Update attribute values
result = client.update_attributes(
    updates=[
        AttributeValue(name="steps", date="2024-01-20", value=10000),
        AttributeValue(name="mood", date="2024-01-20", value=8)
    ]
)
```

## Testing Strategy

### Unit Tests (`test_client_mock.py`)

- Use `respx` to mock HTTP responses
- Fast, isolated tests
- Test individual API methods
- Good for testing error handling

### Integration Tests (`test_client_simulator.py`)

- Use Flask + `flask-httpauth` to simulate Exist.io API
- Test realistic workflows (acquire → update)
- Test authentication (valid/invalid tokens)
- Uses `syrupy` for snapshot testing

### Test Fixtures

**`exist_api_mock`** (conftest.py):
- Mocked HTTP client using `respx`
- Used for simple unit tests

**`exist_api_simulator`** (test_client_simulator.py):
- Full Flask application simulating Exist.io
- Implements OAuth token verification
- Simulates attribute ownership model
- Realistic error responses

## Common Patterns

### Adding a New API Endpoint

1. **Update OpenAPI spec** (`codegen/exist.io.yaml`):
   ```yaml
   /api/2/new-endpoint/:
     post:
       operationId: new-endpoint
       requestBody:
         content:
           application/json:
             schema:
               $ref: '#/components/schemas/NewRequestType'
       responses:
         "200":
           description: Success
           content:
             application/json:
               schema:
                 $ref: '#/components/schemas/NewResponseType'
       security:
         - http: []
   ```

2. **Define schemas** (in same file):
   ```yaml
   components:
     schemas:
       NewRequestType:
         properties:
           field_name:
             type: string
         required:
           - field_name
   ```

3. **Regenerate client**:
   ```bash
   poetry run ./codegen/update-client.sh
   ```

4. **Add wrapper method** (`src/exist_client/client.py`):
   ```python
   from ._exist_io_client.api.default import new_endpoint
   from ._exist_io_client.models import NewResponseType

   def call_new_endpoint(self, *, param: str) -> Optional[NewResponseType]:
       return new_endpoint.sync(client=self.client, param=param)
   ```

5. **Add tests** (`tests/test_client_mock.py`):
   ```python
   def test_new_endpoint(exist_api_mock: MockRouter) -> None:
       client = ExistClient(token="token")
       exist_api_mock.post("/api/2/new-endpoint/").return_value = httpx.Response(
           200,
           json={"field": "value"}
       )
       result = client.call_new_endpoint(param="test")
       assert result is not None
   ```

### Handling OAuth Token Refresh

When using the client in a larger application (e.g., LifeDash):

1. **Detect expired token** (401 response)
2. **Call refresh_tokens()** with stored refresh_token
3. **Update database** with new tokens
4. **Retry original request** with new access_token

Example:
```python
def get_exist_client_with_refresh(user: User) -> ExistClient:
    """Get client with automatic token refresh."""
    try:
        client = ExistClient(token=user.exist_tokens.access_token)
        # Test token validity
        client.get_profile()
        return client
    except UnexpectedStatus as e:
        if e.status_code == 401:
            # Refresh tokens
            new_tokens = ExistClient.refresh_tokens(
                refresh_token=user.exist_tokens.refresh_token,
                client_id=EXIST_CLIENT_ID,
                client_secret=EXIST_CLIENT_SECRET
            )
            # Update database
            user.exist_tokens.access_token = new_tokens.access_token
            user.exist_tokens.refresh_token = new_tokens.refresh_token
            db.commit()
            # Return new client
            return ExistClient(token=new_tokens.access_token)
        raise
```

## Important Notes

### DO NOT

- ❌ Edit files in `_exist_io_client/` directory directly
- ❌ Commit `use.py` with real tokens (it's a local scratch file)
- ❌ Skip pre-commit hooks when committing
- ❌ Modify generated model files

### DO

- ✅ Update `codegen/exist.io.yaml` when API changes
- ✅ Run tests after regenerating client code
- ✅ Use conventional commits for changelog automation
- ✅ Add tests for new functionality
- ✅ Keep `client.py` as a thin wrapper around generated code
- ✅ Use type hints in all custom code

## Debugging

### Enable Verbose Logging

```python
from loguru import logger
logger.enable("exist_client")
```

### Inspect Generated Code

When debugging issues with the generated client:

```bash
# View generated API endpoint
cat src/exist_client/_exist_io_client/api/default/attributes_update.py

# View generated models
cat src/exist_client/_exist_io_client/models/attribute_value.py
```

### Test with Real API

Use `use.py` for manual testing (never commit with real tokens):

```python
from exist_client import ExistClient

client = ExistClient(token="your_test_token")
attributes = client.get_attributes(groups=["custom"])
print(attributes)
```

## Dependencies

### Runtime Dependencies

- **attrs** (^23.1.0) - Used by generated code for dataclasses
- **loguru** (*) - Logging
- **pytilz** (^0.1.0) - Utility functions

### Development Dependencies

- **openapi-python-client** - Code generation
- **pytest** / **pytest-cov** - Testing
- **mypy** - Type checking
- **respx** - HTTP mocking
- **flask** / **flask-httpauth** - API simulation
- **syrupy** - Snapshot testing
- **commitizen** - Conventional commits
- **pre-commit** - Git hooks

## Related Projects

- **LifeDash** - Main application using this library
- **Exist.io API Docs** - https://developer.exist.io/
