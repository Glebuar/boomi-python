
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"component_id": "componentId"})
class PublicCertificate(BaseModel):
    """PublicCertificate

    :param alias: alias, defaults to None
    :type alias: str, optional
    :param certificate: certificate, defaults to None
    :type certificate: List[str], optional
    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    """

    def __init__(
        self,
        alias: str = SENTINEL,
        certificate: List[str] = SENTINEL,
        component_id: str = SENTINEL,
        **kwargs
    ):
        """PublicCertificate

        :param alias: alias, defaults to None
        :type alias: str, optional
        :param certificate: certificate, defaults to None
        :type certificate: List[str], optional
        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        """
        if alias is not SENTINEL:
            self.alias = alias
        if certificate is not SENTINEL:
            self.certificate = certificate
        if component_id is not SENTINEL:
            self.component_id = component_id
        self._kwargs = kwargs
