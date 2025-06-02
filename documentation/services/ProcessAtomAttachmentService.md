# ProcessAtomAttachmentService

A list of all methods in the `ProcessAtomAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_process_atom_attachment](#create_process_atom_attachment)         | Attaches a process having the specified ID to the Runtime having the specified ID.                                                                                                                                                              |
| [query_process_atom_attachment](#query_process_atom_attachment)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_process_atom_attachment](#query_more_process_atom_attachment) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |
| [delete_process_atom_attachment](#delete_process_atom_attachment)         | Detaches a process from a Runtime where the attachment is specified by the conceptual Process Atom Attachment object ID.                                                                                                                        |

## create_process_atom_attachment

Attaches a process having the specified ID to the Runtime having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/ProcessAtomAttachment`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessAtomAttachment](../models/ProcessAtomAttachment.md) | ❌       | The request body. |

**Return Type**

`ProcessAtomAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessAtomAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessAtomAttachment(
    atom_id="atomId",
    component_type="componentType",
    id_="id",
    process_id="processId"
)

result = sdk.process_atom_attachment.create_process_atom_attachment(request_body=request_body)

print(result)
```

## query_process_atom_attachment

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessAtomAttachment/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ProcessAtomAttachmentQueryConfig](../models/ProcessAtomAttachmentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`ProcessAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessAtomAttachmentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessAtomAttachmentQueryConfig(
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

result = sdk.process_atom_attachment.query_process_atom_attachment(request_body=request_body)

print(result)
```

## query_more_process_atom_attachment

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/ProcessAtomAttachment/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`ProcessAtomAttachmentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "cillu"

result = sdk.process_atom_attachment.query_more_process_atom_attachment(request_body=request_body)

print(result)
```

## delete_process_atom_attachment

Detaches a process from a Runtime where the attachment is specified by the conceptual Process Atom Attachment object ID.

- HTTP Method: `DELETE`
- Endpoint: `/ProcessAtomAttachment/{id}`

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

result = sdk.process_atom_attachment.delete_process_atom_attachment(id_="id")

print(result)
```

