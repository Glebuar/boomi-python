
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .topic_subscriber import TopicSubscriber


@JsonMap(
    {
        "dead_letters_count": "deadLettersCount",
        "messages_count": "messagesCount",
        "queue_name": "queueName",
        "queue_type": "queueType",
        "topic_subscribers": "topicSubscribers",
    }
)
class QueueRecord(BaseModel):
    """QueueRecord

    :param dead_letters_count: dead_letters_count, defaults to None
    :type dead_letters_count: int, optional
    :param messages_count: messages_count, defaults to None
    :type messages_count: int, optional
    :param queue_name: queue_name, defaults to None
    :type queue_name: str, optional
    :param queue_type: queue_type, defaults to None
    :type queue_type: str, optional
    :param topic_subscribers: topic_subscribers, defaults to None
    :type topic_subscribers: List[TopicSubscriber], optional
    """

    def __init__(
        self,
        dead_letters_count: int = SENTINEL,
        messages_count: int = SENTINEL,
        queue_name: str = SENTINEL,
        queue_type: str = SENTINEL,
        topic_subscribers: List[TopicSubscriber] = SENTINEL,
        **kwargs,
    ):
        """QueueRecord

        :param dead_letters_count: dead_letters_count, defaults to None
        :type dead_letters_count: int, optional
        :param messages_count: messages_count, defaults to None
        :type messages_count: int, optional
        :param queue_name: queue_name, defaults to None
        :type queue_name: str, optional
        :param queue_type: queue_type, defaults to None
        :type queue_type: str, optional
        :param topic_subscribers: topic_subscribers, defaults to None
        :type topic_subscribers: List[TopicSubscriber], optional
        """
        if dead_letters_count is not SENTINEL:
            self.dead_letters_count = dead_letters_count
        if messages_count is not SENTINEL:
            self.messages_count = messages_count
        if queue_name is not SENTINEL:
            self.queue_name = queue_name
        if queue_type is not SENTINEL:
            self.queue_type = queue_type
        if topic_subscribers is not SENTINEL:
            self.topic_subscribers = self._define_list(
                topic_subscribers, TopicSubscriber
            )
        self._kwargs = kwargs
