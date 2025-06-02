# EdifactConnectorRecordGroupingExpression

**Properties**

| Name              | Type                                             | Required | Description |
| :---------------- | :----------------------------------------------- | :------- | :---------- |
| operator          | EdifactConnectorRecordGroupingExpressionOperator | ✅       |             |
| nested_expression | List[EdifactConnectorRecordExpression]           | ❌       |             |

# EdifactConnectorRecordGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

