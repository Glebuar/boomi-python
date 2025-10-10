# EdifactConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                           | Required | Description |
| :------- | :--------------------------------------------- | :------- | :---------- |
| operator | EdifactConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | EdifactConnectorRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                      | ❌       |             |

# EdifactConnectorRecordSimpleExpressionOperator

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

# EdifactConnectorRecordSimpleExpressionProperty

**Properties**

| Name                        | Type | Required | Description                   |
| :-------------------------- | :--- | :------- | :---------------------------- |
| EXECUTIONID                 | str  | ✅       | "executionId"                 |
| ATOMID                      | str  | ✅       | "atomId"                      |
| DATEPROCESSED               | str  | ✅       | "dateProcessed"               |
| ID                          | str  | ✅       | "id"                          |
| ACTIONTYPE                  | str  | ✅       | "actionType"                  |
| CONNECTORTYPE               | str  | ✅       | "connectorType"               |
| CONNECTORNAME               | str  | ✅       | "connectorName"               |
| OPERATIONNAME               | str  | ✅       | "operationName"               |
| DOCUMENTINDEX               | str  | ✅       | "documentIndex"               |
| SUCCESSFUL                  | str  | ✅       | "successful"                  |
| SIZE                        | str  | ✅       | "size"                        |
| ERRORMESSAGE                | str  | ✅       | "errorMessage"                |
| ACKSTATUS                   | str  | ✅       | "ackStatus"                   |
| ACKREPORT                   | str  | ✅       | "ackReport"                   |
| SENDERID                    | str  | ✅       | "senderID"                    |
| RECEIVERID                  | str  | ✅       | "receiverID"                  |
| INTERCHANGECONTROLREFERENCE | str  | ✅       | "interchangeControlReference" |
| MESSAGETYPE                 | str  | ✅       | "messageType"                 |
| MESSAGEREFERENCENUMBER      | str  | ✅       | "messageReferenceNumber"      |
| INTERCHANGEDATE             | str  | ✅       | "interchangeDate"             |
| INTERCHANGETIME             | str  | ✅       | "interchangeTime"             |
| ACKREQUESTED                | str  | ✅       | "ackRequested"                |
| OUTBOUNDVALIDATIONSTATUS    | str  | ✅       | "outboundValidationStatus"    |
| OUTBOUNDVALIDATIONREPORT    | str  | ✅       | "outboundValidationReport"    |

