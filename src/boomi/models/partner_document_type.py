
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class InvalidDocumentRouting(Enum):
    """An enumeration representing different categories.

    :cvar DOCUMENTSPATH: "documentsPath"
    :vartype DOCUMENTSPATH: str
    :cvar ERRORSPATH: "errorsPath"
    :vartype ERRORSPATH: str
    """

    DOCUMENTSPATH = "documentsPath"
    ERRORSPATH = "errorsPath"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, InvalidDocumentRouting._member_map_.values())
        )


@JsonMap(
    {
        "expect_ack_for_outbound": "expectAckForOutbound",
        "invalid_document_routing": "invalidDocumentRouting",
        "profile_id": "profileId",
        "qualifier_validation": "qualifierValidation",
        "type_id": "typeId",
        "use999_ack": "use999Ack",
        "use_ta1_ack": "useTA1Ack",
        "validate_outbound_transaction_sets": "validateOutboundTransactionSets",
    }
)
class PartnerDocumentType(BaseModel):
    """PartnerDocumentType

    :param expect_ack_for_outbound: expect_ack_for_outbound, defaults to None
    :type expect_ack_for_outbound: bool, optional
    :param invalid_document_routing: invalid_document_routing, defaults to None
    :type invalid_document_routing: InvalidDocumentRouting, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param profile_id: profile_id, defaults to None
    :type profile_id: str, optional
    :param qualifier_validation: qualifier_validation, defaults to None
    :type qualifier_validation: bool, optional
    :param type_id: type_id, defaults to None
    :type type_id: str, optional
    :param use999_ack: use999_ack, defaults to None
    :type use999_ack: bool, optional
    :param use_ta1_ack: use_ta1_ack, defaults to None
    :type use_ta1_ack: bool, optional
    :param validate_outbound_transaction_sets: validate_outbound_transaction_sets, defaults to None
    :type validate_outbound_transaction_sets: bool, optional
    """

    def __init__(
        self,
        expect_ack_for_outbound: bool = SENTINEL,
        invalid_document_routing: InvalidDocumentRouting = SENTINEL,
        name: str = SENTINEL,
        profile_id: str = SENTINEL,
        qualifier_validation: bool = SENTINEL,
        type_id: str = SENTINEL,
        use999_ack: bool = SENTINEL,
        use_ta1_ack: bool = SENTINEL,
        validate_outbound_transaction_sets: bool = SENTINEL,
        **kwargs
    ):
        """PartnerDocumentType

        :param expect_ack_for_outbound: expect_ack_for_outbound, defaults to None
        :type expect_ack_for_outbound: bool, optional
        :param invalid_document_routing: invalid_document_routing, defaults to None
        :type invalid_document_routing: InvalidDocumentRouting, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param profile_id: profile_id, defaults to None
        :type profile_id: str, optional
        :param qualifier_validation: qualifier_validation, defaults to None
        :type qualifier_validation: bool, optional
        :param type_id: type_id, defaults to None
        :type type_id: str, optional
        :param use999_ack: use999_ack, defaults to None
        :type use999_ack: bool, optional
        :param use_ta1_ack: use_ta1_ack, defaults to None
        :type use_ta1_ack: bool, optional
        :param validate_outbound_transaction_sets: validate_outbound_transaction_sets, defaults to None
        :type validate_outbound_transaction_sets: bool, optional
        """
        if expect_ack_for_outbound is not SENTINEL:
            self.expect_ack_for_outbound = expect_ack_for_outbound
        if invalid_document_routing is not SENTINEL:
            self.invalid_document_routing = self._enum_matching(
                invalid_document_routing,
                InvalidDocumentRouting.list(),
                "invalid_document_routing",
            )
        if name is not SENTINEL:
            self.name = name
        if profile_id is not SENTINEL:
            self.profile_id = profile_id
        if qualifier_validation is not SENTINEL:
            self.qualifier_validation = qualifier_validation
        if type_id is not SENTINEL:
            self.type_id = type_id
        if use999_ack is not SENTINEL:
            self.use999_ack = use999_ack
        if use_ta1_ack is not SENTINEL:
            self.use_ta1_ack = use_ta1_ack
        if validate_outbound_transaction_sets is not SENTINEL:
            self.validate_outbound_transaction_sets = validate_outbound_transaction_sets
        self._kwargs = kwargs
