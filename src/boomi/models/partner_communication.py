
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .as2_communication_options import As2CommunicationOptions
from .disk_communication_options import DiskCommunicationOptions
from .ftp_communication_options import FtpCommunicationOptions
from .http_communication_options import HttpCommunicationOptions
from .mllp_communication_options import MllpCommunicationOptions
from .oftp_communication_options import OftpCommunicationOptions
from .sftp_communication_options import SftpCommunicationOptions


@JsonMap(
    {
        "as2_communication_options": "AS2CommunicationOptions",
        "disk_communication_options": "DiskCommunicationOptions",
        "ftp_communication_options": "FTPCommunicationOptions",
        "http_communication_options": "HTTPCommunicationOptions",
        "mllp_communication_options": "MLLPCommunicationOptions",
        "oftp_communication_options": "OFTPCommunicationOptions",
        "sftp_communication_options": "SFTPCommunicationOptions",
    }
)
class PartnerCommunication(BaseModel):
    """PartnerCommunication

    :param as2_communication_options: as2_communication_options, defaults to None
    :type as2_communication_options: As2CommunicationOptions, optional
    :param disk_communication_options: disk_communication_options, defaults to None
    :type disk_communication_options: DiskCommunicationOptions, optional
    :param ftp_communication_options: ftp_communication_options, defaults to None
    :type ftp_communication_options: FtpCommunicationOptions, optional
    :param http_communication_options: http_communication_options, defaults to None
    :type http_communication_options: HttpCommunicationOptions, optional
    :param mllp_communication_options: mllp_communication_options, defaults to None
    :type mllp_communication_options: MllpCommunicationOptions, optional
    :param oftp_communication_options: oftp_communication_options, defaults to None
    :type oftp_communication_options: OftpCommunicationOptions, optional
    :param sftp_communication_options: sftp_communication_options, defaults to None
    :type sftp_communication_options: SftpCommunicationOptions, optional
    """

    def __init__(
        self,
        as2_communication_options: As2CommunicationOptions = SENTINEL,
        disk_communication_options: DiskCommunicationOptions = SENTINEL,
        ftp_communication_options: FtpCommunicationOptions = SENTINEL,
        http_communication_options: HttpCommunicationOptions = SENTINEL,
        mllp_communication_options: MllpCommunicationOptions = SENTINEL,
        oftp_communication_options: OftpCommunicationOptions = SENTINEL,
        sftp_communication_options: SftpCommunicationOptions = SENTINEL,
        **kwargs,
    ):
        """PartnerCommunication

        :param as2_communication_options: as2_communication_options, defaults to None
        :type as2_communication_options: As2CommunicationOptions, optional
        :param disk_communication_options: disk_communication_options, defaults to None
        :type disk_communication_options: DiskCommunicationOptions, optional
        :param ftp_communication_options: ftp_communication_options, defaults to None
        :type ftp_communication_options: FtpCommunicationOptions, optional
        :param http_communication_options: http_communication_options, defaults to None
        :type http_communication_options: HttpCommunicationOptions, optional
        :param mllp_communication_options: mllp_communication_options, defaults to None
        :type mllp_communication_options: MllpCommunicationOptions, optional
        :param oftp_communication_options: oftp_communication_options, defaults to None
        :type oftp_communication_options: OftpCommunicationOptions, optional
        :param sftp_communication_options: sftp_communication_options, defaults to None
        :type sftp_communication_options: SftpCommunicationOptions, optional
        """
        if as2_communication_options is not SENTINEL:
            self.as2_communication_options = self._define_object(
                as2_communication_options, As2CommunicationOptions
            )
        if disk_communication_options is not SENTINEL:
            self.disk_communication_options = self._define_object(
                disk_communication_options, DiskCommunicationOptions
            )
        if ftp_communication_options is not SENTINEL:
            self.ftp_communication_options = self._define_object(
                ftp_communication_options, FtpCommunicationOptions
            )
        if http_communication_options is not SENTINEL:
            self.http_communication_options = self._define_object(
                http_communication_options, HttpCommunicationOptions
            )
        if mllp_communication_options is not SENTINEL:
            self.mllp_communication_options = self._define_object(
                mllp_communication_options, MllpCommunicationOptions
            )
        if oftp_communication_options is not SENTINEL:
            self.oftp_communication_options = self._define_object(
                oftp_communication_options, OftpCommunicationOptions
            )
        if sftp_communication_options is not SENTINEL:
            self.sftp_communication_options = self._define_object(
                sftp_communication_options, SftpCommunicationOptions
            )
        self._kwargs = kwargs
