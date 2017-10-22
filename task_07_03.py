#!/usr/bin/python3.5
from inspect import signature
from functools import wraps


def strict_argument_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        bind_args = sig.bind(*args, **kwargs).arguments

        for key, val in bind_args.items():
            anno = sig.parameters[key].annotation
            if not isinstance(val, anno):
                raise TypeError('The argument "{}" must be "{}", passed "{}"'.format(key, anno, type(val)))
            else:
                pass

        return func(*args, **kwargs)
    return wrapper


def strict_return_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sig = signature(func)
        anno = sig.return_annotation
        res_type = type(result)

        if not isinstance(result, anno):
            raise TypeError('The return value must be "{}", not "{}"'.format(anno, res_type))
        else:
            pass

        return result
    return wrapper
