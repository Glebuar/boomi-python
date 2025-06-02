
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"id_": "id"})
class ComponentInfo(BaseModel):
    """ComponentInfo

    :param id_: The ID of the component.The component ID is available in the Revision History dialog, which you can open from the Build page in the user interface. Potentially, this ID can return multiple components., defaults to None
    :type id_: str, optional
    :param version: Each saved configuration is assigned a Revision History number when you change a component on the Build tab. The component version is available in the Revision History dialog, which you can access from the Build page  service., defaults to None
    :type version: int, optional
    """

    def __init__(self, id_: str = SENTINEL, version: int = SENTINEL, **kwargs):
        """ComponentInfo

        :param id_: The ID of the component.The component ID is available in the Revision History dialog, which you can open from the Build page in the user interface. Potentially, this ID can return multiple components., defaults to None
        :type id_: str, optional
        :param version: Each saved configuration is assigned a Revision History number when you change a component on the Build tab. The component version is available in the Revision History dialog, which you can access from the Build page  service., defaults to None
        :type version: int, optional
        """
        if id_ is not SENTINEL:
            self.id_ = id_
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
