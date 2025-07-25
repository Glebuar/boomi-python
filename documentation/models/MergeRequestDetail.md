# MergeRequestDetail

**Properties**

| Name                         | Type                    | Required | Description                                                              |
| :--------------------------- | :---------------------- | :------- | :----------------------------------------------------------------------- |
| change_type                  | ChangeType              | ❌       |                                                                          |
| component_guid               | str                     | ❌       |                                                                          |
| conflict                     | bool                    | ❌       |                                                                          |
| created_by                   | str                     | ❌       |                                                                          |
| created_date                 | str                     | ❌       |                                                                          |
| destination_revision         | int                     | ❌       |                                                                          |
| excluded                     | bool                    | ❌       | When true, signifies that a component will not be included in the Merge. |
| locked_on_destination_branch | bool                    | ❌       |                                                                          |
| merge_revision               | int                     | ❌       |                                                                          |
| modified_by                  | str                     | ❌       |                                                                          |
| modified_date                | str                     | ❌       |                                                                          |
| resolution                   | Resolution              | ❌       |                                                                          |
| source_revision              | int                     | ❌       |                                                                          |
| stage                        | MergeRequestDetailStage | ❌       |                                                                          |

# ChangeType

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| ADDED    | str  | ✅       | "ADDED"     |
| MODIFIED | str  | ✅       | "MODIFIED"  |
| DELETED  | str  | ✅       | "DELETED"   |

# Resolution

**Properties**

| Name            | Type | Required | Description        |
| :-------------- | :--- | :------- | :----------------- |
| OVERRIDE        | str  | ✅       | "OVERRIDE"         |
| KEEPDESTINATION | str  | ✅       | "KEEP_DESTINATION" |

# MergeRequestDetailStage

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| DRAFTED          | str  | ✅       | "DRAFTED"           |
| REVIEWED         | str  | ✅       | "REVIEWED"          |
| CONFLICTRESOLVED | str  | ✅       | "CONFLICT_RESOLVED" |
| MERGED           | str  | ✅       | "MERGED"            |
| REVERTED         | str  | ✅       | "REVERTED"          |

