# AtomAs2ArtifactsService

A list of all methods in the `AtomAs2ArtifactsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                      |
| :------------------------------------------------------ | :----------------------------------------------------------------------------------------------- |
| [create_atom_as2_artifacts](#create_atom_as2_artifacts) | You can use the Download AS2 Artifacts Log operation to request and download AS2 artifacts logs. |

## create_atom_as2_artifacts

You can use the Download AS2 Artifacts Log operation to request and download AS2 artifacts logs.

- HTTP Method: `POST`
- Endpoint: `/AtomAS2Artifacts`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [AtomAs2Artifacts](../models/AtomAs2Artifacts.md) | ❌       | The request body. |

**Return Type**

`LogDownload`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomAs2Artifacts

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomAs2Artifacts(
    atom_id="3456789a-bcde-f012-3456-789abcdef012",
    log_date="2016-02-05"
)

result = sdk.atom_as2_artifacts.create_atom_as2_artifacts(request_body=request_body)

print(result)
```

