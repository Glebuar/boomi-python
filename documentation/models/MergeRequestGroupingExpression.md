# MergeRequestGroupingExpression

**Properties**

| Name              | Type                                   | Required | Description |
| :---------------- | :------------------------------------- | :------- | :---------- |
| operator          | MergeRequestGroupingExpressionOperator | ✅       |             |
| nested_expression | List[MergeRequestExpression]           | ❌       |             |

# MergeRequestGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

