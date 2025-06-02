# ConnectorDocumentService

A list of all methods in the `ConnectorDocumentService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                                                                            |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_connector_document](#create_connector_document) | The Connector Document operation allows you to download the raw, document data for a specific Generic Connector Record. This action submits the download request and the call returns a URL used to download the actual document data. |

## create_connector_document

The Connector Document operation allows you to download the raw, document data for a specific Generic Connector Record. This action submits the download request and the call returns a URL used to download the actual document data.

- HTTP Method: `POST`
- Endpoint: `/ConnectorDocument`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [ConnectorDocument](../models/ConnectorDocument.md) | ❌       | The request body. |

**Return Type**

`ConnectorDocumentDownload`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ConnectorDocument

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ConnectorDocument(
    generic_connector_record_id="genericConnectorRecordId"
)

result = sdk.connector_document.create_connector_document(request_body=request_body)

print(result)
```

