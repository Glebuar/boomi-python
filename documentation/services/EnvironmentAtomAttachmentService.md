# EnvironmentAtomAttachmentService

A list of all methods in the `EnvironmentAtomAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_environment_atom_attachment](#create_environment_atom_attachment)         | Attaches a Runtime having the specified ID to the environment having the specified ID. Attaching an already attached Runtime moves the Runtime to the environment specified in the request. \>**Note:** For accounts with Basic environment support, you can attach a single Runtime to each environment. For accounts with Unlimited environment support, you can attach have an unlimited number of Runtimes attached in each environment. |
| [query_environment_atom_attachment](#query_environment_atom_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                              |
| [query_more_environment_atom_attachment](#query_more_environment_atom_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                               |
| [delete_environment_atom_attachment](#delete_environment_atom_attachment)         | Detaches a Runtime from an environment where the attachment is specified by the conceptual Environment Atom Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. If you successfully detach the Runtime from the environment, the response is `\<true/\>`.                                                                                      |

## create_environment_atom_attachment

Attaches a Runtime having the specified ID to the environment having the specified ID. Attaching an already attached Runtime moves the Runtime to the environment specified in the request. \>**Note:** For accounts with Basic environment support, you can attach a single Runtime to each environment. For accounts with Unlimited environment support, you can attach have an unlimited number of Runtimes attached in each environment.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentAtomAttachment`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [EnvironmentAtomAttachment](../models/EnvironmentAtomAttachment.md) | ❌       | The request body. |

**Return Type**

`EnvironmentAtomAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentAtomAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentAtomAttachment(
    atom_id="3456789a-bcde-f012-3456-789abcdef012",
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg"
)

result = sdk.environment_atom_attachment.create_environment_atom_attachment(request_body=request_body)

print(result)
```

## query_environment_atom_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentAtomAttachment/query`

**Parameters**

| Name         | Type                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentAtomAttachmentQueryConfig](../models/EnvironmentAtomAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentAtomAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentAtomAttachmentQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "atomId"
        }
    }
)

result = sdk.environment_atom_attachment.query_environment_atom_attachment(request_body=request_body)

print(result)
```

## query_more_environment_atom_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentAtomAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "labore "

result = sdk.environment_atom_attachment.query_more_environment_atom_attachment(request_body=request_body)

print(result)
```

## delete_environment_atom_attachment

Detaches a Runtime from an environment where the attachment is specified by the conceptual Environment Atom Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. If you successfully detach the Runtime from the environment, the response is `\<true/\>`.

- HTTP Method: `DELETE`
- Endpoint: `/EnvironmentAtomAttachment/{id}`

**Parameters**

| Name | Type | Required | Description                                                                            |
| :--- | :--- | :------- | :------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The object’s conceptual ID, which is synthesized from the Runtime and environment IDs. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_atom_attachment.delete_environment_atom_attachment(id_="id")

print(result)
```

