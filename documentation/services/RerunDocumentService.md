# RerunDocumentService

A list of all methods in the `RerunDocumentService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                        |
| :---------------------------------------------- | :----------------------------------------------------------------- |
| [create_rerun_document](#create_rerun_document) | Allows you to reprocess one or more documents from a previous run. |

## create_rerun_document

Allows you to reprocess one or more documents from a previous run.

- HTTP Method: `POST`
- Endpoint: `/RerunDocument`

**Parameters**

| Name         | Type                                        | Required | Description       |
| :----------- | :------------------------------------------ | :------- | :---------------- |
| request_body | [RerunDocument](../models/RerunDocument.md) | ❌       | The request body. |

**Return Type**

`RerunDocument`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RerunDocument

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RerunDocument(
    all_documents={
        "document_status": "ANY"
    },
    selected_documents={
        "document": [
            {
                "generic_connector_record_id": "genericConnectorRecordId"
            }
        ]
    },
    original_execution_id="originalExecutionId",
    record_url="recordUrl",
    request_id="requestId"
)

result = sdk.rerun_document.create_rerun_document(request_body=request_body)

print(result)
```

