# IntegrationPackInstanceGroupingExpression

**Properties**

| Name              | Type                                              | Required | Description |
| :---------------- | :------------------------------------------------ | :------- | :---------- |
| operator          | IntegrationPackInstanceGroupingExpressionOperator | ✅       |             |
| nested_expression | List[IntegrationPackInstanceExpression]           | ❌       |             |

# IntegrationPackInstanceGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

