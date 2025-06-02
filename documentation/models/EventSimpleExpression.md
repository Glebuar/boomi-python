# EventSimpleExpression

**Properties**

| Name     | Type                          | Required | Description |
| :------- | :---------------------------- | :------- | :---------- |
| operator | EventSimpleExpressionOperator | ✅       |             |
| property | EventSimpleExpressionProperty | ✅       |             |
| argument | List[str]                     | ❌       |             |

# EventSimpleExpressionOperator

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

# EventSimpleExpressionProperty

**Properties**

| Name                  | Type | Required | Description             |
| :-------------------- | :--- | :------- | :---------------------- |
| EVENTID               | str  | ✅       | "eventId"               |
| ACCOUNTID             | str  | ✅       | "accountId"             |
| ATOMID                | str  | ✅       | "atomId"                |
| ATOMNAME              | str  | ✅       | "atomName"              |
| EVENTLEVEL            | str  | ✅       | "eventLevel"            |
| EVENTDATE             | str  | ✅       | "eventDate"             |
| STATUS                | str  | ✅       | "status"                |
| EVENTTYPE             | str  | ✅       | "eventType"             |
| EXECUTIONID           | str  | ✅       | "executionId"           |
| TITLE                 | str  | ✅       | "title"                 |
| UPDATEDATE            | str  | ✅       | "updateDate"            |
| STARTTIME             | str  | ✅       | "startTime"             |
| ENDTIME               | str  | ✅       | "endTime"               |
| ERRORDOCUMENTCOUNT    | str  | ✅       | "errorDocumentCount"    |
| INBOUNDDOCUMENTCOUNT  | str  | ✅       | "inboundDocumentCount"  |
| OUTBOUNDDOCUMENTCOUNT | str  | ✅       | "outboundDocumentCount" |
| PROCESSNAME           | str  | ✅       | "processName"           |
| RECORDDATE            | str  | ✅       | "recordDate"            |
| ERROR                 | str  | ✅       | "error"                 |
| ENVIRONMENT           | str  | ✅       | "environment"           |
| CLASSIFICATION        | str  | ✅       | "classification"        |

