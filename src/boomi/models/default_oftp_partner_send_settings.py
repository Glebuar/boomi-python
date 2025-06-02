
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class DefaultOftpPartnerSendSettings(BaseModel):
    """DefaultOftpPartnerSendSettings

    :param cd: cd, defaults to None
    :type cd: bool, optional
    :param operation: operation, defaults to None
    :type operation: str, optional
    :param sfiddesc: sfiddesc, defaults to None
    :type sfiddesc: str, optional
    :param sfiddsn: sfiddsn, defaults to None
    :type sfiddsn: str, optional
    """

    def __init__(
        self,
        cd: bool = SENTINEL,
        operation: str = SENTINEL,
        sfiddesc: str = SENTINEL,
        sfiddsn: str = SENTINEL,
        **kwargs
    ):
        """DefaultOftpPartnerSendSettings

        :param cd: cd, defaults to None
        :type cd: bool, optional
        :param operation: operation, defaults to None
        :type operation: str, optional
        :param sfiddesc: sfiddesc, defaults to None
        :type sfiddesc: str, optional
        :param sfiddsn: sfiddsn, defaults to None
        :type sfiddsn: str, optional
        """
        if cd is not SENTINEL:
            self.cd = cd
        if operation is not SENTINEL:
            self.operation = operation
        if sfiddesc is not SENTINEL:
            self.sfiddesc = sfiddesc
        if sfiddsn is not SENTINEL:
            self.sfiddsn = sfiddsn
        self._kwargs = kwargs
