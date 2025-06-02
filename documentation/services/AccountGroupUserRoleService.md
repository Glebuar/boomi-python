# AccountGroupUserRoleService

A list of all methods in the `AccountGroupUserRoleService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_account_group_user_role](#create_account_group_user_role)         | Adds a user to an account group.                                                                                                                                                                                                                |
| [query_account_group_user_role](#query_account_group_user_role)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_account_group_user_role](#query_more_account_group_user_role) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |
| [delete_account_group_user_role](#delete_account_group_user_role)         | Removes the user from an account group specified by the conceptual Account Group User Role object ID.                                                                                                                                           |

## create_account_group_user_role

Adds a user to an account group.

- HTTP Method: `POST`
- Endpoint: `/AccountGroupUserRole`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupUserRole](../models/AccountGroupUserRole.md) | ❌       | The request body. |

**Return Type**

`AccountGroupUserRole`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupUserRole

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupUserRole(
    account_group_id="fedcba98-7654-3210-fedc-ba9876543c210",
    first_name="John",
    id_="Ab0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1Hg",
    last_name="Doe",
    notify_user=True,
    role_id="01234567-89ab-cdef-0123-456789abcdef",
    user_id="user123company.biz"
)

result = sdk.account_group_user_role.create_account_group_user_role(request_body=request_body)

print(result)
```

## query_account_group_user_role

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroupUserRole/query`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [AccountGroupUserRoleQueryConfig](../models/AccountGroupUserRoleQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AccountGroupUserRoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupUserRoleQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupUserRoleQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "accountGroupId"
        }
    }
)

result = sdk.account_group_user_role.query_account_group_user_role(request_body=request_body)

print(result)
```

## query_more_account_group_user_role

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroupUserRole/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountGroupUserRoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "laborum c"

result = sdk.account_group_user_role.query_more_account_group_user_role(request_body=request_body)

print(result)
```

## delete_account_group_user_role

Removes the user from an account group specified by the conceptual Account Group User Role object ID.

- HTTP Method: `DELETE`
- Endpoint: `/AccountGroupUserRole/{id}`

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

result = sdk.account_group_user_role.delete_account_group_user_role(id_="id")

print(result)
```

