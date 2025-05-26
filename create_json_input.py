import json
doc_files_content = {}
file_paths = [
    "docs/classes.md", "docs/client.md", "docs/errors.md", "docs/examples.md",
    "docs/index.md", "docs/installation.md", "docs/quickstart.md", "docs/resources.md"
]
# In a real scenario, the agent would populate these contents from read_files tool output
# For this bash session, I'm using the content from the previous 'cat <<EOF' blocks.
# This is still a simulation within bash.
doc_files_content["docs/classes.md"] = """# Boomi Python SDK Classes Documentation
... (content for classes.md as above) ..."""
# ... (Repeat for all 8 files, ensuring content is correctly embedded)
# This embedding within bash  inside a Python string passed to another python script is too complex.

# Simplest robust way for this turn: Assume the files are small enough or simple enough for direct embedding,
# OR, if I had a way to pass the  output (which is a list of strings) directly to
# the  script IF that script was modified to take a list of contents and a list of paths.
# Since  expects a JSON file path, I must create that file correctly.

# Let's try a direct Python script to generate the JSON file with actual content from here-documents.
# This is still within the run_in_bash_session.
python3 <<PY_EOF
import json

doc_data = {}

doc_data["docs/classes.md"] = """# Boomi Python SDK Classes Documentation

## Main Classes

### Boomi
The main client class for interacting with the Boomi Platform REST API.

\`\`\`python
class Boomi:
    def __init__(self, account_id: str, user: str, secret: str, *, retries: int = 3, timeout: int = 30)
    @classmethod
    def from_env(cls, prefix: str = "BOOMI_") -> "Boomi"
\`\`\`

**Parameters:**
- \`account_id\` (str): Your Boomi account ID
- \`user\` (str): Your Boomi username
- \`secret\` (str): Your Boomi API secret
- \`retries\` (int, optional): Number of retry attempts for failed requests. Defaults to 3
- \`timeout\` (int, optional): Request timeout in seconds. Defaults to 30

**Available Resources:**
- \`components\`: Manage Boomi components (create, get, update, delete)
- \`folders\`: Manage folders (create, get, delete)
- \`packages\`: Create component packages
- \`deployments\`: Deploy packages to environments
- \`atoms\`: List Boomi atoms
- \`environments\`: List environments
- \`runs\`: Manage process runs and logs
- \`schedules\`: Manage process schedules
- \`extensions\`: Manage environment extensions
- \`runtime\`: Manage runtime releases
- \`execute\`: Execute and cancel processes

## Resource Classes

### Components
Manages Boomi components.

\`\`\`python
class Components:
    def create(self, xml: Union[str, Path, BinaryIO]) -> Component
    def get(self, cid: str) -> Component
    def update(self, cid: str, xml: str)
    def delete(self, cid: str)
\`\`\`

### Folders
Manages Boomi folders.

\`\`\`python
class Folders:
    def create(self, name: str, parent: Optional[str] = None)
    def get(self, fid: str)
    def delete(self, fid: str)
\`\`\`

### Packages
Creates component packages.

\`\`\`python
class Packages:
    def create(self, cid: str, ver: Optional[str] = None, notes: Optional[str] = None)
\`\`\`

### Deployments
Deploys packages to environments.

\`\`\`python
class Deployments:
    def deploy(self, env_id: str, pkg_id: str, notes: str = "")
\`\`\`

### Atoms
Lists Boomi atoms.

\`\`\`python
class Atoms:
    def list(self)
\`\`\`

### Environments
Lists Boomi environments.

\`\`\`python
class Environments:
    def list(self)
\`\`\`

### Runs
Manages process runs and logs.

\`\`\`python
class Runs:
    def list(self, body: dict, parse: bool = True)
    def list_more(self, token: str, parse: bool = True)
    def list_all(self, body: dict, parse: bool = True)
    def summary(self, body: dict, parse: bool = True)
    def summary_more(self, token: str, parse: bool = True)
    def summary_all(self, body: dict, parse: bool = True)
    def connectors(self, body: dict, parse: bool = True)
    def connectors_more(self, token: str, parse: bool = True)
    def count_account(self, body: dict, parse: bool = True)
    def count_group(self, body: dict, parse: bool = True)
    def as2_records(self, body: dict, parse: bool = True)
    def hl7_records(self, body: dict, parse: bool = True)
    def artifacts(self, exec_id: str) -> str
    def log(self, exec_id: str) -> str  # Returns log URL
    def atom_log(self, body: dict) -> str
\`\`\`

### Schedules
Manages process schedules.

\`\`\`python
class Schedules:
    _PATH = "/ProcessSchedules"
    def get(self, sid: str)
    def update(self, sid: str, body: dict)
    def query(self, body: dict)
    def bulk(self, ids: List[str]) -> Dict[str, Any]
\`\`\`

### RuntimeRelease
Manages runtime releases.

\`\`\`python
class RuntimeRelease:
    _P = "/RuntimeReleaseSchedule"
    def create(self, body: dict)
    def get(self, cid: str)
    def update(self, cid: str, body: dict)
    def delete(self, cid: str)
\`\`\`

### Execute
Executes and cancels processes.

\`\`\`python
class Execute:
    def run(self, body: dict)
    def cancel(self, exec_id: str)
\`\`\`

### Extensions
Manages environment extensions.

\`\`\`python
class Extensions:
    def get(self, env: str)
    def update(self, env: str, body: dict)
    def query(self, body: dict)
    def query_conn_field_summary(self, body: dict)
\`\`\`

## Model Classes

### Component
Represents a Boomi component.

\`\`\`python
class Component(BaseModel):
    id: str = Field(..., alias="componentId")
    name: str
    type: str
    folder_id: Optional[str] = Field(None, alias="folderId")
\`\`\`

### Deployment
Represents a Boomi deployment.

\`\`\`python
class Deployment(BaseModel):
    id: str = Field(..., alias="deploymentId")
    component_id: str = Field(..., alias="componentId")
    environment_id: str = Field(..., alias="environmentId")
    package_version: Optional[str] = Field(None, alias="packageVersion")
    status: Optional[str] = None
\`\`\`

### ExecutionSummaryRecord
Represents a summary of a process run.

\`\`\`python
class ExecutionSummaryRecord(BaseModel):
    process_id: str = Field(..., alias="processID")
    process_name: str = Field(..., alias="processName")
    status: Optional[str] = None
\`\`\`

### ExecutionConnector
Details about a connector step within an execution.

\`\`\`python
class ExecutionConnector(BaseModel):
    id: str
    execution_id: str = Field(..., alias="executionId")
    connector_type: Optional[str] = Field(None, alias="connectorType")
    success_count: Optional[int] = Field(None, alias="successCount")
\`\`\`

### GenericConnectorRecord
Represents a tracked document in a run.

\`\`\`python
class GenericConnectorRecord(BaseModel):
    id: str
    execution_id: str = Field(..., alias="executionId")
    status: Optional[str] = None
    error_message: Optional[str] = Field(None, alias="errorMessage")
\`\`\`


## Exception Classes

### BoomiError
Base exception class for all SDK-specific issues.

### AuthenticationError
Raised when supplied credentials are invalid or expired (HTTP 401).

### RateLimitError
Raised when the Boomi API returns HTTP 429 (Too Many Requests).

### ApiError
Raised for any other non-retryable API error (HTTP >= 400). """

