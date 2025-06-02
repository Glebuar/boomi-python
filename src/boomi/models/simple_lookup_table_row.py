
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SimpleLookupTableRow(BaseModel):
    """SimpleLookupTableRow

    :param ref1: ref1
    :type ref1: str
    :param ref2: ref2
    :type ref2: str
    """

    def __init__(self, ref1: str, ref2: str, **kwargs):
        """SimpleLookupTableRow

        :param ref1: ref1
        :type ref1: str
        :param ref2: ref2
        :type ref2: str
        """
        self.ref1 = ref1
        self.ref2 = ref2
        self._kwargs = kwargs
