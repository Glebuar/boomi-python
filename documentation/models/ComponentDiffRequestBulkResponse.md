# ComponentDiffRequestBulkResponse

**Properties**

| Name     | Type                                           | Required | Description |
| :------- | :--------------------------------------------- | :------- | :---------- |
| response | List[ComponentDiffRequestBulkResponseResponse] | ❌       |             |

# ComponentDiffRequestBulkResponseResponse

**Properties**

| Name          | Type                 | Required | Description |
| :------------ | :------------------- | :------- | :---------- |
| result        | ComponentDiffRequest | ✅       |             |
| index         | int                  | ❌       |             |
| id\_          | str                  | ❌       |             |
| status_code   | int                  | ❌       |             |
| error_message | str                  | ❌       |             |

