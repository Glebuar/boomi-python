# DeployedExpiredCertificateSimpleExpression

**Properties**

| Name     | Type                                               | Required | Description |
| :------- | :------------------------------------------------- | :------- | :---------- |
| operator | DeployedExpiredCertificateSimpleExpressionOperator | ✅       |             |
| property | DeployedExpiredCertificateSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                          | ❌       |             |

# DeployedExpiredCertificateSimpleExpressionOperator

**Properties**

| Name            | Type | Required | Description          |
| :-------------- | :--- | :------- | :------------------- |
| LESSTHANOREQUAL | str  | ✅       | "LESS_THAN_OR_EQUAL" |

# DeployedExpiredCertificateSimpleExpressionProperty

**Properties**

| Name               | Type | Required | Description          |
| :----------------- | :--- | :------- | :------------------- |
| CONTAINERID        | str  | ✅       | "containerId"        |
| CONTAINERNAME      | str  | ✅       | "containerName"      |
| ENVIRONMENTID      | str  | ✅       | "environmentId"      |
| ENVIRONMENTNAME    | str  | ✅       | "environmentName"    |
| EXPIRATIONBOUNDARY | str  | ✅       | "expirationBoundary" |

