# SharedCommunicationChannelComponentGroupingExpression

**Properties**

| Name              | Type                                                          | Required | Description |
| :---------------- | :------------------------------------------------------------ | :------- | :---------- |
| operator          | SharedCommunicationChannelComponentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[SharedCommunicationChannelComponentExpression]           | ❌       |             |

# SharedCommunicationChannelComponentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

