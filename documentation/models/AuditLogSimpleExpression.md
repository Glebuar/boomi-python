# AuditLogSimpleExpression

**Properties**

| Name     | Type                             | Required | Description |
| :------- | :------------------------------- | :------- | :---------- |
| operator | AuditLogSimpleExpressionOperator | ✅       |             |
| property | AuditLogSimpleExpressionProperty | ✅       |             |
| argument | List[str]                        | ❌       |             |

# AuditLogSimpleExpressionOperator

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

# AuditLogSimpleExpressionProperty

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| CONTAINERID | str  | ✅       | "containerId" |
| USERID      | str  | ✅       | "userId"      |
| DATE        | str  | ✅       | "date"        |
| TYPE        | str  | ✅       | "type"        |
| ACTION      | str  | ✅       | "action"      |
| MODIFIER    | str  | ✅       | "modifier"    |
| LEVEL       | str  | ✅       | "level"       |
| SOURCE      | str  | ✅       | "source"      |

