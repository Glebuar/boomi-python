# ExecutionSummaryRecordService

A list of all methods in the `ExecutionSummaryRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_execution_summary_record](#query_execution_summary_record)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_execution_summary_record](#query_more_execution_summary_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_execution_summary_record

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionSummaryRecord/query`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ExecutionSummaryRecordQueryConfig](../models/ExecutionSummaryRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ExecutionSummaryRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ExecutionSummaryRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ExecutionSummaryRecordQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "processId"
        }
    }
)

result = sdk.execution_summary_record.query_execution_summary_record(request_body=request_body)

print(result)
```

## query_more_execution_summary_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ExecutionSummaryRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ExecutionSummaryRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "sint d"

result = sdk.execution_summary_record.query_more_execution_summary_record(request_body=request_body)

print(result)
```

