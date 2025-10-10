# AccountSsoConfigService

A list of all methods in the `AccountSsoConfigService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                            |
| :------------------------------------------------------ | :----------------------------------------------------------------------------------------------------- |
| [get_account_sso_config](#get_account_sso_config)       | Returns the Account Single Sign-on Configuration for the supplied account ID.                          |
| [update_account_sso_config](#update_account_sso_config) | Updates the Account Single Sign-on Configuration for the supplied account ID.                          |
| [delete_account_sso_config](#delete_account_sso_config) | Deletes the Account Single Sign-on Configuration for the supplied account ID.                          |
| [bulk_account_sso_config](#bulk_account_sso_config)     | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations). |

## get_account_sso_config

Returns the Account Single Sign-on Configuration for the supplied account ID.

- HTTP Method: `GET`
- Endpoint: `/AccountSSOConfig/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AccountSsoConfig`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_sso_config.get_account_sso_config(id_="id")

print(result)
```

## update_account_sso_config

Updates the Account Single Sign-on Configuration for the supplied account ID.

- HTTP Method: `POST`
- Endpoint: `/AccountSSOConfig/{id}`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [AccountSsoConfig](../models/AccountSsoConfig.md) | ❌       | The request body. |
| id\_         | str                                               | ✅       |                   |

**Return Type**

`AccountSsoConfig`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountSsoConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountSsoConfig(
    account_id="accountId",
    assertion_encryption=False,
    authn_context="authnContext",
    authn_context_comparison="authnContextComparison",
    cert_info="certInfo",
    certificate=[
        "certificate"
    ],
    enabled=True,
    fed_id_from_name_id=True,
    idp_url="idpUrl",
    name_id_policy="nameIdPolicy",
    signout_redirect_url="signoutRedirectUrl"
)

result = sdk.account_sso_config.update_account_sso_config(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_account_sso_config

Deletes the Account Single Sign-on Configuration for the supplied account ID.

- HTTP Method: `DELETE`
- Endpoint: `/AccountSSOConfig/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_sso_config.delete_account_sso_config(id_="id")

print(result)
```

## bulk_account_sso_config

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AccountSSOConfig/bulk`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountSsoConfigBulkRequest](../models/AccountSsoConfigBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AccountSsoConfigBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountSsoConfigBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountSsoConfigBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.account_sso_config.bulk_account_sso_config(request_body=request_body)

print(result)
```

