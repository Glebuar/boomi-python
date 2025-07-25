# ExecutionConnectorService

A list of all methods in the `ExecutionConnectorService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_execution_connector](#query_execution_connector)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). - The QUERY operation allows you to query the connectors involved in a process run by filtering on attributes like executionId, actionType, successCount, and so on. - Requires one or more execution IDs in the request body. - You can filter all fields except executionConnector and id. |
| [query_more_execution_connector](#query_more_execution_connector) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## query_execution_connector

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). - The QUERY operation allows you to query the connectors involved in a process run by filtering on attributes like executionId, actionType, successCount, and so on. - Requires one or more execution IDs in the request body. - You can filter all fields except executionConnector and id.

- HTTP Method: `POST`
- Endpoint: `/ExecutionConnector/query`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ExecutionConnectorQueryConfig](../models/ExecutionConnectorQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ExecutionConnectorQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ExecutionConnectorQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ExecutionConnectorQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "executionId"
        }
    }
)

result = sdk.execution_connector.query_execution_connector(request_body=request_body)

print(result)
```

## query_more_execution_connector

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionConnector/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ExecutionConnectorQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "Lorem ex"

result = sdk.execution_connector.query_more_execution_connector(request_body=request_body)

print(result)
```

