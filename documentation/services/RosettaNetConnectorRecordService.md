# RosettaNetConnectorRecordService

A list of all methods in the `RosettaNetConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_rosetta_net_connector_record](#query_rosetta_net_connector_record)           | - To filter by a customField, use the format customFields/fieldName as the filter property where fieldName is the element name of the custom field in the EDIFACT Connector Record structure. To get a list of the available custom fields, refer to [Custom Tracked Field object](#tag/CustomTrackedField). - The STARTS_WITH operator accepts values that do not include spaces only. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_rosetta_net_connector_record](#query_more_rosetta_net_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## query_rosetta_net_connector_record

- To filter by a customField, use the format customFields/fieldName as the filter property where fieldName is the element name of the custom field in the EDIFACT Connector Record structure. To get a list of the available custom fields, refer to [Custom Tracked Field object](#tag/CustomTrackedField). - The STARTS_WITH operator accepts values that do not include spaces only. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/RosettaNetConnectorRecord/query`

**Parameters**

| Name         | Type                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [RosettaNetConnectorRecordQueryConfig](../models/RosettaNetConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`RosettaNetConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RosettaNetConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RosettaNetConnectorRecordQueryConfig(
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

result = sdk.rosetta_net_connector_record.query_rosetta_net_connector_record(request_body=request_body)

print(result)
```

## query_more_rosetta_net_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/RosettaNetConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`RosettaNetConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "fugiat esse"

result = sdk.rosetta_net_connector_record.query_more_rosetta_net_connector_record(request_body=request_body)

print(result)
```

