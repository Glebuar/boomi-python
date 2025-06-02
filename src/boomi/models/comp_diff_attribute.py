
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CompDiffAttribute(BaseModel):
    """CompDiffAttribute

    :param idpart: Whether the attribute is part of an identifying key for the element., defaults to None
    :type idpart: bool, optional
    :param ignored: Whether the element described in the `CompDiffElement` section is excluded from the comparative diff results., defaults to None
    :type ignored: bool, optional
    :param name: The name of the attribute for the element that you want to configure for the comparative diff results., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        idpart: bool = SENTINEL,
        ignored: bool = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """CompDiffAttribute

        :param idpart: Whether the attribute is part of an identifying key for the element., defaults to None
        :type idpart: bool, optional
        :param ignored: Whether the element described in the `CompDiffElement` section is excluded from the comparative diff results., defaults to None
        :type ignored: bool, optional
        :param name: The name of the attribute for the element that you want to configure for the comparative diff results., defaults to None
        :type name: str, optional
        """
        if idpart is not SENTINEL:
            self.idpart = idpart
        if ignored is not SENTINEL:
            self.ignored = ignored
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
