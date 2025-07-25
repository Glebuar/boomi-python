# PublisherIntegrationPackService

A list of all methods in the `PublisherIntegrationPackService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_publisher_integration_pack](#create_publisher_integration_pack)         | Creates a single attachment or multiple attachment integration pack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [get_publisher_integration_pack](#get_publisher_integration_pack)               | Retrieves the details of the integration pack and packaged components. The standard GET operation retrieves the properties of the integration pack with a specified ID. The bulk GET operation retrieves the properties of the integration packs with the specified IDs to a maximum of 100.                                                                                                                                                                                                                                                                                            |
| [update_publisher_integration_pack](#update_publisher_integration_pack)         | The Update operation adds or removes the packaged components from the publisher integration pack. It also updates the description field of single and multiple attachment integration packs and the name field only for a single attachment integration pack. \>**Note:** When updating an integration pack, you must include all the packaged components associated with it in the request body. If a packaged component is not included, it will be deleted upon updating an integration pack. For example, include all packaged components while updating the integration pack name. |
| [delete_publisher_integration_pack](#delete_publisher_integration_pack)         | Deletes the publisher integration pack having a specified ID from the requesting account. The deleted integration pack is automatically uninstalled from all accounts where it was installed. Any Runtimes or environments attached to the integration pack are also detached.                                                                                                                                                                                                                                                                                                          |
| [bulk_publisher_integration_pack](#bulk_publisher_integration_pack)             | The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                          |
| [query_publisher_integration_pack](#query_publisher_integration_pack)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                         |
| [query_more_publisher_integration_pack](#query_more_publisher_integration_pack) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## create_publisher_integration_pack

Creates a single attachment or multiple attachment integration pack.

- HTTP Method: `POST`
- Endpoint: `/PublisherIntegrationPack`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PublisherIntegrationPack](../models/PublisherIntegrationPack.md) | ❌       | The request body. |

**Return Type**

`PublisherIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PublisherIntegrationPack

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PublisherIntegrationPack(
    description="Description",
    publisher_packaged_components={
        "publisher_packaged_component": [
            {
                "component_id": "76742659-845c-45e4-bb9f-d63ff998f658",
                "component_name": "New Process 4",
                "component_type": "process",
                "current_version": "1.0",
                "deleted": False,
                "latest_version": "1.2",
                "pending_version": "1.1"
            }
        ]
    },
    id_="d7c16f5d-3311-417e-a149-3c55436f7d8d",
    installation_type="SINGLE",
    name="perf testing ipack",
    operation_type="ADD"
)

result = sdk.publisher_integration_pack.create_publisher_integration_pack(request_body=request_body)

print(result)
```

## get_publisher_integration_pack

Retrieves the details of the integration pack and packaged components. The standard GET operation retrieves the properties of the integration pack with a specified ID. The bulk GET operation retrieves the properties of the integration packs with the specified IDs to a maximum of 100.

- HTTP Method: `GET`
- Endpoint: `/PublisherIntegrationPack/{id}`

**Parameters**

| Name | Type | Required | Description                                                 |
| :--- | :--- | :------- | :---------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the integration pack. |

**Return Type**

`PublisherIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.publisher_integration_pack.get_publisher_integration_pack(id_="id")

print(result)
```

## update_publisher_integration_pack

The Update operation adds or removes the packaged components from the publisher integration pack. It also updates the description field of single and multiple attachment integration packs and the name field only for a single attachment integration pack. \>**Note:** When updating an integration pack, you must include all the packaged components associated with it in the request body. If a packaged component is not included, it will be deleted upon updating an integration pack. For example, include all packaged components while updating the integration pack name.

- HTTP Method: `POST`
- Endpoint: `/PublisherIntegrationPack/{id}`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PublisherIntegrationPack](../models/PublisherIntegrationPack.md) | ❌       | The request body. |
| id\_         | str                                                               | ✅       |                   |

**Return Type**

`PublisherIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PublisherIntegrationPack

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PublisherIntegrationPack(
    description="Description",
    publisher_packaged_components={
        "publisher_packaged_component": [
            {
                "component_id": "76742659-845c-45e4-bb9f-d63ff998f658",
                "component_name": "New Process 4",
                "component_type": "process",
                "current_version": "1.0",
                "deleted": False,
                "latest_version": "1.2",
                "pending_version": "1.1"
            }
        ]
    },
    id_="d7c16f5d-3311-417e-a149-3c55436f7d8d",
    installation_type="SINGLE",
    name="perf testing ipack",
    operation_type="ADD"
)

result = sdk.publisher_integration_pack.update_publisher_integration_pack(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_publisher_integration_pack

Deletes the publisher integration pack having a specified ID from the requesting account. The deleted integration pack is automatically uninstalled from all accounts where it was installed. Any Runtimes or environments attached to the integration pack are also detached.

- HTTP Method: `DELETE`
- Endpoint: `/PublisherIntegrationPack/{id}`

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

result = sdk.publisher_integration_pack.delete_publisher_integration_pack(id_="id")

print(result)
```

## bulk_publisher_integration_pack

The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/PublisherIntegrationPack/bulk`

**Parameters**

| Name         | Type                                                                                    | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PublisherIntegrationPackBulkRequest](../models/PublisherIntegrationPackBulkRequest.md) | ❌       | The request body. |

**Return Type**

`PublisherIntegrationPackBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PublisherIntegrationPackBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PublisherIntegrationPackBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.publisher_integration_pack.bulk_publisher_integration_pack(request_body=request_body)

print(result)
```

## query_publisher_integration_pack

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/PublisherIntegrationPack/query`

**Parameters**

| Name         | Type                                                                                    | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PublisherIntegrationPackQueryConfig](../models/PublisherIntegrationPackQueryConfig.md) | ❌       | The request body. |

**Return Type**

`PublisherIntegrationPackQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PublisherIntegrationPackQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PublisherIntegrationPackQueryConfig(
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

result = sdk.publisher_integration_pack.query_publisher_integration_pack(request_body=request_body)

print(result)
```

## query_more_publisher_integration_pack

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/PublisherIntegrationPack/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`PublisherIntegrationPackQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "anim nostrud a"

result = sdk.publisher_integration_pack.query_more_publisher_integration_pack(request_body=request_body)

print(result)
```

