# AtomService

A list of all methods in the `AtomService` service. Click on the method name to view detailed information about that method.

| Methods                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_atom](#create_atom)                                                           | Creates and attaches a Runtime with the specified name to a specified Runtime cloud owned by the requesting account. This operation cannot be used to create a local Runtime. You must have the Runtime Management privilege to perform the POST operation. \>**Note:** The `createdBy` is a system-generated or read-only field. It cannot be passed in a CREATE request.                                                                                                                                                                    |
| [get_atom](#get_atom)                                                                 | Retrieves the properties of the Runtime, Runtime cluster, or Runtime cloud having the specified ID. For Runtime clusters and Runtime clouds that are part of a multi-node runtime, the GET operation returns values for the following additional variables: - _nodeId_ - _hostName_ - _status_ - _clusterProblem_ For more information on these variables, see the topic [Cluster Status panel](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Cluster_Status_panel_fbdb3645-00e2-4c3c-bba8-bf5fdb0f90f6). |
| [update_atom](#update_atom)                                                           | Updates the Runtime object having the specified ID. You can only update the name, purgeHistoryDays, purgeImmediate, forceRestartTime. You must have the Runtime Management privilege to perform the UPDATE operation. If you have the Runtime Management Read Access privilege, you cannot update an Runtime. \>**Note:** There might be a delay before you see the changes in the Runtime Information panel.                                                                                                                                 |
| [delete_atom](#delete_atom)                                                           | Deletes the Runtime object with the specified ID. You must have the Runtime Management privilege to perform the DELETE operation. If you have the Runtime Management Read Access privilege, you cannot delete a Runtime.                                                                                                                                                                                                                                                                                                                      |
| [bulk_atom](#bulk_atom)                                                               | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [query_atom](#query_atom)                                                             | Use either `BROKER` or `GATEWAY` with either the CONTAINS or NOT_CONTAINS operator to filter by API Gateways and Authentication Brokers that you own. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                         |
| [query_more_atom](#query_more_atom)                                                   | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [async_token_atom_counters](#async_token_atom_counters)                               | For a response, use the token from the initial GET response in a new request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [async_get_atom_counters](#async_get_atom_counters)                                   | The GET operation returns the current state of the counter names and values for the specified Runtime. The initial GET operation returns a token for the specified Runtime. `accountId` is the Platform account that you are authenticating with and `id` is the Runtime ID for the counters you are attempting to GET.                                                                                                                                                                                                                       |
| [async_token_persisted_process_properties](#async_token_persisted_process_properties) | For a response, use the token from the response in a new request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [async_get_persisted_process_properties](#async_get_persisted_process_properties)     | The GET operation returns the current state of the Persisted Process properties names and values for the specified Runtime. The initial GET operation returns a token for the specified Runtime.                                                                                                                                                                                                                                                                                                                                              |

## create_atom

Creates and attaches a Runtime with the specified name to a specified Runtime cloud owned by the requesting account. This operation cannot be used to create a local Runtime. You must have the Runtime Management privilege to perform the POST operation. \>**Note:** The `createdBy` is a system-generated or read-only field. It cannot be passed in a CREATE request.

- HTTP Method: `POST`
- Endpoint: `/Atom`

**Parameters**

| Name         | Type                      | Required | Description       |
| :----------- | :------------------------ | :------- | :---------------- |
| request_body | [Atom](../models/Atom.md) | ❌       | The request body. |

**Return Type**

`Atom`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Atom

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Atom(
    capabilities=[
        "GATEWAY"
    ],
    cloud_id="cloudId",
    cloud_molecule_id="cloudMoleculeId",
    cloud_molecule_name="cloudMoleculeName",
    cloud_name="cloudName",
    cloud_owner_name="cloudOwnerName",
    cluster={
        "node": [
            {
                "cluster_problem": "clusterProblem",
                "host_name": "hostName",
                "node_id": "nodeId",
                "status": "status"
            }
        ]
    },
    created_by="createdBy",
    current_version="17.08.0.0",
    date_installed="2016-02-05T14:49:21Z",
    force_restart_time="9",
    host_name="WN7X64-11A2BB3",
    id_="3456789a-bcde-f012-3456-789abcdef012",
    instance_id="instanceId",
    is_cloud_attachment=False,
    name="My Local Atom",
    purge_history_days="18",
    purge_immediate="false",
    status="UNKNOWN",
    type_="CLOUD",
    status_detail="statusDetail"
)

result = sdk.atom.create_atom(request_body=request_body)

print(result)
```

## get_atom

Retrieves the properties of the Runtime, Runtime cluster, or Runtime cloud having the specified ID. For Runtime clusters and Runtime clouds that are part of a multi-node runtime, the GET operation returns values for the following additional variables: - _nodeId_ - _hostName_ - _status_ - _clusterProblem_ For more information on these variables, see the topic [Cluster Status panel](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Cluster_Status_panel_fbdb3645-00e2-4c3c-bba8-bf5fdb0f90f6).

- HTTP Method: `GET`
- Endpoint: `/Atom/{id}`

**Parameters**

| Name | Type | Required | Description                                                     |
| :--- | :--- | :------- | :-------------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID for the Runtime, Runtime cluster, or Runtime cloud. |

**Return Type**

`Atom`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom.get_atom(id_="id")

print(result)
```

## update_atom

Updates the Runtime object having the specified ID. You can only update the name, purgeHistoryDays, purgeImmediate, forceRestartTime. You must have the Runtime Management privilege to perform the UPDATE operation. If you have the Runtime Management Read Access privilege, you cannot update an Runtime. \>**Note:** There might be a delay before you see the changes in the Runtime Information panel.

- HTTP Method: `POST`
- Endpoint: `/Atom/{id}`

**Parameters**

| Name         | Type                      | Required | Description                                                     |
| :----------- | :------------------------ | :------- | :-------------------------------------------------------------- |
| request_body | [Atom](../models/Atom.md) | ❌       | The request body.                                               |
| id\_         | str                       | ✅       | A unique ID for the Runtime, Runtime cluster, or Runtime cloud. |

**Return Type**

`Atom`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Atom

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Atom(
    capabilities=[
        "GATEWAY"
    ],
    cloud_id="cloudId",
    cloud_molecule_id="cloudMoleculeId",
    cloud_molecule_name="cloudMoleculeName",
    cloud_name="cloudName",
    cloud_owner_name="cloudOwnerName",
    cluster={
        "node": [
            {
                "cluster_problem": "clusterProblem",
                "host_name": "hostName",
                "node_id": "nodeId",
                "status": "status"
            }
        ]
    },
    created_by="createdBy",
    current_version="17.08.0.0",
    date_installed="2016-02-05T14:49:21Z",
    force_restart_time="9",
    host_name="WN7X64-11A2BB3",
    id_="3456789a-bcde-f012-3456-789abcdef012",
    instance_id="instanceId",
    is_cloud_attachment=False,
    name="My Local Atom",
    purge_history_days="18",
    purge_immediate="false",
    status="UNKNOWN",
    type_="CLOUD",
    status_detail="statusDetail"
)

result = sdk.atom.update_atom(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_atom

Deletes the Runtime object with the specified ID. You must have the Runtime Management privilege to perform the DELETE operation. If you have the Runtime Management Read Access privilege, you cannot delete a Runtime.

- HTTP Method: `DELETE`
- Endpoint: `/Atom/{id}`

**Parameters**

| Name | Type | Required | Description                                                     |
| :--- | :--- | :------- | :-------------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID for the Runtime, Runtime cluster, or Runtime cloud. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom.delete_atom(id_="id")

print(result)
```

## bulk_atom

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Atom/bulk`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [AtomBulkRequest](../models/AtomBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AtomBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.atom.bulk_atom(request_body=request_body)

print(result)
```

## query_atom

Use either `BROKER` or `GATEWAY` with either the CONTAINS or NOT_CONTAINS operator to filter by API Gateways and Authentication Brokers that you own. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Atom/query`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [AtomQueryConfig](../models/AtomQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AtomQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.atom.query_atom(request_body=request_body)

print(result)
```

## query_more_atom

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Atom/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AtomQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "laboris"

result = sdk.atom.query_more_atom(request_body=request_body)

print(result)
```

## async_token_atom_counters

For a response, use the token from the initial GET response in a new request.

- HTTP Method: `GET`
- Endpoint: `/async/AtomCounters/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`AtomCountersAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom.async_token_atom_counters(token="token")

print(result)
```

## async_get_atom_counters

The GET operation returns the current state of the counter names and values for the specified Runtime. The initial GET operation returns a token for the specified Runtime. `accountId` is the Platform account that you are authenticating with and `id` is the Runtime ID for the counters you are attempting to GET.

- HTTP Method: `GET`
- Endpoint: `/async/AtomCounters/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom.async_get_atom_counters(id_="id")

print(result)
```

## async_token_persisted_process_properties

For a response, use the token from the response in a new request.

- HTTP Method: `GET`
- Endpoint: `/async/PersistedProcessProperties/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`PersistedProcessPropertiesAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom.async_token_persisted_process_properties(token="token")

print(result)
```

## async_get_persisted_process_properties

The GET operation returns the current state of the Persisted Process properties names and values for the specified Runtime. The initial GET operation returns a token for the specified Runtime.

- HTTP Method: `GET`
- Endpoint: `/async/PersistedProcessProperties/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom.async_get_persisted_process_properties(id_="id")

print(result)
```

