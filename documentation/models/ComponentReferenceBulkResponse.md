# ComponentReferenceBulkResponse

**Properties**

| Name     | Type                                         | Required | Description |
| :------- | :------------------------------------------- | :------- | :---------- |
| response | List[ComponentReferenceBulkResponseResponse] | ❌       |             |

# ComponentReferenceBulkResponseResponse

**Properties**

| Name          | Type               | Required | Description |
| :------------ | :----------------- | :------- | :---------- |
| result        | ComponentReference | ✅       |             |
| index         | int                | ❌       |             |
| id\_          | str                | ❌       |             |
| status_code   | int                | ❌       |             |
| error_message | str                | ❌       |             |

