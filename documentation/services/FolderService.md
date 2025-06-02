# FolderService

A list of all methods in the `FolderService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_folder](#create_folder)         | - When using the CREATE operation, you can create a new folder within the parent folder. - When creating a new folder, a name is required but PermittedRoles are optional. Unless it includes a list of UserRoles, in which case the GUID is required for the UserRole. - `parentId` must be a valid, non-deleted folder. If omitted or blank, it defaults to the root folder. - To Restore a folder you need to use the CREATE operation call, using a valid GUID for a deleted item. This will also restore any deleted components within that folder.   |
| [get_folder](#get_folder)               | Retrieves the folder with the particular ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [update_folder](#update_folder)         | You can update by changing the name of the folder and following the same considerations for the CREATE parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [delete_folder](#delete_folder)         | - Deleting a folder will delete the folder and its contents including all components and sub-folders. - The root folder cannot be deleted. - Folders containing actively deployed processes or other deployable components cannot be deleted. \>**Note:** You can restore a deleted folder by requesting a CREATE operation and specifying the ID of the deleted folder.                                                                                                                                                                                   |
| [bulk_folder](#bulk_folder)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [query_folder](#query_folder)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). - You can perform the QUERY operation for the Folder object by id, name, fullPath and deleted. - The QUERY MORE operation is also available for the Folder object. - You can perform an empty QUERY to return all folders. - If no filter is specified, both non-deleted and deleted records are returned. |
| [query_more_folder](#query_more_folder) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## create_folder

- When using the CREATE operation, you can create a new folder within the parent folder. - When creating a new folder, a name is required but PermittedRoles are optional. Unless it includes a list of UserRoles, in which case the GUID is required for the UserRole. - `parentId` must be a valid, non-deleted folder. If omitted or blank, it defaults to the root folder. - To Restore a folder you need to use the CREATE operation call, using a valid GUID for a deleted item. This will also restore any deleted components within that folder.

- HTTP Method: `POST`
- Endpoint: `/Folder`

**Parameters**

| Name         | Type                          | Required | Description       |
| :----------- | :---------------------------- | :------- | :---------------- |
| request_body | [Folder](../models/Folder.md) | ❌       | The request body. |

**Return Type**

`Folder`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Folder

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Folder(
    permitted_roles={
        "role_reference": [
            {
                "id_": "id",
                "name": "name"
            }
        ]
    },
    deleted="false",
    full_path="Platform API/Folder/Tests/Folder-Name",
    id_="folderId123",
    name="Folder-Name",
    parent_id="parentId",
    parent_name="parentName"
)

result = sdk.folder.create_folder(request_body=request_body)

print(result)
```

## get_folder

Retrieves the folder with the particular ID.

- HTTP Method: `GET`
- Endpoint: `/Folder/{id}`

**Parameters**

| Name | Type | Required | Description                                                                |
| :--- | :--- | :------- | :------------------------------------------------------------------------- |
| id\_ | str  | ✅       | Required. Read only. The Boomi-generated, unique identifier of the folder. |

**Return Type**

`Folder`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.folder.get_folder(id_="id")

print(result)
```

## update_folder

You can update by changing the name of the folder and following the same considerations for the CREATE parameters.

- HTTP Method: `POST`
- Endpoint: `/Folder/{id}`

**Parameters**

| Name         | Type                          | Required | Description                                                                |
| :----------- | :---------------------------- | :------- | :------------------------------------------------------------------------- |
| request_body | [Folder](../models/Folder.md) | ❌       | The request body.                                                          |
| id\_         | str                           | ✅       | Required. Read only. The Boomi-generated, unique identifier of the folder. |

**Return Type**

`Folder`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Folder

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Folder(
    permitted_roles={
        "role_reference": [
            {
                "id_": "id",
                "name": "name"
            }
        ]
    },
    deleted="false",
    full_path="Platform API/Folder/Tests/Folder-Name",
    id_="folderId123",
    name="Folder-Name",
    parent_id="parentId",
    parent_name="parentName"
)

result = sdk.folder.update_folder(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_folder

- Deleting a folder will delete the folder and its contents including all components and sub-folders. - The root folder cannot be deleted. - Folders containing actively deployed processes or other deployable components cannot be deleted. \>**Note:** You can restore a deleted folder by requesting a CREATE operation and specifying the ID of the deleted folder.

- HTTP Method: `DELETE`
- Endpoint: `/Folder/{id}`

**Parameters**

| Name | Type | Required | Description                                                                |
| :--- | :--- | :------- | :------------------------------------------------------------------------- |
| id\_ | str  | ✅       | Required. Read only. The Boomi-generated, unique identifier of the folder. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.folder.delete_folder(id_="id")

print(result)
```

## bulk_folder

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Folder/bulk`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [FolderBulkRequest](../models/FolderBulkRequest.md) | ❌       | The request body. |

**Return Type**

`FolderBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import FolderBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = FolderBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.folder.bulk_folder(request_body=request_body)

print(result)
```

## query_folder

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). - You can perform the QUERY operation for the Folder object by id, name, fullPath and deleted. - The QUERY MORE operation is also available for the Folder object. - You can perform an empty QUERY to return all folders. - If no filter is specified, both non-deleted and deleted records are returned.

- HTTP Method: `POST`
- Endpoint: `/Folder/query`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [FolderQueryConfig](../models/FolderQueryConfig.md) | ❌       | The request body. |

**Return Type**

`FolderQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import FolderQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = FolderQueryConfig(
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

result = sdk.folder.query_folder(request_body=request_body)

print(result)
```

## query_more_folder

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Folder/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`FolderQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "exercitation c"

result = sdk.folder.query_more_folder(request_body=request_body)

print(result)
```

