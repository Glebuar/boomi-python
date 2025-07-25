
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"component_id": "componentId", "pass_phrase": "passPhrase"})
class PrivateCertificate(BaseModel):
    """PrivateCertificate

    :param alias: alias, defaults to None
    :type alias: str, optional
    :param certificate: certificate, defaults to None
    :type certificate: List[str], optional
    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    :param pass_phrase: pass_phrase, defaults to None
    :type pass_phrase: str, optional
    """

    def __init__(
        self,
        alias: str = SENTINEL,
        certificate: List[str] = SENTINEL,
        component_id: str = SENTINEL,
        pass_phrase: str = SENTINEL,
        **kwargs
    ):
        """PrivateCertificate

        :param alias: alias, defaults to None
        :type alias: str, optional
        :param certificate: certificate, defaults to None
        :type certificate: List[str], optional
        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        :param pass_phrase: pass_phrase, defaults to None
        :type pass_phrase: str, optional
        """
        if alias is not SENTINEL:
            self.alias = alias
        if certificate is not SENTINEL:
            self.certificate = certificate
        if component_id is not SENTINEL:
            self.component_id = component_id
        if pass_phrase is not SENTINEL:
            self.pass_phrase = pass_phrase
        self._kwargs = kwargs
