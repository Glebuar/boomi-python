# TradingPartnerProcessingGroupGroupingExpression

**Properties**

| Name              | Type                                                    | Required | Description |
| :---------------- | :------------------------------------------------------ | :------- | :---------- |
| operator          | TradingPartnerProcessingGroupGroupingExpressionOperator | ✅       |             |
| nested_expression | List[TradingPartnerProcessingGroupExpression]           | ❌       |             |

# TradingPartnerProcessingGroupGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

