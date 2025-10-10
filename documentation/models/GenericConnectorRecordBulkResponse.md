# GenericConnectorRecordBulkResponse

**Properties**

| Name     | Type                                             | Required | Description |
| :------- | :----------------------------------------------- | :------- | :---------- |
| response | List[GenericConnectorRecordBulkResponseResponse] | ❌       |             |

# GenericConnectorRecordBulkResponseResponse

**Properties**

| Name          | Type                   | Required | Description |
| :------------ | :--------------------- | :------- | :---------- |
| result        | GenericConnectorRecord | ✅       |             |
| index         | int                    | ❌       |             |
| id\_          | str                    | ❌       |             |
| status_code   | int                    | ❌       |             |
| error_message | str                    | ❌       |             |

