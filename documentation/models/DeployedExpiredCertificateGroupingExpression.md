# DeployedExpiredCertificateGroupingExpression

**Properties**

| Name              | Type                                                 | Required | Description |
| :---------------- | :--------------------------------------------------- | :------- | :---------- |
| operator          | DeployedExpiredCertificateGroupingExpressionOperator | ✅       |             |
| nested_expression | List[DeployedExpiredCertificateExpression]           | ❌       |             |

# DeployedExpiredCertificateGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

