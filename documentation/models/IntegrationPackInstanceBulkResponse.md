# IntegrationPackInstanceBulkResponse

**Properties**

| Name     | Type                                              | Required | Description |
| :------- | :------------------------------------------------ | :------- | :---------- |
| response | List[IntegrationPackInstanceBulkResponseResponse] | ❌       |             |

# IntegrationPackInstanceBulkResponseResponse

**Properties**

| Name          | Type                    | Required | Description |
| :------------ | :---------------------- | :------- | :---------- |
| result        | IntegrationPackInstance | ✅       |             |
| index         | int                     | ❌       |             |
| id\_          | str                     | ❌       |             |
| status_code   | int                     | ❌       |             |
| error_message | str                     | ❌       |             |

