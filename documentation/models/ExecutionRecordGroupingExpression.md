# ExecutionRecordGroupingExpression

**Properties**

| Name              | Type                                      | Required | Description |
| :---------------- | :---------------------------------------- | :------- | :---------- |
| operator          | ExecutionRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ExecutionRecordExpression]           | ❌       |             |

# ExecutionRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

