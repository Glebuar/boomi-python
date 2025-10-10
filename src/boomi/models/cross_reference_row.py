
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class CrossReferenceRow(BaseModel):
    """CrossReferenceRow

    :param ref1: ref1, defaults to None
    :type ref1: str, optional
    :param ref10: ref10, defaults to None
    :type ref10: str, optional
    :param ref11: ref11, defaults to None
    :type ref11: str, optional
    :param ref12: ref12, defaults to None
    :type ref12: str, optional
    :param ref13: ref13, defaults to None
    :type ref13: str, optional
    :param ref14: ref14, defaults to None
    :type ref14: str, optional
    :param ref15: ref15, defaults to None
    :type ref15: str, optional
    :param ref16: ref16, defaults to None
    :type ref16: str, optional
    :param ref17: ref17, defaults to None
    :type ref17: str, optional
    :param ref18: ref18, defaults to None
    :type ref18: str, optional
    :param ref19: ref19, defaults to None
    :type ref19: str, optional
    :param ref2: ref2, defaults to None
    :type ref2: str, optional
    :param ref20: ref20, defaults to None
    :type ref20: str, optional
    :param ref3: ref3, defaults to None
    :type ref3: str, optional
    :param ref4: ref4, defaults to None
    :type ref4: str, optional
    :param ref5: ref5, defaults to None
    :type ref5: str, optional
    :param ref6: ref6, defaults to None
    :type ref6: str, optional
    :param ref7: ref7, defaults to None
    :type ref7: str, optional
    :param ref8: ref8, defaults to None
    :type ref8: str, optional
    :param ref9: ref9, defaults to None
    :type ref9: str, optional
    """

    def __init__(
        self,
        ref1: str = SENTINEL,
        ref10: str = SENTINEL,
        ref11: str = SENTINEL,
        ref12: str = SENTINEL,
        ref13: str = SENTINEL,
        ref14: str = SENTINEL,
        ref15: str = SENTINEL,
        ref16: str = SENTINEL,
        ref17: str = SENTINEL,
        ref18: str = SENTINEL,
        ref19: str = SENTINEL,
        ref2: str = SENTINEL,
        ref20: str = SENTINEL,
        ref3: str = SENTINEL,
        ref4: str = SENTINEL,
        ref5: str = SENTINEL,
        ref6: str = SENTINEL,
        ref7: str = SENTINEL,
        ref8: str = SENTINEL,
        ref9: str = SENTINEL,
        **kwargs
    ):
        """CrossReferenceRow

        :param ref1: ref1, defaults to None
        :type ref1: str, optional
        :param ref10: ref10, defaults to None
        :type ref10: str, optional
        :param ref11: ref11, defaults to None
        :type ref11: str, optional
        :param ref12: ref12, defaults to None
        :type ref12: str, optional
        :param ref13: ref13, defaults to None
        :type ref13: str, optional
        :param ref14: ref14, defaults to None
        :type ref14: str, optional
        :param ref15: ref15, defaults to None
        :type ref15: str, optional
        :param ref16: ref16, defaults to None
        :type ref16: str, optional
        :param ref17: ref17, defaults to None
        :type ref17: str, optional
        :param ref18: ref18, defaults to None
        :type ref18: str, optional
        :param ref19: ref19, defaults to None
        :type ref19: str, optional
        :param ref2: ref2, defaults to None
        :type ref2: str, optional
        :param ref20: ref20, defaults to None
        :type ref20: str, optional
        :param ref3: ref3, defaults to None
        :type ref3: str, optional
        :param ref4: ref4, defaults to None
        :type ref4: str, optional
        :param ref5: ref5, defaults to None
        :type ref5: str, optional
        :param ref6: ref6, defaults to None
        :type ref6: str, optional
        :param ref7: ref7, defaults to None
        :type ref7: str, optional
        :param ref8: ref8, defaults to None
        :type ref8: str, optional
        :param ref9: ref9, defaults to None
        :type ref9: str, optional
        """
        if ref1 is not SENTINEL:
            self.ref1 = ref1
        if ref10 is not SENTINEL:
            self.ref10 = ref10
        if ref11 is not SENTINEL:
            self.ref11 = ref11
        if ref12 is not SENTINEL:
            self.ref12 = ref12
        if ref13 is not SENTINEL:
            self.ref13 = ref13
        if ref14 is not SENTINEL:
            self.ref14 = ref14
        if ref15 is not SENTINEL:
            self.ref15 = ref15
        if ref16 is not SENTINEL:
            self.ref16 = ref16
        if ref17 is not SENTINEL:
            self.ref17 = ref17
        if ref18 is not SENTINEL:
            self.ref18 = ref18
        if ref19 is not SENTINEL:
            self.ref19 = ref19
        if ref2 is not SENTINEL:
            self.ref2 = ref2
        if ref20 is not SENTINEL:
            self.ref20 = ref20
        if ref3 is not SENTINEL:
            self.ref3 = ref3
        if ref4 is not SENTINEL:
            self.ref4 = ref4
        if ref5 is not SENTINEL:
            self.ref5 = ref5
        if ref6 is not SENTINEL:
            self.ref6 = ref6
        if ref7 is not SENTINEL:
            self.ref7 = ref7
        if ref8 is not SENTINEL:
            self.ref8 = ref8
        if ref9 is not SENTINEL:
            self.ref9 = ref9
        self._kwargs = kwargs
