# ProcessEnvironmentAttachmentService

A list of all methods in the `ProcessEnvironmentAttachmentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                            |
| :------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------- |
| [create_process_environment_attachment](#create_process_environment_attachment) | Attaches a process having the specified ID to the environment having the specified ID. |

## create_process_environment_attachment

Attaches a process having the specified ID to the environment having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/ProcessEnvironmentAttachment`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ProcessEnvironmentAttachment](../models/ProcessEnvironmentAttachment.md) | ❌       | The request body. |

**Return Type**

`ProcessEnvironmentAttachment`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ProcessEnvironmentAttachment

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ProcessEnvironmentAttachment(
    component_type="process",
    environment_id="456789ab-cdef-0123-4567-89abcdef0123",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    process_id="56789abc-def0-1234-5678-9abcdef01234"
)

result = sdk.process_environment_attachment.create_process_environment_attachment(request_body=request_body)

print(result)
```

