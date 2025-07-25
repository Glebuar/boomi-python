
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "atom_id": "AtomId",
        "dlq": "DLQ",
        "queue_name": "QueueName",
        "subscriber_name": "SubscriberName",
    }
)
class ClearQueueRequest(BaseModel):
    """ClearQueueRequest

    :param atom_id: The unique ID assigned by the system to the container. \<br /\>The Runtime ID for Runtimes, Runtime clusters, and Runtime clouds is found in the user interface by navigating to **Manage** \\> **Runtime Management** and viewing the **Runtime Information** panel for the selected container.
    :type atom_id: str
    :param dlq: When set to *true*, it deletes messages from the regular queue only.When set to *false* \(default\), it deletes messages from the regular queue., defaults to None
    :type dlq: bool, optional
    :param queue_name: The name of the queue or topic. You can locate the queue or topic name by navigating to **Manage** \\> **Runtime Management** \\> **Queue Management panel** or by employing the ListQueues API action to retrieve the names of all queues on a given Runtime.
    :type queue_name: str
    :param subscriber_name: The subscriber name as it exists on the Runtime. You can find the subscriber name using the ListQueues API action or by looking up the Component ID of the process tied to the subscriber.   \>**Note:** The subscriber name does not necessarily equate to the Subscriber Name as is shown in Queue Management. If there is a process in Queue Management with the same name, use the Component ID of that process., defaults to None
    :type subscriber_name: str, optional
    """

    def __init__(
        self,
        atom_id: str,
        queue_name: str,
        dlq: bool = SENTINEL,
        subscriber_name: str = SENTINEL,
        **kwargs
    ):
        """ClearQueueRequest

        :param atom_id: The unique ID assigned by the system to the container. \<br /\>The Runtime ID for Runtimes, Runtime clusters, and Runtime clouds is found in the user interface by navigating to **Manage** \\> **Runtime Management** and viewing the **Runtime Information** panel for the selected container.
        :type atom_id: str
        :param dlq: When set to *true*, it deletes messages from the regular queue only.When set to *false* \(default\), it deletes messages from the regular queue., defaults to None
        :type dlq: bool, optional
        :param queue_name: The name of the queue or topic. You can locate the queue or topic name by navigating to **Manage** \\> **Runtime Management** \\> **Queue Management panel** or by employing the ListQueues API action to retrieve the names of all queues on a given Runtime.
        :type queue_name: str
        :param subscriber_name: The subscriber name as it exists on the Runtime. You can find the subscriber name using the ListQueues API action or by looking up the Component ID of the process tied to the subscriber.   \>**Note:** The subscriber name does not necessarily equate to the Subscriber Name as is shown in Queue Management. If there is a process in Queue Management with the same name, use the Component ID of that process., defaults to None
        :type subscriber_name: str, optional
        """
        self.atom_id = atom_id
        if dlq is not SENTINEL:
            self.dlq = dlq
        self.queue_name = queue_name
        if subscriber_name is not SENTINEL:
            self.subscriber_name = subscriber_name
        self._kwargs = kwargs
