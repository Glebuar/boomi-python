
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .scripting_inputs import ScriptingInputs
from .scripting_outputs import ScriptingOutputs


class Language(Enum):
    """An enumeration representing different categories.

    :cvar GROOVY: "GROOVY"
    :vartype GROOVY: str
    :cvar GROOVY2: "GROOVY2"
    :vartype GROOVY2: str
    :cvar JAVASCRIPT: "Javascript"
    :vartype JAVASCRIPT: str
    """

    GROOVY = "GROOVY"
    GROOVY2 = "GROOVY2"
    JAVASCRIPT = "Javascript"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Language._member_map_.values()))


@JsonMap({"inputs": "Inputs", "outputs": "Outputs", "script": "Script"})
class MapExtensionsScripting(BaseModel):
    """MapExtensionsScripting

    :param inputs: inputs
    :type inputs: ScriptingInputs
    :param outputs: outputs
    :type outputs: ScriptingOutputs
    :param script: script
    :type script: str
    :param language: language, defaults to None
    :type language: Language, optional
    """

    def __init__(
        self,
        inputs: ScriptingInputs,
        outputs: ScriptingOutputs,
        script: str,
        language: Language = SENTINEL,
        **kwargs,
    ):
        """MapExtensionsScripting

        :param inputs: inputs
        :type inputs: ScriptingInputs
        :param outputs: outputs
        :type outputs: ScriptingOutputs
        :param script: script
        :type script: str
        :param language: language, defaults to None
        :type language: Language, optional
        """
        self.inputs = self._define_object(inputs, ScriptingInputs)
        self.outputs = self._define_object(outputs, ScriptingOutputs)
        self.script = script
        if language is not SENTINEL:
            self.language = self._enum_matching(language, Language.list(), "language")
        self._kwargs = kwargs
