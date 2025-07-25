# OdetteConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                          | Required | Description                                                         |
| :------- | :-------------------------------------------- | :------- | :------------------------------------------------------------------ |
| operator | OdetteConnectorRecordSimpleExpressionOperator | ✅       | The STARTS_WITH operator accepts values that do not include spaces. |
| property | str                                           | ✅       |                                                                     |
| argument | List[str]                                     | ❌       |                                                                     |

# OdetteConnectorRecordSimpleExpressionOperator

The STARTS_WITH operator accepts values that do not include spaces.

**Properties**

| Name               | Type | Required | Description             |
| :----------------- | :--- | :------- | :---------------------- |
| EQUALS             | str  | ✅       | "EQUALS"                |
| STARTSWITH         | str  | ✅       | "STARTS_WITH"           |
| BETWEEN            | str  | ✅       | "BETWEEN"               |
| GREATERTHAN        | str  | ✅       | "GREATER_THAN"          |
| GREATERTHANOREQUAL | str  | ✅       | "GREATER_THAN_OR_EQUAL" |
| LESSTHAN           | str  | ✅       | "LESS_THAN"             |
| LESSTHANOREQUAL    | str  | ✅       | "LESS_THAN_OR_EQUAL"    |

