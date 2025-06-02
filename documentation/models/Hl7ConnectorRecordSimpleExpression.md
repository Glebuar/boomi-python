# Hl7ConnectorRecordSimpleExpression

**Properties**

| Name     | Type                                       | Required | Description |
| :------- | :----------------------------------------- | :------- | :---------- |
| operator | Hl7ConnectorRecordSimpleExpressionOperator | ✅       |             |
| property | str                                        | ✅       |             |
| argument | List[str]                                  | ❌       |             |

# Hl7ConnectorRecordSimpleExpressionOperator

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

