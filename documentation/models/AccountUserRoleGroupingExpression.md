# AccountUserRoleGroupingExpression

**Properties**

| Name              | Type                                      | Required | Description |
| :---------------- | :---------------------------------------- | :------- | :---------- |
| operator          | AccountUserRoleGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountUserRoleExpression]           | ❌       |             |

# AccountUserRoleGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

