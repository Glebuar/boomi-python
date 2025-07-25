# PackagedComponentGroupingExpression

**Properties**

| Name              | Type                                        | Required | Description |
| :---------------- | :------------------------------------------ | :------- | :---------- |
| operator          | PackagedComponentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[PackagedComponentExpression]           | ❌       |             |

# PackagedComponentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

