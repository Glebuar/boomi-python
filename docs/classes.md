# Boomi Python SDK Classes Documentation

## Main Classes

### Boomi
The main client class for interacting with the Boomi Platform REST API.

```python
class Boomi:
    def __init__(self, account_id: str, user: str, secret: str, *, retries: int = 3, timeout: int = 30)
    @classmethod
    def from_env(cls, prefix: str = "BOOMI_") -> "Boomi"
```

**Parameters:**
- `account_id` (str): Your Boomi account ID
- `user` (str): Your Boomi username
- `secret` (str): Your Boomi API secret
- `retries` (int, optional): Number of retry attempts for failed requests. Defaults to 3
- `timeout` (int, optional): Request timeout in seconds. Defaults to 30

**Available Resources:**
- `components`: Manage Boomi components (create, get, update, delete)
- `folders`: Manage folders (create, get, delete)
- `packages`: Create component packages
- `deployments`: Deploy packages to environments
- `atoms`: List Boomi atoms
- `environments`: List environments
- `runs`: Manage process runs and logs
- `schedules`: Manage process schedules
- `extensions`: Manage environment extensions
- `runtime`: Manage runtime releases
- `execute`: Execute and cancel processes

## Resource Classes

### Components
Manages Boomi components.

```python
class Components:
    def create(self, xml: Union[str, Path, BinaryIO]) -> Component
    def get(self, cid: str) -> Component
    def update(self, cid: str, xml: str)
    def delete(self, cid: str)
```

### Folders
Manages Boomi folders.

```python
class Folders:
    def create(self, name: str, parent: Optional[str] = None)
    def get(self, fid: str)
    def delete(self, fid: str)
```

### Packages
Creates component packages.

```python
class Packages:
    def create(self, cid: str, ver: Optional[str] = None, notes: Optional[str] = None)
```

### Deployments
Deploys packages to environments.

```python
class Deployments:
    def deploy(self, env_id: str, pkg_id: str, notes: str = "")
```

### Atoms
Lists Boomi atoms.

```python
class Atoms:
    def list(self)
```

### Environments
Lists Boomi environments.

```python
class Environments:
    def list(self)
```

### Runs
Manages process runs and logs.

```python
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
```

### Schedules
Manages process schedules.

```python
class Schedules:
    _PATH = "/ProcessSchedules"
    def get(self, sid: str)
    def update(self, sid: str, body: dict)
    def query(self, body: dict)
    def bulk(self, ids: List[str]) -> Dict[str, Any]
```

### RuntimeRelease
Manages runtime releases.

```python
class RuntimeRelease:
    _P = "/RuntimeReleaseSchedule"
    def create(self, body: dict)
    def get(self, cid: str)
    def update(self, cid: str, body: dict)
    def delete(self, cid: str)
```

### Execute
Executes and cancels processes.

```python
class Execute:
    def run(self, body: dict)
    def cancel(self, exec_id: str)
```

### Extensions
Manages environment extensions.

```python
class Extensions:
    def get(self, env: str)
    def update(self, env: str, body: dict)
    def query(self, body: dict)
    def query_conn_field_summary(self, body: dict)
```

## Model Classes

### Component
Represents a Boomi component.

```python
class Component(BaseModel):
    id: str = Field(..., alias="componentId")
    name: str
    type: str
    folder_id: Optional[str] = Field(None, alias="folderId")
```

### Deployment
Represents a Boomi deployment.

```python
class Deployment(BaseModel):
    id: str = Field(..., alias="deploymentId")
    component_id: str = Field(..., alias="componentId")
    environment_id: str = Field(..., alias="environmentId")
    package_version: Optional[str] = Field(None, alias="packageVersion")
    status: Optional[str] = None
```

### ExecutionSummaryRecord
Represents a summary of a process run.

```python
class ExecutionSummaryRecord(BaseModel):
    process_id: str = Field(..., alias="processID")
    process_name: str = Field(..., alias="processName")
    status: Optional[str] = None
```

### ExecutionConnector
Details about a connector step within an execution.

```python
class ExecutionConnector(BaseModel):
    id: str
    execution_id: str = Field(..., alias="executionId")
    connector_type: Optional[str] = Field(None, alias="connectorType")
    success_count: Optional[int] = Field(None, alias="successCount")
```

### GenericConnectorRecord
Represents a tracked document in a run.

```python
class GenericConnectorRecord(BaseModel):
    id: str
    execution_id: str = Field(..., alias="executionId")
    status: Optional[str] = None
    error_message: Optional[str] = Field(None, alias="errorMessage")
```


## Exception Classes

### BoomiError
Base exception class for all SDK-specific issues.

### AuthenticationError
Raised when supplied credentials are invalid or expired (HTTP 401).

### RateLimitError
Raised when the Boomi API returns HTTP 429 (Too Many Requests).

### ApiError
Raised for any other non-retryable API error (HTTP >= 400). 
