# Oftp2ConnectorRecordService

A list of all methods in the `Oftp2ConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :---------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_oftp2_connector_record](#query_oftp2_connector_record)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). To filter by a custom field, use the format `customFields/fieldName` as the filter property, where `fieldName` is the element name of the custom field in the OFTP2 Connector Record structure. To get a list of the available custom fields, see [Custom Tracked Field](/api/platformapi#tag/CustomTrackedField) object. The STARTS_WITH operator accepts only values that do not include spaces. Sorting of the QUERY results are by the dateProcessed field value, from the oldest to the newest. |
| [query_more_oftp2_connector_record](#query_more_oftp2_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## query_oftp2_connector_record

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). To filter by a custom field, use the format `customFields/fieldName` as the filter property, where `fieldName` is the element name of the custom field in the OFTP2 Connector Record structure. To get a list of the available custom fields, see [Custom Tracked Field](/api/platformapi#tag/CustomTrackedField) object. The STARTS_WITH operator accepts only values that do not include spaces. Sorting of the QUERY results are by the dateProcessed field value, from the oldest to the newest.

- HTTP Method: `POST`
- Endpoint: `/OFTP2ConnectorRecord/query`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [Oftp2ConnectorRecordQueryConfig](../models/Oftp2ConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`Oftp2ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Oftp2ConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Oftp2ConnectorRecordQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "sfiddsn"
        }
    }
)

result = sdk.oftp2_connector_record.query_oftp2_connector_record(request_body=request_body)

print(result)
```

## query_more_oftp2_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/OFTP2ConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`Oftp2ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "qui Ut"

result = sdk.oftp2_connector_record.query_more_oftp2_connector_record(request_body=request_body)

print(result)
```

