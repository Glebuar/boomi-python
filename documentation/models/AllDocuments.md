# AllDocuments

You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both. Indicates that the Rerun Document operation reruns all documents in the original run. When using AllDocuments in a request, you must also specify a `documentStatus` value.

**Properties**

| Name            | Type           | Required | Description                                                                                                                                                                                                                                                                |
| :-------------- | :------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document_status | DocumentStatus | ❌       | - A value of ANY reruns all documents in the specified process run (in other words, the originalExecutionID). - A value of SUCCESS returns successfully run documents in the process run. - A value of ERROR returns documents that unsuccessfully ran in the process run. |

# DocumentStatus

- A value of ANY reruns all documents in the specified process run (in other words, the originalExecutionID). - A value of SUCCESS returns successfully run documents in the process run. - A value of ERROR returns documents that unsuccessfully ran in the process run.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| ANY     | str  | ✅       | "ANY"       |
| SUCCESS | str  | ✅       | "SUCCESS"   |
| ERROR   | str  | ✅       | "ERROR"     |

