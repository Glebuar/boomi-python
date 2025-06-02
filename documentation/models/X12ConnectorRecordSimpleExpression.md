# X12ConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                       | Required | Description |
| :------- | :----------------------------------------- | :------- | :---------- |
| operator | X12ConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | X12ConnectorRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                  | ❌       |             |

# X12ConnectorRecordSimpleExpressionOperator

**Properties**

| Name               | Type | Required | Description             |
| :----------------- | :--- | :------- | :---------------------- |
| EQUALS             | str  | ✅       | "EQUALS"                |
| STARTSWITH         | str  | ✅       | "STARTS_WITH"           |
| BETWEEN            | str  | ✅       | "BETWEEN"               |
| GREATERTHAN        | str  | ✅       | "GREATER_THAN"          |
| GREATERTHANOREQUAL | str  | ✅       | "GREATER_THAN_OR_EQUAL" |
| LESSTHAN           | str  | ✅       | "LESS_THAN"             |
| LESSTHANOREQUAL    | str  | ✅       | "LESS_THAN_OR_EQUAL"    |

# X12ConnectorRecordSimpleExpressionProperty

**Properties**

| Name                     | Type | Required | Description                |
| :----------------------- | :--- | :------- | :------------------------- |
| EXECUTIONID              | str  | ✅       | "executionId"              |
| ATOMID                   | str  | ✅       | "atomId"                   |
| DATEPROCESSED            | str  | ✅       | "dateProcessed"            |
| ID                       | str  | ✅       | "id"                       |
| ACTIONTYPE               | str  | ✅       | "actionType"               |
| CONNECTORTYPE            | str  | ✅       | "connectorType"            |
| CONNECTORNAME            | str  | ✅       | "connectorName"            |
| OPERATIONNAME            | str  | ✅       | "operationName"            |
| DOCUMENTINDEX            | str  | ✅       | "documentIndex"            |
| SUCCESSFUL               | str  | ✅       | "successful"               |
| SIZE                     | str  | ✅       | "size"                     |
| ERRORMESSAGE             | str  | ✅       | "errorMessage"             |
| ISAACKSTATUS             | str  | ✅       | "isaAckStatus"             |
| ISAACKREPORT             | str  | ✅       | "isaAckReport"             |
| ACKSTATUS                | str  | ✅       | "ackStatus"                |
| ACKREPORT                | str  | ✅       | "ackReport"                |
| ISACONTROL               | str  | ✅       | "isaControl"               |
| GSCONTROL                | str  | ✅       | "gsControl"                |
| STCONTROL                | str  | ✅       | "stControl"                |
| FUNCTIONALID             | str  | ✅       | "functionalID"             |
| TRANSACTIONSET           | str  | ✅       | "transactionSet"           |
| TESTINDICATOR            | str  | ✅       | "testIndicator"            |
| SENDERIDQUALIFIER        | str  | ✅       | "senderIDQualifier"        |
| SENDERID                 | str  | ✅       | "senderID"                 |
| RECEIVERIDQUALIFIER      | str  | ✅       | "receiverIDQualifier"      |
| RECEIVERID               | str  | ✅       | "receiverID"               |
| APPSENDERID              | str  | ✅       | "appSenderID"              |
| APPRECEIVERID            | str  | ✅       | "appReceiverID"            |
| STANDARDID               | str  | ✅       | "standardID"               |
| STANDARD                 | str  | ✅       | "standard"                 |
| GSVERSION                | str  | ✅       | "gsVersion"                |
| AGENCYCODE               | str  | ✅       | "agencyCode"               |
| GSDATE                   | str  | ✅       | "gsDate"                   |
| GSTIME                   | str  | ✅       | "gsTime"                   |
| OUTBOUNDVALIDATIONSTATUS | str  | ✅       | "outboundValidationStatus" |
| OUTBOUNDVALIDATIONREPORT | str  | ✅       | "outboundValidationReport" |

