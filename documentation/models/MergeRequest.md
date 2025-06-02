# MergeRequest

**Properties**

| Name                    | Type                | Required | Description                                                 |
| :---------------------- | :------------------ | :------- | :---------------------------------------------------------- |
| merge_request_details   | MergeRequestDetails | ✅       |                                                             |
| created_by              | str                 | ❌       | The user who created the merge request.                     |
| created_date            | str                 | ❌       | The date and time the merge request was created.            |
| destination_branch_id   | str                 | ❌       | The ID of the destination branch.                           |
| destination_branch_name | str                 | ❌       |                                                             |
| id\_                    | str                 | ❌       |                                                             |
| inactive_date           | str                 | ❌       |                                                             |
| lock_nonce              | int                 | ❌       |                                                             |
| locked_by               | str                 | ❌       |                                                             |
| locked_date             | str                 | ❌       |                                                             |
| merge_request_action    | MergeRequestAction  | ❌       |                                                             |
| modified_by             | str                 | ❌       | The user who last modified the merge request.               |
| modified_date           | str                 | ❌       | The date and time the merge request was last modified.      |
| note                    | str                 | ❌       |                                                             |
| previous_stage          | PreviousStage       | ❌       | The previous stage of the merge.                            |
| priority_branch         | PriorityBranch      | ❌       | The branch which should take priority in an override merge. |
| source_branch_id        | str                 | ❌       | The ID of the source branch.                                |
| source_branch_name      | str                 | ❌       |                                                             |
| stage                   | MergeRequestStage   | ❌       | The current stage of the merge.                             |
| strategy                | Strategy            | ❌       | The merge strategy.                                         |

# MergeRequestAction

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| UPDATE        | str  | ✅       | "UPDATE"         |
| MERGE         | str  | ✅       | "MERGE"          |
| RETRYDRAFTING | str  | ✅       | "RETRY_DRAFTING" |
| REVERT        | str  | ✅       | "REVERT"         |

# PreviousStage

The previous stage of the merge.

**Properties**

| Name            | Type | Required | Description         |
| :-------------- | :--- | :------- | :------------------ |
| NOTEXIST        | str  | ✅       | "NOT_EXIST"         |
| DRAFTING        | str  | ✅       | "DRAFTING"          |
| FAILEDTODRAFT   | str  | ✅       | "FAILED_TO_DRAFT"   |
| FAILEDTOREDRAFT | str  | ✅       | "FAILED_TO_REDRAFT" |
| DRAFTED         | str  | ✅       | "DRAFTED"           |
| REVIEWING       | str  | ✅       | "REVIEWING"         |
| MERGING         | str  | ✅       | "MERGING"           |
| MERGED          | str  | ✅       | "MERGED"            |
| FAILEDTOMERGE   | str  | ✅       | "FAILED_TO_MERGE"   |
| DELETED         | str  | ✅       | "DELETED"           |
| REDRAFTING      | str  | ✅       | "REDRAFTING"        |
| REVERTED        | str  | ✅       | "REVERTED"          |

# PriorityBranch

The branch which should take priority in an override merge.

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| SOURCE      | str  | ✅       | "SOURCE"      |
| DESTINATION | str  | ✅       | "DESTINATION" |

# MergeRequestStage

The current stage of the merge.

**Properties**

| Name            | Type | Required | Description         |
| :-------------- | :--- | :------- | :------------------ |
| NOTEXIST        | str  | ✅       | "NOT_EXIST"         |
| DRAFTING        | str  | ✅       | "DRAFTING"          |
| FAILEDTODRAFT   | str  | ✅       | "FAILED_TO_DRAFT"   |
| FAILEDTOREDRAFT | str  | ✅       | "FAILED_TO_REDRAFT" |
| DRAFTED         | str  | ✅       | "DRAFTED"           |
| REVIEWING       | str  | ✅       | "REVIEWING"         |
| MERGING         | str  | ✅       | "MERGING"           |
| MERGED          | str  | ✅       | "MERGED"            |
| FAILEDTOMERGE   | str  | ✅       | "FAILED_TO_MERGE"   |
| DELETED         | str  | ✅       | "DELETED"           |
| REDRAFTING      | str  | ✅       | "REDRAFTING"        |
| REVERTED        | str  | ✅       | "REVERTED"          |

# Strategy

The merge strategy.

**Properties**

| Name            | Type | Required | Description        |
| :-------------- | :--- | :------- | :----------------- |
| OVERRIDE        | str  | ✅       | "OVERRIDE"         |
| CONFLICTRESOLVE | str  | ✅       | "CONFLICT_RESOLVE" |
| SUBSET          | str  | ✅       | "SUBSET"           |

