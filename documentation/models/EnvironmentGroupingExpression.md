# EnvironmentGroupingExpression

**Properties**

| Name              | Type                                  | Required | Description |
| :---------------- | :------------------------------------ | :------- | :---------- |
| operator          | EnvironmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentExpression]           | ❌       |             |

# EnvironmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

