
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .atom_security_policy import AtomSecurityPolicy


@JsonMap({})
class AtomSecurityPoliciesType(BaseModel):
    """AtomSecurityPoliciesType

    :param policies: policies, defaults to None
    :type policies: List[AtomSecurityPolicy], optional
    """

    def __init__(self, policies: List[AtomSecurityPolicy] = SENTINEL, **kwargs):
        """AtomSecurityPoliciesType

        :param policies: policies, defaults to None
        :type policies: List[AtomSecurityPolicy], optional
        """
        if policies is not SENTINEL:
            self.policies = self._define_list(policies, AtomSecurityPolicy)
        self._kwargs = kwargs
