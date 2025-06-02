
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {"dh_key_size_max1024": "dhKeySizeMax1024", "known_host_entry": "knownHostEntry"}
)
class SftpsshOptions(BaseModel):
    """SftpsshOptions

    :param dh_key_size_max1024: dh_key_size_max1024, defaults to None
    :type dh_key_size_max1024: bool, optional
    :param known_host_entry: known_host_entry
    :type known_host_entry: str
    :param sshkeyauth: sshkeyauth, defaults to None
    :type sshkeyauth: bool, optional
    :param sshkeypassword: sshkeypassword
    :type sshkeypassword: str
    :param sshkeypath: sshkeypath
    :type sshkeypath: str
    """

    def __init__(
        self,
        known_host_entry: str,
        sshkeypassword: str,
        sshkeypath: str,
        dh_key_size_max1024: bool = SENTINEL,
        sshkeyauth: bool = SENTINEL,
        **kwargs
    ):
        """SftpsshOptions

        :param dh_key_size_max1024: dh_key_size_max1024, defaults to None
        :type dh_key_size_max1024: bool, optional
        :param known_host_entry: known_host_entry
        :type known_host_entry: str
        :param sshkeyauth: sshkeyauth, defaults to None
        :type sshkeyauth: bool, optional
        :param sshkeypassword: sshkeypassword
        :type sshkeypassword: str
        :param sshkeypath: sshkeypath
        :type sshkeypath: str
        """
        if dh_key_size_max1024 is not SENTINEL:
            self.dh_key_size_max1024 = dh_key_size_max1024
        self.known_host_entry = known_host_entry
        if sshkeyauth is not SENTINEL:
            self.sshkeyauth = sshkeyauth
        self.sshkeypassword = sshkeypassword
        self.sshkeypath = sshkeypath
        self._kwargs = kwargs
