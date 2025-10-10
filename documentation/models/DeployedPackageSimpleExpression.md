# DeployedPackageSimpleExpression

**Properties**

| Name     | Type                                    | Required | Description |
| :------- | :-------------------------------------- | :------- | :---------- |
| operator | DeployedPackageSimpleExpressionOperator | ✅       |             |
| property | DeployedPackageSimpleExpressionProperty | ✅       |             |
| argument | List[str]                               | ❌       |             |

# DeployedPackageSimpleExpressionOperator

**Properties**

| Name               | Type | Required | Description             |
| :----------------- | :--- | :------- | :---------------------- |
| EQUALS             | str  | ✅       | "EQUALS"                |
| LIKE               | str  | ✅       | "LIKE"                  |
| NOTEQUALS          | str  | ✅       | "NOT_EQUALS"            |
| ISNULL             | str  | ✅       | "IS_NULL"               |
| ISNOTNULL          | str  | ✅       | "IS_NOT_NULL"           |
| BETWEEN            | str  | ✅       | "BETWEEN"               |
| GREATERTHAN        | str  | ✅       | "GREATER_THAN"          |
| GREATERTHANOREQUAL | str  | ✅       | "GREATER_THAN_OR_EQUAL" |
| LESSTHAN           | str  | ✅       | "LESS_THAN"             |
| LESSTHANOREQUAL    | str  | ✅       | "LESS_THAN_OR_EQUAL"    |
| CONTAINS           | str  | ✅       | "CONTAINS"              |
| NOTCONTAINS        | str  | ✅       | "NOT_CONTAINS"          |

# DeployedPackageSimpleExpressionProperty

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| UID              | str  | ✅       | "uid"              |
| NOTES            | str  | ✅       | "notes"            |
| CURRENT          | str  | ✅       | "current"          |
| PACKAGENOTES     | str  | ✅       | "packageNotes"     |
| ACTIVE           | str  | ✅       | "active"           |
| COMPONENTID      | str  | ✅       | "componentId"      |
| COMPONENTVERSION | str  | ✅       | "componentVersion" |
| COMPONENTNAME    | str  | ✅       | "componentName"    |
| COMPONENTTYPE    | str  | ✅       | "componentType"    |
| DEPLOYEDBY       | str  | ✅       | "deployedBy"       |
| DEPLOYEDDATE     | str  | ✅       | "deployedDate"     |
| DEPLOYMENTID     | str  | ✅       | "deploymentId"     |
| ENVIRONMENTID    | str  | ✅       | "environmentId"    |
| ENVIRONMENTNAME  | str  | ✅       | "environmentName"  |
| PACKAGEID        | str  | ✅       | "packageId"        |
| PACKAGEVERSION   | str  | ✅       | "packageVersion"   |
| VERSION          | str  | ✅       | "version"          |
| ACCOUNTID        | str  | ✅       | "accountId"        |
| BRANCH           | str  | ✅       | "branch"           |

