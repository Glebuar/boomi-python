# ExecutionCountAccountGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | ExecutionCountAccountGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ExecutionCountAccountExpression]           | ❌       |             |

# ExecutionCountAccountGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

