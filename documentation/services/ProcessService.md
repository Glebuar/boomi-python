# ProcessService

A list of all methods in the `ProcessService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                                                                                                                                                                                                                                                                  |
| :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_process](#get_process)               | Retrieves the properties of the process having the specified ID. The ordinary GET operation retrieves the properties of the process having the specified ID. The bulk GET operation retrieves the properties of the processes having the specified IDs, to a maximum of 100. |
| [bulk_process](#bulk_process)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                       |
| [query_process](#query_process)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                              |
| [query_more_process](#query_more_process) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                               |

## get_process

Retrieves the properties of the process having the specified ID. The ordinary GET operation retrieves the properties of the process having the specified ID. The bulk GET operation retrieves the properties of the processes having the specified IDs, to a maximum of 100.

- HTTP Method: `GET`
- Endpoint: `/Process/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the process. For deployed processes and processes belonging to single-install integration packs, this value is the process component ID. For processes belonging to multi-install integration packs, this is an synthetic ID and does not match an actual process component. You can use this value as the `extensionGroupId` when querying the Environment Extensions object. |

**Return Type**

`Process`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.process.get_process(id_="id")

print(result)
```

## bulk_process

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Process/bulk`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessBulkRequest](../models/ProcessBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ProcessBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.process.bulk_process(request_body=request_body)

print(result)
```

## query_process

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Process/query`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessQueryConfig](../models/ProcessQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ProcessQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessQueryConfig(
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

result = sdk.process.query_process(request_body=request_body)

print(result)
```

## query_more_process

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Process/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ProcessQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "exculpa eiusm"

result = sdk.process.query_more_process(request_body=request_body)

print(result)
```