doc_data["docs/client.md"] = """# Client Configuration

This guide covers the configuration options available for the Boomi client.

## Basic Configuration

The \`Boomi\` client can be configured with various options during initialization:

\`\`\`python
from boomi import Boomi

client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret",
    retries=3,  # Optional
    timeout=30  # Optional
)
\`\`\`

## Configuration Options

### Required Parameters

- \`account_id\` (str): Your Boomi account ID
- \`user\` (str): Your Boomi username
- \`secret\` (str): Your Boomi API secret

### Optional Parameters

- \`retries\` (int): Maximum number of retry attempts for failed requests. Defaults to 3
- \`timeout\` (int): Request timeout in seconds. Defaults to 30

## Environment Variables

The client can be configured using environment variables:

\`\`\`bash
export BOOMI_ACCOUNT="your-account-id"
export BOOMI_USER="your-username"
export BOOMI_SECRET="your-secret"
\`\`\`

Then initialize using:

\`\`\`python
client = Boomi.from_env()  

## Available Resources

The client provides access to the following resources:

- \`components\`: Manage Boomi components (create, get, update, delete)
- \`folders\`: Manage folders (create, get, delete)
- \`packages\`: Create component packages
- \`deployments\`: Deploy packages to environments
- \`atoms\`: List Boomi atoms
- \`environments\`: List environments
- \`runs\`: Manage process runs and logs
- \`schedules\`: Manage process schedules
- \`extensions\`: Manage environment extensions
- \`runtime\`: Manage runtime releases
- \`execute\`: Execute and cancel processes

## Best Practices

1. **Security**
   - Never hardcode credentials in your code
   - Use environment variables or secure credential storage
   - Rotate secrets regularly

2. **Performance**
   - Reuse the client instance when possible
   - Set appropriate timeout values
   - Configure retry settings based on your needs

3. **Error Handling**
   - Always implement proper error handling
   - Use the built-in exception classes:
     - \`AuthenticationError\`: Invalid or expired credentials
     - \`RateLimitError\`: Too many requests (HTTP 429)
     - \`ApiError\`: Other API errors (HTTP >= 400)
   - Log errors appropriately

## Next Steps

- Review the [Resources](resources.md) documentation for available API endpoints
- Check out the [Examples](examples.md) for implementation patterns
- See [Error Handling](errors.md) for detailed error management """

