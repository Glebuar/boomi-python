# ProcessSchedulesBulkResponse

**Properties**

| Name     | Type                                       | Required | Description |
| :------- | :----------------------------------------- | :------- | :---------- |
| response | List[ProcessSchedulesBulkResponseResponse] | ❌       |             |

# ProcessSchedulesBulkResponseResponse

**Properties**

| Name          | Type             | Required | Description |
| :------------ | :--------------- | :------- | :---------- |
| result        | ProcessSchedules | ✅       |             |
| index         | int              | ❌       |             |
| id\_          | str              | ❌       |             |
| status_code   | int              | ❌       |             |
| error_message | str              | ❌       |             |

