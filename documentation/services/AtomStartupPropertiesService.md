# AtomStartupPropertiesService

A list of all methods in the `AtomStartupPropertiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                |
| :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------- |
| [get_atom_startup_properties](#get_atom_startup_properties)   | Retrieves the startup properties for the Runtime, Runtime cluster, or Runtime cloud with the specified ID. |
| [bulk_atom_startup_properties](#bulk_atom_startup_properties) | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).     |

## get_atom_startup_properties

Retrieves the startup properties for the Runtime, Runtime cluster, or Runtime cloud with the specified ID.

- HTTP Method: `GET`
- Endpoint: `/AtomStartupProperties/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                                                  |
| :--- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID for the Runtime, Runtime cluster, or Runtime cloud. (This API is not applicable for runtimes attached to clouds) |

**Return Type**

`AtomStartupProperties`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom_startup_properties.get_atom_startup_properties(id_="id")

print(result)
```

## bulk_atom_startup_properties

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AtomStartupProperties/bulk`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AtomStartupPropertiesBulkRequest](../models/AtomStartupPropertiesBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AtomStartupPropertiesBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomStartupPropertiesBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomStartupPropertiesBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.atom_startup_properties.bulk_atom_startup_properties(request_body=request_body)

print(result)
```