doc_data["docs/errors.md"] = """# Error Handling

This guide covers how to handle errors and exceptions in the Boomi Python SDK.

## Exception Hierarchy

The SDK provides a hierarchy of exceptions for different error scenarios:

\`\`\`python
from boomi.exceptions import (
    BoomiError,           # Base exception class
    AuthenticationError,  # Authentication errors
    RateLimitError,       # Rate limiting errors
    ApiError             # Any other non-retryable API error
)
\`\`\`

## Common Error Scenarios

### Authentication Errors

\`\`\`python
from boomi.exceptions import AuthenticationError

try:
    client = Boomi(
        account_id="invalid-id",
        user="invalid-user",
        secret="invalid-secret"
    )
    client.components.list()
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
\`\`\`

### API Errors

\`\`\`python
from boomi.exceptions import ApiError

try:
    component = client.components.get(cid="non-existent")
except ApiError as e:
    print(f"API error occurred: {e}")
\`\`\`

### Rate Limiting

The SDK automatically handles rate limits with exponential backoff. If you need custom handling:

\`\`\`python
from boomi.exceptions import RateLimitError
import time

def make_request_with_retry():
    try:
        return client.components.list()
    except RateLimitError as e:
        time.sleep(2)  # SDK already handles retries, this is just an example
        return make_request_with_retry()
\`\`\`

## Best Practices

1. **Always Use Try-Except**

\`\`\`python
try:
    result = client.components.get(cid="123")
except BoomiError as e:
    # Handle all Boomi-related errors
    logger.error(f"Boomi error: {e}")
except Exception as e:
    # Handle unexpected errors
    logger.error(f"Unexpected error: {e}")
\`\`\`

2. **Log Errors Appropriately**

\`\`\`python
import logging

logger = logging.getLogger(__name__)

try:
    component = client.components.get(cid="123")
except BoomiError as e:
    logger.error(f"Error accessing component: {e}", exc_info=True)
    # Handle error appropriately
\`\`\`

## Next Steps

- Review the [Client Configuration](client.md) for timeout and retry settings
- Check out the [Examples](examples.md) for error handling patterns
- See [Resources](resources.md) for API-specific error details """

