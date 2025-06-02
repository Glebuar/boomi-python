
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .encrypted_value import EncryptedValue


@JsonMap({"encrypted_value": "encryptedValue"})
class EncryptedValues(BaseModel):
    """EncryptedValues

    :param encrypted_value: encrypted_value, defaults to None
    :type encrypted_value: List[EncryptedValue], optional
    """

    def __init__(self, encrypted_value: List[EncryptedValue] = SENTINEL, **kwargs):
        """EncryptedValues

        :param encrypted_value: encrypted_value, defaults to None
        :type encrypted_value: List[EncryptedValue], optional
        """
        if encrypted_value is not SENTINEL:
            self.encrypted_value = self._define_list(encrypted_value, EncryptedValue)
        self._kwargs = kwargs
