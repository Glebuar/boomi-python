# ComponentAtomAttachmentService

A list of all methods in the `ComponentAtomAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_component_atom_attachment](#create_component_atom_attachment)         | Attaches a component with a specific ID to the Runtime with a specific ID. You must have the Runtime Management privilege to perform the CREATE operation. If you have the Runtime Management Read Access privilege, you cannot attach components.                                                                                       |
| [query_component_atom_attachment](#query_component_atom_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                          |
| [query_more_component_atom_attachment](#query_more_component_atom_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                           |
| [delete_component_atom_attachment](#delete_component_atom_attachment)         | Detaches a component from a Runtime where the attachment is specified by the conceptual Component Atom Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. You must have the Runtime Management privilege to perform the DELETE operation. |

## create_component_atom_attachment

Attaches a component with a specific ID to the Runtime with a specific ID. You must have the Runtime Management privilege to perform the CREATE operation. If you have the Runtime Management Read Access privilege, you cannot attach components.

- HTTP Method: `POST`
- Endpoint: `/ComponentAtomAttachment`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentAtomAttachment](../models/ComponentAtomAttachment.md) | ❌       | The request body. |

**Return Type**

`ComponentAtomAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentAtomAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentAtomAttachment(
    atom_id="3456789a-bcde-f012-3456-789abcdef012",
    component_id="56789abc-def0-1234-5678-9abcdef01234",
    component_type="process",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg"
)

result = sdk.component_atom_attachment.create_component_atom_attachment(request_body=request_body)

print(result)
```

## query_component_atom_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentAtomAttachment/query`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ComponentAtomAttachmentQueryConfig](../models/ComponentAtomAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ComponentAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentAtomAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ComponentAtomAttachmentQueryConfig(
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

result = sdk.component_atom_attachment.query_component_atom_attachment(request_body=request_body)

print(result)
```

## query_more_component_atom_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ComponentAtomAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ComponentAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolore ip"

result = sdk.component_atom_attachment.query_more_component_atom_attachment(request_body=request_body)

print(result)
```

## delete_component_atom_attachment

Detaches a component from a Runtime where the attachment is specified by the conceptual Component Atom Attachment object ID. This ID is returned by the CREATE operation that originated the attachment and can also be obtained from a QUERY operation. You must have the Runtime Management privilege to perform the DELETE operation.

- HTTP Method: `DELETE`
- Endpoint: `/ComponentAtomAttachment/{id}`

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

result = sdk.component_atom_attachment.delete_component_atom_attachment(id_="id")

print(result)
```

