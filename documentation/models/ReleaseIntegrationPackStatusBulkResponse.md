# ReleaseIntegrationPackStatusBulkResponse

**Properties**

| Name     | Type                                                   | Required | Description |
| :------- | :----------------------------------------------------- | :------- | :---------- |
| response | List[ReleaseIntegrationPackStatusBulkResponseResponse] | ❌       |             |

# ReleaseIntegrationPackStatusBulkResponseResponse

**Properties**

| Name          | Type                         | Required | Description |
| :------------ | :--------------------------- | :------- | :---------- |
| result        | ReleaseIntegrationPackStatus | ✅       |             |
| index         | int                          | ❌       |             |
| id\_          | str                          | ❌       |             |
| status_code   | int                          | ❌       |             |
| error_message | str                          | ❌       |             |

