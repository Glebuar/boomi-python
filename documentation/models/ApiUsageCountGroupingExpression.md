# ApiUsageCountGroupingExpression

**Properties**

| Name              | Type                                    | Required | Description |
| :---------------- | :-------------------------------------- | :------- | :---------- |
| operator          | ApiUsageCountGroupingExpressionOperator | ✅       |             |
| nested_expression | List[ApiUsageCountExpression]           | ❌       |             |

# ApiUsageCountGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

