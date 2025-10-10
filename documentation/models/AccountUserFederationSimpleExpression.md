# AccountUserFederationSimpleExpression

**Properties**

| Name     | Type                                          | Required | Description |
| :------- | :-------------------------------------------- | :------- | :---------- |
| operator | AccountUserFederationSimpleExpressionOperator | ✅       |             |
| property | AccountUserFederationSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                     | ❌       |             |

# AccountUserFederationSimpleExpressionOperator

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

# AccountUserFederationSimpleExpressionProperty

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ACCOUNTID    | str  | ✅       | "accountId"    |
| USERID       | str  | ✅       | "userId"       |
| FEDERATIONID | str  | ✅       | "federationId" |

