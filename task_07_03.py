#!/usr/bin/python3.5
from inspect import signature, getcallargs, getmembers
from functools import wraps


def strict_argument_types(func):
    @wraps(func)
    def wrapper(*args):
        call_args = getcallargs(func, *args)

        for key, val in call_args.items():
            sig = signature(func).parameters[key].annotation
            try:
                if sig != type(val):
                    raise TypeError
            except TypeError:
                raise TypeError("The argument {} must be {}, passed {}".format(key, sig, type(val)))
        return func(*args)
    return wrapper
