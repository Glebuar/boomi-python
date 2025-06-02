# EnvironmentAtomAttachmentGroupingExpression

**Properties**

| Name              | Type                                                | Required | Description |
| :---------------- | :-------------------------------------------------- | :------- | :---------- |
| operator          | EnvironmentAtomAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentAtomAttachmentExpression]           | ❌       |             |

# EnvironmentAtomAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

