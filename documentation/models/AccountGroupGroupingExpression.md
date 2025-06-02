# AccountGroupGroupingExpression

**Properties**

| Name              | Type                                   | Required | Description |
| :---------------- | :------------------------------------- | :------- | :---------- |
| operator          | AccountGroupGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountGroupExpression]           | ❌       |             |

# AccountGroupGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

