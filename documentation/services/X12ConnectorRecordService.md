# X12ConnectorRecordService

A list of all methods in the `X12ConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [query_x12_connector_record](#query_x12_connector_record)           | To filter by a custom field, use the format customFields. Use the fieldName as the filter property where fieldName is the element name of the custom field in the X12 Connector Record structure. To get a list of the available custom fields see the [Custom Tracked Field](/api/platformapi#tag/CustomTrackedField) object. The STARTS_WITH operator only accepts values that do not include spaces. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_x12_connector_record](#query_more_x12_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## query_x12_connector_record

To filter by a custom field, use the format customFields. Use the fieldName as the filter property where fieldName is the element name of the custom field in the X12 Connector Record structure. To get a list of the available custom fields see the [Custom Tracked Field](/api/platformapi#tag/CustomTrackedField) object. The STARTS_WITH operator only accepts values that do not include spaces. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/X12ConnectorRecord/query`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [X12ConnectorRecordQueryConfig](../models/X12ConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`X12ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import X12ConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = X12ConnectorRecordQueryConfig(
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

result = sdk.x12_connector_record.query_x12_connector_record(request_body=request_body)

print(result)
```

## query_more_x12_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/X12ConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`X12ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "sit id adi"

result = sdk.x12_connector_record.query_more_x12_connector_record(request_body=request_body)

print(result)
```

