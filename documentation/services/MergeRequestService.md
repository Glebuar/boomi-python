# MergeRequestService

A list of all methods in the `MergeRequestService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_merge_request](#create_merge_request)         | You can use the Merge Request object to merge a development branch into the main branch. - To create a merge request, you need the branch IDs for the source and destination branches. The source branch is the branch you want to merge into the destination branch. - There are two merge request strategies you can choose from: OVERRIDE or CONFLICT_RESOLVE. An override merge automatically resolves any merge conflicts by prioritizing the branch specified in the `priorityBranch` field. If you choose the CONFLICT_RESOLVE strategy, you have the opportunity to review any conflicts and choose which version you want to keep.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [get_merge_request](#get_merge_request)               | Retrieve more information about the recently performed merge. - The `resolution` parameter is generated from the original merge request and specifies either the source branch for the final content for the merge or the destination. It can have the following values: - OVERRIDE: The source branch has taken priority - KEEP_DESTINATION: The destination branch has taken priority - The `changeType` parameter is generated from a branch diff that is performed on merge and can be one of the following values: - ADDED: A component was added to the source branch - MODIFIED: A component was modified in the source branch - DELETED: A component was deleted in the source branch After performing a merge request between two branches, you can use the merge request’s ID to retrieve more information about the recently performed merge. The following example shows a merge between two branches where something was deleted in the source branch: Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/MergeRequest/{mergeRequestId}` where `{accountId}` is the ID of the authenticating account and `{mergeRequestId}` is the ID of the merge request. You can also use the GET operation to view a user's current working branch: Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/UserAccountProperty/defaultWorkingBranch` where the `{accountId}` is the ID of the account for which you want to view the working branch. |
| [update_merge_request](#update_merge_request)         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [delete_merge_request](#delete_merge_request)         | - There are three actions you can choose from when executing a merge request: - MERGE: Use to start or restart a merge request; the `stage` must be REVIEWING or FAILED_TO_MERGE - REVERT: Use to revert a merge request; the `stage` must be MERGED or DELETED and `previousStage` is MERGED - RETRY_DRAFTING: Use when the merge request `stage` is FAILED_TO_DRAFT or FAILED_TO_REDRAFT - If the merge is successful, the `stage` and/or `previousStage` might be in one of the following stages: - DRAFTING: The merge request is in the queue. - DRAFTED: The merge request is drafted for review. - REVIEWING: The merge request is being reviewed. - MERGING: The merge request is being processed. - MERGED: The merge request has successfully completed. - FAILED_TO_MERGE: The merge request failed to merge. - NOT_EXIST: No previous merge request has been submitted. This stage is typically returned in the `previousStage` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [bulk_merge_request](#bulk_merge_request)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [execute_merge_request](#execute_merge_request)       | - These are the actions you can choose from when executing a merge request: - MERGE: Use to start or restart a merge request; the stage must be REVIEWING or FAILED_TO_MERGE - REVERT: Use to revert a merge request; the stage must be MERGED or DELETED and previousStage is MERGED - RETRY_DRAFTING: Use when the merge request stage is FAILED_TO_DRAFT or FAILED_TO_REDRAFT - If the merge is successful, the `stage` and/or `previousStage` might be in one of the following stages: - DRAFTING - The merge request is in the queue. - DRAFTED - The merge request is drafted for review. - REVIEWING - The merge request is being reviewed. _ MERGING - The merge request is being processed. _ MERGED - The merge request has successfully completed. \* FAILED_TO_MERGE - The merge request failed to merge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [query_merge_request](#query_merge_request)           | - You can query a branch to retrieve a list of all active merge request IDs. - You must include the destination or source branch as a parameter. Only EQUALS is allowed for these parameters. - Optional parameters include: - `createdDate` - `createdBy` - `stage` - `modifiedDate` - `modifiedBy` - You can use the `queryMore` request to return more than 100 results. For more information about query filters, refer to [Query filters](/api/platformapi#section/Introduction/Query-filters).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [query_more_merge_request](#query_more_merge_request) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## create_merge_request

You can use the Merge Request object to merge a development branch into the main branch. - To create a merge request, you need the branch IDs for the source and destination branches. The source branch is the branch you want to merge into the destination branch. - There are two merge request strategies you can choose from: OVERRIDE or CONFLICT_RESOLVE. An override merge automatically resolves any merge conflicts by prioritizing the branch specified in the `priorityBranch` field. If you choose the CONFLICT_RESOLVE strategy, you have the opportunity to review any conflicts and choose which version you want to keep.

- HTTP Method: `POST`
- Endpoint: `/MergeRequest`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [MergeRequest](../models/MergeRequest.md) | ❌       | The request body. |

**Return Type**

`MergeRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import MergeRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = MergeRequest(
    merge_request_details={
        "merge_request_detail": [
            {
                "change_type": "ADDED",
                "component_guid": "componentGuid",
                "conflict": True,
                "created_by": "createdBy",
                "created_date": "createdDate",
                "destination_revision": 7,
                "excluded": True,
                "locked_on_destination_branch": True,
                "merge_revision": 0,
                "modified_by": "modifiedBy",
                "modified_date": "modifiedDate",
                "resolution": "OVERRIDE",
                "source_revision": 4,
                "stage": "DRAFTED"
            }
        ]
    },
    created_by="createdBy",
    created_date="createdDate",
    destination_branch_id="destinationBranchId",
    destination_branch_name="destinationBranchName",
    id_="id",
    inactive_date="inactiveDate",
    lock_nonce=4,
    locked_by="lockedBy",
    locked_date="lockedDate",
    merge_request_action="UPDATE",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    note="note",
    previous_stage="NOT_EXIST",
    priority_branch="SOURCE",
    source_branch_id="sourceBranchId",
    source_branch_name="sourceBranchName",
    stage="NOT_EXIST",
    strategy="OVERRIDE"
)

result = sdk.merge_request.create_merge_request(request_body=request_body)

print(result)
```

## get_merge_request

Retrieve more information about the recently performed merge. - The `resolution` parameter is generated from the original merge request and specifies either the source branch for the final content for the merge or the destination. It can have the following values: - OVERRIDE: The source branch has taken priority - KEEP_DESTINATION: The destination branch has taken priority - The `changeType` parameter is generated from a branch diff that is performed on merge and can be one of the following values: - ADDED: A component was added to the source branch - MODIFIED: A component was modified in the source branch - DELETED: A component was deleted in the source branch After performing a merge request between two branches, you can use the merge request’s ID to retrieve more information about the recently performed merge. The following example shows a merge between two branches where something was deleted in the source branch: Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/MergeRequest/{mergeRequestId}` where `{accountId}` is the ID of the authenticating account and `{mergeRequestId}` is the ID of the merge request. You can also use the GET operation to view a user's current working branch: Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/UserAccountProperty/defaultWorkingBranch` where the `{accountId}` is the ID of the account for which you want to view the working branch.

- HTTP Method: `GET`
- Endpoint: `/MergeRequest/{id}`

**Parameters**

| Name | Type | Required | Description              |
| :--- | :--- | :------- | :----------------------- |
| id\_ | str  | ✅       | ID of the merge request. |

**Return Type**

`MergeRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.merge_request.get_merge_request(id_="id")

print(result)
```

## update_merge_request

- HTTP Method: `POST`
- Endpoint: `/MergeRequest/{id}`

**Parameters**

| Name         | Type                                      | Required | Description              |
| :----------- | :---------------------------------------- | :------- | :----------------------- |
| request_body | [MergeRequest](../models/MergeRequest.md) | ❌       | The request body.        |
| id\_         | str                                       | ✅       | ID of the merge request. |

**Return Type**

`MergeRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import MergeRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = MergeRequest(
    merge_request_details={
        "merge_request_detail": [
            {
                "change_type": "ADDED",
                "component_guid": "componentGuid",
                "conflict": True,
                "created_by": "createdBy",
                "created_date": "createdDate",
                "destination_revision": 7,
                "excluded": True,
                "locked_on_destination_branch": True,
                "merge_revision": 0,
                "modified_by": "modifiedBy",
                "modified_date": "modifiedDate",
                "resolution": "OVERRIDE",
                "source_revision": 4,
                "stage": "DRAFTED"
            }
        ]
    },
    created_by="createdBy",
    created_date="createdDate",
    destination_branch_id="destinationBranchId",
    destination_branch_name="destinationBranchName",
    id_="id",
    inactive_date="inactiveDate",
    lock_nonce=4,
    locked_by="lockedBy",
    locked_date="lockedDate",
    merge_request_action="UPDATE",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    note="note",
    previous_stage="NOT_EXIST",
    priority_branch="SOURCE",
    source_branch_id="sourceBranchId",
    source_branch_name="sourceBranchName",
    stage="NOT_EXIST",
    strategy="OVERRIDE"
)

result = sdk.merge_request.update_merge_request(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_merge_request

- There are three actions you can choose from when executing a merge request: - MERGE: Use to start or restart a merge request; the `stage` must be REVIEWING or FAILED_TO_MERGE - REVERT: Use to revert a merge request; the `stage` must be MERGED or DELETED and `previousStage` is MERGED - RETRY_DRAFTING: Use when the merge request `stage` is FAILED_TO_DRAFT or FAILED_TO_REDRAFT - If the merge is successful, the `stage` and/or `previousStage` might be in one of the following stages: - DRAFTING: The merge request is in the queue. - DRAFTED: The merge request is drafted for review. - REVIEWING: The merge request is being reviewed. - MERGING: The merge request is being processed. - MERGED: The merge request has successfully completed. - FAILED_TO_MERGE: The merge request failed to merge. - NOT_EXIST: No previous merge request has been submitted. This stage is typically returned in the `previousStage` parameter.

- HTTP Method: `DELETE`
- Endpoint: `/MergeRequest/{id}`

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

result = sdk.merge_request.delete_merge_request(id_="id")

print(result)
```

## bulk_merge_request

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/MergeRequest/bulk`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [MergeRequestBulkRequest](../models/MergeRequestBulkRequest.md) | ❌       | The request body. |

**Return Type**

`MergeRequestBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import MergeRequestBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = MergeRequestBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.merge_request.bulk_merge_request(request_body=request_body)

print(result)
```

## execute_merge_request

- These are the actions you can choose from when executing a merge request: - MERGE: Use to start or restart a merge request; the stage must be REVIEWING or FAILED_TO_MERGE - REVERT: Use to revert a merge request; the stage must be MERGED or DELETED and previousStage is MERGED - RETRY_DRAFTING: Use when the merge request stage is FAILED_TO_DRAFT or FAILED_TO_REDRAFT - If the merge is successful, the `stage` and/or `previousStage` might be in one of the following stages: - DRAFTING - The merge request is in the queue. - DRAFTED - The merge request is drafted for review. - REVIEWING - The merge request is being reviewed. _ MERGING - The merge request is being processed. _ MERGED - The merge request has successfully completed. \* FAILED_TO_MERGE - The merge request failed to merge.

- HTTP Method: `POST`
- Endpoint: `/MergeRequest/execute/{id}`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [MergeRequest](../models/MergeRequest.md) | ❌       | The request body. |
| id\_         | str                                       | ✅       |                   |

**Return Type**

`MergeRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import MergeRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = MergeRequest(
    merge_request_details={
        "merge_request_detail": [
            {
                "change_type": "ADDED",
                "component_guid": "componentGuid",
                "conflict": True,
                "created_by": "createdBy",
                "created_date": "createdDate",
                "destination_revision": 7,
                "excluded": True,
                "locked_on_destination_branch": True,
                "merge_revision": 0,
                "modified_by": "modifiedBy",
                "modified_date": "modifiedDate",
                "resolution": "OVERRIDE",
                "source_revision": 4,
                "stage": "DRAFTED"
            }
        ]
    },
    created_by="createdBy",
    created_date="createdDate",
    destination_branch_id="destinationBranchId",
    destination_branch_name="destinationBranchName",
    id_="id",
    inactive_date="inactiveDate",
    lock_nonce=4,
    locked_by="lockedBy",
    locked_date="lockedDate",
    merge_request_action="UPDATE",
    modified_by="modifiedBy",
    modified_date="modifiedDate",
    note="note",
    previous_stage="NOT_EXIST",
    priority_branch="SOURCE",
    source_branch_id="sourceBranchId",
    source_branch_name="sourceBranchName",
    stage="NOT_EXIST",
    strategy="OVERRIDE"
)

result = sdk.merge_request.execute_merge_request(
    request_body=request_body,
    id_="id"
)

print(result)
```

## query_merge_request

- You can query a branch to retrieve a list of all active merge request IDs. - You must include the destination or source branch as a parameter. Only EQUALS is allowed for these parameters. - Optional parameters include: - `createdDate` - `createdBy` - `stage` - `modifiedDate` - `modifiedBy` - You can use the `queryMore` request to return more than 100 results. For more information about query filters, refer to [Query filters](/api/platformapi#section/Introduction/Query-filters).

- HTTP Method: `POST`
- Endpoint: `/MergeRequest/query`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [MergeRequestQueryConfig](../models/MergeRequestQueryConfig.md) | ❌       | The request body. |

**Return Type**

`MergeRequestQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import MergeRequestQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = MergeRequestQueryConfig(
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

result = sdk.merge_request.query_merge_request(request_body=request_body)

print(result)
```

## query_more_merge_request

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/MergeRequest/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`MergeRequestQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "labore"

result = sdk.merge_request.query_more_merge_request(request_body=request_body)

print(result)
```