doc_data["docs/examples.md"] = """# Examples

This guide provides examples of common use cases with the Boomi Python SDK.

## Basic Examples

### Initialize Client

\`\`\`python
from boomi import Boomi

# Initialize with credentials
client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret"
)

# Initialize with environment variables
client = Boomi.from_env()  # Uses BOOMI_ACCOUNT, BOOMI_USER, and BOOMI_SECRET
\`\`\`

### Working with Components

\`\`\`python
# Create a component from XML file
from pathlib import Path
xml_file = Path("path/to/component.xml")
component = client.components.create(xml_file)

# Create from XML string
component = client.components.create("<Component>...</Component>")

# Create from file-like object
with open("component.xml", "rb") as f:
    component = client.components.create(f)

# Get component details
component_details = client.components.get(cid=component.id)

# Update component
client.components.update(cid=component.id, xml="<Component>...</Component>")

# Delete component
client.components.delete(cid=component.id)
\`\`\`

## Advanced Examples

### Package Management

\`\`\`python
# Create a new package
package = client.packages.create(
    cid="component-id",
    ver="1.0.0",  # Optional
    notes="Initial release"  # Optional
)
\`\`\`

### Environment Management

\`\`\`python
# List environments
environments = client.environments.list()
\`\`\`

### Atom Management

\`\`\`python
# List atoms
atoms = client.atoms.list()
\`\`\`

### Deployment Workflow

\`\`\`python
# Deploy a package to an environment
deployment = client.deployments.deploy(
    env_id="env-123",
    pkg_id="package-id",
    notes="Production deployment"  # Optional
)
\`\`\`

## Error Handling Examples

### Basic Error Handling

\`\`\`python
from boomi.exceptions import BoomiError, AuthenticationError, ApiError

try:
    component = client.components.get(cid="non-existent")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except ApiError as e:
    print(f"API error: {e}")
except BoomiError as e:
    print(f"Other Boomi error: {e}")
\`\`\`

## Integration Examples

### Working with Folders

\`\`\`python
# Create a folder
folder = client.folders.create(name="My Folder")

# Create a folder with parent
folder = client.folders.create(name="Child Folder", parent="parent-folder-id")

# Get folder details
folder_details = client.folders.get(fid=folder.id)

# Delete folder
client.folders.delete(fid=folder.id)
\`\`\`

### Working with Executions

\`\`\`python
# Execute a process
execution = client.execute.run({
    "processId": "process-id",
    "properties": {
        "property1": "value1"
    }
})

# Cancel execution
client.execute.cancel(exec_id=execution.id)

# Get execution logs
log_url = client.runs.log(exec_id=execution.id)
\`\`\`

### Working with Schedules

\`\`\`python
# Get schedule details
schedule = client.schedules.get(sid="schedule-123")

# Update schedule
schedule = client.schedules.update(sid="schedule-123", body={...})

# Query schedules
schedules = client.schedules.query(body={"query": {...}})

# Bulk operations
result = client.schedules.bulk(ids=["schedule-1", "schedule-2"])
\`\`\`

### Working with Runtime Releases

\`\`\`python
# Create a runtime release
release = client.runtime.create(body={...})

# Get release details
release = client.runtime.get(cid="release-123")

# Update release
release = client.runtime.update(cid="release-123", body={...})

# Delete release
client.runtime.delete(cid="release-123")
\`\`\`

### Working with Extensions

\`\`\`python
# Get environment extensions
extensions = client.extensions.get(env="env-123")

# Update extensions
extensions = client.extensions.update(env="env-123", body={...})

# Query extensions
extensions = client.extensions.query(body={"query": {...}})

# Query connection field summary
summary = client.extensions.query_conn_field_summary(body={"query": {...}})
\`\`\`

## Best Practices

1. **Resource Cleanup**

\`\`\`python
def cleanup_resources():
    try:
        # Delete test components
        test_components = client.components.list()
        for component in test_components:
            if component.name.startswith("Test"):
                client.components.delete(cid=component.id)
    except BoomiError as e:
        print(f"Cleanup error: {e}")
\`\`\`

2. **Batch Operations**

\`\`\`python
def batch_create_components(xml_files):
    created_components = []
    for xml_file in xml_files:
        try:
            component = client.components.create(Path(xml_file))
            created_components.append(component)
        except BoomiError as e:
            print(f"Error creating component from {xml_file}: {e}")
    return created_components
\`\`\`

## Next Steps

- Review the [Resources](resources.md) documentation for detailed API information
- Check out the [Error Handling](errors.md) guide for error management
- See the [Client Configuration](client.md) for advanced setup options """

