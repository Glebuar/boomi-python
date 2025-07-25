# AtomSimpleExpression

**Properties**

| Name     | Type                         | Required | Description |
| :------- | :--------------------------- | :------- | :---------- |
| operator | AtomSimpleExpressionOperator | ✅       |             |
| property | AtomSimpleExpressionProperty | ✅       |             |
| argument | List[str]                    | ❌       |             |

# AtomSimpleExpressionOperator

**Properties**

| Name        | Type | Required | Description    |
| :---------- | :--- | :------- | :------------- |
| EQUALS      | str  | ✅       | "EQUALS"       |
| NOTEQUALS   | str  | ✅       | "NOT_EQUALS"   |
| CONTAINS    | str  | ✅       | "CONTAINS"     |
| NOTCONTAINS | str  | ✅       | "NOT_CONTAINS" |

# AtomSimpleExpressionProperty

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| NAME         | str  | ✅       | "name"         |
| ID           | str  | ✅       | "id"           |
| HOSTNAME     | str  | ✅       | "hostname"     |
| STATUS       | str  | ✅       | "status"       |
| TYPE         | str  | ✅       | "type"         |
| CAPABILITIES | str  | ✅       | "capabilities" |

