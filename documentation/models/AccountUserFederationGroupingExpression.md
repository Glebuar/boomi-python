# AccountUserFederationGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | AccountUserFederationGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountUserFederationExpression]           | ❌       |             |

# AccountUserFederationGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

