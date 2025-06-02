# FolderGroupingExpression

**Properties**

| Name              | Type                             | Required | Description |
| :---------------- | :------------------------------- | :------- | :---------- |
| operator          | FolderGroupingExpressionOperator | ✅       |             |
| nested_expression | List[FolderExpression]           | ❌       |             |

# FolderGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

