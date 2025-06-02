# DocumentCountAccountGroupingExpression

**Properties**

| Name              | Type                                           | Required | Description |
| :---------------- | :--------------------------------------------- | :------- | :---------- |
| operator          | DocumentCountAccountGroupingExpressionOperator | ✅       |             |
| nested_expression | List[DocumentCountAccountExpression]           | ❌       |             |

# DocumentCountAccountGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

