# As2ConnectorRecordService

A list of all methods in the `As2ConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_as2_connector_record](#query_as2_connector_record)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_as2_connector_record](#query_more_as2_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_as2_connector_record

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AS2ConnectorRecord/query`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [As2ConnectorRecordQueryConfig](../models/As2ConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`As2ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import As2ConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = As2ConnectorRecordQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "property"
        }
    }
)

result = sdk.as2_connector_record.query_as2_connector_record(request_body=request_body)

print(result)
```

## query_more_as2_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AS2ConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`As2ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "fugiat "

result = sdk.as2_connector_record.query_more_as2_connector_record(request_body=request_body)

print(result)
```

