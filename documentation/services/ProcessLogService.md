# ProcessLogService

A list of all methods in the `ProcessLogService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                |
| :---------------------------------------- | :------------------------- |
| [create_process_log](#create_process_log) | Download process run logs. |

## create_process_log

Download process run logs.

- HTTP Method: `POST`
- Endpoint: `/ProcessLog`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [ProcessLog](../models/ProcessLog.md) | ❌       | The request body. |

**Return Type**

`LogDownload`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessLog

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessLog(
    execution_id="execution-3456789a-bcde-f012-3456-789abcdef012-2015.01.01",
    log_level="SEVERE"
)

result = sdk.process_log.create_process_log(request_body=request_body)

print(result)
```

