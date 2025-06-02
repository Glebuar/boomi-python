# Hl7ConnectorRecordService

A list of all methods in the `Hl7ConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_hl7_connector_record](#query_hl7_connector_record)           | To filter by a customField, use the format `customFields.fieldName` as the filter property where `fieldName` is the element name of the custom field in the HL7 Connector Record structure. To get a list of the available custom fields, refer to [CustomTrackedField object](#tag/CustomTrackedField). The STARTS_WITH operator accepts values that do not include spaces. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_hl7_connector_record](#query_more_hl7_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## query_hl7_connector_record

To filter by a customField, use the format `customFields.fieldName` as the filter property where `fieldName` is the element name of the custom field in the HL7 Connector Record structure. To get a list of the available custom fields, refer to [CustomTrackedField object](#tag/CustomTrackedField). The STARTS_WITH operator accepts values that do not include spaces. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/HL7ConnectorRecord/query`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [Hl7ConnectorRecordQueryConfig](../models/Hl7ConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`Hl7ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Hl7ConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Hl7ConnectorRecordQueryConfig(
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

result = sdk.hl7_connector_record.query_hl7_connector_record(request_body=request_body)

print(result)
```

## query_more_hl7_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/HL7ConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`Hl7ConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "esse et Ex"

result = sdk.hl7_connector_record.query_more_hl7_connector_record(request_body=request_body)

print(result)
```

