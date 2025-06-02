# EnvironmentConnectionFieldExtensionSummaryGroupingExpression

**Properties**

| Name              | Type                                                                 | Required | Description |
| :---------------- | :------------------------------------------------------------------- | :------- | :---------- |
| operator          | EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentConnectionFieldExtensionSummaryExpression]           | ❌       |             |

# EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

