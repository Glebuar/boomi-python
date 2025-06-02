# TradingPartnerComponentSimpleExpression

**Properties**

| Name     | Type                                            | Required | Description |
| :------- | :---------------------------------------------- | :------- | :---------- |
| operator | TradingPartnerComponentSimpleExpressionOperator | ✅       |             |
| property | TradingPartnerComponentSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                       | ❌       |             |

# TradingPartnerComponentSimpleExpressionOperator

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

# TradingPartnerComponentSimpleExpressionProperty

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| NAME           | str  | ✅       | "name"           |
| CLASSIFICATION | str  | ✅       | "classification" |
| STANDARD       | str  | ✅       | "standard"       |
| IDENTIFIER     | str  | ✅       | "identifier"     |
| AS2            | str  | ✅       | "as2"            |
| DISK           | str  | ✅       | "disk"           |
| FTP            | str  | ✅       | "ftp"            |
| MLLP           | str  | ✅       | "mllp"           |
| SFTP           | str  | ✅       | "sftp"           |
| HTTP           | str  | ✅       | "http"           |
| OFTP           | str  | ✅       | "oftp"           |

