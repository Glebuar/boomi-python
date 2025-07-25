# DocumentCountAccountGroupService

A list of all methods in the `DocumentCountAccountGroupService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_document_count_account_group](#query_document_count_account_group)           | - You can use the EQUALS operator only with the `accountGroupId` filter parameter. - The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_document_count_account_group](#query_more_document_count_account_group) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                        |

## query_document_count_account_group

- You can use the EQUALS operator only with the `accountGroupId` filter parameter. - The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DocumentCountAccountGroup/query`

**Parameters**

| Name         | Type                                                                                      | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [DocumentCountAccountGroupQueryConfig](../models/DocumentCountAccountGroupQueryConfig.md) | ❌       | The request body. |

**Return Type**

`DocumentCountAccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DocumentCountAccountGroupQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DocumentCountAccountGroupQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "accountGroupId"
        }
    }
)

result = sdk.document_count_account_group.query_document_count_account_group(request_body=request_body)

print(result)
```

## query_more_document_count_account_group

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DocumentCountAccountGroup/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`DocumentCountAccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "velit laborum"

result = sdk.document_count_account_group.query_more_document_count_account_group(request_body=request_body)

print(result)
```

