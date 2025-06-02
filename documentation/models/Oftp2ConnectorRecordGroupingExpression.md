# Oftp2ConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                           | Required | Description |
| :---------------- | :--------------------------------------------- | :------- | :---------- |
| operator          | Oftp2ConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[Oftp2ConnectorRecordExpression]           | ❌       |             |

# Oftp2ConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

