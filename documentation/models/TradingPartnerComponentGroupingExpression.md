# TradingPartnerComponentGroupingExpression

**Properties**

| Name              | Type                                              | Required | Description |
| :---------------- | :------------------------------------------------ | :------- | :---------- |
| operator          | TradingPartnerComponentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[TradingPartnerComponentExpression]           | ❌       |             |

# TradingPartnerComponentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

