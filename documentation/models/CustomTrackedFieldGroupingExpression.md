# CustomTrackedFieldGroupingExpression

**Properties**

| Name              | Type                                         | Required | Description |
| :---------------- | :------------------------------------------- | :------- | :---------- |
| operator          | CustomTrackedFieldGroupingExpressionOperator | ✅       |             |
| nested_expression | List[CustomTrackedFieldExpression]           | ❌       |             |

# CustomTrackedFieldGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

