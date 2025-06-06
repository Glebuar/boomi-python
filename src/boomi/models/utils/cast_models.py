
from enum import Enum
from typing import get_args, Union
from inspect import isclass
from .one_of_base_model import OneOfBaseModel


def cast_models(func):
    """
    A decorator that allows for the conversion of dictionaries and enum values to model instances.

    :param func: The function to decorate.
    :type func: Callable
    :return: The decorated function.
    :rtype: Callable
    """

    def wrapper(self, *clss, **kwargs):
        cls_types = func.__annotations__
        new_cls_args = []
        new_kwargs = {}

        for input, input_type in zip(clss, cls_types.values()):
            new_cls_args.append(_get_instanced_type(input, input_type))

        for type_name, input in kwargs.items():
            new_kwargs[type_name] = _get_instanced_type(input, cls_types[type_name])

        return func(self, *new_cls_args, **new_kwargs)

    def _get_instanced_type(data, input_type):
        """
        Get instanced type based on the input data and type.

        :param data: The input data.
        :param input_type: The type of the input.
        :return: The instanced type.
        """
        # Instanciate oneOf models
        if _is_one_of_model(input_type):
            class_list = {
                getattr(arg, "__name__", str(arg)): arg for arg in get_args(input_type)
            }
            OneOfBaseModel.class_list = class_list
            return OneOfBaseModel.return_one_of(data)

        # Instanciate enum values
        elif (
            isclass(input_type)
            and issubclass(input_type, Enum)
            and not isinstance(data, input_type)
        ):
            return input_type(data)

        # Instanciate object models
        elif isinstance(data, dict) and input_type is not str:
            return input_type(**data)

        # Instanciate list of object models
        elif isinstance(data, list) and all(isinstance(i, dict) for i in data):
            element_type = get_args(input_type)[0]
            return [element_type(**item) for item in data]

        # Instanciate bytes if input is str
        elif input_type is bytes and isinstance(data, str):
            return data.encode()

        # Pass other types
        else:
            return data

    def _is_one_of_model(cls_type):
        """
        Check if the class type is a oneOf model.

        :param cls_type: The class type to check.
        :return: True if the class type is a oneOf model, False otherwise.
        :rtype: bool
        """
        return hasattr(cls_type, "__origin__") and cls_type.__origin__ is Union

    return wrapper
