# Quick Start Guide

This guide will help you get started with the Boomi Python SDK quickly.

## Basic Usage

Here's a simple example of how to use the SDK:

```python
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
component_details = client.components.get(component_id=component.id)
```

## Authentication

The SDK requires three pieces of information for authentication:

1. Account ID
2. Username
3. Secret

You can provide these in several ways:

### Environment Variables

```bash
export BOOMI_ACCOUNT="your-account-id"
export BOOMI_USER="your-username"
export BOOMI_SECRET="your-secret"
```

Then initialize the client without parameters:

```python
client = Boomi.from_env()
```

### Direct Initialization

```python
client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret"
)
```

## Common Operations

### Working with Components

```python
# Create a component from XML
from pathlib import Path
xml_file = Path("path/to/component.xml")
component = client.components.create(xml_file)

# Get component details
component_details = client.components.get(component_id=component.id)

# Update component
client.components.update(component_id=component.id, xml="<Component>...</Component>")

# Delete component
client.components.delete(component_id=component.id)
```

### Working with Packages

```python
# Create a package
package = client.packages.create(
    cid=component.id,
    ver="1.0.0",
    notes="Initial release"
)
```

### Working with Deployments

```python
# Deploy a package
deployment = client.deployments.deploy(
    env_id="env-123",
    pkg_id=package.id,
    notes="Production deployment"
)
```

### Working with Folders

```python
# Create a folder
folder = client.folders.create(
    name="My Folder",
    parent="parent-folder-id"  # Optional
)

# Get folder details
folder_details = client.folders.get(folder_id=folder.id)

# Delete folder
client.folders.delete(folder_id=folder.id)
```

### Executing Processes

```python
# Execute a process
execution = client.execute.run({
    "processId": "process-id",
    "properties": {
        "property1": "value1"
    }
})

# Get execution logs
log_url = client.runs.log(execution_id=execution.id)
```

## Error Handling

The SDK provides built-in error handling:

```python
from boomi.exceptions import BoomiError, AuthenticationError, ApiError

try:
    component = client.components.get(component_id="non-existent")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except ApiError as e:
    print(f"API error: {e}")
except BoomiError as e:
    print(f"Other Boomi error: {e}")
```

## Next Steps

- Check out the [Client Configuration](client.md) for advanced setup options
- Review the [Resources](resources.md) documentation for detailed API information
- See [Examples](examples.md) for more complex use cases 