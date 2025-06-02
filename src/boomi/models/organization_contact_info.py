
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "contact_name": "contactName",
        "contact_url": "contactUrl",
        "country": "country",
        "email": "email",
        "fax": "fax",
        "phone": "phone",
        "postalcode": "postalcode",
        "state": "state",
    }
)
class OrganizationContactInfo(BaseModel):
    """OrganizationContactInfo

    :param address1: First line of the street address of the organization.
    :type address1: str
    :param address2: Second line of the street address of the organization.
    :type address2: str
    :param city: Location of the city for the organization.
    :type city: str
    :param contact_name: Name of the contact for the organization.
    :type contact_name: str
    :param contact_url: Contact URL for the organization.
    :type contact_url: str
    :param country: Location of the country for the organization.
    :type country: str
    :param email: Email address of the organization.
    :type email: str
    :param fax: Fax number for the organization.
    :type fax: str
    :param phone: Phone number for the organization.
    :type phone: str
    :param postalcode: Postal code, such as a Zip Code.
    :type postalcode: str
    :param state: Location of the state or province for the organization.
    :type state: str
    """

    def __init__(
        self,
        address1: str,
        address2: str,
        city: str,
        contact_name: str,
        contact_url: str,
        country: str,
        email: str,
        fax: str,
        phone: str,
        postalcode: str,
        state: str,
        **kwargs
    ):
        """OrganizationContactInfo

        :param address1: First line of the street address of the organization.
        :type address1: str
        :param address2: Second line of the street address of the organization.
        :type address2: str
        :param city: Location of the city for the organization.
        :type city: str
        :param contact_name: Name of the contact for the organization.
        :type contact_name: str
        :param contact_url: Contact URL for the organization.
        :type contact_url: str
        :param country: Location of the country for the organization.
        :type country: str
        :param email: Email address of the organization.
        :type email: str
        :param fax: Fax number for the organization.
        :type fax: str
        :param phone: Phone number for the organization.
        :type phone: str
        :param postalcode: Postal code, such as a Zip Code.
        :type postalcode: str
        :param state: Location of the state or province for the organization.
        :type state: str
        """
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.contact_name = contact_name
        self.contact_url = contact_url
        self.country = country
        self.email = email
        self.fax = fax
        self.phone = phone
        self.postalcode = postalcode
        self.state = state
        self._kwargs = kwargs
