# ThroughputAccountGroupGroupingExpression

**Properties**

| Name              | Type                                             | Required | Description |
| :---------------- | :----------------------------------------------- | :------- | :---------- |
| operator          | ThroughputAccountGroupGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ThroughputAccountGroupExpression]           | ❌       |             |

# ThroughputAccountGroupGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

