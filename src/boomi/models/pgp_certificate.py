
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"id_": "id", "use_default": "useDefault"})
class PgpCertificate(BaseModel):
    """PgpCertificate

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param use_default: use_default, defaults to None
    :type use_default: bool, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(
        self,
        id_: str = SENTINEL,
        use_default: bool = SENTINEL,
        value: str = SENTINEL,
        **kwargs
    ):
        """PgpCertificate

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param use_default: use_default, defaults to None
        :type use_default: bool, optional
        :param value: value, defaults to None
        :type value: str, optional
        """
        if id_ is not SENTINEL:
            self.id_ = id_
        if use_default is not SENTINEL:
            self.use_default = use_default
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
