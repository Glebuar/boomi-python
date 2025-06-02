# PackagedComponentManifestService

A list of all methods in the `PackagedComponentManifestService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                         |
| :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| [get_packaged_component_manifest](#get_packaged_component_manifest)   | Retrieve a list of the included components and their summary metadata for a single version of a packaged component. |
| [bulk_packaged_component_manifest](#bulk_packaged_component_manifest) | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).              |

## get_packaged_component_manifest

Retrieve a list of the included components and their summary metadata for a single version of a packaged component.

- HTTP Method: `GET`
- Endpoint: `/PackagedComponentManifest/{packageId}`

**Parameters**

| Name       | Type | Required | Description                       |
| :--------- | :--- | :------- | :-------------------------------- |
| package_id | str  | ✅       | The ID of the packaged component. |

**Return Type**

`PackagedComponentManifest`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.packaged_component_manifest.get_packaged_component_manifest(package_id="packageId")

print(result)
```

## bulk_packaged_component_manifest

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/PackagedComponentManifest/bulk`

**Parameters**

| Name         | Type                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PackagedComponentManifestBulkRequest](../models/PackagedComponentManifestBulkRequest.md) | ❌       | The request body. |

**Return Type**

`PackagedComponentManifestBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import PackagedComponentManifestBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = PackagedComponentManifestBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.packaged_component_manifest.bulk_packaged_component_manifest(request_body=request_body)

print(result)
```

