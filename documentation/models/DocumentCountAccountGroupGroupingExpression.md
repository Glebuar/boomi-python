# DocumentCountAccountGroupGroupingExpression

**Properties**

| Name              | Type                                                | Required | Description |
| :---------------- | :-------------------------------------------------- | :------- | :---------- |
| operator          | DocumentCountAccountGroupGroupingExpressionOperator | ✅       |             |
| nested_expression | List[DocumentCountAccountGroupExpression]           | ❌       |             |

# DocumentCountAccountGroupGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