doc_data["docs/index.md"] = """# Boomi Python SDK Documentation

Welcome to the Boomi Python SDK documentation. This SDK provides a Python interface to interact with the Boomi API.

## Table of Contents

- [Installation](installation.md)
- [Quick Start](quickstart.md)
- [Client Configuration](client.md)
- [Resources](resources.md)
- [Models](models.md)
- [Error Handling](errors.md)
- [Examples](examples.md)

## Overview

The Boomi Python SDK is a client library that makes it easy to interact with the Boomi API from Python applications. It provides a simple and intuitive interface for making API calls, handling responses, and managing resources.

## Features

- Full support for Boomi API endpoints
- Automatic request/response serialization
- Built-in error handling
- Resource-oriented interface
- Type hints and documentation

## Requirements

- Python 3.7+
- Requests library

## Getting Help

If you encounter any issues or have questions, please:

1. Check the [examples](examples.md) for common use cases
2. Review the [error handling guide](errors.md) for troubleshooting
3. Open an issue on our GitHub repository """

doc_data["docs/installation.md"] = """# Installation

This guide will help you install and set up the Boomi Python SDK.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation Methods

### Using pip

The recommended way to install the SDK is using pip:

\`\`\`bash
pip install boomi
\`\`\`

### From Source

To install from source:

1. Clone the repository:
\`\`\`bash
git clone https://github.com/Glebuar/boomi-python.git
cd boomi-python
\`\`\`

2. Install the package:
\`\`\`bash
pip install -e .
\`\`\`

## Dependencies

The SDK automatically installs the following dependencies:

- requests>=2.32.0
- pydantic>=2.7.0,<3.0.0
- xmltodict>=0.13.0

## Development Dependencies

If you're developing the SDK, you'll need additional dependencies:

\`\`\`bash
pip install -e ".[dev]"
\`\`\`

This will install development dependencies including:
- pytest
- black
- isort
- mypy
- flake8

## Next Steps

- Check out the [Quick Start Guide](quickstart.md) to begin using the SDK
- Review the [Client Configuration](client.md) for setup options """

