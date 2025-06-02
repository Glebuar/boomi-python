# MoveQueueRequestService

A list of all methods in the `MoveQueueRequestService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_move_queue_request](#create_move_queue_request) | Moves messages from one Runtime queue to another. - You must have the **Runtime Management** privilege to use the Move queue request operation. - You can only move messages between queues of the same type. For example, moving queue messages from a point-to-point queue to a _Publish/Subscribe_ queue results in an error. - Any Runtime queues that you specify in the request must currently exist on the Runtime. For clarification, you cannot create a new endpoint using the CREATE operation. - You must supply the _AtomID_, _SourceQueue_, _QueueName_, _DLQ_, and _DestinationQueue_ fields in the request. - If the operation returns an error, it logs a message in the Runtime, Runtime cluster, or Runtime cloud, but is not sent to the platform. - You cannot track move updates directly through this operation. Instead, to see if the action is in progress or complete, use the Queue Management API or the ListQueues API to observe the number of messages in the queue. |

## create_move_queue_request

Moves messages from one Runtime queue to another. - You must have the **Runtime Management** privilege to use the Move queue request operation. - You can only move messages between queues of the same type. For example, moving queue messages from a point-to-point queue to a _Publish/Subscribe_ queue results in an error. - Any Runtime queues that you specify in the request must currently exist on the Runtime. For clarification, you cannot create a new endpoint using the CREATE operation. - You must supply the _AtomID_, _SourceQueue_, _QueueName_, _DLQ_, and _DestinationQueue_ fields in the request. - If the operation returns an error, it logs a message in the Runtime, Runtime cluster, or Runtime cloud, but is not sent to the platform. - You cannot track move updates directly through this operation. Instead, to see if the action is in progress or complete, use the Queue Management API or the ListQueues API to observe the number of messages in the queue.

- HTTP Method: `POST`
- Endpoint: `/MoveQueueRequest`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [MoveQueueRequest](../models/MoveQueueRequest.md) | ❌       | The request body. |

**Return Type**

`MoveQueueRequest`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import MoveQueueRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = MoveQueueRequest(
    atom_id="${#TestSuite#atomId}",
    destination_queue={
        "dlq": False,
        "queue_name": "QueueName",
        "subscriber_name": "SubscriberName"
    },
    source_queue={
        "dlq": False,
        "queue_name": "QueueName",
        "subscriber_name": "SubscriberName"
    }
)

result = sdk.move_queue_request.create_move_queue_request(request_body=request_body)

print(result)
```

