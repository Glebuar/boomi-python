# ProcessAtomAttachmentGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | ProcessAtomAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ProcessAtomAttachmentExpression]           | ❌       |             |

# ProcessAtomAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

