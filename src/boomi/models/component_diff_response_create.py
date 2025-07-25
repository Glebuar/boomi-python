
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class KeyPart(BaseModel):
    """KeyPart

    :param attribute: Attribute name, defaults to None
    :type attribute: str, optional
    :param value: Attribute value, defaults to None
    :type value: str, optional
    """

    def __init__(self, attribute: str = SENTINEL, value: str = SENTINEL, **kwargs):
        """KeyPart

        :param attribute: Attribute name, defaults to None
        :type attribute: str, optional
        :param value: Attribute value, defaults to None
        :type value: str, optional
        """
        if attribute is not SENTINEL:
            self.attribute = attribute
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs


@JsonMap({"element_name": "elementName", "key_part": "key-part"})
class ChangeElementKey1(BaseModel):
    """ChangeElementKey1

    :param element_name: Name of the element, defaults to None
    :type element_name: str, optional
    :param key_part: key_part, defaults to None
    :type key_part: KeyPart, optional
    """

    def __init__(
        self, element_name: str = SENTINEL, key_part: KeyPart = SENTINEL, **kwargs
    ):
        """ChangeElementKey1

        :param element_name: Name of the element, defaults to None
        :type element_name: str, optional
        :param key_part: key_part, defaults to None
        :type key_part: KeyPart, optional
        """
        if element_name is not SENTINEL:
            self.element_name = element_name
        if key_part is not SENTINEL:
            self.key_part = self._define_object(key_part, KeyPart)
        self._kwargs = kwargs


@JsonMap(
    {
        "type_": "type",
        "changed_particle_name": "changedParticleName",
        "element_key": "elementKey",
        "new_value": "newValue",
    }
)
class AdditionChange(BaseModel):
    """AdditionChange

    :param type_: Type of change (e.g., element), defaults to None
    :type type_: str, optional
    :param changed_particle_name: Name of the particle that changed, defaults to None
    :type changed_particle_name: str, optional
    :param element_key: element_key, defaults to None
    :type element_key: ChangeElementKey1, optional
    :param new_value: New value of the element in the diff, defaults to None
    :type new_value: str, optional
    """

    def __init__(
        self,
        type_: str = SENTINEL,
        changed_particle_name: str = SENTINEL,
        element_key: ChangeElementKey1 = SENTINEL,
        new_value: str = SENTINEL,
        **kwargs
    ):
        """AdditionChange

        :param type_: Type of change (e.g., element), defaults to None
        :type type_: str, optional
        :param changed_particle_name: Name of the particle that changed, defaults to None
        :type changed_particle_name: str, optional
        :param element_key: element_key, defaults to None
        :type element_key: ChangeElementKey1, optional
        :param new_value: New value of the element in the diff, defaults to None
        :type new_value: str, optional
        """
        if type_ is not SENTINEL:
            self.type_ = type_
        if changed_particle_name is not SENTINEL:
            self.changed_particle_name = changed_particle_name
        if element_key is not SENTINEL:
            self.element_key = self._define_object(element_key, ChangeElementKey1)
        if new_value is not SENTINEL:
            self.new_value = new_value
        self._kwargs = kwargs


@JsonMap({})
class Addition(BaseModel):
    """Addition

    :param total: Total number of additions, defaults to None
    :type total: int, optional
    :param change: change, defaults to None
    :type change: AdditionChange, optional
    """

    def __init__(
        self, total: int = SENTINEL, change: AdditionChange = SENTINEL, **kwargs
    ):
        """Addition

        :param total: Total number of additions, defaults to None
        :type total: int, optional
        :param change: change, defaults to None
        :type change: AdditionChange, optional
        """
        if total is not SENTINEL:
            self.total = total
        if change is not SENTINEL:
            self.change = self._define_object(change, AdditionChange)
        self._kwargs = kwargs


@JsonMap({"element_name": "elementName"})
class ChangeElementKey2(BaseModel):
    """ChangeElementKey2

    :param element_name: Name of the element, defaults to None
    :type element_name: str, optional
    """

    def __init__(self, element_name: str = SENTINEL, **kwargs):
        """ChangeElementKey2

        :param element_name: Name of the element, defaults to None
        :type element_name: str, optional
        """
        if element_name is not SENTINEL:
            self.element_name = element_name
        self._kwargs = kwargs


