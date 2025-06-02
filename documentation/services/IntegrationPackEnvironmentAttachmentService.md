# IntegrationPackEnvironmentAttachmentService

A list of all methods in the `IntegrationPackEnvironmentAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                   | Description                                                                                                                                                                                                                                                       |
| :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_integration_pack_environment_attachment](#create_integration_pack_environment_attachment)         | Attaches an integration pack instance having the specified ID to the environment having the specified ID.                                                                                                                                                         |
| [query_integration_pack_environment_attachment](#query_integration_pack_environment_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                   |
| [query_more_integration_pack_environment_attachment](#query_more_integration_pack_environment_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                    |
| [delete_integration_pack_environment_attachment](#delete_integration_pack_environment_attachment)         | Detaches an integration pack instance from an environment where the conceptual Integration Pack Environment Attachment object ID specifies the attachment. If you successfully detach the integration pack instance from the environment, the response is `true`. |

## create_integration_pack_environment_attachment

Attaches an integration pack instance having the specified ID to the environment having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackEnvironmentAttachment`

**Parameters**

| Name         | Type                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IntegrationPackEnvironmentAttachment](../models/IntegrationPackEnvironmentAttachment.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackEnvironmentAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackEnvironmentAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackEnvironmentAttachment(
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    integration_pack_instance_id="76543210-fedc-ba98-7654-3210fedcba98"
)

result = sdk.integration_pack_environment_attachment.create_integration_pack_environment_attachment(request_body=request_body)

print(result)
```

## query_integration_pack_environment_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackEnvironmentAttachment/query`

**Parameters**

| Name         | Type                                                                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IntegrationPackEnvironmentAttachmentQueryConfig](../models/IntegrationPackEnvironmentAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackEnvironmentAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackEnvironmentAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackEnvironmentAttachmentQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "environmentId"
        }
    }
)

result = sdk.integration_pack_environment_attachment.query_integration_pack_environment_attachment(request_body=request_body)

print(result)
```

## query_more_integration_pack_environment_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackEnvironmentAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`IntegrationPackEnvironmentAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "doLorem sed"

result = sdk.integration_pack_environment_attachment.query_more_integration_pack_environment_attachment(request_body=request_body)

print(result)
```

## delete_integration_pack_environment_attachment

Detaches an integration pack instance from an environment where the conceptual Integration Pack Environment Attachment object ID specifies the attachment. If you successfully detach the integration pack instance from the environment, the response is `true`.

- HTTP Method: `DELETE`
- Endpoint: `/IntegrationPackEnvironmentAttachment/{id}`

**Parameters**

| Name | Type | Required | Description                                                      |
| :--- | :--- | :------- | :--------------------------------------------------------------- |
| id\_ | str  | ✅       | The conceptual Integration Pack Environment Attachment object ID |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.integration_pack_environment_attachment.delete_integration_pack_environment_attachment(id_="id")

print(result)
```

