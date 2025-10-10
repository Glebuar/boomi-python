# AtomConnectionFieldExtensionSummaryGroupingExpression

**Properties**

| Name              | Type                                                          | Required | Description |
| :---------------- | :------------------------------------------------------------ | :------- | :---------- |
| operator          | AtomConnectionFieldExtensionSummaryGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AtomConnectionFieldExtensionSummaryExpression]           | ❌       |             |

# AtomConnectionFieldExtensionSummaryGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

