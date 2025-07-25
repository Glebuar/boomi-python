
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .counter import Counter


@JsonMap({"atom_id": "atomId"})
class AtomCounters(BaseModel):
    """AtomCounters

    :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
    :type atom_id: str, optional
    :param counter: counter, defaults to None
    :type counter: List[Counter], optional
    """

    def __init__(
        self, atom_id: str = SENTINEL, counter: List[Counter] = SENTINEL, **kwargs
    ):
        """AtomCounters

        :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
        :type atom_id: str, optional
        :param counter: counter, defaults to None
        :type counter: List[Counter], optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if counter is not SENTINEL:
            self.counter = self._define_list(counter, Counter)
        self._kwargs = kwargs
