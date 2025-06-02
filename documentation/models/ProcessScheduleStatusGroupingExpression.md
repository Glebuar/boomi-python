# ProcessScheduleStatusGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | ProcessScheduleStatusGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ProcessScheduleStatusExpression]           | ❌       |             |

# ProcessScheduleStatusGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

