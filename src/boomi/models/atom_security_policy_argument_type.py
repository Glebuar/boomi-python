
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class AtomSecurityPolicyArgumentType(BaseModel):
    """AtomSecurityPolicyArgumentType

    :param value: An argument value in a Java runtime permission.
    :type value: str
    """

    def __init__(self, value: str, **kwargs):
        """AtomSecurityPolicyArgumentType

        :param value: An argument value in a Java runtime permission.
        :type value: str
        """
        self.value = value
        self._kwargs = kwargs
