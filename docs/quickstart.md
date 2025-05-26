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
component_details = client.components.get(cid=component.id)
# The component_details object is an instance of the Component model.
# It now includes 'description' and 'version' fields (if provided by the API).
# Example: print(component_details.description)
# Example: print(component_details.version)
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
component_details = client.components.get(cid=component.id)

# Update component
client.components.update(cid=component.id, xml="<Component>...</Component>")

# Delete component
client.components.delete(cid=component.id)
```

### Working with Accounts

```python
# Assuming 'client' is an initialized Boomi client instance

# Example for get_account_details
try:
    result = client.accounts.get_account_details(account_id="your-account-id-example")
    print(result)
except Exception as e:
    print(f'Error calling get_account_details: {e}')

# Example for get_account_list
try:
    result = client.accounts.get_account_list(query_payload={"filter": "example_filter"})
    print(result)
except Exception as e:
    print(f'Error calling get_account_list: {e}')

```

### Atom Management (Updated Example)

```python
# List all atoms (uses GET /Atom)
all_atoms = client.atoms.list()
print(f"Found {len(all_atoms)} atoms.")

# Example: Query for specific atoms (uses POST /Atom/query)
# The exact query_payload structure depends on API capabilities.
query_payload_example = {'QueryFilter': {'expression': {'operator': 'and', 'nestedExpression': [
    {'argument': ['MyAtomName'], 'operator': 'EQUALS', 'property': 'name'}
]}}}
filtered_atoms = client.atoms.list(query_payload=query_payload_example)
print(f"Found {len(filtered_atoms)} atoms matching the query.")

# Example usage for new Atom methods (conceptual):
# atom_id_to_disable = "your_atom_id_here" 
# disable_payload = {"reason": "Scheduled maintenance"} 
# try:
#     client.atoms.post_atom_disable(atomid_val=atom_id_to_disable, payload=disable_payload)
#     print(f"Atom {atom_id_to_disable} disable request sent.")
# except Exception as e:
#     print(f"Error disabling atom: {e}")

# specific_query_payload = {'QueryFilter': {'expression': {'operator': 'EQUALS', 'property': 'type', 'argument': ['CLOUD']}}}
# cloud_atoms = client.atoms.post_atom_query(query_payload=specific_query_payload)
# print(f"Found {len(cloud_atoms)} cloud atoms.")
```

### Working with Packages

```python
# Create a package
# Assuming 'component' is a Component object from a previous step
package = client.packages.create(
    cid=component.id, 
    ver="1.0.0",
    notes="Initial release"
)
```

### Working with Deployments

```python
# Deploy a package
# Assuming 'package' is a Package object from a previous step
deployment = client.deployments.deploy(
    env_id="env-123", # Replace with an actual environment ID
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
folder_details = client.folders.get(fid=folder.id)

# Delete folder
client.folders.delete(fid=folder.id)
```

### Executing Processes

```python
# Execute a process
execution = client.execute.run({
    "processId": "process-id", # Replace with an actual process ID
    "properties": {
        "property1": "value1"
    }
})

# Get execution logs
log_url = client.runs.log(exec_id=execution.id)
```

## Error Handling

The SDK provides built-in error handling:

```python
from boomi.exceptions import BoomiError, AuthenticationError, ApiError

try:
    # Example operation that might fail
    component = client.components.get(cid="non-existent-component-id")
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
