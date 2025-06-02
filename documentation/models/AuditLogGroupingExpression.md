# AuditLogGroupingExpression

**Properties**

| Name              | Type                               | Required | Description |
| :---------------- | :--------------------------------- | :------- | :---------- |
| operator          | AuditLogGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AuditLogExpression]           | ❌       |             |

# AuditLogGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

