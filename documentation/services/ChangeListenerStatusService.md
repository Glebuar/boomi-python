# ChangeListenerStatusService

A list of all methods in the `ChangeListenerStatusService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                                                                                                                                                                        |
| :-------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_change_listener_status](#create_change_listener_status) | You can use the changeListenerStatus operation to pause, resume, or restart listeners. A successful changeListenerStatus call returns an empty changeListenerStatusResponse to indicate acceptance of the request. |

## create_change_listener_status

You can use the changeListenerStatus operation to pause, resume, or restart listeners. A successful changeListenerStatus call returns an empty changeListenerStatusResponse to indicate acceptance of the request.

- HTTP Method: `POST`
- Endpoint: `/ChangeListenerStatus`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ChangeListenerStatusRequest](../models/ChangeListenerStatusRequest.md) | ❌       | The request body. |

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ChangeListenerStatusRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ChangeListenerStatusRequest(
    action="restart",
    container_id="containerId",
    listener_id="listenerId"
)

result = sdk.change_listener_status.create_change_listener_status(request_body=request_body)

print(result)
```

