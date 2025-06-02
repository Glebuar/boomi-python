# IntegrationPackEnvironmentAttachmentSimpleExpression

**Properties**

| Name     | Type                                                         | Required | Description |
| :------- | :----------------------------------------------------------- | :------- | :---------- |
| operator | IntegrationPackEnvironmentAttachmentSimpleExpressionOperator | ✅       |             |
| property | IntegrationPackEnvironmentAttachmentSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                                    | ❌       |             |

# IntegrationPackEnvironmentAttachmentSimpleExpressionOperator

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

# IntegrationPackEnvironmentAttachmentSimpleExpressionProperty

**Properties**

| Name                      | Type | Required | Description                 |
| :------------------------ | :--- | :------- | :-------------------------- |
| ENVIRONMENTID             | str  | ✅       | "environmentId"             |
| INTEGRATIONPACKINSTANCEID | str  | ✅       | "integrationPackInstanceId" |

