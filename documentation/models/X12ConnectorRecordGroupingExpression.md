# X12ConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                         | Required | Description |
| :---------------- | :------------------------------------------- | :------- | :---------- |
| operator          | X12ConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[X12ConnectorRecordExpression]           | ❌       |             |

# X12ConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

