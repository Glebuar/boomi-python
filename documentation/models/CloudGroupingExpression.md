# CloudGroupingExpression

**Properties**

| Name              | Type                            | Required | Description |
| :---------------- | :------------------------------ | :------- | :---------- |
| operator          | CloudGroupingExpressionOperator | ✅       |             |
| nested_expression | List[CloudExpression]           | ❌       |             |

# CloudGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

