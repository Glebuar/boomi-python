# ConnectorGroupingExpression

**Properties**

| Name              | Type                                | Required | Description |
| :---------------- | :---------------------------------- | :------- | :---------- |
| operator          | ConnectorGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ConnectorExpression]           | ❌       |             |

# ConnectorGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

