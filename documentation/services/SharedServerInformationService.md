# SharedServerInformationService

A list of all methods in the `SharedServerInformationService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [get_shared_server_information](#get_shared_server_information)       | Retrieve Shared Server Information records for a specific single Runtime ID. You can retrieve Shared Server Information records only by an ordinary GET operation specifying a single Runtime ID or a bulk GET operation with a maximum of 100 Runtime IDs. This option is because the object ID for the Shared Server Information is not available currently (except by requesting the information from services). Therefore, this operation does not return the Shared Server Information object auth field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [update_shared_server_information](#update_shared_server_information) | Updates a Shared Server Information object based on the supplied Runtime ID. - The UPDATE operation updates a Shared Server Information object based on the supplied Runtime ID. To clear a field, set the attribute corresponding to that field to an empty string. You must have the Runtime Management privilege to perform the UPDATE operation. If you have the Runtime Management Read Access privilege, you cannot update shared server information. It is not possible to set authToken through this operation. This operation generates a token if it requires authentication, but a token does not currently exist. The new authToken appears in the response. - If you specify sslCertificateId, the certificate must be accessible by the account making the request. -If you do not configure the Authentication Type and Ports, using the Shared Server Information object to update only the API Type of a Runtime fails. If you are the owner of a Runtime, Runtime cluster, or Runtime cloud, you must update the API Type, Authentication Type, and HTTP Port or HTTPS Port through the Shared Server Information object for the API to succeed. Runtime cloud attachments cannot update the HTTP Port or HTTPS Port. - If you configure the Authentication Type and Ports, you can use the Shared Server Information object to update only the API Type of a Runtime. - This API does not support the configuration of multiple authentication types on a Runtime. |
| [bulk_shared_server_information](#bulk_shared_server_information)     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## get_shared_server_information

Retrieve Shared Server Information records for a specific single Runtime ID. You can retrieve Shared Server Information records only by an ordinary GET operation specifying a single Runtime ID or a bulk GET operation with a maximum of 100 Runtime IDs. This option is because the object ID for the Shared Server Information is not available currently (except by requesting the information from services). Therefore, this operation does not return the Shared Server Information object auth field.

- HTTP Method: `GET`
- Endpoint: `/SharedServerInformation/{id}`

**Parameters**

| Name | Type | Required | Description                                                  |
| :--- | :--- | :------- | :----------------------------------------------------------- |
| id\_ | str  | ✅       | The ID of the Runtime that is hosting the shared web server. |

**Return Type**

`SharedServerInformation`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.shared_server_information.get_shared_server_information(id_="id")

print(result)
```

## update_shared_server_information

Updates a Shared Server Information object based on the supplied Runtime ID. - The UPDATE operation updates a Shared Server Information object based on the supplied Runtime ID. To clear a field, set the attribute corresponding to that field to an empty string. You must have the Runtime Management privilege to perform the UPDATE operation. If you have the Runtime Management Read Access privilege, you cannot update shared server information. It is not possible to set authToken through this operation. This operation generates a token if it requires authentication, but a token does not currently exist. The new authToken appears in the response. - If you specify sslCertificateId, the certificate must be accessible by the account making the request. -If you do not configure the Authentication Type and Ports, using the Shared Server Information object to update only the API Type of a Runtime fails. If you are the owner of a Runtime, Runtime cluster, or Runtime cloud, you must update the API Type, Authentication Type, and HTTP Port or HTTPS Port through the Shared Server Information object for the API to succeed. Runtime cloud attachments cannot update the HTTP Port or HTTPS Port. - If you configure the Authentication Type and Ports, you can use the Shared Server Information object to update only the API Type of a Runtime. - This API does not support the configuration of multiple authentication types on a Runtime.

- HTTP Method: `POST`
- Endpoint: `/SharedServerInformation/{id}`

**Parameters**

| Name         | Type                                                            | Required | Description                                                  |
| :----------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| request_body | [SharedServerInformation](../models/SharedServerInformation.md) | ❌       | The request body.                                            |
| id\_         | str                                                             | ✅       | The ID of the Runtime that is hosting the shared web server. |

**Return Type**

`SharedServerInformation`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedServerInformation

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedServerInformation(
    api_type="basic",
    atom_id="3456789a-bcde-f012-3456-789abcdef012",
    auth="none",
    auth_token="bcdef012-3456-789a-bcde-f0123456789a",
    check_forwarded_headers="false",
    external_host="externalHost",
    external_http_port="0",
    external_https_port="0",
    http_port="9090",
    https_port="9093",
    internal_host="127.0.0.1",
    max_threads="250",
    min_auth="none",
    override_url="false",
    ssl_certificate_id="6789abcd-ef01-2345-6789-abcdef012345",
    url="http://system.sub.domain.tld:9090"
)

result = sdk.shared_server_information.update_shared_server_information(
    request_body=request_body,
    id_="id"
)

print(result)
```

## bulk_shared_server_information

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/SharedServerInformation/bulk`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SharedServerInformationBulkRequest](../models/SharedServerInformationBulkRequest.md) | ❌       | The request body. |

**Return Type**

`SharedServerInformationBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedServerInformationBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedServerInformationBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.shared_server_information.bulk_shared_server_information(request_body=request_body)

print(result)
```

