# AtomConnectorVersionsService

A list of all methods in the `AtomConnectorVersionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                      |
| :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| [get_atom_connector_versions](#get_atom_connector_versions)   | Retrieves the properties of connectors used by the Runtime, Runtime cluster, or Runtime cloud with specified ID. |
| [bulk_atom_connector_versions](#bulk_atom_connector_versions) | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).           |

## get_atom_connector_versions

Retrieves the properties of connectors used by the Runtime, Runtime cluster, or Runtime cloud with specified ID.

- HTTP Method: `GET`
- Endpoint: `/AtomConnectorVersions/{id}`

**Parameters**

| Name | Type | Required | Description                                               |
| :--- | :--- | :------- | :-------------------------------------------------------- |
| id\_ | str  | ✅       | The ID of the Runtime, Runtime cluster, or Runtime cloud. |

**Return Type**

`AtomConnectorVersions`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.atom_connector_versions.get_atom_connector_versions(id_="id")

print(result)
```

## bulk_atom_connector_versions

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AtomConnectorVersions/bulk`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AtomConnectorVersionsBulkRequest](../models/AtomConnectorVersionsBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AtomConnectorVersionsBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomConnectorVersionsBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomConnectorVersionsBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.atom_connector_versions.bulk_atom_connector_versions(request_body=request_body)

print(result)
```

