
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "from_function": "fromFunction",
        "from_key": "fromKey",
        "to_function": "toFunction",
        "to_key": "toKey",
    }
)
class MapExtensionsFunctionMapping(BaseModel):
    """MapExtensionsFunctionMapping

    :param from_function: from_function, defaults to None
    :type from_function: str, optional
    :param from_key: from_key, defaults to None
    :type from_key: int, optional
    :param to_function: to_function, defaults to None
    :type to_function: str, optional
    :param to_key: to_key, defaults to None
    :type to_key: int, optional
    """

    def __init__(
        self,
        from_function: str = SENTINEL,
        from_key: int = SENTINEL,
        to_function: str = SENTINEL,
        to_key: int = SENTINEL,
        **kwargs
    ):
        """MapExtensionsFunctionMapping

        :param from_function: from_function, defaults to None
        :type from_function: str, optional
        :param from_key: from_key, defaults to None
        :type from_key: int, optional
        :param to_function: to_function, defaults to None
        :type to_function: str, optional
        :param to_key: to_key, defaults to None
        :type to_key: int, optional
        """
        if from_function is not SENTINEL:
            self.from_function = from_function
        if from_key is not SENTINEL:
            self.from_key = from_key
        if to_function is not SENTINEL:
            self.to_function = to_function
        if to_key is not SENTINEL:
            self.to_key = to_key
        self._kwargs = kwargs
