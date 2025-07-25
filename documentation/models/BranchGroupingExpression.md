# BranchGroupingExpression

**Properties**

| Name              | Type                             | Required | Description |
| :---------------- | :------------------------------- | :------- | :---------- |
| operator          | BranchGroupingExpressionOperator | ✅       |             |
| nested_expression | List[BranchExpression]           | ❌       |             |

# BranchGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

