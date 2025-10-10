# RoleService

A list of all methods in the `RoleService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                                                                                                                                                                                                                                     |
| :---------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_role](#create_role)         | Creates a Role object based on the supplied values.                                                                                                                                                                                             |
| [get_role](#get_role)               | Returns a single Role object based on the supplied role ID.                                                                                                                                                                                     |
| [update_role](#update_role)         | Updates a role as identified by its role ID.                                                                                                                                                                                                    |
| [delete_role](#delete_role)         | Deletes a Role object based on the supplied role ID.                                                                                                                                                                                            |
| [bulk_role](#bulk_role)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                          |
| [query_role](#query_role)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_role](#query_more_role) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## create_role

Creates a Role object based on the supplied values.

- HTTP Method: `POST`
- Endpoint: `/Role`

**Parameters**

| Name         | Type                      | Required | Description       |
| :----------- | :------------------------ | :------- | :---------------- |
| request_body | [Role](../models/Role.md) | ❌       | The request body. |

**Return Type**

`Role`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Role

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Role(
    description="This is a custom role added",
    privileges={
        "privilege": [
            {
                "name": "name"
            }
        ]
    },
    account_id="accountId-12345",
    id_="794f61e2-b483-40cd-81f9-de0f835fee1d",
    name="myRole",
    parent_id="parentId"
)

result = sdk.role.create_role(request_body=request_body)

print(result)
```

## get_role

Returns a single Role object based on the supplied role ID.

- HTTP Method: `GET`
- Endpoint: `/Role/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`Role`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.role.get_role(id_="id")

print(result)
```

## update_role

Updates a role as identified by its role ID.

- HTTP Method: `POST`
- Endpoint: `/Role/{id}`

**Parameters**

| Name         | Type                      | Required | Description       |
| :----------- | :------------------------ | :------- | :---------------- |
| request_body | [Role](../models/Role.md) | ❌       | The request body. |
| id\_         | str                       | ✅       |                   |

**Return Type**

`Role`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Role

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Role(
    description="This is a custom role added",
    privileges={
        "privilege": [
            {
                "name": "name"
            }
        ]
    },
    account_id="accountId-12345",
    id_="794f61e2-b483-40cd-81f9-de0f835fee1d",
    name="myRole",
    parent_id="parentId"
)

result = sdk.role.update_role(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_role

Deletes a Role object based on the supplied role ID.

- HTTP Method: `DELETE`
- Endpoint: `/Role/{id}`

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

result = sdk.role.delete_role(id_="id")

print(result)
```

## bulk_role

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Role/bulk`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [RoleBulkRequest](../models/RoleBulkRequest.md) | ❌       | The request body. |

**Return Type**

`RoleBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RoleBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RoleBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.role.bulk_role(request_body=request_body)

print(result)
```

## query_role

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Role/query`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [RoleQueryConfig](../models/RoleQueryConfig.md) | ❌       | The request body. |

**Return Type**

`RoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RoleQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RoleQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.role.query_role(request_body=request_body)

print(result)
```

## query_more_role

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Role/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`RoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "nulla"

result = sdk.role.query_more_role(request_body=request_body)

print(result)
```

