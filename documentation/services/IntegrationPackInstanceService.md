# IntegrationPackInstanceService

A list of all methods in the `IntegrationPackInstanceService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_integration_pack_instance](#create_integration_pack_instance)         | Installs an instance of the integration pack with a specific ID in the requesting account. You can set the integrationPackOverrideName field only if you configure the specified integration pack to allow multiple installs.                                                                                                                                                                            |
| [get_integration_pack_instance](#get_integration_pack_instance)               | Retrieves the properties of the integration pack instance having the specified ID. The ordinary GET operation retrieves the properties of the integration pack instance having the specified ID. The bulk GET operation retrieves the properties of the integration pack instances having the specified IDs, to a maximum of 100. You can obtain integration pack instance IDs from the QUERY operation. |
| [delete_integration_pack_instance](#delete_integration_pack_instance)         | Uninstalls the integration pack instance having a specified ID from the requesting account. You can obtain this ID from a QUERY operation.                                                                                                                                                                                                                                                               |
| [bulk_integration_pack_instance](#bulk_integration_pack_instance)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                   |
| [query_integration_pack_instance](#query_integration_pack_instance)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                          |
| [query_more_integration_pack_instance](#query_more_integration_pack_instance) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                           |

## create_integration_pack_instance

Installs an instance of the integration pack with a specific ID in the requesting account. You can set the integrationPackOverrideName field only if you configure the specified integration pack to allow multiple installs.

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackInstance`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IntegrationPackInstance](../models/IntegrationPackInstance.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackInstance`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackInstance

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackInstance(
    process_id=[
        {
            "name": "name",
            "original_process_id": "originalProcessId",
            "wrapper_process_id": "wrapperProcessId"
        }
    ],
    id_="SW50ZWdyYXRpb25QYWNrSW5zdGFuY2UyMA",
    integration_pack_id="a3c4917d-9622-4c5f-978c-0f02b5f5457a",
    integration_pack_override_name="Domestic Order Intake"
)

result = sdk.integration_pack_instance.create_integration_pack_instance(request_body=request_body)

print(result)
```

## get_integration_pack_instance

Retrieves the properties of the integration pack instance having the specified ID. The ordinary GET operation retrieves the properties of the integration pack instance having the specified ID. The bulk GET operation retrieves the properties of the integration pack instances having the specified IDs, to a maximum of 100. You can obtain integration pack instance IDs from the QUERY operation.

- HTTP Method: `GET`
- Endpoint: `/IntegrationPackInstance/{id}`

**Parameters**

| Name | Type | Required | Description                       |
| :--- | :--- | :------- | :-------------------------------- |
| id\_ | str  | ✅       | The integration pack instance ID. |

**Return Type**

`IntegrationPackInstance`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.integration_pack_instance.get_integration_pack_instance(id_="id")

print(result)
```

## delete_integration_pack_instance

Uninstalls the integration pack instance having a specified ID from the requesting account. You can obtain this ID from a QUERY operation.

- HTTP Method: `DELETE`
- Endpoint: `/IntegrationPackInstance/{id}`

**Parameters**

| Name | Type | Required | Description                       |
| :--- | :--- | :------- | :-------------------------------- |
| id\_ | str  | ✅       | The integration pack instance ID. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.integration_pack_instance.delete_integration_pack_instance(id_="id")

print(result)
```

## bulk_integration_pack_instance

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackInstance/bulk`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [IntegrationPackInstanceBulkRequest](../models/IntegrationPackInstanceBulkRequest.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackInstanceBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackInstanceBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackInstanceBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.integration_pack_instance.bulk_integration_pack_instance(request_body=request_body)

print(result)
```

## query_integration_pack_instance

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackInstance/query`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [IntegrationPackInstanceQueryConfig](../models/IntegrationPackInstanceQueryConfig.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackInstanceQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackInstanceQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackInstanceQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "integrationPackOverrideName"
        }
    }
)

result = sdk.integration_pack_instance.query_integration_pack_instance(request_body=request_body)

print(result)
```

## query_more_integration_pack_instance

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackInstance/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`IntegrationPackInstanceQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolor sunt"

result = sdk.integration_pack_instance.query_more_integration_pack_instance(request_body=request_body)

print(result)
```

