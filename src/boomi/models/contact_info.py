
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"contact_name": "contactName"})
class ContactInfo(BaseModel):
    """ContactInfo

    :param address1: address1
    :type address1: str
    :param address2: address2
    :type address2: str
    :param city: city
    :type city: str
    :param contact_name: contact_name
    :type contact_name: str
    :param country: country
    :type country: str
    :param email: email
    :type email: str
    :param fax: fax
    :type fax: str
    :param phone: phone
    :type phone: str
    :param postalcode: postalcode
    :type postalcode: str
    :param state: state
    :type state: str
    """

    def __init__(
        self,
        address1: str,
        address2: str,
        city: str,
        contact_name: str,
        country: str,
        email: str,
        fax: str,
        phone: str,
        postalcode: str,
        state: str,
        **kwargs
    ):
        """ContactInfo

        :param address1: address1
        :type address1: str
        :param address2: address2
        :type address2: str
        :param city: city
        :type city: str
        :param contact_name: contact_name
        :type contact_name: str
        :param country: country
        :type country: str
        :param email: email
        :type email: str
        :param fax: fax
        :type fax: str
        :param phone: phone
        :type phone: str
        :param postalcode: postalcode
        :type postalcode: str
        :param state: state
        :type state: str
        """
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.contact_name = contact_name
        self.country = country
        self.email = email
        self.fax = fax
        self.phone = phone
        self.postalcode = postalcode
        self.state = state
        self._kwargs = kwargs
