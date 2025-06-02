# AccountGroupAccountService

A list of all methods in the `AccountGroupAccountService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_account_group_account](#create_account_group_account)         | Adds an account to an account group.                                                                                                                                                                                                            |
| [query_account_group_account](#query_account_group_account)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_account_group_account](#query_more_account_group_account) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |
| [delete_account_group_account](#delete_account_group_account)         | Removes an account from an account group.                                                                                                                                                                                                       |

## create_account_group_account

Adds an account to an account group.

- HTTP Method: `POST`
- Endpoint: `/AccountGroupAccount`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [AccountGroupAccount](../models/AccountGroupAccount.md) | ❌       | The request body. |

**Return Type**

`AccountGroupAccount`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupAccount

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupAccount(
    account_group_id="fedcba98-7654-3210-fedc-ba9876543c210",
    account_id="account-123456",
    id_="gAb0Cd1Ef1Gh3Ij4Kl5Mn6Op7Qr8St9Uv0Wx9Yz8Zy7Xw6Vu5Ts4Rq3Po2Nm1Lk0Ji1H"
)

result = sdk.account_group_account.create_account_group_account(request_body=request_body)

print(result)
```

## query_account_group_account

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroupAccount/query`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupAccountQueryConfig](../models/AccountGroupAccountQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AccountGroupAccountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupAccountQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupAccountQueryConfig(
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

result = sdk.account_group_account.query_account_group_account(request_body=request_body)

print(result)
```

## query_more_account_group_account

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroupAccount/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountGroupAccountQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "cupid"

result = sdk.account_group_account.query_more_account_group_account(request_body=request_body)

print(result)
```

## delete_account_group_account

Removes an account from an account group.

- HTTP Method: `DELETE`
- Endpoint: `/AccountGroupAccount/{id}`

**Parameters**

| Name | Type | Required | Description                                                                          |
| :--- | :--- | :------- | :----------------------------------------------------------------------------------- |
| id\_ | str  | ✅       | The object’s conceptual ID from which the account and account group IDs synthesizes. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_group_account.delete_account_group_account(id_="id")

print(result)
```

