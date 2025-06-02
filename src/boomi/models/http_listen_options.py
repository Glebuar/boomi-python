
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "mime_passthrough": "mimePassthrough",
        "object_name": "objectName",
        "operation_type": "operationType",
        "use_default_listen_options": "useDefaultListenOptions",
    }
)
class HttpListenOptions(BaseModel):
    """HttpListenOptions

    :param mime_passthrough: mime_passthrough, defaults to None
    :type mime_passthrough: bool, optional
    :param object_name: object_name, defaults to None
    :type object_name: str, optional
    :param operation_type: operation_type, defaults to None
    :type operation_type: str, optional
    :param password: password, defaults to None
    :type password: str, optional
    :param use_default_listen_options: use_default_listen_options, defaults to None
    :type use_default_listen_options: bool, optional
    :param username: username, defaults to None
    :type username: str, optional
    """

    def __init__(
        self,
        mime_passthrough: bool = SENTINEL,
        object_name: str = SENTINEL,
        operation_type: str = SENTINEL,
        password: str = SENTINEL,
        use_default_listen_options: bool = SENTINEL,
        username: str = SENTINEL,
        **kwargs
    ):
        """HttpListenOptions

        :param mime_passthrough: mime_passthrough, defaults to None
        :type mime_passthrough: bool, optional
        :param object_name: object_name, defaults to None
        :type object_name: str, optional
        :param operation_type: operation_type, defaults to None
        :type operation_type: str, optional
        :param password: password, defaults to None
        :type password: str, optional
        :param use_default_listen_options: use_default_listen_options, defaults to None
        :type use_default_listen_options: bool, optional
        :param username: username, defaults to None
        :type username: str, optional
        """
        if mime_passthrough is not SENTINEL:
            self.mime_passthrough = mime_passthrough
        if object_name is not SENTINEL:
            self.object_name = object_name
        if operation_type is not SENTINEL:
            self.operation_type = operation_type
        if password is not SENTINEL:
            self.password = password
        if use_default_listen_options is not SENTINEL:
            self.use_default_listen_options = use_default_listen_options
        if username is not SENTINEL:
            self.username = username
        self._kwargs = kwargs
