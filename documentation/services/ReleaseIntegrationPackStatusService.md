# ReleaseIntegrationPackStatusService

A list of all methods in the `ReleaseIntegrationPackStatusService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_release_integration_pack_status](#get_release_integration_pack_status)   | To retrieve the release status of the publisher integration pack, follow these steps: 1. Send a POST request to the ReleaseIntegrationPackStatus object. The response will return a requestId. 2. Use the requestId returned in Step 1 to make a subsequent call to the ReleaseIntegrationPackStatus object to retrieve detailed information about the released integration pack. 3. Repeatedly poll the ReleaseIntegrationPackStatus object using the requestId until the details of the released integration pack are available. If the request is still in progress or scheduled, it returns an HTTP 202 status code. When the integration pack is released successfully, the ReleaseIntegrationPackStatus object returns the released details. |
| [bulk_release_integration_pack_status](#bulk_release_integration_pack_status) | The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## get_release_integration_pack_status

To retrieve the release status of the publisher integration pack, follow these steps: 1. Send a POST request to the ReleaseIntegrationPackStatus object. The response will return a requestId. 2. Use the requestId returned in Step 1 to make a subsequent call to the ReleaseIntegrationPackStatus object to retrieve detailed information about the released integration pack. 3. Repeatedly poll the ReleaseIntegrationPackStatus object using the requestId until the details of the released integration pack are available. If the request is still in progress or scheduled, it returns an HTTP 202 status code. When the integration pack is released successfully, the ReleaseIntegrationPackStatus object returns the released details.

- HTTP Method: `GET`
- Endpoint: `/ReleaseIntegrationPackStatus/{id}`

**Parameters**

| Name | Type | Required | Description                                                 |
| :--- | :--- | :------- | :---------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the integration pack. |

**Return Type**

`ReleaseIntegrationPackStatus`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.release_integration_pack_status.get_release_integration_pack_status(id_="id")

print(result)
```

## bulk_release_integration_pack_status

The bulk GET operation returns multiple objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/ReleaseIntegrationPackStatus/bulk`

**Parameters**

| Name         | Type                                                                                            | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ReleaseIntegrationPackStatusBulkRequest](../models/ReleaseIntegrationPackStatusBulkRequest.md) | ❌       | The request body. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ReleaseIntegrationPackStatusBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ReleaseIntegrationPackStatusBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.release_integration_pack_status.bulk_release_integration_pack_status(request_body=request_body)

with open("output-file.ext", "w") as f:
    f.write(result)
```

