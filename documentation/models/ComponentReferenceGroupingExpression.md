# ComponentReferenceGroupingExpression

**Properties**

| Name              | Type                                         | Required | Description |
| :---------------- | :------------------------------------------- | :------- | :---------- |
| operator          | ComponentReferenceGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ComponentReferenceExpression]           | ❌       |             |

# ComponentReferenceGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

