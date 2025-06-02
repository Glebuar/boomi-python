# As2ConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                         | Required | Description |
| :---------------- | :------------------------------------------- | :------- | :---------- |
| operator          | As2ConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[As2ConnectorRecordExpression]           | ❌       |             |

# As2ConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

