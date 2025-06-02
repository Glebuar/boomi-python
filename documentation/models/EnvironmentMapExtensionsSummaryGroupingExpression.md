# EnvironmentMapExtensionsSummaryGroupingExpression

**Properties**

| Name              | Type                                                      | Required | Description |
| :---------------- | :-------------------------------------------------------- | :------- | :---------- |
| operator          | EnvironmentMapExtensionsSummaryGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentMapExtensionsSummaryExpression]           | ❌       |             |

# EnvironmentMapExtensionsSummaryGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

