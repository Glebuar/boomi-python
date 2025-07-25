# ConnectorBulkResponse

**Properties**

| Name     | Type                                | Required | Description |
| :------- | :---------------------------------- | :------- | :---------- |
| response | List[ConnectorBulkResponseResponse] | ❌       |             |

# ConnectorBulkResponseResponse

**Properties**

| Name          | Type      | Required | Description |
| :------------ | :-------- | :------- | :---------- |
| result        | Connector | ✅       |             |
| index         | int       | ❌       |             |
| id\_          | str       | ❌       |             |
| status_code   | int       | ❌       |             |
| error_message | str       | ❌       |             |

