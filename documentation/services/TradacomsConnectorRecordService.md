# TradacomsConnectorRecordService

A list of all methods in the `TradacomsConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_tradacoms_connector_record](#query_tradacoms_connector_record)           | - To filter by a custom field, use the format `customFields`. Use the `fieldName` as the filter property where `fieldName` is the element name of the custom field in the record structure. To get a list of the available custom fields see the [Custom Tracked Field](#tag/CustomTrackedField) object. - The STARTS_WITH operator only accepts values that do not include spaces. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_tradacoms_connector_record](#query_more_tradacoms_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## query_tradacoms_connector_record

- To filter by a custom field, use the format `customFields`. Use the `fieldName` as the filter property where `fieldName` is the element name of the custom field in the record structure. To get a list of the available custom fields see the [Custom Tracked Field](#tag/CustomTrackedField) object. - The STARTS_WITH operator only accepts values that do not include spaces. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradacomsConnectorRecord/query`

**Parameters**

| Name         | Type                                                                                    | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TradacomsConnectorRecordQueryConfig](../models/TradacomsConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`TradacomsConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradacomsConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradacomsConnectorRecordQueryConfig(
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

result = sdk.tradacoms_connector_record.query_tradacoms_connector_record(request_body=request_body)

print(result)
```

## query_more_tradacoms_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradacomsConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`TradacomsConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "Uteu off"

result = sdk.tradacoms_connector_record.query_more_tradacoms_connector_record(request_body=request_body)

print(result)
```

