# FolderSimpleExpression

**Properties**

| Name     | Type                           | Required | Description |
| :------- | :----------------------------- | :------- | :---------- |
| operator | FolderSimpleExpressionOperator | ✅       |             |
| property | FolderSimpleExpressionProperty | ✅       |             |
| argument | List[str]                      | ❌       |             |

# FolderSimpleExpressionOperator

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

# FolderSimpleExpressionProperty

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| ACCOUNTID      | str  | ✅       | "accountId"      |
| ID             | str  | ✅       | "id"             |
| NAME           | str  | ✅       | "name"           |
| FULLPATH       | str  | ✅       | "fullPath"       |
| DELETED        | str  | ✅       | "deleted"        |
| PARENTID       | str  | ✅       | "parentId"       |
| PARENTNAME     | str  | ✅       | "parentName"     |
| PERMITTEDROLES | str  | ✅       | "permittedRoles" |

