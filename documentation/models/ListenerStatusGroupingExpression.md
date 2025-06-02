# ListenerStatusGroupingExpression

**Properties**

| Name              | Type                                     | Required | Description |
| :---------------- | :--------------------------------------- | :------- | :---------- |
| operator          | ListenerStatusGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ListenerStatusExpression]           | ❌       |             |

# ListenerStatusGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

