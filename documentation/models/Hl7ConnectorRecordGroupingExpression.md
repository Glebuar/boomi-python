# Hl7ConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                         | Required | Description |
| :---------------- | :------------------------------------------- | :------- | :---------- |
| operator          | Hl7ConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[Hl7ConnectorRecordExpression]           | ❌       |             |

# Hl7ConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

