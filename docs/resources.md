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

Retrieves component details by its ID. The API is expected to return JSON, which is then validated into a `Component` model instance.

**Signature:**
```python
get(self, cid: str) -> Component
```

**Parameters:**
- `cid` (str): The ID of the component to retrieve.

**Returns:**
- A `Component` object populated with the component's details (including new fields like `description` and `version`).

**Example:**
```python
component_details = client.components.get(cid="comp-123")
print(component_details.name)
# Access new fields if available
# print(component_details.version)
# print(component_details.description)
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

Lists Atoms. This method can perform a simple GET request to list all atoms or a POST-based query if a `query_payload` is provided to filter results.

**Signature:**
```python
list(self, query_payload: Optional[dict] = None) -> List[dict]
```

**Parameters:**
- `query_payload` (Optional[dict]): A dictionary representing the query filter for a POST request to `/Atom/query`. If `None` or omitted, a `GET /Atom` request is made.

**Returns:**
- List of Atom details as dictionaries.

**Behavior:**
- If `query_payload` is `None`: Makes a `GET /Atom` request.
- If `query_payload` is provided: Makes a `POST /Atom/query` request with the payload.

**Example:**
```python
# Get all atoms
all_atoms = client.atoms.list()

# Query for specific atoms (example payload structure)
query = {'QueryFilter': {'expression': {'operator': 'and', 'nestedExpression': [
    {'argument': ['MyAtomName'], 'operator': 'EQUALS', 'property': 'name'}
]}}}
filtered_atoms = client.atoms.list(query_payload=query)
```

### Post Atom Disable

Disables an Atom by making a POST request to /atom/{atomId}/disable.

**Signature:**
```python
post_atom_disable(self, atomid_val: str, payload: dict) -> dict
```

### Post Atom Query

Queries Atoms using a POST request to /atom/query with the given payload.

**Signature:**
```python
post_atom_query(self, query_payload: dict) -> List[dict]
```

**Returns:**
A list of dictionaries, where each dictionary represents an Atom and contains its details.
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
# Fetch all pages at once
all_runs = list(client.runs.list_all(body={"query": {...}}))
```

### More Runs Results

```python
# Get additional execution records
more = client.runs.list_more(token="TOKEN")
```

### Summary Records

```python
# Query summary records
summary = client.runs.summary(body={"query": {...}})
```

### Connector Details

```python
# Query execution connectors as model objects
connectors = client.runs.connectors(body={"query": {...}})
# raw JSON
raw = client.runs.connectors(body={"query": {...}}, parse=False)
```

### Download Artifacts

```python
# Get download URL for execution artifacts
url = client.runs.artifacts(exec_id="exec-123")
```

### Get Logs

```python
# Get execution logs
log_url = client.runs.log(exec_id="exec-123")
# log_url is a download link. Use get_log_content() to fetch the text
```

### Atom Log

```python
# Download atom log
atom_url = client.runs.atom_log({"atomId": "123", "logDate": "2024-01-01"})
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
release = client.runtime.create(body={...})
```

### Get Release

```python
# Get release details
release = client.runtime.get(cid="release-123")
```

### Update Release

```python
# Update a release
release = client.runtime.update(cid="release-123", body={...})
```

### Delete Release

```python
# Delete a release
client.runtime.delete(cid="release-123")
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


## Account Resource

### Get Account Details

Retrieves details for a specific account.

**Signature:**
```python
get_account_details(self, account_id: str) -> dict
```

**Parameters:**
- `account_id` (str): The ID of the resource.

**Returns:**
- dict

### Get Account List

Retrieves a list of accounts, optionally filtered by a query payload.

**Signature:**
```python
get_account_list(self, query_payload: dict = None) -> dict
```

**Parameters:**
- `query_payload` (dict = None): The data payload for the request.

**Returns:**
- dict

## Next Steps

- Check out the [Examples](examples.md) for more complex use cases
- Review the [Error Handling](errors.md) guide for error management
- See the [Client Configuration](client.md) for advanced setup options
