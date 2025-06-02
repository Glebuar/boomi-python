
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .release_packaged_components import ReleasePackagedComponents


class ReleaseIntegrationPackInstallationType(Enum):
    """An enumeration representing different categories.

    :cvar SINGLE: "SINGLE"
    :vartype SINGLE: str
    :cvar MULTI: "MULTI"
    :vartype MULTI: str
    """

    SINGLE = "SINGLE"
    MULTI = "MULTI"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ReleaseIntegrationPackInstallationType._member_map_.values(),
            )
        )


class ReleaseIntegrationPackReleaseSchedule(Enum):
    """An enumeration representing different categories.

    :cvar IMMEDIATELY: "IMMEDIATELY"
    :vartype IMMEDIATELY: str
    :cvar RELEASEONSPECIFIEDDATE: "RELEASE_ON_SPECIFIED_DATE"
    :vartype RELEASEONSPECIFIEDDATE: str
    """

    IMMEDIATELY = "IMMEDIATELY"
    RELEASEONSPECIFIEDDATE = "RELEASE_ON_SPECIFIED_DATE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ReleaseIntegrationPackReleaseSchedule._member_map_.values(),
            )
        )


@JsonMap(
    {
        "release_packaged_components": "ReleasePackagedComponents",
        "id_": "id",
        "installation_type": "installationType",
        "release_on_date": "releaseOnDate",
        "release_schedule": "releaseSchedule",
        "release_status_url": "releaseStatusUrl",
        "request_id": "requestId",
    }
)
class ReleaseIntegrationPack(BaseModel):
    """ReleaseIntegrationPack

    :param release_packaged_components: release_packaged_components, defaults to None
    :type release_packaged_components: ReleasePackagedComponents, optional
    :param id_: The ID of the integration pack., defaults to None
    :type id_: str, optional
    :param installation_type: The type of integration pack. Possible values: - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
    :type installation_type: ReleaseIntegrationPackInstallationType, optional
    :param name: The name of the integration pack., defaults to None
    :type name: str, optional
    :param release_on_date: Date for future release of integration pack.  Date Format: yyyy-MM-dd, defaults to None
    :type release_on_date: str, optional
    :param release_schedule: Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release, defaults to None
    :type release_schedule: ReleaseIntegrationPackReleaseSchedule, optional
    :param release_status_url: The complete endpoint URL used to make a second call to the ReleaseIntegrationPackStatus object.  It is provided for your convenience in the `releaseStatusUrl` field of the initial POST response., defaults to None
    :type release_status_url: str, optional
    :param request_id: A unique ID assigned by the system to the integration pack release request., defaults to None
    :type request_id: str, optional
    """

    def __init__(
        self,
        release_packaged_components: ReleasePackagedComponents = SENTINEL,
        id_: str = SENTINEL,
        installation_type: ReleaseIntegrationPackInstallationType = SENTINEL,
        name: str = SENTINEL,
        release_on_date: str = SENTINEL,
        release_schedule: ReleaseIntegrationPackReleaseSchedule = SENTINEL,
        release_status_url: str = SENTINEL,
        request_id: str = SENTINEL,
        **kwargs,
    ):
        """ReleaseIntegrationPack

        :param release_packaged_components: release_packaged_components, defaults to None
        :type release_packaged_components: ReleasePackagedComponents, optional
        :param id_: The ID of the integration pack., defaults to None
        :type id_: str, optional
        :param installation_type: The type of integration pack. Possible values: - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
        :type installation_type: ReleaseIntegrationPackInstallationType, optional
        :param name: The name of the integration pack., defaults to None
        :type name: str, optional
        :param release_on_date: Date for future release of integration pack.  Date Format: yyyy-MM-dd, defaults to None
        :type release_on_date: str, optional
        :param release_schedule: Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release, defaults to None
        :type release_schedule: ReleaseIntegrationPackReleaseSchedule, optional
        :param release_status_url: The complete endpoint URL used to make a second call to the ReleaseIntegrationPackStatus object.  It is provided for your convenience in the `releaseStatusUrl` field of the initial POST response., defaults to None
        :type release_status_url: str, optional
        :param request_id: A unique ID assigned by the system to the integration pack release request., defaults to None
        :type request_id: str, optional
        """
        if release_packaged_components is not SENTINEL:
            self.release_packaged_components = self._define_object(
                release_packaged_components, ReleasePackagedComponents
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        if installation_type is not SENTINEL:
            self.installation_type = self._enum_matching(
                installation_type,
                ReleaseIntegrationPackInstallationType.list(),
                "installation_type",
            )
        if name is not SENTINEL:
            self.name = name
        if release_on_date is not SENTINEL:
            self.release_on_date = release_on_date
        if release_schedule is not SENTINEL:
            self.release_schedule = self._enum_matching(
                release_schedule,
                ReleaseIntegrationPackReleaseSchedule.list(),
                "release_schedule",
            )
        if release_status_url is not SENTINEL:
            self.release_status_url = release_status_url
        if request_id is not SENTINEL:
            self.request_id = request_id
        self._kwargs = kwargs
