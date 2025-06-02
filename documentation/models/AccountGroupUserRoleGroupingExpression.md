# AccountGroupUserRoleGroupingExpression

**Properties**

| Name              | Type                                           | Required | Description |
| :---------------- | :--------------------------------------------- | :------- | :---------- |
| operator          | AccountGroupUserRoleGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountGroupUserRoleExpression]           | ❌       |             |

# AccountGroupUserRoleGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

