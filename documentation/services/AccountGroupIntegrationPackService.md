# AccountGroupIntegrationPackService

A list of all methods in the `AccountGroupIntegrationPackService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                 | Description                                                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_account_group_integration_pack](#create_account_group_integration_pack)         | Adds an integration pack to the requesting account group.                                                                                                                                                                                                                                                             |
| [get_account_group_integration_pack](#get_account_group_integration_pack)               | The ordinary GET operation retrieves the properties of the AccountGroupIntegrationPack with the specified ID. The bulk GET operation retrieves the properties of the AccountGroupIntegrationPack with the specified IDs to a maximum of 100. You can obtain AccountGroupIntegrationPack IDs from the QUERY operation. |
| [delete_account_group_integration_pack](#delete_account_group_integration_pack)         | Removes the integration pack with a specified ID from the requesting account group. You can obtain this ID from a QUERY operation.                                                                                                                                                                                    |
| [bulk_account_group_integration_pack](#bulk_account_group_integration_pack)             | The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                        |
| [query_account_group_integration_pack](#query_account_group_integration_pack)           | Retrieves all integration packs available to the requesting account group ID. For general information about the structure of QUERY filters and how to handle paged results, see the Query filters and Query paging topics.                                                                                            |
| [query_more_account_group_integration_pack](#query_more_account_group_integration_pack) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                        |

## create_account_group_integration_pack

Adds an integration pack to the requesting account group.

- HTTP Method: `POST`
- Endpoint: `/AccountGroupIntegrationPack`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupIntegrationPack](../models/AccountGroupIntegrationPack.md) | ❌       | The request body. |

**Return Type**

`AccountGroupIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupIntegrationPack

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupIntegrationPack(
    account_group_id="cd17f866-c247-4c54-a1a1-ea8f8f86a1d1",
    id_="MXxjZDE3Zjg2Ni1jMjQ3LTRjNTQtYTFhMS1lYThmOGY4NmExZDE",
    installation_type="SINGLE",
    integration_pack_id="cd17f866-c247-4c54-a1a1-ea8f8f863456",
    integration_pack_name="test integration pack"
)

result = sdk.account_group_integration_pack.create_account_group_integration_pack(request_body=request_body)

print(result)
```

## get_account_group_integration_pack

The ordinary GET operation retrieves the properties of the AccountGroupIntegrationPack with the specified ID. The bulk GET operation retrieves the properties of the AccountGroupIntegrationPack with the specified IDs to a maximum of 100. You can obtain AccountGroupIntegrationPack IDs from the QUERY operation.

- HTTP Method: `GET`
- Endpoint: `/AccountGroupIntegrationPack/{id}`

**Parameters**

| Name | Type | Required | Description                                                 |
| :--- | :--- | :------- | :---------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the integration pack. |

**Return Type**

`AccountGroupIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_group_integration_pack.get_account_group_integration_pack(id_="id")

print(result)
```

## delete_account_group_integration_pack

Removes the integration pack with a specified ID from the requesting account group. You can obtain this ID from a QUERY operation.

- HTTP Method: `DELETE`
- Endpoint: `/AccountGroupIntegrationPack/{id}`

**Parameters**

| Name | Type | Required | Description                                                 |
| :--- | :--- | :------- | :---------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the integration pack. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_group_integration_pack.delete_account_group_integration_pack(id_="id")

print(result)
```

## bulk_account_group_integration_pack

The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AccountGroupIntegrationPack/bulk`

**Parameters**

| Name         | Type                                                                                          | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupIntegrationPackBulkRequest](../models/AccountGroupIntegrationPackBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AccountGroupIntegrationPackBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupIntegrationPackBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupIntegrationPackBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.account_group_integration_pack.bulk_account_group_integration_pack(request_body=request_body)

print(result)
```

## query_account_group_integration_pack

Retrieves all integration packs available to the requesting account group ID. For general information about the structure of QUERY filters and how to handle paged results, see the Query filters and Query paging topics.

- HTTP Method: `POST`
- Endpoint: `/AccountGroupIntegrationPack/query`

**Parameters**

| Name         | Type                                                                                          | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupIntegrationPackQueryConfig](../models/AccountGroupIntegrationPackQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AccountGroupIntegrationPackQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupIntegrationPackQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupIntegrationPackQueryConfig(
    query_filter={
        "expression": {
            "id_": "id",
            "name": "name",
            "status": "status",
            "metadata": {
                "created_at": "createdAt",
                "updated_at": "updatedAt"
            }
        }
    }
)

result = sdk.account_group_integration_pack.query_account_group_integration_pack(request_body=request_body)

print(result)
```

## query_more_account_group_integration_pack

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroupIntegrationPack/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountGroupIntegrationPackQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "quisaliqu"

result = sdk.account_group_integration_pack.query_more_account_group_integration_pack(request_body=request_body)

print(result)
```

