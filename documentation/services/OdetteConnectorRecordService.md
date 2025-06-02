# OdetteConnectorRecordService

A list of all methods in the `OdetteConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_odette_connector_record](#query_odette_connector_record)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_odette_connector_record](#query_more_odette_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## query_odette_connector_record

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ODETTEConnectorRecord/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [OdetteConnectorRecordQueryConfig](../models/OdetteConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`OdetteConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import OdetteConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = OdetteConnectorRecordQueryConfig(
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

result = sdk.odette_connector_record.query_odette_connector_record(request_body=request_body)

print(result)
```

## query_more_odette_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ODETTEConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`OdetteConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ad dolor"

result = sdk.odette_connector_record.query_more_odette_connector_record(request_body=request_body)

print(result)
```

