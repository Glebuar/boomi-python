
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .pgp_certificate import PgpCertificate


@JsonMap({"pgp_certificate": "PGPCertificate"})
class PgpCertificates(BaseModel):
    """PgpCertificates

    :param pgp_certificate: pgp_certificate, defaults to None
    :type pgp_certificate: List[PgpCertificate], optional
    """

    def __init__(self, pgp_certificate: List[PgpCertificate] = SENTINEL, **kwargs):
        """PgpCertificates

        :param pgp_certificate: pgp_certificate, defaults to None
        :type pgp_certificate: List[PgpCertificate], optional
        """
        if pgp_certificate is not SENTINEL:
            self.pgp_certificate = self._define_list(pgp_certificate, PgpCertificate)
        self._kwargs = kwargs
