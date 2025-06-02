# DocumentCountAccountService

A list of all methods in the `DocumentCountAccountService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                                                                                      |
| :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [query_document_count_account](#query_document_count_account)           | The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_document_count_account](#query_more_document_count_account) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                   |

## query_document_count_account

The authenticating user for a QUERY operation must have the Dashboard privilege. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DocumentCountAccount/query`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [DocumentCountAccountQueryConfig](../models/DocumentCountAccountQueryConfig.md) | ❌       | The request body. |

**Return Type**

`DocumentCountAccountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import DocumentCountAccountQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = DocumentCountAccountQueryConfig(
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

result = sdk.document_count_account.query_document_count_account(request_body=request_body)

print(result)
```

## query_more_document_count_account

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/DocumentCountAccount/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`DocumentCountAccountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolor L"

result = sdk.document_count_account.query_more_document_count_account(request_body=request_body)

print(result)
```

