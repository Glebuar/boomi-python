# ConnectorService

A list of all methods in the `ConnectorService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_connector](#get_connector)               | You can only perform the GET operation by `type` and not by `name`. Send an HTTP GET where `accountId` is the ID of the authenticating account for the request and `connectorType` is the name of the connector subtype you are attempting to GET. For example, sending an HTTP GET to `https://api.boomi.com/api/rest/v1/accountId/Connector/database` returns `Database` type connectors available on the account. |
| [bulk_connector](#bulk_connector)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                               |
| [query_connector](#query_connector)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                      |
| [query_more_connector](#query_more_connector) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                       |

## get_connector

You can only perform the GET operation by `type` and not by `name`. Send an HTTP GET where `accountId` is the ID of the authenticating account for the request and `connectorType` is the name of the connector subtype you are attempting to GET. For example, sending an HTTP GET to `https://api.boomi.com/api/rest/v1/accountId/Connector/database` returns `Database` type connectors available on the account.

- HTTP Method: `GET`
- Endpoint: `/Connector/{connectorType}`

**Parameters**

| Name           | Type | Required | Description                                                                                                                                                                                             |
| :------------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| connector_type | str  | ✅       | The internal and unique identifier for connector type, such as `http`, `ftp`, `greatplains`. The [Component Metadata object](/api/platformapi#tag/ComponentMetadata) refers to this field as _subType_. |

**Return Type**

`Connector`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.connector.get_connector(connector_type="connectorType")

print(result)
```

## bulk_connector

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Connector/bulk`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ConnectorBulkRequest](../models/ConnectorBulkRequest.md) | ❌       | The request body. |

**Return Type**

`ConnectorBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ConnectorBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ConnectorBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.connector.bulk_connector(request_body=request_body)

print(result)
```

## query_connector

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Connector/query`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ConnectorQueryConfig](../models/ConnectorQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ConnectorQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ConnectorQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ConnectorQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "type"
        }
    }
)

result = sdk.connector.query_connector(request_body=request_body)

print(result)
```

## query_more_connector

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Connector/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ConnectorQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ametdolo"

result = sdk.connector.query_more_connector(request_body=request_body)

print(result)
```

