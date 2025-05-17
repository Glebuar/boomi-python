# Resources

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
```

### Get Component

```python
# Get component details
component = client.components.get(cid="comp-123")
```

### Update Component

```python
# Update component with new XML
client.components.update(cid="comp-123", xml="<Component>...</Component>")
```

### Delete Component

```python
# Delete a component
client.components.delete(cid="comp-123")
```

## Folder Resource

### Create Folder

```python
# Create a folder
folder = client.folders.create(name="My Folder")

# Create a folder with parent
folder = client.folders.create(name="Child Folder", parent="parent-folder-id")
```

### Get Folder

```python
# Get folder details
folder = client.folders.get(fid="folder-123")
```

### Delete Folder

```python
# Delete a folder
client.folders.delete(fid="folder-123")
```

## Package Resource

### Create Package

```python
# Create a new package
package = client.packages.create(
    cid="component-id",
    ver="1.0.0",  # Optional
    notes="Initial release"  # Optional
)
```

## Deployment Resource

### Deploy Package

```python
# Deploy a package to an environment
deployment = client.deployments.deploy(
    env_id="env-123",
    pkg_id="package-id",
    notes="Production deployment"  # Optional
)
```

## Atom Resource

### List Atoms

```python
# List all atoms
atoms = client.atoms.list()
```

## Environment Resource

### List Environments

```python
# List all environments
environments = client.environments.list()
```

## Run Resource

### List Runs

```python
# List execution records
runs = client.runs.list(body={"query": {...}})
```

### Get Logs

```python
# Get execution logs
log_url = client.runs.log(execution_id="exec-123")
```

## Execute Resource

### Run Process

```python
# Execute a process
execution = client.execute.run({
    "processId": "process-id",
    "properties": {
        "property1": "value1"
    }
})
```

### Cancel Execution

```python
# Cancel a running execution
client.execute.cancel(exec_id="exec-123")
```

## Schedule Resource

### Get Schedule

```python
# Get schedule details
schedule = client.schedules.get(sid="schedule-123")
```

### Update Schedule

```python
# Update a schedule
schedule = client.schedules.update(sid="schedule-123", body={...})
```

### Query Schedules

```python
# Query schedules
schedules = client.schedules.query(body={"query": {...}})
```

### Bulk Schedule Operations

```python
# Perform bulk operations on schedules
result = client.schedules.bulk(ids=["schedule-1", "schedule-2"])
```

## Runtime Release Resource

### Create Release

```python
# Create a runtime release
release = client.runtime_release.create(body={...})
```

### Get Release

```python
# Get release details
release = client.runtime_release.get(cid="release-123")
```

### Update Release

```python
# Update a release
release = client.runtime_release.update(cid="release-123", body={...})
```

### Delete Release

```python
# Delete a release
client.runtime_release.delete(cid="release-123")
```

## Extensions Resource

### Get Extensions

```python
# Get environment extensions
extensions = client.extensions.get(env="env-123")
```

### Update Extensions

```python
# Update environment extensions
extensions = client.extensions.update(env="env-123", body={...})
```

### Query Extensions

```python
# Query extensions
extensions = client.extensions.query(body={"query": {...}})
```

### Query Connection Field Summary

```python
# Query connection field summary
summary = client.extensions.query_conn_field_summary(body={"query": {...}})
```

## Next Steps

- Check out the [Examples](examples.md) for more complex use cases
- Review the [Error Handling](errors.md) guide for error management
- See the [Client Configuration](client.md) for advanced setup options 