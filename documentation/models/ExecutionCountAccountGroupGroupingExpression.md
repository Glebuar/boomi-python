# ExecutionCountAccountGroupGroupingExpression

**Properties**

| Name              | Type                                                 | Required | Description |
| :---------------- | :--------------------------------------------------- | :------- | :---------- |
| operator          | ExecutionCountAccountGroupGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ExecutionCountAccountGroupExpression]           | ❌       |             |

# ExecutionCountAccountGroupGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

