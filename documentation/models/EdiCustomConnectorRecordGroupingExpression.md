# EdiCustomConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                               | Required | Description |
| :---------------- | :------------------------------------------------- | :------- | :---------- |
| operator          | EdiCustomConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EdiCustomConnectorRecordExpression]           | ❌       |             |

# EdiCustomConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

