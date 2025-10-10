# AccountGroupAccountGroupingExpression

**Properties**

| Name              | Type                                          | Required | Description |
| :---------------- | :-------------------------------------------- | :------- | :---------- |
| operator          | AccountGroupAccountGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountGroupAccountExpression]           | ❌       |             |

# AccountGroupAccountGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

