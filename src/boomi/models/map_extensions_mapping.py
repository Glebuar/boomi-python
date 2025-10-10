
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "from_function": "fromFunction",
        "from_x_path": "fromXPath",
        "to_function": "toFunction",
        "to_x_path": "toXPath",
    }
)
class MapExtensionsMapping(BaseModel):
    """MapExtensionsMapping

    :param from_function: from_function, defaults to None
    :type from_function: str, optional
    :param from_x_path: from_x_path, defaults to None
    :type from_x_path: str, optional
    :param to_function: to_function, defaults to None
    :type to_function: str, optional
    :param to_x_path: to_x_path, defaults to None
    :type to_x_path: str, optional
    """

    def __init__(
        self,
        from_function: str = SENTINEL,
        from_x_path: str = SENTINEL,
        to_function: str = SENTINEL,
        to_x_path: str = SENTINEL,
        **kwargs
    ):
        """MapExtensionsMapping

        :param from_function: from_function, defaults to None
        :type from_function: str, optional
        :param from_x_path: from_x_path, defaults to None
        :type from_x_path: str, optional
        :param to_function: to_function, defaults to None
        :type to_function: str, optional
        :param to_x_path: to_x_path, defaults to None
        :type to_x_path: str, optional
        """
        if from_function is not SENTINEL:
            self.from_function = from_function
        if from_x_path is not SENTINEL:
            self.from_x_path = from_x_path
        if to_function is not SENTINEL:
            self.to_function = to_function
        if to_x_path is not SENTINEL:
            self.to_x_path = to_x_path
        self._kwargs = kwargs
