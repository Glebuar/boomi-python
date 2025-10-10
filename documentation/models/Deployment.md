# Deployment

**Properties**

| Name            | Type                     | Required | Description |
| :-------------- | :----------------------- | :------- | :---------- |
| component_id    | str                      | ✅       |             |
| component_type  | str                      | ✅       |             |
| deployed_by     | str                      | ✅       |             |
| deployed_on     | str                      | ✅       |             |
| digest          | str                      | ✅       |             |
| environment_id  | str                      | ✅       |             |
| id\_            | str                      | ✅       |             |
| notes           | str                      | ✅       |             |
| process_id      | str                      | ✅       |             |
| current         | bool                     | ❌       |             |
| listener_status | DeploymentListenerStatus | ❌       |             |
| message         | str                      | ❌       |             |
| version         | int                      | ❌       |             |

# DeploymentListenerStatus

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| RUNNING | str  | ✅       | "RUNNING"   |
| PAUSED  | str  | ✅       | "PAUSED"    |

