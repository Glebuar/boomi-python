# RosettaNetConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                                | Required | Description |
| :---------------- | :-------------------------------------------------- | :------- | :---------- |
| operator          | RosettaNetConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[RosettaNetConnectorRecordExpression]           | ❌       |             |

# RosettaNetConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

