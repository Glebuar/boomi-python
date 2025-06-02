# SharedWebServerBulkResponse

**Properties**

| Name     | Type                                      | Required | Description |
| :------- | :---------------------------------------- | :------- | :---------- |
| response | List[SharedWebServerBulkResponseResponse] | ❌       |             |

# SharedWebServerBulkResponseResponse

**Properties**

| Name          | Type            | Required | Description |
| :------------ | :-------------- | :------- | :---------- |
| result        | SharedWebServer | ✅       |             |
| index         | int             | ❌       |             |
| id\_          | str             | ❌       |             |
| status_code   | int             | ❌       |             |
| error_message | str             | ❌       |             |

