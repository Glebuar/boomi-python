# ThroughputAccountGroupingExpression

**Properties**

| Name              | Type                                        | Required | Description |
| :---------------- | :------------------------------------------ | :------- | :---------- |
| operator          | ThroughputAccountGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ThroughputAccountExpression]           | ❌       |             |

# ThroughputAccountGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

