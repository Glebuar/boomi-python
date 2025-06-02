
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"ref_id": "refId"})
class CrossReferenceParameter(BaseModel):
    """CrossReferenceParameter

    :param index: index, defaults to None
    :type index: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param ref_id: ref_id, defaults to None
    :type ref_id: int, optional
    """

    def __init__(
        self,
        index: int = SENTINEL,
        name: str = SENTINEL,
        ref_id: int = SENTINEL,
        **kwargs
    ):
        """CrossReferenceParameter

        :param index: index, defaults to None
        :type index: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param ref_id: ref_id, defaults to None
        :type ref_id: int, optional
        """
        if index is not SENTINEL:
            self.index = index
        if name is not SENTINEL:
            self.name = name
        if ref_id is not SENTINEL:
            self.ref_id = ref_id
        self._kwargs = kwargs
