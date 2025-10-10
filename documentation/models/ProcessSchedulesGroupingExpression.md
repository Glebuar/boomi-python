# ProcessSchedulesGroupingExpression

**Properties**

| Name              | Type                                       | Required | Description |
| :---------------- | :----------------------------------------- | :------- | :---------- |
| operator          | ProcessSchedulesGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ProcessSchedulesExpression]           | ❌       |             |

# ProcessSchedulesGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

