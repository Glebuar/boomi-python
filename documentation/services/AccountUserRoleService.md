# AccountUserRoleService

A list of all methods in the `AccountUserRoleService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_account_user_role](#create_account_user_role)         | Adds a user to an account. If you provide a user ID (email address) that does not exist, the system creates the user and adds them to the account. When creating a new user, the API request does not require the firstName and lastName fields. If you do not provide those fields, it assigns the default firstName or lastName values automatically. If you include the firstName and lastName fields in a CREATE request for a user name that exists, the request ignores those fields. |
| [query_account_user_role](#query_account_user_role)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                             |
| [query_more_account_user_role](#query_more_account_user_role) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                              |
| [delete_account_user_role](#delete_account_user_role)         | Removes the specified user by a specified conceptual Account User Role object ID from an account.                                                                                                                                                                                                                                                                                                                                                                                           |

## create_account_user_role

Adds a user to an account. If you provide a user ID (email address) that does not exist, the system creates the user and adds them to the account. When creating a new user, the API request does not require the firstName and lastName fields. If you do not provide those fields, it assigns the default firstName or lastName values automatically. If you include the firstName and lastName fields in a CREATE request for a user name that exists, the request ignores those fields.

- HTTP Method: `POST`
- Endpoint: `/AccountUserRole`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [AccountUserRole](../models/AccountUserRole.md) | ❌       | The request body. |

**Return Type**

`AccountUserRole`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountUserRole

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountUserRole(
    account_id="account-123456",
    first_name="John",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    last_name="Doe",
    notify_user=False,
    role_id="01234567-89ab-cdef-0123-456789abcdef",
    user_id="user123company.biz"
)

result = sdk.account_user_role.create_account_user_role(request_body=request_body)

print(result)
```

## query_account_user_role

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountUserRole/query`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountUserRoleQueryConfig](../models/AccountUserRoleQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AccountUserRoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountUserRoleQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountUserRoleQueryConfig(
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

result = sdk.account_user_role.query_account_user_role(request_body=request_body)

print(result)
```

## query_more_account_user_role

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountUserRole/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountUserRoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "dolore"

result = sdk.account_user_role.query_more_account_user_role(request_body=request_body)

print(result)
```

## delete_account_user_role

Removes the specified user by a specified conceptual Account User Role object ID from an account.

- HTTP Method: `DELETE`
- Endpoint: `/AccountUserRole/{id}`

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

result = sdk.account_user_role.delete_account_user_role(id_="id")

print(result)
```

