
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_communication import SharedCommunication


@JsonMap({"shared_communication": "sharedCommunication"})
class SharedCommunications(BaseModel):
    """SharedCommunications

    :param shared_communication: shared_communication, defaults to None
    :type shared_communication: List[SharedCommunication], optional
    """

    def __init__(
        self, shared_communication: List[SharedCommunication] = SENTINEL, **kwargs
    ):
        """SharedCommunications

        :param shared_communication: shared_communication, defaults to None
        :type shared_communication: List[SharedCommunication], optional
        """
        if shared_communication is not SENTINEL:
            self.shared_communication = self._define_list(
                shared_communication, SharedCommunication
            )
        self._kwargs = kwargs
