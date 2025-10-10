
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_inputs import MapExtensionsInputs
from .map_extensions_function_mappings import MapExtensionsFunctionMappings
from .map_extensions_outputs import MapExtensionsOutputs
from .map_extensions_function_steps import MapExtensionsFunctionSteps


@JsonMap(
    {
        "inputs": "Inputs",
        "mappings": "Mappings",
        "outputs": "Outputs",
        "steps": "Steps",
        "created_by": "createdBy",
        "created_date": "createdDate",
        "environment_map_extension_id": "environmentMapExtensionId",
        "id_": "id",
        "modified_by": "modifiedBy",
        "modified_date": "modifiedDate",
    }
)
class EnvironmentMapExtensionUserDefinedFunction(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunction

    :param inputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
    :type inputs: MapExtensionsInputs
    :param mappings: Defines the mapping of inputs and outputs for the user-defined function and each function step. It uses the following attributes:  1. fromFunction - represents the function ID from which you are mapping.  2. fromKey - represents the function's output key from which you are mapping.  3. toFunction - represents the function ID to which you are mapping.  4. toKey - represents the function's input key to which you are mapping.
    :type mappings: MapExtensionsFunctionMappings
    :param outputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
    :type outputs: MapExtensionsOutputs
    :param steps: Defines the individual function steps and the order in which they need to occur within the greater user-defined function. The following attributes are used: 1.`position` - represents the step's number order in the greater function. 2.`cacheType` - indicates the caching behavior of the individual function step. The allowed `cacheType` values are:1.`None` \(default, if omitted in the request\)— It does not use Map function caching. 2. `ByDocument` — Caches the map function’s input and output values for each processed document. 3. `ByMap` — Caches the map function’s input and output values for each processed map. -   `id` - represents the function step's ID in the format of "FUNCEXT--xxxxxxxxxx". 4. `type` - represents the type of function \(for example, "MathCeil" or "CustomScripting"\).\<br /\> Within the `Steps` element, you also need to define the following `input` and `output` variables for each function step:\<br /\>1. `default` - Optional. Specifies the input value that the function uses if not provided by the user.\<br /\>2. `name` - the user-defined name of the associated input or output.   \>**Note:** The user interface automatically uses the used function type as the step name, but you can use this API object to change function step names. 3. `key` - the number ID assigned to a function step. This key is used to map function steps together in the `Mappings` attribute.
    :type steps: MapExtensionsFunctionSteps
    :param created_by: The user ID of the user who created the user-defined function., defaults to None
    :type created_by: str, optional
    :param created_date: Timestamp of the creation of the user-defined function., defaults to None
    :type created_date: str, optional
    :param deleted: This variable indicates the deleted status of the user defined function component. If the value is true, it indicates the deletion of the referenced user-defined function. A false value indicates that the referenced user-defined function is not deleted and is available for use., defaults to None
    :type deleted: bool, optional
    :param description: Optional. Additional details about the user-defined function component., defaults to None
    :type description: str, optional
    :param environment_map_extension_id: The ID of an environment map extension. **Important:** This and other Environment Map Extension API objects require the client to know the ID of the environment map extension. In the user-defined function interface, click **Copy EME ID** to easily copy this ID for use in your API requests, or query the [Environment Map Extensions Summary object](/api/platformapi#tag/EnvironmentMapExtensionsSummary)., defaults to None
    :type environment_map_extension_id: str, optional
    :param id_: Required. Represents the unique, system-generated ID of the extended user-defined function., defaults to None
    :type id_: str, optional
    :param modified_by: The user ID of the user who last updated the user-defined function., defaults to None
    :type modified_by: str, optional
    :param modified_date: Timestamp of when the user-defined function was last updated., defaults to None
    :type modified_date: str, optional
    :param name: Required. Represents the name of the user-defined function component., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        inputs: MapExtensionsInputs,
        mappings: MapExtensionsFunctionMappings,
        outputs: MapExtensionsOutputs,
        steps: MapExtensionsFunctionSteps,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        deleted: bool = SENTINEL,
        description: str = SENTINEL,
        environment_map_extension_id: str = SENTINEL,
        id_: str = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunction

        :param inputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
        :type inputs: MapExtensionsInputs
        :param mappings: Defines the mapping of inputs and outputs for the user-defined function and each function step. It uses the following attributes:  1. fromFunction - represents the function ID from which you are mapping.  2. fromKey - represents the function's output key from which you are mapping.  3. toFunction - represents the function ID to which you are mapping.  4. toKey - represents the function's input key to which you are mapping.
        :type mappings: MapExtensionsFunctionMappings
        :param outputs: Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.   The maximum number of inputs or outputs is 100.
        :type outputs: MapExtensionsOutputs
        :param steps: Defines the individual function steps and the order in which they need to occur within the greater user-defined function. The following attributes are used: 1.`position` - represents the step's number order in the greater function. 2.`cacheType` - indicates the caching behavior of the individual function step. The allowed `cacheType` values are:1.`None` \(default, if omitted in the request\)— It does not use Map function caching. 2. `ByDocument` — Caches the map function’s input and output values for each processed document. 3. `ByMap` — Caches the map function’s input and output values for each processed map. -   `id` - represents the function step's ID in the format of "FUNCEXT--xxxxxxxxxx". 4. `type` - represents the type of function \(for example, "MathCeil" or "CustomScripting"\).\<br /\> Within the `Steps` element, you also need to define the following `input` and `output` variables for each function step:\<br /\>1. `default` - Optional. Specifies the input value that the function uses if not provided by the user.\<br /\>2. `name` - the user-defined name of the associated input or output.   \>**Note:** The user interface automatically uses the used function type as the step name, but you can use this API object to change function step names. 3. `key` - the number ID assigned to a function step. This key is used to map function steps together in the `Mappings` attribute.
        :type steps: MapExtensionsFunctionSteps
        :param created_by: The user ID of the user who created the user-defined function., defaults to None
        :type created_by: str, optional
        :param created_date: Timestamp of the creation of the user-defined function., defaults to None
        :type created_date: str, optional
        :param deleted: This variable indicates the deleted status of the user defined function component. If the value is true, it indicates the deletion of the referenced user-defined function. A false value indicates that the referenced user-defined function is not deleted and is available for use., defaults to None
        :type deleted: bool, optional
        :param description: Optional. Additional details about the user-defined function component., defaults to None
        :type description: str, optional
        :param environment_map_extension_id: The ID of an environment map extension. **Important:** This and other Environment Map Extension API objects require the client to know the ID of the environment map extension. In the user-defined function interface, click **Copy EME ID** to easily copy this ID for use in your API requests, or query the [Environment Map Extensions Summary object](/api/platformapi#tag/EnvironmentMapExtensionsSummary)., defaults to None
        :type environment_map_extension_id: str, optional
        :param id_: Required. Represents the unique, system-generated ID of the extended user-defined function., defaults to None
        :type id_: str, optional
        :param modified_by: The user ID of the user who last updated the user-defined function., defaults to None
        :type modified_by: str, optional
        :param modified_date: Timestamp of when the user-defined function was last updated., defaults to None
        :type modified_date: str, optional
        :param name: Required. Represents the name of the user-defined function component., defaults to None
        :type name: str, optional
        """
        self.inputs = self._define_object(inputs, MapExtensionsInputs)
        self.mappings = self._define_object(mappings, MapExtensionsFunctionMappings)
        self.outputs = self._define_object(outputs, MapExtensionsOutputs)
        self.steps = self._define_object(steps, MapExtensionsFunctionSteps)
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if deleted is not SENTINEL:
            self.deleted = deleted
        if description is not SENTINEL:
            self.description = description
        if environment_map_extension_id is not SENTINEL:
            self.environment_map_extension_id = environment_map_extension_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
