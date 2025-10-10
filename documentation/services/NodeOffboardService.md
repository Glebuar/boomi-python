# NodeOffboardService

A list of all methods in the `NodeOffboardService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                 |
| :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_node_offboard](#create_node_offboard) | Employs a POST method to delete a node. After you successfully perform the POST operation, the nodes status immediately changes to `Deleting` on the Cluster Status panel of the interface. |

## create_node_offboard

Employs a POST method to delete a node. After you successfully perform the POST operation, the nodes status immediately changes to `Deleting` on the Cluster Status panel of the interface.

- HTTP Method: `POST`
- Endpoint: `/NodeOffboard`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [NodeOffboard](../models/NodeOffboard.md) | ❌       | The request body. |

**Return Type**

`NodeOffboard`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import NodeOffboard

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = NodeOffboard(
    atom_id="3456789a-bcde-f012-3456-789abcdef012",
    node_id=[
        "nodeId"
    ]
)

result = sdk.node_offboard.create_node_offboard(request_body=request_body)

print(result)
```

