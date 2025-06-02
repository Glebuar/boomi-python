# EnvironmentMapExtensionExternalComponentGroupingExpression

**Properties**

| Name              | Type                                                               | Required | Description |
| :---------------- | :----------------------------------------------------------------- | :------- | :---------- |
| operator          | EnvironmentMapExtensionExternalComponentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentMapExtensionExternalComponentExpression]           | ❌       |             |

# EnvironmentMapExtensionExternalComponentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

