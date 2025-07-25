# DeploymentGroupingExpression

**Properties**

| Name              | Type                                 | Required | Description |
| :---------------- | :----------------------------------- | :------- | :---------- |
| operator          | DeploymentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[DeploymentExpression]           | ❌       |             |

# DeploymentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

