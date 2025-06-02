# ExecutionCountAccountService

A list of all methods in the `ExecutionCountAccountService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_execution_count_account](#query_execution_count_account)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_execution_count_account](#query_more_execution_count_account) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_execution_count_account

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionCountAccount/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ExecutionCountAccountQueryConfig](../models/ExecutionCountAccountQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ExecutionCountAccountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ExecutionCountAccountQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ExecutionCountAccountQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "environmentId"
        }
    }
)

result = sdk.execution_count_account.query_execution_count_account(request_body=request_body)

print(result)
```

## query_more_execution_count_account

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionCountAccount/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ExecutionCountAccountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ex tempor dol"

result = sdk.execution_count_account.query_more_execution_count_account(request_body=request_body)

print(result)
```

