
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .deployed_process import DeployedProcess


@JsonMap({"process": "Process", "atom_id": "atomId"})
class PersistedProcessProperties(BaseModel):
    """PersistedProcessProperties

    :param process: process, defaults to None
    :type process: List[DeployedProcess], optional
    :param atom_id: A unique ID assigned by the system to the Runtime.
    :type atom_id: str
    """

    def __init__(
        self, atom_id: str, process: List[DeployedProcess] = SENTINEL, **kwargs
    ):
        """PersistedProcessProperties

        :param process: process, defaults to None
        :type process: List[DeployedProcess], optional
        :param atom_id: A unique ID assigned by the system to the Runtime.
        :type atom_id: str
        """
        if process is not SENTINEL:
            self.process = self._define_list(process, DeployedProcess)
        self.atom_id = atom_id
        self._kwargs = kwargs
