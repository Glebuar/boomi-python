# ThroughputAccountGroupService

A list of all methods in the `ThroughputAccountGroupService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_throughput_account_group](#query_throughput_account_group)           | - You can only use the EQUALS operator with the `environmentId` filter parameter. - The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_throughput_account_group](#query_more_throughput_account_group) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                       |

## query_throughput_account_group

- You can only use the EQUALS operator with the `environmentId` filter parameter. - The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ThroughputAccountGroup/query`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ThroughputAccountGroupQueryConfig](../models/ThroughputAccountGroupQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ThroughputAccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ThroughputAccountGroupQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ThroughputAccountGroupQueryConfig(
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

result = sdk.throughput_account_group.query_throughput_account_group(request_body=request_body)

print(result)
```

## query_more_throughput_account_group

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ThroughputAccountGroup/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ThroughputAccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "tempor in dolor"

result = sdk.throughput_account_group.query_more_throughput_account_group(request_body=request_body)

print(result)
```

