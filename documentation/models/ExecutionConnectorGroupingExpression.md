# ExecutionConnectorGroupingExpression

**Properties**

| Name              | Type                                         | Required | Description |
| :---------------- | :------------------------------------------- | :------- | :---------- |
| operator          | ExecutionConnectorGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ExecutionConnectorExpression]           | ❌       |             |

# ExecutionConnectorGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

