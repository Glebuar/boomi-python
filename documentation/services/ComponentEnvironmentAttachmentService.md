# ComponentEnvironmentAttachmentService

A list of all methods in the `ComponentEnvironmentAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                     | Description                                                                                                                                                                                                                                                          |
| :------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_component_environment_attachment](#create_component_environment_attachment)         | Attaches a component with a specific ID to the environment with a specific ID.                                                                                                                                                                                       |
| [query_component_environment_attachment](#query_component_environment_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                      |
| [query_more_component_environment_attachment](#query_more_component_environment_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                       |
| [delete_component_environment_attachment](#delete_component_environment_attachment)         | Detaches a component from an environment where the attachment is specified by the conceptual Component Environment Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. |

## create_component_environment_attachment

Attaches a component with a specific ID to the environment with a specific ID.

- HTTP Method: `POST`
- Endpoint: `/ComponentEnvironmentAttachment`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentEnvironmentAttachment](../models/ComponentEnvironmentAttachment.md) | ❌       | The request body. |

**Return Type**

`ComponentEnvironmentAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentEnvironmentAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentEnvironmentAttachment(
    component_id="56789abc-def0-1234-5678-9abcdef01234",
    component_type="process",
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg"
)

result = sdk.component_environment_attachment.create_component_environment_attachment(request_body=request_body)

print(result)
```

## query_component_environment_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentEnvironmentAttachment/query`

**Parameters**

| Name         | Type                                                                                                | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentEnvironmentAttachmentQueryConfig](../models/ComponentEnvironmentAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ComponentEnvironmentAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentEnvironmentAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentEnvironmentAttachmentQueryConfig(
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

result = sdk.component_environment_attachment.query_component_environment_attachment(request_body=request_body)

print(result)
```

## query_more_component_environment_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentEnvironmentAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ComponentEnvironmentAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "reprehenderit"

result = sdk.component_environment_attachment.query_more_component_environment_attachment(request_body=request_body)

print(result)
```

## delete_component_environment_attachment

Detaches a component from an environment where the attachment is specified by the conceptual Component Environment Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation.

- HTTP Method: `DELETE`
- Endpoint: `/ComponentEnvironmentAttachment/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.component_environment_attachment.delete_component_environment_attachment(id_="id")

print(result)
```

