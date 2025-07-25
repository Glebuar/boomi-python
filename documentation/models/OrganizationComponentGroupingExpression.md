# OrganizationComponentGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | OrganizationComponentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[OrganizationComponentExpression]           | ❌       |             |

# OrganizationComponentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

