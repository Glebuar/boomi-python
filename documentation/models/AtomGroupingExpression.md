# AtomGroupingExpression

**Properties**

| Name              | Type                           | Required | Description |
| :---------------- | :----------------------------- | :------- | :---------- |
| operator          | AtomGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AtomExpression]           | ❌       |             |

# AtomGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

