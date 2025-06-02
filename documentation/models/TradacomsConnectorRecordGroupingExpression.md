# TradacomsConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                               | Required | Description |
| :---------------- | :------------------------------------------------- | :------- | :---------- |
| operator          | TradacomsConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[TradacomsConnectorRecordExpression]           | ❌       |             |

# TradacomsConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

