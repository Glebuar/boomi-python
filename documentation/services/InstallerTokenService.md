# InstallerTokenService

A list of all methods in the `InstallerTokenService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                   |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| [create_installer_token](#create_installer_token) | Creates an installer token of a specific type that is valid for a specific number of minutes. |

## create_installer_token

Creates an installer token of a specific type that is valid for a specific number of minutes.

- HTTP Method: `POST`
- Endpoint: `/InstallerToken`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [InstallerToken](../models/InstallerToken.md) | ❌       | The request body. |

**Return Type**

`InstallerToken`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import InstallerToken

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = InstallerToken(
    account_id="fakeAccountId",
    cloud_id="cloudId",
    created="2017-02-07T22:31:10.136Z",
    duration_minutes=9,
    expiration="2017-02-07T23:01:10.136Z",
    install_type="CLOUD",
    token="molecule-45aa1e3c-499a-4405-9869-51c1914cdfb9"
)

result = sdk.installer_token.create_installer_token(request_body=request_body)

print(result)
```

