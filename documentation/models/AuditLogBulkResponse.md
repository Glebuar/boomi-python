# AuditLogBulkResponse

**Properties**

| Name     | Type                               | Required | Description |
| :------- | :--------------------------------- | :------- | :---------- |
| response | List[AuditLogBulkResponseResponse] | ❌       |             |

# AuditLogBulkResponseResponse

**Properties**

| Name          | Type     | Required | Description |
| :------------ | :------- | :------- | :---------- |
| result        | AuditLog | ✅       |             |
| index         | int      | ❌       |             |
| id\_          | str      | ❌       |             |
| status_code   | int      | ❌       |             |
| error_message | str      | ❌       |             |

