# As2ConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                       | Required | Description |
| :------- | :----------------------------------------- | :------- | :---------- |
| operator | As2ConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | str                                        | ✅       |             |
| argument | List[str]                                  | ❌       |             |

# As2ConnectorRecordSimpleExpressionOperator

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

