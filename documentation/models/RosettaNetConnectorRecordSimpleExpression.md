# RosettaNetConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                              | Required | Description |
| :------- | :------------------------------------------------ | :------- | :---------- |
| operator | RosettaNetConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | RosettaNetConnectorRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                         | ❌       |             |

# RosettaNetConnectorRecordSimpleExpressionOperator

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

# RosettaNetConnectorRecordSimpleExpressionProperty

**Properties**

| Name                                    | Type | Required | Description                               |
| :-------------------------------------- | :--- | :------- | :---------------------------------------- |
| EXECUTIONID                             | str  | ✅       | "executionId"                             |
| ATOMID                                  | str  | ✅       | "atomId"                                  |
| DATEPROCESSED                           | str  | ✅       | "dateProcessed"                           |
| ID                                      | str  | ✅       | "id"                                      |
| ACTIONTYPE                              | str  | ✅       | "actionType"                              |
| CONNECTORTYPE                           | str  | ✅       | "connectorType"                           |
| CONNECTORNAME                           | str  | ✅       | "connectorName"                           |
| OPERATIONNAME                           | str  | ✅       | "operationName"                           |
| DOCUMENTINDEX                           | str  | ✅       | "documentIndex"                           |
| SUCCESSFUL                              | str  | ✅       | "successful"                              |
| SIZE                                    | str  | ✅       | "size"                                    |
| ERRORMESSAGE                            | str  | ✅       | "errorMessage"                            |
| ACKSTATUS                               | str  | ✅       | "ackStatus"                               |
| ACKREPORT                               | str  | ✅       | "ackReport"                               |
| SENDERID                                | str  | ✅       | "senderID"                                |
| RECEIVERID                              | str  | ✅       | "receiverID"                              |
| KNOWNINITIATINGPARTNERID                | str  | ✅       | "knownInitiatingPartnerID"                |
| FRAMEWORKVERSION                        | str  | ✅       | "frameworkVersion"                        |
| PIPCODE                                 | str  | ✅       | "PIPCode"                                 |
| PIPVERSION                              | str  | ✅       | "PIPVersion"                              |
| GLOBALPROCESSCODE                       | str  | ✅       | "globalProcessCode"                       |
| GLOBALBUSINESSACTIONCODE                | str  | ✅       | "globalBusinessActionCode"                |
| GLOBALDOCUMENTFUNCTIONCODE              | str  | ✅       | "globalDocumentFunctionCode"              |
| FROMGLOBALPARTNERROLECLASSIFICATIONCODE | str  | ✅       | "fromGlobalPartnerRoleClassificationCode" |
| TOGLOBALPARTNERROLECLASSIFICATIONCODE   | str  | ✅       | "toGlobalPartnerRoleClassificationCode"   |
| FROMGLOBALBUSINESSSERVICECODE           | str  | ✅       | "fromGlobalBusinessServiceCode"           |
| TOGLOBALBUSINESSSERVICECODE             | str  | ✅       | "toGlobalBusinessServiceCode"             |
| BUSINESSACTIVITYIDENTIFIER              | str  | ✅       | "businessActivityIdentifier"              |
| PROCESSINSTANCEIDENTIFIER               | str  | ✅       | "processInstanceIdentifier"               |
| TRANSACTIONINSTANCEIDENTIFIER           | str  | ✅       | "transactionInstanceIdentifier"           |
| ACTIONINSTANCEIDENTIFIER                | str  | ✅       | "actionInstanceIdentifier"                |
| INRESPONSETOGLOBALBUSINESSACTIONCODE    | str  | ✅       | "inResponseToGlobalBusinessActionCode"    |
| INRESPONSETOINSTANCEIDENTIFIER          | str  | ✅       | "inResponseToInstanceIdentifier"          |
| GLOBALUSAGECODE                         | str  | ✅       | "globalUsageCode"                         |
| ATTEMPTCOUNT                            | str  | ✅       | "attemptCount"                            |
| DATETIME                                | str  | ✅       | "dateTime"                                |
| ISSECURETRANSPORTREQUIRED               | str  | ✅       | "isSecureTransportRequired"               |
| TIMETOACKNOWLEDGEACCEPTANCE             | str  | ✅       | "timeToAcknowledgeAcceptance"             |
| TIMETOACKNOWLEDGERECEIPT                | str  | ✅       | "timeToAcknowledgeReceipt"                |
| TIMETOPERFORM                           | str  | ✅       | "timeToPerform"                           |
| OUTBOUNDVALIDATIONSTATUS                | str  | ✅       | "outboundValidationStatus"                |
| OUTBOUNDVALIDATIONREPORT                | str  | ✅       | "outboundValidationReport"                |

