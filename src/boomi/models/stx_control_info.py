
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "interchange_id": "interchangeId",
        "interchange_id_qualifier": "interchangeIdQualifier",
    }
)
class StxControlInfo(BaseModel):
    """StxControlInfo

    :param interchange_id: interchange_id, defaults to None
    :type interchange_id: str, optional
    :param interchange_id_qualifier: interchange_id_qualifier, defaults to None
    :type interchange_id_qualifier: str, optional
    """

    def __init__(
        self,
        interchange_id: str = SENTINEL,
        interchange_id_qualifier: str = SENTINEL,
        **kwargs
    ):
        """StxControlInfo

        :param interchange_id: interchange_id, defaults to None
        :type interchange_id: str, optional
        :param interchange_id_qualifier: interchange_id_qualifier, defaults to None
        :type interchange_id_qualifier: str, optional
        """
        if interchange_id is not SENTINEL:
            self.interchange_id = interchange_id
        if interchange_id_qualifier is not SENTINEL:
            self.interchange_id_qualifier = interchange_id_qualifier
        self._kwargs = kwargs
