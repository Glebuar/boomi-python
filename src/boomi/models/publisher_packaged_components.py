
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .publisher_packaged_component import PublisherPackagedComponent


@JsonMap({"publisher_packaged_component": "PublisherPackagedComponent"})
class PublisherPackagedComponents(BaseModel):
    """PublisherPackagedComponents

    :param publisher_packaged_component: publisher_packaged_component, defaults to None
    :type publisher_packaged_component: List[PublisherPackagedComponent], optional
    """

    def __init__(
        self,
        publisher_packaged_component: List[PublisherPackagedComponent] = SENTINEL,
        **kwargs,
    ):
        """PublisherPackagedComponents

        :param publisher_packaged_component: publisher_packaged_component, defaults to None
        :type publisher_packaged_component: List[PublisherPackagedComponent], optional
        """
        if publisher_packaged_component is not SENTINEL:
            self.publisher_packaged_component = self._define_list(
                publisher_packaged_component, PublisherPackagedComponent
            )
        self._kwargs = kwargs
