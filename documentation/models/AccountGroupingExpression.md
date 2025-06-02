# AccountGroupingExpression

**Properties**

| Name              | Type                              | Required | Description |
| :---------------- | :-------------------------------- | :------- | :---------- |
| operator          | AccountGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountExpression]           | ❌       |             |

# AccountGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

