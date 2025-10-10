# ConnectorSimpleExpression

**Properties**

| Name     | Type                              | Required | Description |
| :------- | :-------------------------------- | :------- | :---------- |
| operator | ConnectorSimpleExpressionOperator | ✅       |             |
| property | ConnectorSimpleExpressionProperty | ✅       |             |
| argument | List[str]                         | ❌       |             |

# ConnectorSimpleExpressionOperator

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

# ConnectorSimpleExpressionProperty

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| TYPE | str  | ✅       | "type"      |
| NAME | str  | ✅       | "name"      |