@JsonMap(
    {
        "type_": "type",
        "changed_particle_name": "changedParticleName",
        "element_key": "elementKey",
        "new_value": "newValue",
        "old_value": "oldValue",
    }
)
class ModificationChange(BaseModel):
    """ModificationChange

    :param type_: Type of modification (e.g., attribute), defaults to None
    :type type_: str, optional
    :param changed_particle_name: Name of the particle that was modified, defaults to None
    :type changed_particle_name: str, optional
    :param element_key: element_key, defaults to None
    :type element_key: ChangeElementKey2, optional
    :param new_value: New value of the attribute, defaults to None
    :type new_value: str, optional
    :param old_value: Old value of the attribute, defaults to None
    :type old_value: str, optional
    """

    def __init__(
        self,
        type_: str = SENTINEL,
        changed_particle_name: str = SENTINEL,
        element_key: ChangeElementKey2 = SENTINEL,
        new_value: str = SENTINEL,
        old_value: str = SENTINEL,
        **kwargs
    ):
        """ModificationChange

        :param type_: Type of modification (e.g., attribute), defaults to None
        :type type_: str, optional
        :param changed_particle_name: Name of the particle that was modified, defaults to None
        :type changed_particle_name: str, optional
        :param element_key: element_key, defaults to None
        :type element_key: ChangeElementKey2, optional
        :param new_value: New value of the attribute, defaults to None
        :type new_value: str, optional
        :param old_value: Old value of the attribute, defaults to None
        :type old_value: str, optional
        """
        if type_ is not SENTINEL:
            self.type_ = type_
        if changed_particle_name is not SENTINEL:
            self.changed_particle_name = changed_particle_name
        if element_key is not SENTINEL:
            self.element_key = self._define_object(element_key, ChangeElementKey2)
        if new_value is not SENTINEL:
            self.new_value = new_value
        if old_value is not SENTINEL:
            self.old_value = old_value
        self._kwargs = kwargs


@JsonMap({})
class Modification(BaseModel):
    """Modification

    :param total: Total number of modifications, defaults to None
    :type total: int, optional
    :param change: change, defaults to None
    :type change: ModificationChange, optional
    """

    def __init__(
        self, total: int = SENTINEL, change: ModificationChange = SENTINEL, **kwargs
    ):
        """Modification

        :param total: Total number of modifications, defaults to None
        :type total: int, optional
        :param change: change, defaults to None
        :type change: ModificationChange, optional
        """
        if total is not SENTINEL:
            self.total = total
        if change is not SENTINEL:
            self.change = self._define_object(change, ModificationChange)
        self._kwargs = kwargs


@JsonMap({})
class GenericDiff(BaseModel):
    """GenericDiff

    :param addition: addition, defaults to None
    :type addition: Addition, optional
    :param modification: modification, defaults to None
    :type modification: Modification, optional
    """

    def __init__(
        self,
        addition: Addition = SENTINEL,
        modification: Modification = SENTINEL,
        **kwargs
    ):
        """GenericDiff

        :param addition: addition, defaults to None
        :type addition: Addition, optional
        :param modification: modification, defaults to None
        :type modification: Modification, optional
        """
        if addition is not SENTINEL:
            self.addition = self._define_object(addition, Addition)
        if modification is not SENTINEL:
            self.modification = self._define_object(modification, Modification)
        self._kwargs = kwargs


@JsonMap({"generic_diff": "GenericDiff"})
class ComponentDiffResponse(BaseModel):
    """ComponentDiffResponse

    :param message: Message providing details about the diffed components, defaults to None
    :type message: str, optional
    :param generic_diff: generic_diff, defaults to None
    :type generic_diff: GenericDiff, optional
    """

    def __init__(
        self, message: str = SENTINEL, generic_diff: GenericDiff = SENTINEL, **kwargs
    ):
        """ComponentDiffResponse

        :param message: Message providing details about the diffed components, defaults to None
        :type message: str, optional
        :param generic_diff: generic_diff, defaults to None
        :type generic_diff: GenericDiff, optional
        """
        if message is not SENTINEL:
            self.message = message
        if generic_diff is not SENTINEL:
            self.generic_diff = self._define_object(generic_diff, GenericDiff)
        self._kwargs = kwargs


@JsonMap({"component_diff_response": "ComponentDiffResponse"})
class ComponentDiffResponseCreate(BaseModel):
    """ComponentDiffResponseCreate

    :param component_diff_response: component_diff_response, defaults to None
    :type component_diff_response: ComponentDiffResponse, optional
    """

    def __init__(
        self, component_diff_response: ComponentDiffResponse = SENTINEL, **kwargs
    ):
        """ComponentDiffResponseCreate

        :param component_diff_response: component_diff_response, defaults to None
        :type component_diff_response: ComponentDiffResponse, optional
        """
        if component_diff_response is not SENTINEL:
            self.component_diff_response = self._define_object(
                component_diff_response, ComponentDiffResponse
            )
        self._kwargs = kwargs
