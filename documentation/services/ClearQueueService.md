# ClearQueueService

A list of all methods in the `ClearQueueService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [execute_clear_queue](#execute_clear_queue) | - When you run the Clear queue messages action, it deletes all messages in a queue name from the queue. Note that this clears all messages in the queue; you cannot select and remove individual messages using this action. In addition, the action overrides any purge settings you might configure in the user interface. - The immediate response indicates success in passing the request to the Runtime. - If the specified Runtime queue does not contain any messages to clear, the response only returns a success message stating that the message passed even though there is no action taken on the Runtime. - You can use the Get queue list API action to retrieve the number of messages in a queue, which works as an alternative way to check if the clear queue message action succeeded on the Runtime. |

## execute_clear_queue

- When you run the Clear queue messages action, it deletes all messages in a queue name from the queue. Note that this clears all messages in the queue; you cannot select and remove individual messages using this action. In addition, the action overrides any purge settings you might configure in the user interface. - The immediate response indicates success in passing the request to the Runtime. - If the specified Runtime queue does not contain any messages to clear, the response only returns a success message stating that the message passed even though there is no action taken on the Runtime. - You can use the Get queue list API action to retrieve the number of messages in a queue, which works as an alternative way to check if the clear queue message action succeeded on the Runtime.

- HTTP Method: `POST`
- Endpoint: `/ClearQueue/execute/{id}`

**Parameters**

| Name         | Type                                                | Required | Description                                                                                                                                                                                                                                                                 |
| :----------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ClearQueueRequest](../models/ClearQueueRequest.md) | ❌       | The request body.                                                                                                                                                                                                                                                           |
| id\_         | str                                                 | ✅       | The unique ID assigned by the system to the container. The Runtime ID for Runtimes, Runtime clusters, and Runtime clouds is found in the user interface by navigating to Manage \> Runtime Management and viewing the Runtime Information panel for the selected container. |

**Return Type**

`ClearQueueRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ClearQueueRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = ClearQueueRequest(
    atom_id="ATOM_ID",
    dlq="false",
    queue_name="QUEUE_NAME",
    subscriber_name="SUBSCRIBER_ID"
)

result = sdk.clear_queue.execute_clear_queue(
    request_body=request_body,
    id_="id"
)

print(result)
```

