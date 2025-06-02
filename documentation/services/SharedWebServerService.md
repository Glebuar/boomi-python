# SharedWebServerService

A list of all methods in the `SharedWebServerService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                 |
| :---------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_shared_web_server](#get_shared_web_server)       | Retrieves the details of a Shared Web Server configuration for this atom/cloud ID by its unique ID. The response can be in either XML or JSON format based on your request. |
| [update_shared_web_server](#update_shared_web_server) | Updates a Shared Web Server object based on the supplied Runtime ID.                                                                                                        |
| [bulk_shared_web_server](#bulk_shared_web_server)     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                      |

## get_shared_web_server

Retrieves the details of a Shared Web Server configuration for this atom/cloud ID by its unique ID. The response can be in either XML or JSON format based on your request.

- HTTP Method: `GET`
- Endpoint: `/SharedWebServer/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`SharedWebServer`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.shared_web_server.get_shared_web_server(id_="id")

print(result)
```

## update_shared_web_server

Updates a Shared Web Server object based on the supplied Runtime ID.

- HTTP Method: `POST`
- Endpoint: `/SharedWebServer/{id}`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [SharedWebServer](../models/SharedWebServer.md) | ❌       | The request body. |
| id\_         | str                                             | ✅       |                   |

**Return Type**

`SharedWebServer`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedWebServer

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedWebServer(
    atom_id="atomId",
    cloud_tennant_general={
        "api_type": "apiType",
        "auth_type": "authType",
        "base_url": "baseUrl",
        "listener_ports": {
            "port": [
                {
                    "auth_type": "authType",
                    "base_url_for_request": "baseUrlForRequest",
                    "default_port": True,
                    "enable_port": False,
                    "external_port": 6,
                    "external_ssl": True,
                    "port": 2,
                    "ssl": False
                }
            ]
        }
    },
    cors_configuration={
        "origins": [
            {
                "enable_http_request_handling": False,
                "enable_https_request_handling": True,
                "allow_credentials": True,
                "allow_methods": [
                    "allowMethods"
                ],
                "allow_request_headers": [
                    "allowRequestHeaders"
                ],
                "allow_response_headers": [
                    "allowResponseHeaders"
                ],
                "cache_timeout": 1,
                "domain": "domain",
                "ports": [
                    8
                ]
            }
        ]
    },
    general_settings={
        "api_type": "apiType",
        "authentication": {
            "auth_type": "authType",
            "cache_authentication_timeout": 6,
            "cache_authorization_credentials": False,
            "client_certificate_header_name": "clientCertificateHeaderName",
            "login_module_class_name": "loginModuleClassName",
            "login_module_options": {
                "login_module": [
                    {
                        "encrypt": False,
                        "name": "name",
                        "value": "value"
                    }
                ]
            }
        },
        "base_url": "baseUrl",
        "examine_forward_headers": True,
        "external_host": "externalHost",
        "internal_host": "internalHost",
        "listener_ports": {
            "port": [
                {
                    "auth_type": "authType",
                    "base_url_for_request": "baseUrlForRequest",
                    "default_port": True,
                    "enable_port": False,
                    "external_port": 6,
                    "external_ssl": True,
                    "port": 2,
                    "ssl": False
                }
            ]
        },
        "max_number_of_threads": 5,
        "override_url": False,
        "protected_headers": {
            "header": [
                "header"
            ]
        },
        "ssl_certificate": "sslCertificate"
    },
    should_restart_plugin=True,
    user_management={
        "enable_apim_internal_roles": False,
        "users": [
            {
                "client_certificate": "clientCertificate",
                "component_filters": [
                    "componentFilters"
                ],
                "external_username": "externalUsername",
                "ip_filters": [
                    "ipFilters"
                ],
                "role_associations": [
                    "roleAssociations"
                ],
                "token": "token",
                "username": "username",
                "using_component_filters": True,
                "using_ip_filters": False
            }
        ]
    }
)

result = sdk.shared_web_server.update_shared_web_server(
    request_body=request_body,
    id_="id"
)

print(result)
```

## bulk_shared_web_server

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/SharedWebServer/bulk`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SharedWebServerBulkRequest](../models/SharedWebServerBulkRequest.md) | ❌       | The request body. |

**Return Type**

`SharedWebServerBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedWebServerBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedWebServerBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.shared_web_server.bulk_shared_web_server(request_body=request_body)

print(result)
```

