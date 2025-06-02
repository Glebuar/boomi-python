# DocumentCountAccountGroupSimpleExpression

**Properties**

| Name     | Type                                              | Required | Description                                                                                                                                                           |
| :------- | :------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| operator | DocumentCountAccountGroupSimpleExpressionOperator | ✅       | You can use the EQUALS operator only with the `accountGroupId` filter parameter. The authenticating user for a QUERY operation must have the **Dashboard** privilege. |
| property | DocumentCountAccountGroupSimpleExpressionProperty | ✅       |                                                                                                                                                                       |
| argument | List[str]                                         | ❌       |                                                                                                                                                                       |

# DocumentCountAccountGroupSimpleExpressionOperator

You can use the EQUALS operator only with the `accountGroupId` filter parameter. The authenticating user for a QUERY operation must have the **Dashboard** privilege.

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

# DocumentCountAccountGroupSimpleExpressionProperty

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| ACCOUNTGROUPID | str  | ✅       | "accountGroupId" |
| PROCESSDATE    | str  | ✅       | "processDate"    |

