# BranchService

A list of all methods in the `BranchService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_branch](#create_branch)         | - To create a branch, you need the branch ID for the branch from which you want to create a new branch. New branches return ready as false until the creating stage has cleared. - You can also create a branch from a packaged component. To do so, use the ID of the packaged component as the packageId. - To create a branch from a deployment, use the ID of the deployment for the packageId.                                                                                                                                                                                                                  |
| [get_branch](#get_branch)               | When you have the branch ID, you can query for additional information about the branch. Send an HTTP GET where {accountId} is the ID of the authenticating account and {branchId} is the ID of the branch you want to query.                                                                                                                                                                                                                                                                                                                                                                                         |
| [update_branch](#update_branch)         | To update a branch, you need the branch ID. Currently, you can only update the name of the branch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [delete_branch](#delete_branch)         | Deletes a branch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bulk_branch](#bulk_branch)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [query_branch](#query_branch)           | You must first retrieve the ID of your main branch, using the name of your current branch. If you haven't created any branches, your current branch will be `main`. When you query a branch, it might be in one of the following states: - `CREATING`: The branch is being created - `NORMAL`: The branch is ready to use - `DELETING`: The branch is being deleted. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_branch](#query_more_branch) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## create_branch

- To create a branch, you need the branch ID for the branch from which you want to create a new branch. New branches return ready as false until the creating stage has cleared. - You can also create a branch from a packaged component. To do so, use the ID of the packaged component as the packageId. - To create a branch from a deployment, use the ID of the deployment for the packageId.

- HTTP Method: `POST`
- Endpoint: `/Branch`

**Parameters**

| Name         | Type                          | Required | Description       |
| :----------- | :---------------------------- | :------- | :---------------- |
| request_body | [Branch](../models/Branch.md) | ❌       | The request body. |

**Return Type**

`Branch`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Branch

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Branch(
    created_by="createdBy",
    created_date="createdDate",
    deleted=True,
    deployment_id="deploymentId",
    description="description",
    id_="id",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    name="name",
    package_id="packageId",
    parent_id="parentId",
    ready=True,
    stage="stage"
)

result = sdk.branch.create_branch(request_body=request_body)

print(result)
```

## get_branch

When you have the branch ID, you can query for additional information about the branch. Send an HTTP GET where {accountId} is the ID of the authenticating account and {branchId} is the ID of the branch you want to query.

- HTTP Method: `GET`
- Endpoint: `/Branch/{id}`

**Parameters**

| Name | Type | Required | Description           |
| :--- | :--- | :------- | :-------------------- |
| id\_ | str  | ✅       | The ID of the branch. |

**Return Type**

`Branch`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.branch.get_branch(id_="id")

print(result)
```

## update_branch

To update a branch, you need the branch ID. Currently, you can only update the name of the branch.

- HTTP Method: `POST`
- Endpoint: `/Branch/{id}`

**Parameters**

| Name         | Type                          | Required | Description           |
| :----------- | :---------------------------- | :------- | :-------------------- |
| request_body | [Branch](../models/Branch.md) | ❌       | The request body.     |
| id\_         | str                           | ✅       | The ID of the branch. |

**Return Type**

`Branch`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import Branch

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = Branch(
    created_by="createdBy",
    created_date="createdDate",
    deleted=True,
    deployment_id="deploymentId",
    description="description",
    id_="id",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    name="name",
    package_id="packageId",
    parent_id="parentId",
    ready=True,
    stage="stage"
)

result = sdk.branch.update_branch(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_branch

Deletes a branch

- HTTP Method: `DELETE`
- Endpoint: `/Branch/{id}`

**Parameters**

| Name | Type | Required | Description           |
| :--- | :--- | :------- | :-------------------- |
| id\_ | str  | ✅       | The ID of the branch. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.branch.delete_branch(id_="id")

print(result)
```

## bulk_branch

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Branch/bulk`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [BranchBulkRequest](../models/BranchBulkRequest.md) | ❌       | The request body. |

**Return Type**

`BranchBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import BranchBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = BranchBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.branch.bulk_branch(request_body=request_body)

print(result)
```

## query_branch

You must first retrieve the ID of your main branch, using the name of your current branch. If you haven't created any branches, your current branch will be `main`. When you query a branch, it might be in one of the following states: - `CREATING`: The branch is being created - `NORMAL`: The branch is ready to use - `DELETING`: The branch is being deleted. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Branch/query`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [BranchQueryConfig](../models/BranchQueryConfig.md) | ❌       | The request body. |

**Return Type**

`BranchQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import BranchQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = BranchQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "property"
        }
    }
)

result = sdk.branch.query_branch(request_body=request_body)

print(result)
```

## query_more_branch

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/Branch/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`BranchQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "consequa"

result = sdk.branch.query_more_branch(request_body=request_body)

print(result)
```

