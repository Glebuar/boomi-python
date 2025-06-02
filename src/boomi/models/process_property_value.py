
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "component_override": "componentOverride",
        "encrypted_value_set": "encryptedValueSet",
        "use_default": "useDefault",
        "uses_encryption": "usesEncryption",
    }
)
class ProcessPropertyValue(BaseModel):
    """ProcessPropertyValue

    :param component_override: component_override, defaults to None
    :type component_override: bool, optional
    :param encrypted_value_set: encrypted_value_set, defaults to None
    :type encrypted_value_set: bool, optional
    :param key: key, defaults to None
    :type key: str, optional
    :param label: label, defaults to None
    :type label: str, optional
    :param use_default: use_default, defaults to None
    :type use_default: bool, optional
    :param uses_encryption: uses_encryption, defaults to None
    :type uses_encryption: bool, optional
    :param validate: validate, defaults to None
    :type validate: bool, optional
    :param value: The value assigned to the persisted process property., defaults to None
    :type value: str, optional
    """

    def __init__(
        self,
        component_override: bool = SENTINEL,
        encrypted_value_set: bool = SENTINEL,
        key: str = SENTINEL,
        label: str = SENTINEL,
        use_default: bool = SENTINEL,
        uses_encryption: bool = SENTINEL,
        validate: bool = SENTINEL,
        value: str = SENTINEL,
        **kwargs
    ):
        """ProcessPropertyValue

        :param component_override: component_override, defaults to None
        :type component_override: bool, optional
        :param encrypted_value_set: encrypted_value_set, defaults to None
        :type encrypted_value_set: bool, optional
        :param key: key, defaults to None
        :type key: str, optional
        :param label: label, defaults to None
        :type label: str, optional
        :param use_default: use_default, defaults to None
        :type use_default: bool, optional
        :param uses_encryption: uses_encryption, defaults to None
        :type uses_encryption: bool, optional
        :param validate: validate, defaults to None
        :type validate: bool, optional
        :param value: The value assigned to the persisted process property., defaults to None
        :type value: str, optional
        """
        if component_override is not SENTINEL:
            self.component_override = component_override
        if encrypted_value_set is not SENTINEL:
            self.encrypted_value_set = encrypted_value_set
        if key is not SENTINEL:
            self.key = key
        if label is not SENTINEL:
            self.label = label
        if use_default is not SENTINEL:
            self.use_default = use_default
        if uses_encryption is not SENTINEL:
            self.uses_encryption = uses_encryption
        if validate is not SENTINEL:
            self.validate = validate
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
