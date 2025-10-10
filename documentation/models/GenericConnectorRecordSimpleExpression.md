# GenericConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                           | Required | Description |
| :------- | :--------------------------------------------- | :------- | :---------- |
| operator | GenericConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | GenericConnectorRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                      | ❌       |             |

# GenericConnectorRecordSimpleExpressionOperator

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| EQUALS | str  | ✅       | "EQUALS"    |

# GenericConnectorRecordSimpleExpressionProperty

**Properties**

| Name                     | Type | Required | Description                |
| :----------------------- | :--- | :------- | :------------------------- |
| ID                       | str  | ✅       | "id"                       |
| EXECUTIONCONNECTORID     | str  | ✅       | "executionConnectorId"     |
| EXECUTIONID              | str  | ✅       | "executionId"              |
| CONNECTIONID             | str  | ✅       | "connectionId"             |
| OPERATIONID              | str  | ✅       | "operationId"              |
| ACTIONTYPE               | str  | ✅       | "actionType"               |
| CONNECTORTYPE            | str  | ✅       | "connectorType"            |
| ATOMID                   | str  | ✅       | "atomId"                   |
| DATEPROCESSED            | str  | ✅       | "dateProcessed"            |
| CONNECTIONNAME           | str  | ✅       | "connectionName"           |
| OPERATIONNAME            | str  | ✅       | "operationName"            |
| ERRORMESSAGE             | str  | ✅       | "errorMessage"             |
| STATUS                   | str  | ✅       | "status"                   |
| DOCUMENTINDEX            | str  | ✅       | "documentIndex"            |
| INCREMENTALDOCUMENTINDEX | str  | ✅       | "incrementalDocumentIndex" |
| SIZE                     | str  | ✅       | "size"                     |
| STARTSHAPE               | str  | ✅       | "startShape"               |
| RETRYABLE                | str  | ✅       | "retryable"                |

