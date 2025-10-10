# Oftp2ConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                         | Required | Description |
| :------- | :------------------------------------------- | :------- | :---------- |
| operator | Oftp2ConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | Oftp2ConnectorRecordSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                    | ❌       |             |

# Oftp2ConnectorRecordSimpleExpressionOperator

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

# Oftp2ConnectorRecordSimpleExpressionProperty

**Properties**

| Name              | Type | Required | Description          |
| :---------------- | :--- | :------- | :------------------- |
| SFIDDSN           | str  | ✅       | "sfiddsn"            |
| SFIDDATE          | str  | ✅       | "sfiddate"           |
| SFIDTIME          | str  | ✅       | "sfidtime"           |
| SFIDDEST          | str  | ✅       | "sfiddest"           |
| INITIATORSSIDCODE | str  | ✅       | "initiator_ssidcode" |
| RESPONDERSSIDCODE | str  | ✅       | "responder_ssidcode" |
| SFIDORIG          | str  | ✅       | "sfidorig"           |
| SFIDSEC           | str  | ✅       | "sfidsec"            |
| SFIDCOMP          | str  | ✅       | "sfidcomp"           |
| SFIDCIPH          | str  | ✅       | "sfidciph"           |
| SFIDDESC          | str  | ✅       | "sfiddesc"           |
| SFIDSIGN          | str  | ✅       | "sfidsign"           |
| SFIDOSIZ          | str  | ✅       | "sfidosiz"           |
| SFIDENV           | str  | ✅       | "sfidenv"            |
| STATUS            | str  | ✅       | "status"             |
| ACCOUNT           | str  | ✅       | "account"            |
| EXECUTIONID       | str  | ✅       | "executionId"        |
| ATOMID            | str  | ✅       | "atomId"             |
| DATEPROCESSED     | str  | ✅       | "dateProcessed"      |
| ID                | str  | ✅       | "id"                 |
| ACTIONTYPE        | str  | ✅       | "actionType"         |
| CONNECTORTYPE     | str  | ✅       | "connectorType"      |
| CONNECTORNAME     | str  | ✅       | "connectorName"      |
| OPERATIONNAME     | str  | ✅       | "operationName"      |
| DOCUMENTINDEX     | str  | ✅       | "documentIndex"      |
| SUCCESSFUL        | str  | ✅       | "successful"         |
| SIZE              | str  | ✅       | "size"               |
| CUSTOMFIELDS      | str  | ✅       | "customFields"       |
| NAREAS            | str  | ✅       | "nareas"             |
| NAREAST           | str  | ✅       | "nareast"            |

