
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .atom_security_policies_type import AtomSecurityPoliciesType


@JsonMap({"atom_id": "atomId"})
class AtomSecurityPolicies(BaseModel):
    """AtomSecurityPolicies

    :param atom_id: The ID of the Runtime cloud or Runtime cluster.
    :type atom_id: str
    :param browser: browser, defaults to None
    :type browser: AtomSecurityPoliciesType, optional
    :param common: common
    :type common: AtomSecurityPoliciesType
    :param runner: runner, defaults to None
    :type runner: AtomSecurityPoliciesType, optional
    :param worker: worker, defaults to None
    :type worker: AtomSecurityPoliciesType, optional
    """

    def __init__(
        self,
        atom_id: str,
        common: AtomSecurityPoliciesType,
        browser: AtomSecurityPoliciesType = SENTINEL,
        runner: AtomSecurityPoliciesType = SENTINEL,
        worker: AtomSecurityPoliciesType = SENTINEL,
        **kwargs,
    ):
        """AtomSecurityPolicies

        :param atom_id: The ID of the Runtime cloud or Runtime cluster.
        :type atom_id: str
        :param browser: browser, defaults to None
        :type browser: AtomSecurityPoliciesType, optional
        :param common: common
        :type common: AtomSecurityPoliciesType
        :param runner: runner, defaults to None
        :type runner: AtomSecurityPoliciesType, optional
        :param worker: worker, defaults to None
        :type worker: AtomSecurityPoliciesType, optional
        """
        self.atom_id = atom_id
        if browser is not SENTINEL:
            self.browser = self._define_object(browser, AtomSecurityPoliciesType)
        self.common = self._define_object(common, AtomSecurityPoliciesType)
        if runner is not SENTINEL:
            self.runner = self._define_object(runner, AtomSecurityPoliciesType)
        if worker is not SENTINEL:
            self.worker = self._define_object(worker, AtomSecurityPoliciesType)
        self._kwargs = kwargs
