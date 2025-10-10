# ReleaseIntegrationPackService

A list of all methods in the `ReleaseIntegrationPackService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_release_integration_pack](#create_release_integration_pack) | Creates an immediate or scheduled release for a publisher integration pack. To schedule the publisher integration pack for release, you must specify the release schedule (immediate or scheduled). The `releaseOnDate` field is required if you schedule the release for a future date. |
| [update_release_integration_pack](#update_release_integration_pack) | Modifies the scheduled release of a publisher integration pack. \> **Note:** The Update operation is only performed when there is an existing scheduled release request for the integration pack.                                                                                        |

## create_release_integration_pack

Creates an immediate or scheduled release for a publisher integration pack. To schedule the publisher integration pack for release, you must specify the release schedule (immediate or scheduled). The `releaseOnDate` field is required if you schedule the release for a future date.

- HTTP Method: `POST`
- Endpoint: `/ReleaseIntegrationPack`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ReleaseIntegrationPack](../models/ReleaseIntegrationPack.md) | ❌       | The request body. |

**Return Type**

`ReleaseIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ReleaseIntegrationPack

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ReleaseIntegrationPack(
    release_packaged_components={
        "release_packaged_component": [
            {
                "component_id": "b420a8ab-8e4e-41b2-93ce-079093a03af2",
                "released_version": "2.0",
                "version": "2.0"
            }
        ]
    },
    id_="f0f7face-3a9d-48b1-8a32-82b84499cd4e",
    installation_type="SINGLE",
    name="Testing MULTI",
    release_on_date="releaseOnDate",
    release_schedule="IMMEDIATELY",
    release_status_url="https://api.boomi.com/api/rest/v1/boomi-8Q78Q1/ReleaseIntegrationPackStatus/release-11031691-dc62-4280-a3b2-dcf7f3521f8a",
    request_id="release-11031691-dc62-4280-a3b2-dcf7f3521f8a"
)

result = sdk.release_integration_pack.create_release_integration_pack(request_body=request_body)

print(result)
```

## update_release_integration_pack

Modifies the scheduled release of a publisher integration pack. \> **Note:** The Update operation is only performed when there is an existing scheduled release request for the integration pack.

- HTTP Method: `POST`
- Endpoint: `/ReleaseIntegrationPack/{id}`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ReleaseIntegrationPack](../models/ReleaseIntegrationPack.md) | ❌       | The request body. |
| id\_         | str                                                           | ✅       |                   |

**Return Type**

`ReleaseIntegrationPack`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ReleaseIntegrationPack

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ReleaseIntegrationPack(
    release_packaged_components={
        "release_packaged_component": [
            {
                "component_id": "b420a8ab-8e4e-41b2-93ce-079093a03af2",
                "released_version": "2.0",
                "version": "2.0"
            }
        ]
    },
    id_="f0f7face-3a9d-48b1-8a32-82b84499cd4e",
    installation_type="SINGLE",
    name="Testing MULTI",
    release_on_date="releaseOnDate",
    release_schedule="IMMEDIATELY",
    release_status_url="https://api.boomi.com/api/rest/v1/boomi-8Q78Q1/ReleaseIntegrationPackStatus/release-11031691-dc62-4280-a3b2-dcf7f3521f8a",
    request_id="release-11031691-dc62-4280-a3b2-dcf7f3521f8a"
)

result = sdk.release_integration_pack.update_release_integration_pack(
    request_body=request_body,
    id_="id"
)

print(result)
```

