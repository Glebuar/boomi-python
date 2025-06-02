# IntegrationPackAtomAttachmentService

A list of all methods in the `IntegrationPackAtomAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                     | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_integration_pack_atom_attachment](#create_integration_pack_atom_attachment)         | Attaches an integration pack instance having the specified ID to the Runtime having the specified ID.                                                                                                                                           |
| [query_integration_pack_atom_attachment](#query_integration_pack_atom_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_integration_pack_atom_attachment](#query_more_integration_pack_atom_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |
| [delete_integration_pack_atom_attachment](#delete_integration_pack_atom_attachment)         | Detaches an integration pack instance from a Runtime, where the attachment is specified by the conceptual Integration Pack Atom Attachment object ID. This ID can be obtained from a QUERY operation.                                           |

## create_integration_pack_atom_attachment

Attaches an integration pack instance having the specified ID to the Runtime having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackAtomAttachment`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [IntegrationPackAtomAttachment](../models/IntegrationPackAtomAttachment.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackAtomAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackAtomAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackAtomAttachment(
    atom_id="3456789a-bcde-f012-3456-789abcdef012",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    integration_pack_instance_id="76543210FEDCBA9876543210FEDCBA98"
)

result = sdk.integration_pack_atom_attachment.create_integration_pack_atom_attachment(request_body=request_body)

print(result)
```

## query_integration_pack_atom_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackAtomAttachment/query`

**Parameters**

| Name         | Type                                                                                              | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [IntegrationPackAtomAttachmentQueryConfig](../models/IntegrationPackAtomAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`IntegrationPackAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import IntegrationPackAtomAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = IntegrationPackAtomAttachmentQueryConfig(
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

result = sdk.integration_pack_atom_attachment.query_integration_pack_atom_attachment(request_body=request_body)

print(result)
```

## query_more_integration_pack_atom_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/IntegrationPackAtomAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`IntegrationPackAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "reprehe"

result = sdk.integration_pack_atom_attachment.query_more_integration_pack_atom_attachment(request_body=request_body)

print(result)
```

## delete_integration_pack_atom_attachment

Detaches an integration pack instance from a Runtime, where the attachment is specified by the conceptual Integration Pack Atom Attachment object ID. This ID can be obtained from a QUERY operation.

- HTTP Method: `DELETE`
- Endpoint: `/IntegrationPackAtomAttachment/{id}`

**Parameters**

| Name | Type | Required | Description                                                                                          |
| :--- | :--- | :------- | :--------------------------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The object’s conceptual ID, which is synthesized from the Runtime and integration pack instance IDs. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.integration_pack_atom_attachment.delete_integration_pack_atom_attachment(id_="id")

print(result)
```

