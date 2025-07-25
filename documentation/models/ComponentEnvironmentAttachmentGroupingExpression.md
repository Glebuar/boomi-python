# ComponentEnvironmentAttachmentGroupingExpression

**Properties**

| Name              | Type                                                     | Required | Description |
| :---------------- | :------------------------------------------------------- | :------- | :---------- |
| operator          | ComponentEnvironmentAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ComponentEnvironmentAttachmentExpression]           | ❌       |             |

# ComponentEnvironmentAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

