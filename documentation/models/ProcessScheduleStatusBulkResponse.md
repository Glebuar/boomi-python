# ProcessScheduleStatusBulkResponse

**Properties**

| Name     | Type                                            | Required | Description |
| :------- | :---------------------------------------------- | :------- | :---------- |
| response | List[ProcessScheduleStatusBulkResponseResponse] | ❌       |             |

# ProcessScheduleStatusBulkResponseResponse

**Properties**

| Name          | Type                  | Required | Description |
| :------------ | :-------------------- | :------- | :---------- |
| result        | ProcessScheduleStatus | ✅       |             |
| index         | int                   | ❌       |             |
| id\_          | str                   | ❌       |             |
| status_code   | int                   | ❌       |             |
| error_message | str                   | ❌       |             |

