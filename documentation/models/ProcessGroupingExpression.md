# ProcessGroupingExpression

**Properties**

| Name              | Type                              | Required | Description |
| :---------------- | :-------------------------------- | :------- | :---------- |
| operator          | ProcessGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ProcessExpression]           | ❌       |             |

# ProcessGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

