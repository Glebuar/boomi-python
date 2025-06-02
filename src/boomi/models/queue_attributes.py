
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"dlq": "DLQ", "queue_name": "QueueName", "subscriber_name": "SubscriberName"})
class QueueAttributes(BaseModel):
    """\(Required\) An instance of a generalized queue object indicating the queue from which to send or obtain the messages. Contains information describing the desired queue.

    :param dlq: (Required) true, or false. Allows the user to choose the regular or dead letter queue for deleting messages. The default is `false`, which deletes messages from the regular queue.
    :type dlq: bool
    :param queue_name: (Required) The name of the queue or topic. You can find this in the [List Queues](/api/platformapi#tag/ListQueues) action or in Queue Management.
    :type queue_name: str
    :param subscriber_name: (Optional. Use only for topic subscribers.) The name of the subscriber as it exists on the Runtime. You can find this by using the [List Queues](/api/platformapi#tag/ListQueues) action or by looking up the Component ID of the process associated with the subscriber.  \>**Note:** This field is not only the subscriber name shown on the Queue Management screen of the user interface., defaults to None
    :type subscriber_name: str, optional
    """

    def __init__(
        self, dlq: bool, queue_name: str, subscriber_name: str = SENTINEL, **kwargs
    ):
        """\(Required\) An instance of a generalized queue object indicating the queue from which to send or obtain the messages. Contains information describing the desired queue.

        :param dlq: (Required) true, or false. Allows the user to choose the regular or dead letter queue for deleting messages. The default is `false`, which deletes messages from the regular queue.
        :type dlq: bool
        :param queue_name: (Required) The name of the queue or topic. You can find this in the [List Queues](/api/platformapi#tag/ListQueues) action or in Queue Management.
        :type queue_name: str
        :param subscriber_name: (Optional. Use only for topic subscribers.) The name of the subscriber as it exists on the Runtime. You can find this by using the [List Queues](/api/platformapi#tag/ListQueues) action or by looking up the Component ID of the process associated with the subscriber.  \>**Note:** This field is not only the subscriber name shown on the Queue Management screen of the user interface., defaults to None
        :type subscriber_name: str, optional
        """
        self.dlq = dlq
        self.queue_name = queue_name
        if subscriber_name is not SENTINEL:
            self.subscriber_name = subscriber_name
        self._kwargs = kwargs
