# EventGroupingExpression

**Properties**

| Name              | Type                            | Required | Description |
| :---------------- | :------------------------------ | :------- | :---------- |
| operator          | EventGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EventExpression]           | ❌       |             |

# EventGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

