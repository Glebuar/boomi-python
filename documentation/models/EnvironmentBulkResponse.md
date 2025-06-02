# EnvironmentBulkResponse

**Properties**

| Name     | Type                                  | Required | Description |
| :------- | :------------------------------------ | :------- | :---------- |
| response | List[EnvironmentBulkResponseResponse] | ❌       |             |

# EnvironmentBulkResponseResponse

**Properties**

| Name          | Type        | Required | Description |
| :------------ | :---------- | :------- | :---------- |
| result        | Environment | ✅       |             |
| index         | int         | ❌       |             |
| id\_          | str         | ❌       |             |
| status_code   | int         | ❌       |             |
| error_message | str         | ❌       |             |

