# EdiCustomConnectorRecordService

A list of all methods in the `EdiCustomConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_edi_custom_connector_record](#query_edi_custom_connector_record)           | - To filter by a customField, use the format customFields. Use fieldName as the filter property where fieldName is the element name of the custom field in the EDI Custom Connector Record structure. To get a list of the available custom fields, refer to [Custom Tracked Field object](#tag/CustomTrackedField). - The STARTS_WITH operator accepts values that do not include spaces. - Sorting of the Query results are by the `dateProcessed` field value, from the oldest to the newest. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_edi_custom_connector_record](#query_more_edi_custom_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## query_edi_custom_connector_record

- To filter by a customField, use the format customFields. Use fieldName as the filter property where fieldName is the element name of the custom field in the EDI Custom Connector Record structure. To get a list of the available custom fields, refer to [Custom Tracked Field object](#tag/CustomTrackedField). - The STARTS_WITH operator accepts values that do not include spaces. - Sorting of the Query results are by the `dateProcessed` field value, from the oldest to the newest. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EdiCustomConnectorRecord/query`

**Parameters**

| Name         | Type                                                                                    | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EdiCustomConnectorRecordQueryConfig](../models/EdiCustomConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EdiCustomConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EdiCustomConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EdiCustomConnectorRecordQueryConfig(
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

result = sdk.edi_custom_connector_record.query_edi_custom_connector_record(request_body=request_body)

print(result)
```

## query_more_edi_custom_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EdiCustomConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EdiCustomConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "consequat"

result = sdk.edi_custom_connector_record.query_more_edi_custom_connector_record(request_body=request_body)

print(result)
```

