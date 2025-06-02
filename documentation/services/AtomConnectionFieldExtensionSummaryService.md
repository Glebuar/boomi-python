# AtomConnectionFieldExtensionSummaryService

A list of all methods in the `AtomConnectionFieldExtensionSummaryService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_atom_connection_field_extension_summary](#query_atom_connection_field_extension_summary)           | All filters are required except for `extensionGroupId`, which is required only for a multi-install integration pack. You can obtain valid values for each filter by using the QUERY operation on the Atom Extensions object. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_atom_connection_field_extension_summary](#query_more_atom_connection_field_extension_summary) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                               |

## query_atom_connection_field_extension_summary

All filters are required except for `extensionGroupId`, which is required only for a multi-install integration pack. You can obtain valid values for each filter by using the QUERY operation on the Atom Extensions object. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AtomConnectionFieldExtensionSummary/query`

**Parameters**

| Name         | Type                                                                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [AtomConnectionFieldExtensionSummaryQueryConfig](../models/AtomConnectionFieldExtensionSummaryQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AtomConnectionFieldExtensionSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomConnectionFieldExtensionSummaryQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomConnectionFieldExtensionSummaryQueryConfig(
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

result = sdk.atom_connection_field_extension_summary.query_atom_connection_field_extension_summary(request_body=request_body)

print(result)
```

## query_more_atom_connection_field_extension_summary

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AtomConnectionFieldExtensionSummary/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AtomConnectionFieldExtensionSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "cupidatat"

result = sdk.atom_connection_field_extension_summary.query_more_atom_connection_field_extension_summary(request_body=request_body)

print(result)
```

