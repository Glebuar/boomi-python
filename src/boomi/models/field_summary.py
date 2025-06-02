
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_properties import CustomProperties


@JsonMap(
    {
        "component_override": "componentOverride",
        "custom_properties": "customProperties",
        "encrypted_value_set": "encryptedValueSet",
        "id_": "id",
        "use_default": "useDefault",
        "uses_encryption": "usesEncryption",
        "oauth2_authorization_url": "oauth2AuthorizationUrl",
    }
)
class FieldSummary(BaseModel):
    """FieldSummary

    :param component_override: component_override, defaults to None
    :type component_override: bool, optional
    :param custom_properties: custom_properties, defaults to None
    :type custom_properties: CustomProperties, optional
    :param encrypted_value_set: encrypted_value_set, defaults to None
    :type encrypted_value_set: bool, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param use_default: use_default, defaults to None
    :type use_default: bool, optional
    :param uses_encryption: uses_encryption, defaults to None
    :type uses_encryption: bool, optional
    :param value: value, defaults to None
    :type value: str, optional
    :param oauth2_authorization_url: oauth2_authorization_url, defaults to None
    :type oauth2_authorization_url: str, optional
    """

    def __init__(
        self,
        component_override: bool = SENTINEL,
        custom_properties: CustomProperties = SENTINEL,
        encrypted_value_set: bool = SENTINEL,
        id_: str = SENTINEL,
        use_default: bool = SENTINEL,
        uses_encryption: bool = SENTINEL,
        value: str = SENTINEL,
        oauth2_authorization_url: str = SENTINEL,
        **kwargs,
    ):
        """FieldSummary

        :param component_override: component_override, defaults to None
        :type component_override: bool, optional
        :param custom_properties: custom_properties, defaults to None
        :type custom_properties: CustomProperties, optional
        :param encrypted_value_set: encrypted_value_set, defaults to None
        :type encrypted_value_set: bool, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param use_default: use_default, defaults to None
        :type use_default: bool, optional
        :param uses_encryption: uses_encryption, defaults to None
        :type uses_encryption: bool, optional
        :param value: value, defaults to None
        :type value: str, optional
        :param oauth2_authorization_url: oauth2_authorization_url, defaults to None
        :type oauth2_authorization_url: str, optional
        """
        if component_override is not SENTINEL:
            self.component_override = component_override
        if custom_properties is not SENTINEL:
            self.custom_properties = self._define_object(
                custom_properties, CustomProperties
            )
        if encrypted_value_set is not SENTINEL:
            self.encrypted_value_set = encrypted_value_set
        if id_ is not SENTINEL:
            self.id_ = id_
        if use_default is not SENTINEL:
            self.use_default = use_default
        if uses_encryption is not SENTINEL:
            self.uses_encryption = uses_encryption
        if value is not SENTINEL:
            self.value = value
        if oauth2_authorization_url is not SENTINEL:
            self.oauth2_authorization_url = oauth2_authorization_url
        self._kwargs = kwargs
