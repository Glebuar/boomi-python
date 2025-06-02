# ThroughputAccountSimpleExpression

**Properties**

| Name     | Type                                      | Required | Description                                                                                                                                                      |
| :------- | :---------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| operator | ThroughputAccountSimpleExpressionOperator | ✅       | You can only use the EQUALS operator with the `environmentId` filter parameter. The authenticating user for a QUERY operation must have the Dashboard privilege. |
| property | ThroughputAccountSimpleExpressionProperty | ✅       |                                                                                                                                                                  |
| argument | List[str]                                 | ❌       |                                                                                                                                                                  |

# ThroughputAccountSimpleExpressionOperator

You can only use the EQUALS operator with the `environmentId` filter parameter. The authenticating user for a QUERY operation must have the Dashboard privilege.

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

# ThroughputAccountSimpleExpressionProperty

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| ENVIRONMENTID | str  | ✅       | "environmentId" |
| ATOMID        | str  | ✅       | "atomId"        |
| PROCESSDATE   | str  | ✅       | "processDate"   |

