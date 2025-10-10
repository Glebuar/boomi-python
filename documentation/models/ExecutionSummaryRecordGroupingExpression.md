# ExecutionSummaryRecordGroupingExpression

**Properties**

| Name              | Type                                             | Required | Description |
| :---------------- | :----------------------------------------------- | :------- | :---------- |
| operator          | ExecutionSummaryRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ExecutionSummaryRecordExpression]           | ❌       |             |

# ExecutionSummaryRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

