# GenericConnectorRecordService

A list of all methods in the `GenericConnectorRecordService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_generic_connector_record](#get_generic_connector_record)               | Allows you to view document metadata for exactly one document based on the provided id.                                                                                                                                                                                                                                                                                                                                     |
| [bulk_generic_connector_record](#bulk_generic_connector_record)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                      |
| [query_generic_connector_record](#query_generic_connector_record)           | - The QUERY operation allows you to view document metadata for all documents in the run. You must query by exactly one `executionId`. - You cannot query `connectorFields`. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_generic_connector_record](#query_more_generic_connector_record) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                              |

## get_generic_connector_record

Allows you to view document metadata for exactly one document based on the provided id.

- HTTP Method: `GET`
- Endpoint: `/GenericConnectorRecord/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                               |
| :--- | :--- | :------- | :-------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The ID of the GenericConnectorRecord. You obtain this ID from querying the GenericConnectorRecord object. |

**Return Type**

`GenericConnectorRecord`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.generic_connector_record.get_generic_connector_record(id_="id")

print(result)
```

## bulk_generic_connector_record

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/GenericConnectorRecord/bulk`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [GenericConnectorRecordBulkRequest](../models/GenericConnectorRecordBulkRequest.md) | ❌       | The request body. |

**Return Type**

`GenericConnectorRecordBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import GenericConnectorRecordBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = GenericConnectorRecordBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.generic_connector_record.bulk_generic_connector_record(request_body=request_body)

print(result)
```

## query_generic_connector_record

- The QUERY operation allows you to view document metadata for all documents in the run. You must query by exactly one `executionId`. - You cannot query `connectorFields`. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/GenericConnectorRecord/query`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [GenericConnectorRecordQueryConfig](../models/GenericConnectorRecordQueryConfig.md) | ❌       | The request body. |

**Return Type**

`GenericConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import GenericConnectorRecordQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = GenericConnectorRecordQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "id"
        }
    }
)

result = sdk.generic_connector_record.query_generic_connector_record(request_body=request_body)

print(result)
```

## query_more_generic_connector_record

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/GenericConnectorRecord/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`GenericConnectorRecordQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "proident"

result = sdk.generic_connector_record.query_more_generic_connector_record(request_body=request_body)

print(result)
```

