# IntegrationPackAtomAttachmentGroupingExpression

**Properties**

| Name              | Type                                                    | Required | Description |
| :---------------- | :------------------------------------------------------ | :------- | :---------- |
| operator          | IntegrationPackAtomAttachmentGroupingExpressionOperator | ✅       |             |
| nested_expression | List[IntegrationPackAtomAttachmentExpression]           | ❌       |             |

# IntegrationPackAtomAttachmentGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |

