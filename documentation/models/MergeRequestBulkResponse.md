# MergeRequestBulkResponse

**Properties**

| Name     | Type                                   | Required | Description |
| :------- | :------------------------------------- | :------- | :---------- |
| response | List[MergeRequestBulkResponseResponse] | ❌       |             |

# MergeRequestBulkResponseResponse

**Properties**

| Name          | Type         | Required | Description |
| :------------ | :----------- | :------- | :---------- |
| result        | MergeRequest | ✅       |             |
| index         | int          | ❌       |             |
| id\_          | str          | ❌       |             |
| status_code   | int          | ❌       |             |
| error_message | str          | ❌       |             |

