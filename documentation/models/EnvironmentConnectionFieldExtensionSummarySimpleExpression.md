# EnvironmentConnectionFieldExtensionSummarySimpleExpression

**Properties**

| Name     | Type                                                               | Required | Description                                                                                                                                                                                                              |
| :------- | :----------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| operator | EnvironmentConnectionFieldExtensionSummarySimpleExpressionOperator | ✅       |                                                                                                                                                                                                                          |
| property | EnvironmentConnectionFieldExtensionSummarySimpleExpressionProperty | ✅       | All filters are required except for extensionGroupId, which is for a multi-install integration pack only. You can obtain valid values for each filter by using the QUERY operation on the Environment Extensions object. |
| argument | List[str]                                                          | ❌       |                                                                                                                                                                                                                          |

# EnvironmentConnectionFieldExtensionSummarySimpleExpressionOperator

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

# EnvironmentConnectionFieldExtensionSummarySimpleExpressionProperty

All filters are required except for extensionGroupId, which is for a multi-install integration pack only. You can obtain valid values for each filter by using the QUERY operation on the Environment Extensions object.

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| ENVIRONMENTID    | str  | ✅       | "environmentId"    |
| EXTENSIONGROUPID | str  | ✅       | "extensionGroupId" |
| CONNECTIONID     | str  | ✅       | "connectionId"     |
| FIELDID          | str  | ✅       | "fieldId"          |

