# ComponentMetadataGroupingExpression

**Properties**

| Name              | Type                                        | Required | Description |
| :---------------- | :------------------------------------------ | :------- | :---------- |
| operator          | ComponentMetadataGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ComponentMetadataExpression]           | ❌       |             |

# ComponentMetadataGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

