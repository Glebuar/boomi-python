# EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression

**Properties**

| Name              | Type                                                                        | Required | Description |
| :---------------- | :-------------------------------------------------------------------------- | :------- | :---------- |
| operator          | EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentMapExtensionUserDefinedFunctionSummaryExpression]           | ❌       |             |

# EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

