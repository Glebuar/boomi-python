# RefreshSecretsManagerService

A list of all methods in the `RefreshSecretsManagerService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description |
| :-------------------------------------------------- | :---------- |
| [refresh_secrets_manager](#refresh_secrets_manager) |             |

## refresh_secrets_manager

- HTTP Method: `POST`
- Endpoint: `/refreshSecretsManager`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SecretsManagerRefreshRequest](../models/SecretsManagerRefreshRequest.md) | ❌       | The request body. |

**Return Type**

`SecretsManagerRefreshResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SecretsManagerRefreshRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SecretsManagerRefreshRequest(
    provider="AWS"
)

result = sdk.refresh_secrets_manager.refresh_secrets_manager(request_body=request_body)

print(result)
```

