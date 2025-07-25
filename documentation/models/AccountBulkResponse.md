# AccountBulkResponse

**Properties**

| Name     | Type                              | Required | Description |
| :------- | :-------------------------------- | :------- | :---------- |
| response | List[AccountBulkResponseResponse] | ❌       |             |

# AccountBulkResponseResponse

**Properties**

| Name          | Type    | Required | Description |
| :------------ | :------ | :------- | :---------- |
| result        | Account | ✅       |             |
| index         | int     | ❌       |             |
| id\_          | str     | ❌       |             |
| status_code   | int     | ❌       |             |
| error_message | str     | ❌       |             |

