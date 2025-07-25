
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .release_packaged_component import ReleasePackagedComponent


@JsonMap({"release_packaged_component": "ReleasePackagedComponent"})
class ReleasePackagedComponents(BaseModel):
    """ReleasePackagedComponents

    :param release_packaged_component: release_packaged_component
    :type release_packaged_component: List[ReleasePackagedComponent]
    """

    def __init__(
        self, release_packaged_component: List[ReleasePackagedComponent], **kwargs
    ):
        """ReleasePackagedComponents

        :param release_packaged_component: release_packaged_component
        :type release_packaged_component: List[ReleasePackagedComponent]
        """
        self.release_packaged_component = self._define_list(
            release_packaged_component, ReleasePackagedComponent
        )
        self._kwargs = kwargs
