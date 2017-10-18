#!/usr/bin/python3.5
from collections import namedtuple
from functools import wraps


def return_namedtuple(*nargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, tuple):
                Ntuple = namedtuple('Ntuple', nargs)
                return Ntuple(*result)
            return result

        return wrapper
    return decorator
