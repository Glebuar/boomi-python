
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "subscriber_name": "SubscriberName",
        "dead_letters_count": "deadLettersCount",
        "message_count": "messageCount",
    }
)
class TopicSubscriber(BaseModel):
    """TopicSubscriber

    :param subscriber_name: subscriber_name, defaults to None
    :type subscriber_name: str, optional
    :param dead_letters_count: dead_letters_count, defaults to None
    :type dead_letters_count: int, optional
    :param message_count: message_count, defaults to None
    :type message_count: int, optional
    """

    def __init__(
        self,
        subscriber_name: str = SENTINEL,
        dead_letters_count: int = SENTINEL,
        message_count: int = SENTINEL,
        **kwargs
    ):
        """TopicSubscriber

        :param subscriber_name: subscriber_name, defaults to None
        :type subscriber_name: str, optional
        :param dead_letters_count: dead_letters_count, defaults to None
        :type dead_letters_count: int, optional
        :param message_count: message_count, defaults to None
        :type message_count: int, optional
        """
        if subscriber_name is not SENTINEL:
            self.subscriber_name = subscriber_name
        if dead_letters_count is not SENTINEL:
            self.dead_letters_count = dead_letters_count
        if message_count is not SENTINEL:
            self.message_count = message_count
        self._kwargs = kwargs
