# ComponentAtomAttachmentGroupingExpression

**Properties**

| Name              | Type                                              | Required | Description |
| :---------------- | :------------------------------------------------ | :------- | :---------- |
| operator          | ComponentAtomAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ComponentAtomAttachmentExpression]           | ❌       |             |

# ComponentAtomAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

