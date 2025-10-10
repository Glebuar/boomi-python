
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .mllpssl_options import MllpsslOptions
from .edi_delimiter import EdiDelimiter


@JsonMap(
    {
        "mllpssl_options": "MLLPSSLOptions",
        "end_block": "endBlock",
        "end_data": "endData",
        "halt_timeout": "haltTimeout",
        "inactivity_timeout": "inactivityTimeout",
        "max_connections": "maxConnections",
        "max_retry": "maxRetry",
        "receive_timeout": "receiveTimeout",
        "send_timeout": "sendTimeout",
        "start_block": "startBlock",
    }
)
class MllpSendSettings(BaseModel):
    """MllpSendSettings

    :param mllpssl_options: mllpssl_options
    :type mllpssl_options: MllpsslOptions
    :param end_block: end_block
    :type end_block: EdiDelimiter
    :param end_data: end_data
    :type end_data: EdiDelimiter
    :param halt_timeout: halt_timeout, defaults to None
    :type halt_timeout: bool, optional
    :param host: host
    :type host: str
    :param inactivity_timeout: inactivity_timeout, defaults to None
    :type inactivity_timeout: int, optional
    :param max_connections: max_connections, defaults to None
    :type max_connections: int, optional
    :param max_retry: max_retry, defaults to None
    :type max_retry: int, optional
    :param persistent: persistent, defaults to None
    :type persistent: bool, optional
    :param port: port
    :type port: int
    :param receive_timeout: receive_timeout, defaults to None
    :type receive_timeout: int, optional
    :param send_timeout: send_timeout, defaults to None
    :type send_timeout: int, optional
    :param start_block: start_block
    :type start_block: EdiDelimiter
    """

    def __init__(
        self,
        mllpssl_options: MllpsslOptions,
        end_block: EdiDelimiter,
        end_data: EdiDelimiter,
        host: str,
        port: int,
        start_block: EdiDelimiter,
        halt_timeout: bool = SENTINEL,
        inactivity_timeout: int = SENTINEL,
        max_connections: int = SENTINEL,
        max_retry: int = SENTINEL,
        persistent: bool = SENTINEL,
        receive_timeout: int = SENTINEL,
        send_timeout: int = SENTINEL,
        **kwargs,
    ):
        """MllpSendSettings

        :param mllpssl_options: mllpssl_options
        :type mllpssl_options: MllpsslOptions
        :param end_block: end_block
        :type end_block: EdiDelimiter
        :param end_data: end_data
        :type end_data: EdiDelimiter
        :param halt_timeout: halt_timeout, defaults to None
        :type halt_timeout: bool, optional
        :param host: host
        :type host: str
        :param inactivity_timeout: inactivity_timeout, defaults to None
        :type inactivity_timeout: int, optional
        :param max_connections: max_connections, defaults to None
        :type max_connections: int, optional
        :param max_retry: max_retry, defaults to None
        :type max_retry: int, optional
        :param persistent: persistent, defaults to None
        :type persistent: bool, optional
        :param port: port
        :type port: int
        :param receive_timeout: receive_timeout, defaults to None
        :type receive_timeout: int, optional
        :param send_timeout: send_timeout, defaults to None
        :type send_timeout: int, optional
        :param start_block: start_block
        :type start_block: EdiDelimiter
        """
        self.mllpssl_options = self._define_object(mllpssl_options, MllpsslOptions)
        self.end_block = self._define_object(end_block, EdiDelimiter)
        self.end_data = self._define_object(end_data, EdiDelimiter)
        if halt_timeout is not SENTINEL:
            self.halt_timeout = halt_timeout
        self.host = host
        if inactivity_timeout is not SENTINEL:
            self.inactivity_timeout = inactivity_timeout
        if max_connections is not SENTINEL:
            self.max_connections = max_connections
        if max_retry is not SENTINEL:
            self.max_retry = max_retry
        if persistent is not SENTINEL:
            self.persistent = persistent
        self.port = port
        if receive_timeout is not SENTINEL:
            self.receive_timeout = receive_timeout
        if send_timeout is not SENTINEL:
            self.send_timeout = send_timeout
        self.start_block = self._define_object(start_block, EdiDelimiter)
        self._kwargs = kwargs
