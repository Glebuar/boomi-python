# TradacomsConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                             | Required | Description |
| :------- | :----------------------------------------------- | :------- | :---------- |
| operator | TradacomsConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | TradacomsConnectorRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                        | ❌       |             |

# TradacomsConnectorRecordSimpleExpressionOperator

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

# TradacomsConnectorRecordSimpleExpressionProperty

**Properties**

| Name                          | Type | Required | Description                     |
| :---------------------------- | :--- | :------- | :------------------------------ |
| EXECUTIONID                   | str  | ✅       | "executionId"                   |
| ATOMID                        | str  | ✅       | "atomId"                        |
| DATEPROCESSED                 | str  | ✅       | "dateProcessed"                 |
| ID                            | str  | ✅       | "id"                            |
| ACTIONTYPE                    | str  | ✅       | "actionType"                    |
| CONNECTORTYPE                 | str  | ✅       | "connectorType"                 |
| CONNECTORNAME                 | str  | ✅       | "connectorName"                 |
| OPERATIONNAME                 | str  | ✅       | "operationName"                 |
| DOCUMENTINDEX                 | str  | ✅       | "documentIndex"                 |
| SUCCESSFUL                    | str  | ✅       | "successful"                    |
| SIZE                          | str  | ✅       | "size"                          |
| ERRORMESSAGE                  | str  | ✅       | "errorMessage"                  |
| VALIDATIONSTATUS              | str  | ✅       | "validationStatus"              |
| VALIDATIONREPORT              | str  | ✅       | "validationReport"              |
| SENDERNAME                    | str  | ✅       | "senderName"                    |
| RECEIVERNAME                  | str  | ✅       | "receiverName"                  |
| MESSAGETYPE                   | str  | ✅       | "messageType"                   |
| DATE                          | str  | ✅       | "date"                          |
| TIME                          | str  | ✅       | "time"                          |
| SENDERTRANSMISSIONREFERENCE   | str  | ✅       | "senderTransmissionReference"   |
| RECEIVERTRANSMISSIONREFERENCE | str  | ✅       | "receiverTransmissionReference" |
| APPLICATIONREFERENCE          | str  | ✅       | "applicationReference"          |
| TRANSMISSIONPRIORITYCODE      | str  | ✅       | "transmissionPriorityCode"      |
| FILEGENERATIONNUMBER          | str  | ✅       | "fileGenerationNumber"          |
| FILEVERSIONNUMBER             | str  | ✅       | "fileVersionNumber"             |

