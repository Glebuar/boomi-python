# IntegrationPackService

A list of all methods in the `IntegrationPackService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_integration_pack](#get_integration_pack)               | Retrieves the properties of the integration pack with a specified ID. The ordinary GET operation retrieves the properties of the integration pack with a specified ID. The bulk GET operation retrieves the properties of the integration packs having the specified IDs, to a maximum of 100. |
| [bulk_integration_pack](#bulk_integration_pack)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                         |
| [query_integration_pack](#query_integration_pack)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                |
| [query_more_integration_pack](#query_more_integration_pack) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                 |

## get_integration_pack

Retrieves the properties of the integration pack with a specified ID. The ordinary GET operation retrieves the properties of the integration pack with a specified ID. The bulk GET operation retrieves the properties of the integration packs having the specified IDs, to a maximum of 100.

- HTTP Method: `GET`
- Endpoint: `/IntegrationPack/{id}`

**Parameters**

| Name | Type | Required | Description                                                 |
| :--- | :--- | :------- | :---------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the integration pack. |

**Return Type**

`IntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.integration_pack.get_integration_pack(id_="id")

print(result)
```

## bulk_integration_pack

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPack/bulk`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IntegrationPackBulkRequest](../models/IntegrationPackBulkRequest.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.integration_pack.bulk_integration_pack(request_body=request_body)

print(result)
```

## query_integration_pack

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPack/query`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IntegrationPackQueryConfig](../models/IntegrationPackQueryConfig.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.integration_pack.query_integration_pack(request_body=request_body)

print(result)
```

## query_more_integration_pack

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPack/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`IntegrationPackQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "repreh"

result = sdk.integration_pack.query_more_integration_pack(request_body=request_body)

print(result)
```

