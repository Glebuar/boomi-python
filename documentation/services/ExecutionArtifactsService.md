# ExecutionArtifactsService

A list of all methods in the `ExecutionArtifactsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_execution_artifacts](#create_execution_artifacts) | Allows you to retrieve a link for downloading detailed information about a given process run. - You must have the Runtime Management privilege to perform the CREATE operation. If you have the Runtime Management Read Access privilege, you cannot download execution artifacts. - Additionally, as the Cloud owner, you must select the **Enable Download of Execution Artifacts and Worker Logs** property for your account. This property permits you to download process execution data, and you can access it from the Cloud Attachment Quota tab of Manage \> Cloud Management. - After providing the endpoint and a request body containing the execution ID, the CREATE response returns a download URL that you can open (or copy and paste) in your web browser, which initiates the file download to your local drive. To retrieve the download link for file containing a process execution artifacts, 1. First create a CREATE (or POST) request to `https://api.boomi.com/api/rest/v1/\<accountId\>/ExecutionArtifacts` where `accountId` is the ID of the account authenticating the request. 2. Populate the request body with the `executionId`, which is the identifier of the given run process. 3. Send the request and either open or copy and paste the URL from the response into your web browser. |

## create_execution_artifacts

Allows you to retrieve a link for downloading detailed information about a given process run. - You must have the Runtime Management privilege to perform the CREATE operation. If you have the Runtime Management Read Access privilege, you cannot download execution artifacts. - Additionally, as the Cloud owner, you must select the **Enable Download of Execution Artifacts and Worker Logs** property for your account. This property permits you to download process execution data, and you can access it from the Cloud Attachment Quota tab of Manage \> Cloud Management. - After providing the endpoint and a request body containing the execution ID, the CREATE response returns a download URL that you can open (or copy and paste) in your web browser, which initiates the file download to your local drive. To retrieve the download link for file containing a process execution artifacts, 1. First create a CREATE (or POST) request to `https://api.boomi.com/api/rest/v1/\<accountId\>/ExecutionArtifacts` where `accountId` is the ID of the account authenticating the request. 2. Populate the request body with the `executionId`, which is the identifier of the given run process. 3. Send the request and either open or copy and paste the URL from the response into your web browser.

- HTTP Method: `POST`
- Endpoint: `/ExecutionArtifacts`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [ExecutionArtifacts](../models/ExecutionArtifacts.md) | ❌       | The request body. |

**Return Type**

`ExecutionArtifacts`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ExecutionArtifacts

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ExecutionArtifacts(
    execution_id="executionId"
)

result = sdk.execution_artifacts.create_execution_artifacts(request_body=request_body)

print(result)
```