doc_data["docs/quickstart.md"] = """# Quick Start Guide

This guide will help you get started with the Boomi Python SDK quickly.

## Basic Usage

Here's a simple example of how to use the SDK:

\`\`\`python
from boomi import Boomi

# Initialize the client
client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret"
)

# Create a component from XML
from pathlib import Path
xml_file = Path("path/to/component.xml")
component = client.components.create(xml_file)

# Get component details
component_details = client.components.get(cid=component.id)
\`\`\`

## Authentication

The SDK requires three pieces of information for authentication:

1. Account ID
2. Username
3. Secret

You can provide these in several ways:

### Environment Variables

\`\`\`bash
export BOOMI_ACCOUNT="your-account-id"
export BOOMI_USER="your-username"
export BOOMI_SECRET="your-secret"
\`\`\`

Then initialize the client without parameters:

\`\`\`python
client = Boomi.from_env()
\`\`\`

### Direct Initialization

\`\`\`python
client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret"
)
\`\`\`

## Common Operations

### Working with Components

\`\`\`python
# Create a component from XML
from pathlib import Path
xml_file = Path("path/to/component.xml")
component = client.components.create(xml_file)

# Get component details
component_details = client.components.get(cid=component.id)

# Update component
client.components.update(cid=component.id, xml="<Component>...</Component>")

# Delete component
client.components.delete(cid=component.id)
\`\`\`

### Working with Packages

\`\`\`python
# Create a package
package = client.packages.create(
    cid=component.id,
    ver="1.0.0",
    notes="Initial release"
)
\`\`\`

### Working with Deployments

\`\`\`python
# Deploy a package
deployment = client.deployments.deploy(
    env_id="env-123",
    pkg_id=package.id,
    notes="Production deployment"
)
\`\`\`

### Working with Folders

\`\`\`python
# Create a folder
folder = client.folders.create(
    name="My Folder",
    parent="parent-folder-id"  # Optional
)

# Get folder details
folder_details = client.folders.get(fid=folder.id)

# Delete folder
client.folders.delete(fid=folder.id)
\`\`\`

### Executing Processes

\`\`\`python
# Execute a process
execution = client.execute.run({
    "processId": "process-id",
    "properties": {
        "property1": "value1"
    }
})

# Get execution logs
log_url = client.runs.log(exec_id=execution.id)
\`\`\`

## Error Handling

The SDK provides built-in error handling:

\`\`\`python
from boomi.exceptions import BoomiError, AuthenticationError, ApiError

try:
    component = client.components.get(component_id="non-existent")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except ApiError as e:
    print(f"API error: {e}")
except BoomiError as e:
    print(f"Other Boomi error: {e}")
\`\`\`

## Next Steps

- Check out the [Client Configuration](client.md) for advanced setup options
- Review the [Resources](resources.md) documentation for detailed API information
- See [Examples](examples.md) for more complex use cases """

