# EnvironmentRoleService

A list of all methods in the `EnvironmentRoleService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                                                                                                                                                                             |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_environment_role](#create_environment_role)         | Associates a role with an environment. You must have the Runtime Management privilege to perform the CREATE operation.                                                                                                                                  |
| [get_environment_role](#get_environment_role)               | Returns a single Environment Role object based on the supplied environment role ID.                                                                                                                                                                     |
| [delete_environment_role](#delete_environment_role)         | Removes the association between a role and an environment. You must have the Runtime Management privilege to perform the DELETE operation. If you have the Runtime Management privilege, you cannot delete associations between roles and environments. |
| [bulk_environment_role](#bulk_environment_role)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                  |
| [query_environment_role](#query_environment_role)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).         |
| [query_more_environment_role](#query_more_environment_role) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                          |

## create_environment_role

Associates a role with an environment. You must have the Runtime Management privilege to perform the CREATE operation.

- HTTP Method: `POST`
- Endpoint: `/EnvironmentRole`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentRole](../models/EnvironmentRole.md) | ❌       | The request body. |

**Return Type**

`EnvironmentRole`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentRole

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentRole(
    environment_id="myEnvironment",
    id_="id",
    role_id="userRole"
)

result = sdk.environment_role.create_environment_role(request_body=request_body)

print(result)
```

## get_environment_role

Returns a single Environment Role object based on the supplied environment role ID.

- HTTP Method: `GET`
- Endpoint: `/EnvironmentRole/{id}`

**Parameters**

| Name | Type | Required | Description                                            |
| :--- | :--- | :------- | :----------------------------------------------------- |
| id\_ | str  | ✅       | The Environment Role object you are attempting to get. |

**Return Type**

`EnvironmentRole`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_role.get_environment_role(id_="id")

print(result)
```

## delete_environment_role

Removes the association between a role and an environment. You must have the Runtime Management privilege to perform the DELETE operation. If you have the Runtime Management privilege, you cannot delete associations between roles and environments.

- HTTP Method: `DELETE`
- Endpoint: `/EnvironmentRole/{id}`

**Parameters**

| Name | Type | Required | Description                                               |
| :--- | :--- | :------- | :-------------------------------------------------------- |
| id\_ | str  | ✅       | The Environment Role object you are attempting to delete. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.environment_role.delete_environment_role(id_="id")

print(result)
```

## bulk_environment_role

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentRole/bulk`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentRoleBulkRequest](../models/EnvironmentRoleBulkRequest.md) | ❌       | The request body. |

**Return Type**

`EnvironmentRoleBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentRoleBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentRoleBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.environment_role.bulk_environment_role(request_body=request_body)

print(result)
```

## query_environment_role

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentRole/query`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvironmentRoleQueryConfig](../models/EnvironmentRoleQueryConfig.md) | ❌       | The request body. |

**Return Type**

`EnvironmentRoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import EnvironmentRoleQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = EnvironmentRoleQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "environmentId"
        }
    }
)

result = sdk.environment_role.query_environment_role(request_body=request_body)

print(result)
```

## query_more_environment_role

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/EnvironmentRole/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`EnvironmentRoleQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "est sint sed"

result = sdk.environment_role.query_more_environment_role(request_body=request_body)

print(result)
```

