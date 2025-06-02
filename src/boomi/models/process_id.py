
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "original_process_id": "originalProcessId",
        "wrapper_process_id": "wrapperProcessId",
    }
)
class ProcessId(BaseModel):
    """ProcessId

    :param name: The name of the process., defaults to None
    :type name: str, optional
    :param original_process_id: A unique ID assigned by the system when the process is created., defaults to None
    :type original_process_id: str, optional
    :param wrapper_process_id: A unique ID assigned to each process associated with multi-install integration packs. A `wrapperProcessId` is generated when an IntegrationPackInstance is installed or created.   \>**Note:** The `wrapperProcessId` will not be returned for the single-install integration pack while making API calls, as it is only generated for the multi-install integration packs., defaults to None
    :type wrapper_process_id: str, optional
    """

    def __init__(
        self,
        name: str = SENTINEL,
        original_process_id: str = SENTINEL,
        wrapper_process_id: str = SENTINEL,
        **kwargs
    ):
        """ProcessId

        :param name: The name of the process., defaults to None
        :type name: str, optional
        :param original_process_id: A unique ID assigned by the system when the process is created., defaults to None
        :type original_process_id: str, optional
        :param wrapper_process_id: A unique ID assigned to each process associated with multi-install integration packs. A `wrapperProcessId` is generated when an IntegrationPackInstance is installed or created.   \>**Note:** The `wrapperProcessId` will not be returned for the single-install integration pack while making API calls, as it is only generated for the multi-install integration packs., defaults to None
        :type wrapper_process_id: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if original_process_id is not SENTINEL:
            self.original_process_id = original_process_id
        if wrapper_process_id is not SENTINEL:
            self.wrapper_process_id = wrapper_process_id
        self._kwargs = kwargs
