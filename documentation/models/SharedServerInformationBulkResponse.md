# SharedServerInformationBulkResponse

**Properties**

| Name     | Type                                              | Required | Description |
| :------- | :------------------------------------------------ | :------- | :---------- |
| response | List[SharedServerInformationBulkResponseResponse] | ❌       |             |

# SharedServerInformationBulkResponseResponse

**Properties**

| Name          | Type                    | Required | Description |
| :------------ | :---------------------- | :------- | :---------- |
| result        | SharedServerInformation | ✅       |             |
| index         | int                     | ❌       |             |
| id\_          | str                     | ❌       |             |
| status_code   | int                     | ❌       |             |
| error_message | str                     | ❌       |             |

