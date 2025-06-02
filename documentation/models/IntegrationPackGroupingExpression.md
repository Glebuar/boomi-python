# IntegrationPackGroupingExpression

**Properties**

| Name              | Type                                      | Required | Description |
| :---------------- | :---------------------------------------- | :------- | :---------- |
| operator          | IntegrationPackGroupingExpressionOperator | ✅       |             |
| nested_expression | List[IntegrationPackExpression]           | ❌       |             |

# IntegrationPackGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

