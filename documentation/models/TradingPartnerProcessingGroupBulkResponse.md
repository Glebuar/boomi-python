# TradingPartnerProcessingGroupBulkResponse

**Properties**

| Name     | Type                                                    | Required | Description |
| :------- | :------------------------------------------------------ | :------- | :---------- |
| response | List[TradingPartnerProcessingGroupBulkResponseResponse] | ❌       |             |

# TradingPartnerProcessingGroupBulkResponseResponse

**Properties**

| Name          | Type                          | Required | Description |
| :------------ | :---------------------------- | :------- | :---------- |
| result        | TradingPartnerProcessingGroup | ✅       |             |
| index         | int                           | ❌       |             |
| id\_          | str                           | ❌       |             |
| status_code   | int                           | ❌       |             |
| error_message | str                           | ❌       |             |

