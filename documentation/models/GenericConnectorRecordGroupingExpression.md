# GenericConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                             | Required | Description |
| :---------------- | :----------------------------------------------- | :------- | :---------- |
| operator          | GenericConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[GenericConnectorRecordExpression]           | ❌       |             |

# GenericConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

