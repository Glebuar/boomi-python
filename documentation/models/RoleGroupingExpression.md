# RoleGroupingExpression

**Properties**

| Name              | Type                           | Required | Description |
| :---------------- | :----------------------------- | :------- | :---------- |
| operator          | RoleGroupingExpressionOperator | ✅       |             |
| nested_expression | List[RoleExpression]           | ❌       |             |

# RoleGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

