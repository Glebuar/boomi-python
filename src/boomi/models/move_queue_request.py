
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .queue_attributes import QueueAttributes


@JsonMap(
    {
        "atom_id": "AtomId",
        "destination_queue": "DestinationQueue",
        "source_queue": "SourceQueue",
    }
)
class MoveQueueRequest(BaseModel):
    """MoveQueueRequest

    :param atom_id: \(Required\) The Runtime ID that the queue or topic exists under and where you can find it in Runtime Management. You can find the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds in the user interface by navigating to **Manage** \\> **Runtime Management** and viewing the **Runtime Information** panel for a selected container.
    :type atom_id: str
    :param destination_queue: \(Required\) An instance of a generalized queue object indicating the queue from which to send or obtain the messages. Contains information describing the desired queue.
    :type destination_queue: QueueAttributes
    :param source_queue: \(Required\) An instance of a generalized queue object indicating the queue from which to send or obtain the messages. Contains information describing the desired queue.
    :type source_queue: QueueAttributes
    """

    def __init__(
        self,
        atom_id: str,
        destination_queue: QueueAttributes,
        source_queue: QueueAttributes,
        **kwargs,
    ):
        """MoveQueueRequest

        :param atom_id: \(Required\) The Runtime ID that the queue or topic exists under and where you can find it in Runtime Management. You can find the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds in the user interface by navigating to **Manage** \\> **Runtime Management** and viewing the **Runtime Information** panel for a selected container.
        :type atom_id: str
        :param destination_queue: \(Required\) An instance of a generalized queue object indicating the queue from which to send or obtain the messages. Contains information describing the desired queue.
        :type destination_queue: QueueAttributes
        :param source_queue: \(Required\) An instance of a generalized queue object indicating the queue from which to send or obtain the messages. Contains information describing the desired queue.
        :type source_queue: QueueAttributes
        """
        self.atom_id = atom_id
        self.destination_queue = self._define_object(destination_queue, QueueAttributes)
        self.source_queue = self._define_object(source_queue, QueueAttributes)
        self._kwargs = kwargs
