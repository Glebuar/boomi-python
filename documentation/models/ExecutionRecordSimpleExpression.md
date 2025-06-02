# ExecutionRecordSimpleExpression

**Properties**

| Name     | Type                                    | Required | Description |
| :------- | :-------------------------------------- | :------- | :---------- |
| operator | ExecutionRecordSimpleExpressionOperator | ✅       |             |
| property | ExecutionRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                               | ❌       |             |

# ExecutionRecordSimpleExpressionOperator

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

# ExecutionRecordSimpleExpressionProperty

**Properties**

| Name                  | Type | Required | Description             |
| :-------------------- | :--- | :------- | :---------------------- |
| EXECUTIONID           | str  | ✅       | "executionId"           |
| ORIGINALEXECUTIONID   | str  | ✅       | "originalExecutionId"   |
| ACCOUNT               | str  | ✅       | "account"               |
| EXECUTIONTIME         | str  | ✅       | "executionTime"         |
| STATUS                | str  | ✅       | "status"                |
| EXECUTIONTYPE         | str  | ✅       | "executionType"         |
| PROCESSNAME           | str  | ✅       | "processName"           |
| PROCESSID             | str  | ✅       | "processId"             |
| ATOMNAME              | str  | ✅       | "atomName"              |
| ATOMID                | str  | ✅       | "atomId"                |
| INBOUNDDOCUMENTCOUNT  | str  | ✅       | "inboundDocumentCount"  |
| OUTBOUNDDOCUMENTCOUNT | str  | ✅       | "outboundDocumentCount" |
| EXECUTIONDURATION     | str  | ✅       | "executionDuration"     |
| MESSAGE               | str  | ✅       | "message"               |
| REPORTKEY             | str  | ✅       | "reportKey"             |
| LAUNCHERID            | str  | ✅       | "launcherId"            |
| NODEID                | str  | ✅       | "nodeId"                |
| RECORDEDDATE          | str  | ✅       | "recordedDate"          |

