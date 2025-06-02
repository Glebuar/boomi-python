# AccountUserFederationService

A list of all methods in the `AccountUserFederationService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_account_user_federation](#create_account_user_federation)         | Enables single sign-on for a specific user under a specific account using a specific federation ID. The user is not visible in the Setup page unless you assign one or more roles to that user.                                                 |
| [query_account_user_federation](#query_account_user_federation)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_account_user_federation](#query_more_account_user_federation) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |
| [update_account_user_federation](#update_account_user_federation)         | Updates the federation ID of a specific user in a specific account.                                                                                                                                                                             |
| [delete_account_user_federation](#delete_account_user_federation)         | Disables single sign-on for the user specified by the conceptual Account User Federation object ID.                                                                                                                                             |

## create_account_user_federation

Enables single sign-on for a specific user under a specific account using a specific federation ID. The user is not visible in the Setup page unless you assign one or more roles to that user.

- HTTP Method: `POST`
- Endpoint: `/AccountUserFederation`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountUserFederation](../models/AccountUserFederation.md) | ❌       | The request body. |

**Return Type**

`AccountUserFederation`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountUserFederation

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountUserFederation(
    account_id="account-123456",
    federation_id="user123",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts",
    user_id="user123company.biz"
)

result = sdk.account_user_federation.create_account_user_federation(request_body=request_body)

print(result)
```

## query_account_user_federation

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountUserFederation/query`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountUserFederationQueryConfig](../models/AccountUserFederationQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AccountUserFederationQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountUserFederationQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountUserFederationQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "accountId"
        }
    }
)

result = sdk.account_user_federation.query_account_user_federation(request_body=request_body)

print(result)
```

## query_more_account_user_federation

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountUserFederation/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountUserFederationQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "elit "

result = sdk.account_user_federation.query_more_account_user_federation(request_body=request_body)

print(result)
```

## update_account_user_federation

Updates the federation ID of a specific user in a specific account.

- HTTP Method: `POST`
- Endpoint: `/AccountUserFederation/{id}`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountUserFederation](../models/AccountUserFederation.md) | ❌       | The request body. |
| id\_         | str                                                         | ✅       |                   |

**Return Type**

`AccountUserFederation`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountUserFederation

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountUserFederation(
    account_id="account-123456",
    federation_id="user123",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts",
    user_id="user123company.biz"
)

result = sdk.account_user_federation.update_account_user_federation(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_account_user_federation

Disables single sign-on for the user specified by the conceptual Account User Federation object ID.

- HTTP Method: `DELETE`
- Endpoint: `/AccountUserFederation/{id}`

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

result = sdk.account_user_federation.delete_account_user_federation(id_="id")

print(result)
```

