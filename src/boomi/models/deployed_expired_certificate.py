
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountId",
        "certificate_id": "certificateId",
        "certificate_name": "certificateName",
        "certificate_type": "certificateType",
        "container_id": "containerId",
        "container_name": "containerName",
        "environment_id": "environmentId",
        "environment_name": "environmentName",
        "expiration_date": "expirationDate",
        "expiration_boundary": "expirationBoundary",
    }
)
class DeployedExpiredCertificate(BaseModel):
    """DeployedExpiredCertificate

    :param account_id: The ID of the account in which you deployed the certificate., defaults to None
    :type account_id: str, optional
    :param certificate_id: The ID of the certificate., defaults to None
    :type certificate_id: str, optional
    :param certificate_name: The name of the certificate., defaults to None
    :type certificate_name: str, optional
    :param certificate_type: The type of the certificate — X.509., defaults to None
    :type certificate_type: str, optional
    :param container_id: The ID of the container \(Runtime, Runtime cluster, or Runtime cloud\) to which you deployed the certificate., defaults to None
    :type container_id: str, optional
    :param container_name: The name of the container \(Runtime, Runtime cluster, or Runtime cloud\) to which you deployed the certificate., defaults to None
    :type container_name: str, optional
    :param environment_id: If applicable, the ID of the environment in which you deployed the certificate., defaults to None
    :type environment_id: str, optional
    :param environment_name: If applicable, the environment in which you deployed the certificate., defaults to None
    :type environment_name: str, optional
    :param expiration_date: The expiration date and time of the certificate., defaults to None
    :type expiration_date: str, optional
    :param location: The location to which you deployed the certificate — either Process, Environment, Runtime, Shared Web Server, Shared Web Server Authorization, or Shared Web Server User Authorization. Environment is valid only for an environment account; Runtime is valid only for a non-environment account., defaults to None
    :type location: str, optional
    :param expiration_boundary: sets the boundary for a timespan filter beginning or ending with the current date. The value is the number of days relative to the current date.   For example, use a value of 1 to retrieve certificates that expire today or tomorrow. Use a value of 365 to retrieve certificates that expire within the next 365 days. Use a value of –1 to retrieve certificates that expired yesterday or expire today., defaults to None
    :type expiration_boundary: int, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        certificate_id: str = SENTINEL,
        certificate_name: str = SENTINEL,
        certificate_type: str = SENTINEL,
        container_id: str = SENTINEL,
        container_name: str = SENTINEL,
        environment_id: str = SENTINEL,
        environment_name: str = SENTINEL,
        expiration_date: str = SENTINEL,
        location: str = SENTINEL,
        expiration_boundary: int = SENTINEL,
        **kwargs
    ):
        """DeployedExpiredCertificate

        :param account_id: The ID of the account in which you deployed the certificate., defaults to None
        :type account_id: str, optional
        :param certificate_id: The ID of the certificate., defaults to None
        :type certificate_id: str, optional
        :param certificate_name: The name of the certificate., defaults to None
        :type certificate_name: str, optional
        :param certificate_type: The type of the certificate — X.509., defaults to None
        :type certificate_type: str, optional
        :param container_id: The ID of the container \(Runtime, Runtime cluster, or Runtime cloud\) to which you deployed the certificate., defaults to None
        :type container_id: str, optional
        :param container_name: The name of the container \(Runtime, Runtime cluster, or Runtime cloud\) to which you deployed the certificate., defaults to None
        :type container_name: str, optional
        :param environment_id: If applicable, the ID of the environment in which you deployed the certificate., defaults to None
        :type environment_id: str, optional
        :param environment_name: If applicable, the environment in which you deployed the certificate., defaults to None
        :type environment_name: str, optional
        :param expiration_date: The expiration date and time of the certificate., defaults to None
        :type expiration_date: str, optional
        :param location: The location to which you deployed the certificate — either Process, Environment, Runtime, Shared Web Server, Shared Web Server Authorization, or Shared Web Server User Authorization. Environment is valid only for an environment account; Runtime is valid only for a non-environment account., defaults to None
        :type location: str, optional
        :param expiration_boundary: sets the boundary for a timespan filter beginning or ending with the current date. The value is the number of days relative to the current date.   For example, use a value of 1 to retrieve certificates that expire today or tomorrow. Use a value of 365 to retrieve certificates that expire within the next 365 days. Use a value of –1 to retrieve certificates that expired yesterday or expire today., defaults to None
        :type expiration_boundary: int, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if certificate_id is not SENTINEL:
            self.certificate_id = certificate_id
        if certificate_name is not SENTINEL:
            self.certificate_name = certificate_name
        if certificate_type is not SENTINEL:
            self.certificate_type = certificate_type
        if container_id is not SENTINEL:
            self.container_id = container_id
        if container_name is not SENTINEL:
            self.container_name = container_name
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if environment_name is not SENTINEL:
            self.environment_name = environment_name
        if expiration_date is not SENTINEL:
            self.expiration_date = expiration_date
        if location is not SENTINEL:
            self.location = location
        if expiration_boundary is not SENTINEL:
            self.expiration_boundary = expiration_boundary
        self._kwargs = kwargs
