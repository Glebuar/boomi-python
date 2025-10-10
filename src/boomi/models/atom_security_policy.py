
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .atom_security_policy_argument_type import AtomSecurityPolicyArgumentType


@JsonMap({"privilege_type": "privilegeType"})
class AtomSecurityPolicy(BaseModel):
    """AtomSecurityPolicy

    :param arguments: arguments, defaults to None
    :type arguments: List[AtomSecurityPolicyArgumentType], optional
    :param privilege_type: A valid Java runtime permission.
    :type privilege_type: str
    """

    def __init__(
        self,
        privilege_type: str,
        arguments: List[AtomSecurityPolicyArgumentType] = SENTINEL,
        **kwargs,
    ):
        """AtomSecurityPolicy

        :param arguments: arguments, defaults to None
        :type arguments: List[AtomSecurityPolicyArgumentType], optional
        :param privilege_type: A valid Java runtime permission.
        :type privilege_type: str
        """
        if arguments is not SENTINEL:
            self.arguments = self._define_list(
                arguments, AtomSecurityPolicyArgumentType
            )
        self.privilege_type = privilege_type
        self._kwargs = kwargs
