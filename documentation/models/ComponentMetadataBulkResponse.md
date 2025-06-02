# ComponentMetadataBulkResponse

**Properties**

| Name     | Type                                        | Required | Description |
| :------- | :------------------------------------------ | :------- | :---------- |
| response | List[ComponentMetadataBulkResponseResponse] | ❌       |             |

# ComponentMetadataBulkResponseResponse

**Properties**

| Name          | Type              | Required | Description |
| :------------ | :---------------- | :------- | :---------- |
| result        | ComponentMetadata | ✅       |             |
| index         | int               | ❌       |             |
| id\_          | str               | ❌       |             |
| status_code   | int               | ❌       |             |
| error_message | str               | ❌       |             |