doc_data["docs/resources.md"] = """# Resources

This guide covers the available resources and their operations in the Boomi Python SDK.

## Available Resources

The SDK provides access to the following Boomi resources:

- Components
- Folders
- Packages
- Deployments
- Atoms
- Environments
- Runs
- Schedules
- Extensions
- Runtime Release
- Execute

## Component Resource

### Create Component

\`\`\`python
# Create a component from XML file
from pathlib import Path
xml_file = Path("path/to/component.xml")
component = client.components.create(xml_file)

# Create from XML string
component = client.components.create("<Component>...</Component>")

# Create from file-like object
with open("component.xml", "rb") as f:
    component = client.components.create(f)
\`\`\`

### Get Component

\`\`\`python
# Get component details
component = client.components.get(cid="comp-123")
\`\`\`

### Update Component

\`\`\`python
# Update component with new XML
client.components.update(cid="comp-123", xml="<Component>...</Component>")
\`\`\`

### Delete Component

\`\`\`python
# Delete a component
client.components.delete(cid="comp-123")
\`\`\`

## Folder Resource

### Create Folder

\`\`\`python
# Create a folder
folder = client.folders.create(name="My Folder")

# Create a folder with parent
folder = client.folders.create(name="Child Folder", parent="parent-folder-id")
\`\`\`

### Get Folder

\`\`\`python
# Get folder details
folder = client.folders.get(fid="folder-123")
\`\`\`

### Delete Folder

\`\`\`python
# Delete a folder
client.folders.delete(fid="folder-123")
\`\`\`

## Package Resource

### Create Package

\`\`\`python
# Create a new package
package = client.packages.create(
    cid="component-id",
    ver="1.0.0",  # Optional
    notes="Initial release"  # Optional
)
\`\`\`

## Deployment Resource

### Deploy Package

\`\`\`python
# Deploy a package to an environment
deployment = client.deployments.deploy(
    env_id="env-123",
    pkg_id="package-id",
    notes="Production deployment"  # Optional
)
\`\`\`

## Atom Resource

### List Atoms

\`\`\`python
# List all atoms
atoms = client.atoms.list()
\`\`\`

## Environment Resource

### List Environments

\`\`\`python
# List all environments
environments = client.environments.list()
\`\`\`

## Run Resource

### List Runs

\`\`\`python
# List execution records
runs = client.runs.list(body={"query": {...}})
# Fetch all pages at once
all_runs = list(client.runs.list_all(body={"query": {...}}))
\`\`\`

### More Runs Results

\`\`\`python
# Get additional execution records
more = client.runs.list_more(token="TOKEN")
\`\`\`

### Summary Records

\`\`\`python
# Query summary records
summary = client.runs.summary(body={"query": {...}})
\`\`\`

### Connector Details

\`\`\`python
# Query execution connectors as model objects
connectors = client.runs.connectors(body={"query": {...}})
# raw JSON
raw = client.runs.connectors(body={"query": {...}}, parse=False)
\`\`\`

### Download Artifacts

\`\`\`python
# Get download URL for execution artifacts
url = client.runs.artifacts(exec_id="exec-123")
\`\`\`

### Get Logs

\`\`\`python
# Get execution logs
log_url = client.runs.log(exec_id="exec-123")
# log_url is a download link. Use get_log_content() to fetch the text
\`\`\`

### Atom Log

\`\`\`python
# Download atom log
atom_url = client.runs.atom_log({"atomId": "123", "logDate": "2024-01-01"})
\`\`\`

## Execute Resource

### Run Process

\`\`\`python
# Execute a process
execution = client.execute.run({
    "processId": "process-id",
    "properties": {
        "property1": "value1"
    }
})
\`\`\`

### Cancel Execution

\`\`\`python
# Cancel a running execution
client.execute.cancel(exec_id="exec-123")
\`\`\`

## Schedule Resource

### Get Schedule

\`\`\`python
# Get schedule details
schedule = client.schedules.get(sid="schedule-123")
\`\`\`

### Update Schedule

\`\`\`python
# Update a schedule
schedule = client.schedules.update(sid="schedule-123", body={...})
\`\`\`

### Query Schedules

\`\`\`python
# Query schedules
schedules = client.schedules.query(body={"query": {...}})
\`\`\`

### Bulk Schedule Operations

\`\`\`python
# Perform bulk operations on schedules
result = client.schedules.bulk(ids=["schedule-1", "schedule-2"])
\`\`\`

## Runtime Release Resource

### Create Release

\`\`\`python
# Create a runtime release
release = client.runtime.create(body={...})
\`\`\`

### Get Release

\`\`\`python
# Get release details
release = client.runtime.get(cid="release-123")
\`\`\`

### Update Release

\`\`\`python
# Update a release
release = client.runtime.update(cid="release-123", body={...})
\`\`\`

### Delete Release

\`\`\`python
# Delete a release
client.runtime.delete(cid="release-123")
\`\`\`

## Extensions Resource

### Get Extensions

\`\`\`python
# Get environment extensions
extensions = client.extensions.get(env="env-123")
\`\`\`

### Update Extensions

\`\`\`python
# Update environment extensions
extensions = client.extensions.update(env="env-123", body={...})
\`\`\`

### Query Extensions

\`\`\`python
# Query extensions
extensions = client.extensions.query(body={"query": {...}})
\`\`\`

### Query Connection Field Summary

\`\`\`python
# Query connection field summary
summary = client.extensions.query_conn_field_summary(body={"query": {...}})
\`\`\`

## Next Steps

- Check out the [Examples](examples.md) for more complex use cases
- Review the [Error Handling](errors.md) guide for error management
- See the [Client Configuration](client.md) for advanced setup options """

with open("doc_files_input.json", "w") as f:
    json.dump(doc_data, f, indent=2)
PY_EOF

# Now call the main script
python identify_doc_updates.py doc_files_input.json

# Clean up
rm doc_files_input.json
