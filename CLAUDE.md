# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Critical Rules — DO NOT VIOLATE 

- **NEVER create mock data or simplified components** unless explicitly told to do so.
- **NEVER replace existing complex components with simplified versions** - always fix the actual problem.
- **ALWAYS work with the existing codebase** - do not create new simplified alternatives.
- **ALWAYS find and fix the root cause** of issues instead of creating workarounds.
- **When debugging issues, focus on fixing the existing implementation, not replacing it**.
- **When something doesn't work, debug and fix it - don't start over with a simple version**.
- **ALWAYS execute commands yourself when possible** - don't ask the user to run commands that you can execute. Only request user assistance when you encounter errors or limitations that prevent you from executing the command directly.
- **NEVER use "Generated with Claude Code" or similar AI tool references** in commit messages, code comments, or any repository content. Keep all contributions clean and professional without AI tool attribution.
- **Commit on every successful task completion**

## Boomi API OpenAPI & SDK Guidelines for AI Agents

**OpenAPI Specification – Source of Truth:** The Boomi API is defined by an OpenAPI 3.0 specification found in the repository's **`/openapi/`** folder. The spec is organized into a main file and many modular child files (e.g. each endpoint under `openapi/paths/` is defined in its own JSON). **Always treat this OpenAPI spec as the source of truth** for Boomi API endpoints, parameters, and models. If any other documentation or code diverges, assume the OpenAPI files are correct.

**Generated Python SDK (Use, Don't Regenerate):** The **`/src/boomi/`** directory contains a Python SDK for the Boomi API, which was **automatically generated** from the OpenAPI spec. AI agents should use this existing SDK when coding solutions. **Do not attempt to regenerate a new client library** from the OpenAPI spec – rely on the provided SDK classes and methods. If you discover a discrepancy between the SDK code and the OpenAPI spec (for example, a method name, parameter, or model not matching), update or patch the SDK code to fix the inconsistency rather than regenerating it from scratch. This ensures the SDK stays aligned with the spec over time.

## Development Commands

**Setup Commands:**
```bash
make install          # Install production dependencies  
make install-dev      # Install development dependencies including test tools
```

**Testing Commands:**
```bash
make test             # Run all tests
make test-unit        # Run unit tests only
make test-integration # Run integration tests only  
make test-examples    # Run example tests only
make test-coverage    # Run tests with coverage report (requires 80% coverage)
make test-quick       # Run a single quick test for validation
```

**Code Quality:**
```bash
make lint             # Run basic Python syntax checks
make format           # Code formatting guidance (suggests black, isort)
```

**Utilities:**
```bash
make clean            # Clean temporary files (.pyc, __pycache__, etc.)
make check-deps       # Verify required dependencies are installed
make setup-env        # Development environment setup guidance
```

**Testing Configuration:** Tests use pytest with markers for `unit`, `integration`, and `slow` tests. Coverage must be ≥80%. Test configuration is in `pyproject.toml`.

## Architecture Overview

**SDK Structure:** 
- **Main SDK class:** `src/boomi/sdk.py` contains the `Boomi` class that provides access to all service endpoints
- **Services:** `src/boomi/services/` contains individual service classes for each API endpoint (e.g., `AccountService`, `ComponentService`, `AtomService`)
- **Models:** `src/boomi/models/` contains data model classes for API request/response objects
- **Async Support:** `src/boomi/services/async_/` provides async versions of all services

**Service Pattern:** Each service follows a consistent pattern:
- Inherits from base service classes in `src/boomi/services/utils/`
- Provides methods like `get_*()`, `create_*()`, `update_*()`, `query_*()`, `delete_*()` 
- Handles authentication, base URL configuration, and timeout settings
- Returns strongly-typed model objects

**Key Services:**
- `ComponentService` - Manage processes, connectors, and other components
- `AccountService` - Account management and user roles
- `AtomService` - Runtime (Atom) management and monitoring
- `DeploymentService` - Deploy components to environments
- `ExecutionRequestService` - Execute processes and view execution records

**Authentication:** The SDK supports multiple authentication methods:
- API tokens (`access_token` parameter)
- Username/password (`username` and `password` parameters)  
- Account ID is required (`account_id` parameter)

**Repository Structure & Resources:**

- **`/src/boomi/`** – *Boomi Python SDK codebase.* This is the library of Python classes (services, models, etc.) for interacting with Boomi API endpoints. All API interactions should go through these classes/methods rather than making raw HTTP calls.  
- **`/documentation/`** – *Human-friendly API docs and usage guides.* Contains Markdown docs for services and data models, illustrating API operations, parameter info, and example usage patterns. These are useful for understanding how to call the SDK methods properly (e.g. request/response formats, required fields).  
- **`/examples/`** – *SDK usage examples.* Contains sample code demonstrating how to initialize the Boomi SDK and call various API methods. Agents can refer to these scripts to see typical usage patterns (authenticating, calling a service method, handling results, etc.).

**Example – Using the Boomi SDK:** AI agents should follow established patterns to call the API via the SDK. For instance, to retrieve a Cloud resource by ID using the SDK: 

```python
from boomi import Boomi

# Initialize the SDK client with credentials and account ID
sdk = Boomi(
    account_id="your-account-id",  # Required
    access_token="YOUR_ACCESS_TOKEN",  # Or use username/password
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=15000  # Optional, defaults to 60000ms
)

# Call the Cloud service to get a cloud object by ID
result = sdk.cloud.get_cloud(id_="YOUR_CLOUD_ID")

print(result)
```

In this example, `Boomi()` creates a client instance (using an API token or username/password for authentication), and `sdk.cloud.get_cloud(...)` invokes the **CloudService**'s `get_cloud` method. The SDK provides similar **service** properties for other API areas (e.g. `sdk.role.create_role(...)` for roles, `sdk.account.query_account(...)` for accounts, etc.), each corresponding to an OpenAPI path. Agents should use these high-level methods rather than direct HTTP calls. By following the SDK's patterns and the OpenAPI spec, agents can reliably integrate with the Boomi Platform API while easily adapting to any spec changes by updating the SDK code when needed.