# OdetteConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                            | Required | Description |
| :---------------- | :---------------------------------------------- | :------- | :---------- |
| operator          | OdetteConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[OdetteConnectorRecordExpression]           | ❌       |             |

# OdetteConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

