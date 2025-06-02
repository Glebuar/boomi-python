
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .comp_diff_config import CompDiffConfig


@JsonMap(
    {
        "comp_diff_config": "CompDiffConfig",
        "component_id": "componentId",
        "source_version": "sourceVersion",
        "target_version": "targetVersion",
    }
)
class ComponentDiffRequest(BaseModel):
    """ComponentDiffRequest

    :param comp_diff_config: comp_diff_config, defaults to None
    :type comp_diff_config: CompDiffConfig, optional
    :param component_id: The ID of the component for which you want to compare versions.
    :type component_id: str
    :param source_version: The source version of the component.
    :type source_version: int
    :param target_version: The target version which you want to compare to the source version.
    :type target_version: int
    """

    def __init__(
        self,
        component_id: str,
        source_version: int,
        target_version: int,
        comp_diff_config: CompDiffConfig = SENTINEL,
        **kwargs,
    ):
        """ComponentDiffRequest

        :param comp_diff_config: comp_diff_config, defaults to None
        :type comp_diff_config: CompDiffConfig, optional
        :param component_id: The ID of the component for which you want to compare versions.
        :type component_id: str
        :param source_version: The source version of the component.
        :type source_version: int
        :param target_version: The target version which you want to compare to the source version.
        :type target_version: int
        """
        if comp_diff_config is not SENTINEL:
            self.comp_diff_config = self._define_object(
                comp_diff_config, CompDiffConfig
            )
        self.component_id = component_id
        self.source_version = source_version
        self.target_version = target_version
        self._kwargs = kwargs
