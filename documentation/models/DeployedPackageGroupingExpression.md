# DeployedPackageGroupingExpression

**Properties**

| Name              | Type                                      | Required | Description |
| :---------------- | :---------------------------------------- | :------- | :---------- |
| operator          | DeployedPackageGroupingExpressionOperator | ✅       |             |
| nested_expression | List[DeployedPackageExpression]           | ❌       |             |

# DeployedPackageGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

