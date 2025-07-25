# ComponentMetadataSimpleExpression

**Properties**

| Name     | Type                                      | Required | Description |
| :------- | :---------------------------------------- | :------- | :---------- |
| operator | ComponentMetadataSimpleExpressionOperator | ✅       |             |
| property | ComponentMetadataSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                 | ❌       |             |

# ComponentMetadataSimpleExpressionOperator

**Properties**

| Name               | Type | Required | Description             |
| :----------------- | :--- | :------- | :---------------------- |
| EQUALS             | str  | ✅       | "EQUALS"                |
| LIKE               | str  | ✅       | "LIKE"                  |
| NOTEQUALS          | str  | ✅       | "NOT_EQUALS"            |
| ISNULL             | str  | ✅       | "IS_NULL"               |
| ISNOTNULL          | str  | ✅       | "IS_NOT_NULL"           |
| BETWEEN            | str  | ✅       | "BETWEEN"               |
| GREATERTHAN        | str  | ✅       | "GREATER_THAN"          |
| GREATERTHANOREQUAL | str  | ✅       | "GREATER_THAN_OR_EQUAL" |
| LESSTHAN           | str  | ✅       | "LESS_THAN"             |
| LESSTHANOREQUAL    | str  | ✅       | "LESS_THAN_OR_EQUAL"    |
| CONTAINS           | str  | ✅       | "CONTAINS"              |
| NOTCONTAINS        | str  | ✅       | "NOT_CONTAINS"          |

# ComponentMetadataSimpleExpressionProperty

**Properties**

| Name                       | Type | Required | Description                  |
| :------------------------- | :--- | :------- | :--------------------------- |
| ACCOUNTID                  | str  | ✅       | "accountId"                  |
| COMPONENTID                | str  | ✅       | "componentId"                |
| VERSION                    | str  | ✅       | "version"                    |
| NAME                       | str  | ✅       | "name"                       |
| TYPE                       | str  | ✅       | "type"                       |
| SUBTYPE                    | str  | ✅       | "subType"                    |
| CREATEDDATE                | str  | ✅       | "createdDate"                |
| CREATEDBY                  | str  | ✅       | "createdBy"                  |
| MODIFIEDDATE               | str  | ✅       | "modifiedDate"               |
| MODIFIEDBY                 | str  | ✅       | "modifiedBy"                 |
| DELETED                    | str  | ✅       | "deleted"                    |
| CURRENTVERSION             | str  | ✅       | "currentVersion"             |
| FOLDERNAME                 | str  | ✅       | "folderName"                 |
| FOLDERID                   | str  | ✅       | "folderId"                   |
| COPIEDFROMCOMPONENTID      | str  | ✅       | "copiedFromComponentId"      |
| COPIEDFROMCOMPONENTVERSION | str  | ✅       | "copiedFromComponentVersion" |
| BRANCHNAME                 | str  | ✅       | "branchName"                 |
| BRANCHID                   | str  | ✅       | "branchId"                   |

