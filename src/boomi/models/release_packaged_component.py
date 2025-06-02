
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"component_id": "componentId", "released_version": "releasedVersion"})
class ReleasePackagedComponent(BaseModel):
    """ReleasePackagedComponent

    :param component_id: The ID of the component., defaults to None
    :type component_id: str, optional
    :param released_version: The released version of the packaged component., defaults to None
    :type released_version: str, optional
    :param version: Packaged component version of the component that will be included in the next release of this integration pack., defaults to None
    :type version: str, optional
    """

    def __init__(
        self,
        component_id: str = SENTINEL,
        released_version: str = SENTINEL,
        version: str = SENTINEL,
        **kwargs
    ):
        """ReleasePackagedComponent

        :param component_id: The ID of the component., defaults to None
        :type component_id: str, optional
        :param released_version: The released version of the packaged component., defaults to None
        :type released_version: str, optional
        :param version: Packaged component version of the component that will be included in the next release of this integration pack., defaults to None
        :type version: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        if released_version is not SENTINEL:
            self.released_version = released_version
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
