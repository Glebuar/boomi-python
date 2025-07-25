# EnvironmentExtensionsGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | EnvironmentExtensionsGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentExtensionsExpression]           | ❌       |             |

# EnvironmentExtensionsGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

