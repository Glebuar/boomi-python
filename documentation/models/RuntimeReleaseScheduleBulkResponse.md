# RuntimeReleaseScheduleBulkResponse

**Properties**

| Name     | Type                                             | Required | Description |
| :------- | :----------------------------------------------- | :------- | :---------- |
| response | List[RuntimeReleaseScheduleBulkResponseResponse] | ❌       |             |

# RuntimeReleaseScheduleBulkResponseResponse

**Properties**

| Name          | Type                   | Required | Description |
| :------------ | :--------------------- | :------- | :---------- |
| result        | RuntimeReleaseSchedule | ✅       |             |
| index         | int                    | ❌       |             |
| id\_          | str                    | ❌       |             |
| status_code   | int                    | ❌       |             |
| error_message | str                    | ❌       |             |

