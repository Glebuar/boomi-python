# AtomWorkerLogService

A list of all methods in the `AtomWorkerLogService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                   |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| [create_atom_worker_log](#create_atom_worker_log) | Allows users to programmatically retrieve a link for downloading a given Runtime workers log. |

## create_atom_worker_log

Allows users to programmatically retrieve a link for downloading a given Runtime workers log.

- HTTP Method: `POST`
- Endpoint: `/AtomWorkerLog`

**Parameters**

| Name         | Type                                        | Required | Description       |
| :----------- | :------------------------------------------ | :------- | :---------------- |
| request_body | [AtomWorkerLog](../models/AtomWorkerLog.md) | ❌       | The request body. |

**Return Type**

`LogDownload`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AtomWorkerLog

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AtomWorkerLog(
    worker_id="workerId"
)

result = sdk.atom_worker_log.create_atom_worker_log(request_body=request_body)

print(result)
```

