# Examples

This guide provides examples of common use cases with the Boomi Python SDK.

## Basic Examples

### Initialize Client

```python
from boomi import Boomi

# Initialize with credentials
client = Boomi(
    account_id="your-account-id",
    user="your-username",
    secret="your-secret"
)

# Initialize with environment variables
client = Boomi.from_env()  # Uses BOOMI_ACCOUNT, BOOMI_USER, and BOOMI_SECRET
```

### Working with Components

```python
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
# The component_details object is an instance of the Component model.
# It now includes 'description' and 'version' fields (if provided by the API).
# Example: print(component_details.description)
# Example: print(component_details.version)

# Update component
client.components.update(cid=component.id, xml="<Component>...</Component>")

# Delete component
client.components.delete(cid=component.id)
```

## Advanced Examples

### Package Management

```python
# Create a new package
package = client.packages.create(
    cid="component-id",
    ver="1.0.0",  # Optional
    notes="Initial release"  # Optional
)
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

### Environment Management

```python
# List environments
environments = client.environments.list()
```

### Atom Management

```python
# List atoms
# Get all atoms (uses GET /Atom)
all_atoms = client.atoms.list()

# Example: Query for specific atoms (uses POST /Atom/query)
# The exact query_payload structure depends on API capabilities.
query_payload_example = {'QueryFilter': {'expression': {'operator': 'and', 'nestedExpression': [
    {'argument': ['MyAtomName'], 'operator': 'EQUALS', 'property': 'name'}
]}}}
filtered_atoms = client.atoms.list(query_payload=query_payload_example)

```python
# Example usage for new Atom methods:
# result = client.atoms.post_atom_disable(atomid_val="your_atom_id", payload={"key": "value"})
# print(result)
# result = client.atoms.post_atom_query(query_payload={"filter": {"example_field": "example_value"}})
# print(result)
```

### Deployment Workflow

```python
# Deploy a package to an environment
deployment = client.deployments.deploy(
    env_id="env-123",
    pkg_id="package-id",
    notes="Production deployment"  # Optional
)
```

## Error Handling Examples

### Basic Error Handling

```python
from boomi.exceptions import BoomiError, AuthenticationError, ApiError

try:
    component = client.components.get(cid="non-existent")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except ApiError as e:
    print(f"API error: {e}")
except BoomiError as e:
    print(f"Other Boomi error: {e}")
```

## Integration Examples

### Working with Folders

```python
# Create a folder
folder = client.folders.create(name="My Folder")

# Create a folder with parent
folder = client.folders.create(name="Child Folder", parent="parent-folder-id")

# Get folder details
folder_details = client.folders.get(fid=folder.id)

# Delete folder
client.folders.delete(fid=folder.id)
```

### Working with Executions

```python
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
```

### Working with Schedules

```python
# Get schedule details
schedule = client.schedules.get(sid="schedule-123")

# Update schedule
schedule = client.schedules.update(sid="schedule-123", body={...})

# Query schedules
schedules = client.schedules.query(body={"query": {...}})

# Bulk operations
result = client.schedules.bulk(ids=["schedule-1", "schedule-2"])
```

### Working with Runtime Releases

```python
# Create a runtime release
release = client.runtime.create(body={...})

# Get release details
release = client.runtime.get(cid="release-123")

# Update release
release = client.runtime.update(cid="release-123", body={...})

# Delete release
client.runtime.delete(cid="release-123")
```

### Working with Extensions

```python
# Get environment extensions
extensions = client.extensions.get(env="env-123")

# Update extensions
extensions = client.extensions.update(env="env-123", body={...})

# Query extensions
extensions = client.extensions.query(body={"query": {...}})

# Query connection field summary
summary = client.extensions.query_conn_field_summary(body={"query": {...}})
```

## Best Practices

1. **Resource Cleanup**

```python
def cleanup_resources():
    try:
        # Delete test components
        test_components = client.components.list()
        for component in test_components:
            if component.name.startswith("Test"):
                client.components.delete(cid=component.id)
    except BoomiError as e:
        print(f"Cleanup error: {e}")
```

2. **Batch Operations**

```python
def batch_create_components(xml_files):
    created_components = []
    for xml_file in xml_files:
        try:
            component = client.components.create(Path(xml_file))
            created_components.append(component)
        except BoomiError as e:
            print(f"Error creating component from {xml_file}: {e}")
    return created_components
```

## Next Steps

- Review the [Resources](resources.md) documentation for detailed API information
- Check out the [Error Handling](errors.md) guide for error management
- See the [Client Configuration](client.md) for advanced setup options
