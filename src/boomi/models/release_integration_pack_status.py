
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .release_packaged_components import ReleasePackagedComponents


class ReleaseIntegrationPackStatusInstallationType(Enum):
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
                ReleaseIntegrationPackStatusInstallationType._member_map_.values(),
            )
        )


class ReleaseIntegrationPackStatusReleaseSchedule(Enum):
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
                ReleaseIntegrationPackStatusReleaseSchedule._member_map_.values(),
            )
        )


class ReleaseStatus(Enum):
    """An enumeration representing different categories.

    :cvar INPROGRESS: "IN_PROGRESS"
    :vartype INPROGRESS: str
    :cvar SUCCESS: "SUCCESS"
    :vartype SUCCESS: str
    :cvar SCHEDULED: "SCHEDULED"
    :vartype SCHEDULED: str
    :cvar ERROR: "ERROR"
    :vartype ERROR: str
    """

    INPROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    SCHEDULED = "SCHEDULED"
    ERROR = "ERROR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ReleaseStatus._member_map_.values()))


@JsonMap(
    {
        "release_packaged_components": "ReleasePackagedComponents",
        "installation_type": "installationType",
        "integration_pack_id": "integrationPackId",
        "release_on_date": "releaseOnDate",
        "release_schedule": "releaseSchedule",
        "release_status": "releaseStatus",
        "request_id": "requestId",
        "response_status_code": "responseStatusCode",
    }
)
class ReleaseIntegrationPackStatus(BaseModel):
    """ReleaseIntegrationPackStatus

    :param release_packaged_components: release_packaged_components, defaults to None
    :type release_packaged_components: ReleasePackagedComponents, optional
    :param installation_type: The type of integration pack. Possible values: - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
    :type installation_type: ReleaseIntegrationPackStatusInstallationType, optional
    :param integration_pack_id: A unique ID assigned by the system to the integration pack., defaults to None
    :type integration_pack_id: str, optional
    :param name: The name of the integration pack., defaults to None
    :type name: str, optional
    :param release_on_date: Date for future release of integration pack.  Date Format: yyyy-MM-dd, defaults to None
    :type release_on_date: str, optional
    :param release_schedule: Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release, defaults to None
    :type release_schedule: ReleaseIntegrationPackStatusReleaseSchedule, optional
    :param release_status: The type of release Status. Possible values: - INPROGRESS — for currently releasing integration pack - SUCCESS — for successfully released integration pack - SCHEDULED — for future release integration pack - ERROR — for any error resulting in the release, defaults to None
    :type release_status: ReleaseStatus, optional
    :param request_id: A unique ID assigned by the system to the integration pack release request., defaults to None
    :type request_id: str, optional
    :param response_status_code: response_status_code
    :type response_status_code: int
    """

    def __init__(
        self,
        response_status_code: int,
        release_packaged_components: ReleasePackagedComponents = SENTINEL,
        installation_type: ReleaseIntegrationPackStatusInstallationType = SENTINEL,
        integration_pack_id: str = SENTINEL,
        name: str = SENTINEL,
        release_on_date: str = SENTINEL,
        release_schedule: ReleaseIntegrationPackStatusReleaseSchedule = SENTINEL,
        release_status: ReleaseStatus = SENTINEL,
        request_id: str = SENTINEL,
        **kwargs,
    ):
        """ReleaseIntegrationPackStatus

        :param release_packaged_components: release_packaged_components, defaults to None
        :type release_packaged_components: ReleasePackagedComponents, optional
        :param installation_type: The type of integration pack. Possible values: - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
        :type installation_type: ReleaseIntegrationPackStatusInstallationType, optional
        :param integration_pack_id: A unique ID assigned by the system to the integration pack., defaults to None
        :type integration_pack_id: str, optional
        :param name: The name of the integration pack., defaults to None
        :type name: str, optional
        :param release_on_date: Date for future release of integration pack.  Date Format: yyyy-MM-dd, defaults to None
        :type release_on_date: str, optional
        :param release_schedule: Specify the type of release schedule for the integration pack. Possible values: - IMMEDIATELY — for immediate release - RELEASE_ON_SPECIFIED_DATE — for future release, defaults to None
        :type release_schedule: ReleaseIntegrationPackStatusReleaseSchedule, optional
        :param release_status: The type of release Status. Possible values: - INPROGRESS — for currently releasing integration pack - SUCCESS — for successfully released integration pack - SCHEDULED — for future release integration pack - ERROR — for any error resulting in the release, defaults to None
        :type release_status: ReleaseStatus, optional
        :param request_id: A unique ID assigned by the system to the integration pack release request., defaults to None
        :type request_id: str, optional
        :param response_status_code: response_status_code
        :type response_status_code: int
        """
        if release_packaged_components is not SENTINEL:
            self.release_packaged_components = self._define_object(
                release_packaged_components, ReleasePackagedComponents
            )
        if installation_type is not SENTINEL:
            self.installation_type = self._enum_matching(
                installation_type,
                ReleaseIntegrationPackStatusInstallationType.list(),
                "installation_type",
            )
        if integration_pack_id is not SENTINEL:
            self.integration_pack_id = integration_pack_id
        if name is not SENTINEL:
            self.name = name
        if release_on_date is not SENTINEL:
            self.release_on_date = release_on_date
        if release_schedule is not SENTINEL:
            self.release_schedule = self._enum_matching(
                release_schedule,
                ReleaseIntegrationPackStatusReleaseSchedule.list(),
                "release_schedule",
            )
        if release_status is not SENTINEL:
            self.release_status = self._enum_matching(
                release_status, ReleaseStatus.list(), "release_status"
            )
        if request_id is not SENTINEL:
            self.request_id = request_id
        self.response_status_code = response_status_code
        self._kwargs = kwargs
