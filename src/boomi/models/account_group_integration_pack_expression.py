
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"created_at": "createdAt", "updated_at": "updatedAt"})
class AccountGroupIntegrationPackExpressionMetadata(BaseModel):
    """AccountGroupIntegrationPackExpressionMetadata

    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param updated_at: updated_at, defaults to None
    :type updated_at: str, optional
    """

    def __init__(
        self, created_at: str = SENTINEL, updated_at: str = SENTINEL, **kwargs
    ):
        """AccountGroupIntegrationPackExpressionMetadata

        :param created_at: created_at, defaults to None
        :type created_at: str, optional
        :param updated_at: updated_at, defaults to None
        :type updated_at: str, optional
        """
        if created_at is not SENTINEL:
            self.created_at = created_at
        if updated_at is not SENTINEL:
            self.updated_at = updated_at
        self._kwargs = kwargs


@JsonMap({"id_": "id"})
class AccountGroupIntegrationPackExpression(BaseModel):
    """AccountGroupIntegrationPackExpression

    :param id_: A unique ID assigned by the system to the integration pack. This field populates only if you add the integration pack to an account group., defaults to None
    :type id_: str, optional
    :param name: The name of the integration pack., defaults to None
    :type name: str, optional
    :param status: status, defaults to None
    :type status: str, optional
    :param metadata: metadata, defaults to None
    :type metadata: AccountGroupIntegrationPackExpressionMetadata, optional
    """

    def __init__(
        self,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        status: str = SENTINEL,
        metadata: AccountGroupIntegrationPackExpressionMetadata = SENTINEL,
        **kwargs
    ):
        """AccountGroupIntegrationPackExpression

        :param id_: A unique ID assigned by the system to the integration pack. This field populates only if you add the integration pack to an account group., defaults to None
        :type id_: str, optional
        :param name: The name of the integration pack., defaults to None
        :type name: str, optional
        :param status: status, defaults to None
        :type status: str, optional
        :param metadata: metadata, defaults to None
        :type metadata: AccountGroupIntegrationPackExpressionMetadata, optional
        """
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        if status is not SENTINEL:
            self.status = status
        if metadata is not SENTINEL:
            self.metadata = self._define_object(
                metadata, AccountGroupIntegrationPackExpressionMetadata
            )
        self._kwargs = kwargs
