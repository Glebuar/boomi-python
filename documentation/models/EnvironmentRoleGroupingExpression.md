# EnvironmentRoleGroupingExpression

**Properties**

| Name              | Type                                      | Required | Description |
| :---------------- | :---------------------------------------- | :------- | :---------- |
| operator          | EnvironmentRoleGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EnvironmentRoleExpression]           | ❌       |             |

# EnvironmentRoleGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

