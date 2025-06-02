# DeploymentBulkResponse

**Properties**

| Name     | Type                                 | Required | Description |
| :------- | :----------------------------------- | :------- | :---------- |
| response | List[DeploymentBulkResponseResponse] | ❌       |             |

# DeploymentBulkResponseResponse

**Properties**

| Name          | Type       | Required | Description |
| :------------ | :--------- | :------- | :---------- |
| result        | Deployment | ✅       |             |
| index         | int        | ❌       |             |
| id\_          | str        | ❌       |             |
| status_code   | int        | ❌       |             |
| error_message | str        | ❌       |             |

