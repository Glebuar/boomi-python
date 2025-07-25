# ExecutionConnectorSimpleExpression

**Properties**

| Name     | Type                                       | Required | Description |
| :------- | :----------------------------------------- | :------- | :---------- |
| operator | ExecutionConnectorSimpleExpressionOperator | ✅       |             |
| property | ExecutionConnectorSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                  | ❌       |             |

# ExecutionConnectorSimpleExpressionOperator

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

# ExecutionConnectorSimpleExpressionProperty

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| EXECUTIONID   | str  | ✅       | "executionId"   |
| CONNECTORTYPE | str  | ✅       | "connectorType" |
| ACTIONTYPE    | str  | ✅       | "actionType"    |
| ERRORCOUNT    | str  | ✅       | "errorCount"    |
| SUCCESSCOUNT  | str  | ✅       | "successCount"  |
| SIZE          | str  | ✅       | "size"          |
| ISSTARTSHAPE  | str  | ✅       | "isStartShape"  |
| RECORDTYPE    | str  | ✅       | "recordType"    |

