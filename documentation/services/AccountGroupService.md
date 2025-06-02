# AccountGroupService

A list of all methods in the `AccountGroupService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                     |
| :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_account_group](#create_account_group)         | Creates an account group based on the supplied name.                                                                                                                                                                                            |
| [get_account_group](#get_account_group)               | Returns a single Account Group object based on the supplied account group ID. \>**Note:** Resources information is returned only for the Get operation, not the Query operation.                                                                |
| [update_account_group](#update_account_group)         | Updates an account group based on the supplied account group ID.                                                                                                                                                                                |
| [bulk_account_group](#bulk_account_group)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                          |
| [query_account_group](#query_account_group)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_account_group](#query_more_account_group) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## create_account_group

Creates an account group based on the supplied name.

- HTTP Method: `POST`
- Endpoint: `/AccountGroup`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroup](../models/AccountGroup.md) | ❌       | The request body. |

**Return Type**

`AccountGroup`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroup

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroup(
    resources={
        "resource": [
            {
                "object_type": "Cloud",
                "resource_id": "ffd7622d-1f6f-4f08-9bf7-5f2f6eabbf30",
                "resource_name": "Test Integration Pack"
            }
        ]
    },
    account_id="account-123456",
    auto_subscribe_alert_level="none",
    default_group="false",
    id_="fedcba98-7654-3210-fedc-ba9876543210",
    name="Analyst Accounts"
)

result = sdk.account_group.create_account_group(request_body=request_body)

print(result)
```

## get_account_group

Returns a single Account Group object based on the supplied account group ID. \>**Note:** Resources information is returned only for the Get operation, not the Query operation.

- HTTP Method: `GET`
- Endpoint: `/AccountGroup/{id}`

**Parameters**

| Name | Type | Required | Description                  |
| :--- | :--- | :------- | :--------------------------- |
| id\_ | str  | ✅       | The ID of the account group. |

**Return Type**

`AccountGroup`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_group.get_account_group(id_="id")

print(result)
```

## update_account_group

Updates an account group based on the supplied account group ID.

- HTTP Method: `POST`
- Endpoint: `/AccountGroup/{id}`

**Parameters**

| Name         | Type                                      | Required | Description                  |
| :----------- | :---------------------------------------- | :------- | :--------------------------- |
| request_body | [AccountGroup](../models/AccountGroup.md) | ❌       | The request body.            |
| id\_         | str                                       | ✅       | The ID of the account group. |

**Return Type**

`AccountGroup`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroup

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroup(
    resources={
        "resource": [
            {
                "object_type": "Cloud",
                "resource_id": "ffd7622d-1f6f-4f08-9bf7-5f2f6eabbf30",
                "resource_name": "Test Integration Pack"
            }
        ]
    },
    account_id="account-123456",
    auto_subscribe_alert_level="none",
    default_group="false",
    id_="fedcba98-7654-3210-fedc-ba9876543210",
    name="Analyst Accounts"
)

result = sdk.account_group.update_account_group(
    request_body=request_body,
    id_="id"
)

print(result)
```

## bulk_account_group

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AccountGroup/bulk`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupBulkRequest](../models/AccountGroupBulkRequest.md) | ❌       | The request body. |

**Return Type**

`AccountGroupBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.account_group.bulk_account_group(request_body=request_body)

print(result)
```

## query_account_group

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroup/query`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountGroupQueryConfig](../models/AccountGroupQueryConfig.md) | ❌       | The request body. |

**Return Type**

`AccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountGroupQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountGroupQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "id"
        }
    }
)

result = sdk.account_group.query_account_group(request_body=request_body)

print(result)
```

## query_more_account_group

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountGroup/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountGroupQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ad qui "

result = sdk.account_group.query_more_account_group(request_body=request_body)

print(result)
```

