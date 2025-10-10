
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cross_reference_inputs import CrossReferenceInputs
from .cross_reference_outputs import CrossReferenceOutputs


@JsonMap(
    {
        "inputs": "Inputs",
        "outputs": "Outputs",
        "lookup_table_id": "lookupTableId",
        "skip_if_no_inputs": "skipIfNoInputs",
    }
)
class MapExtensionsCrossReferenceLookup(BaseModel):
    """MapExtensionsCrossReferenceLookup

    :param inputs: inputs
    :type inputs: CrossReferenceInputs
    :param outputs: outputs
    :type outputs: CrossReferenceOutputs
    :param lookup_table_id: lookup_table_id, defaults to None
    :type lookup_table_id: str, optional
    :param skip_if_no_inputs: skip_if_no_inputs, defaults to None
    :type skip_if_no_inputs: bool, optional
    """

    def __init__(
        self,
        inputs: CrossReferenceInputs,
        outputs: CrossReferenceOutputs,
        lookup_table_id: str = SENTINEL,
        skip_if_no_inputs: bool = SENTINEL,
        **kwargs,
    ):
        """MapExtensionsCrossReferenceLookup

        :param inputs: inputs
        :type inputs: CrossReferenceInputs
        :param outputs: outputs
        :type outputs: CrossReferenceOutputs
        :param lookup_table_id: lookup_table_id, defaults to None
        :type lookup_table_id: str, optional
        :param skip_if_no_inputs: skip_if_no_inputs, defaults to None
        :type skip_if_no_inputs: bool, optional
        """
        self.inputs = self._define_object(inputs, CrossReferenceInputs)
        self.outputs = self._define_object(outputs, CrossReferenceOutputs)
        if lookup_table_id is not SENTINEL:
            self.lookup_table_id = lookup_table_id
        if skip_if_no_inputs is not SENTINEL:
            self.skip_if_no_inputs = skip_if_no_inputs
        self._kwargs = kwargs
