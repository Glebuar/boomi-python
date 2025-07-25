# ExecutionCountAccountGroupService

A list of all methods in the `ExecutionCountAccountGroupService` service. Click on the method name to view detailed information about that method.

| Methods                                                                               | Description                                                                                                                                                                                                                                                                                                                      |
| :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_execution_count_account_group](#query_execution_count_account_group)           | The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_execution_count_account_group](#query_more_execution_count_account_group) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                   |

## query_execution_count_account_group

The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionCountAccountGroup/query`

**Parameters**

| Name         | Type                                                                                        | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ExecutionCountAccountGroupQueryConfig](../models/ExecutionCountAccountGroupQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ExecutionCountAccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ExecutionCountAccountGroupQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ExecutionCountAccountGroupQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "accountGroupId"
        }
    }
)

result = sdk.execution_count_account_group.query_execution_count_account_group(request_body=request_body)

print(result)
```

## query_more_execution_count_account_group

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionCountAccountGroup/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ExecutionCountAccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "sint veli"

result = sdk.execution_count_account_group.query_more_execution_count_account_group(request_body=request_body)

print(result)
```

