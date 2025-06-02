# ProcessEnvironmentAttachmentGroupingExpression

**Properties**

| Name              | Type                                                   | Required | Description |
| :---------------- | :----------------------------------------------------- | :------- | :---------- |
| operator          | ProcessEnvironmentAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ProcessEnvironmentAttachmentExpression]           | ❌       |             |

# ProcessEnvironmentAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

