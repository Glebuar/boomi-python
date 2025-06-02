# IntegrationPackEnvironmentAttachmentGroupingExpression

**Properties**

| Name              | Type                                                           | Required | Description |
| :---------------- | :------------------------------------------------------------- | :------- | :---------- |
| operator          | IntegrationPackEnvironmentAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[IntegrationPackEnvironmentAttachmentExpression]           | ❌       |             |

# IntegrationPackEnvironmentAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

