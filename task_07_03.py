#!/usr/bin/python3.5
from inspect import signature
from functools import wraps


def strict_argument_types(func):
    @wraps(func)
    def wrapper(*args):
        sig = signature(func)
        bind_args = sig.bind(*args).arguments

        for key, val in bind_args.items():
            anno = sig.parameters[key].annotation
            if not isinstance(val, anno):
                raise TypeError('The argument "{}" must be "{}", passed "{}"'.format(key, anno, type(val)))
            else:
                pass

        return func(*args)

    return wrapper


def strict_return_type(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        sig = signature(func)
        res_type = type(result)

        if not isinstance(result, sig.return_annotation):
            raise TypeError('The return value must be "{}", not "{}"'.format(sig.return_annotation, res_type))
        else:
            pass

        return result

    return wrapper
