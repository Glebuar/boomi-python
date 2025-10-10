
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .queue_record import QueueRecord


@JsonMap({"queue_record": "QueueRecord"})
class ListQueues(BaseModel):
    """ListQueues

    :param queue_record: queue_record, defaults to None
    :type queue_record: List[QueueRecord], optional
    """

    def __init__(self, queue_record: List[QueueRecord] = SENTINEL, **kwargs):
        """ListQueues

        :param queue_record: queue_record, defaults to None
        :type queue_record: List[QueueRecord], optional
        """
        if queue_record is not SENTINEL:
            self.queue_record = self._define_list(queue_record, QueueRecord)
        self._kwargs = kwargs
