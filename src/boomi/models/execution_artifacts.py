
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"execution_id": "executionId"})
class ExecutionArtifacts(BaseModel):
    """ExecutionArtifacts

    :param execution_id: The ID of the given process run. You can access the run ID in the View Extended Information dialog (Manage \> Process Reporting \> Action menu) on the user interface., defaults to None
    :type execution_id: str, optional
    """

    def __init__(self, execution_id: str = SENTINEL, **kwargs):
        """ExecutionArtifacts

        :param execution_id: The ID of the given process run. You can access the run ID in the View Extended Information dialog (Manage \> Process Reporting \> Action menu) on the user interface., defaults to None
        :type execution_id: str, optional
        """
        if execution_id is not SENTINEL:
            self.execution_id = execution_id
        self._kwargs = kwargs
