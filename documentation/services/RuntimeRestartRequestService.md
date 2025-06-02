# RuntimeRestartRequestService

A list of all methods in the `RuntimeRestartRequestService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_runtime_restart_request](#create_runtime_restart_request) | Restarts the runtime. - The client sends a runtime restart request to the platform API that specifies the runtimeId that you want to restart. - The platform returns the status code and message while the request is in progress. A successful response implies the restart request was submitted, not when the runtime restart is completed. |

## create_runtime_restart_request

Restarts the runtime. - The client sends a runtime restart request to the platform API that specifies the runtimeId that you want to restart. - The platform returns the status code and message while the request is in progress. A successful response implies the restart request was submitted, not when the runtime restart is completed.

- HTTP Method: `POST`
- Endpoint: `/RuntimeRestartRequest`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [RuntimeRestartRequest](../models/RuntimeRestartRequest.md) | ❌       | The request body. |

**Return Type**

`RuntimeRestartRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeRestartRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeRestartRequest(
    message="message",
    runtime_id="3456789a-bcde-f012-3456-789abcdef012"
)

result = sdk.runtime_restart_request.create_runtime_restart_request(request_body=request_body)

print(result)
```

