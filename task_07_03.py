#!/usr/bin/python3.5
from inspect import signature, getcallargs
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


def strict_return_type(func):
    @wraps(func)
    def wrapper(*args):
        try:
            sig = signature(func)
            if sig.return_annotation != type(func(*args)):
                raise TypeError
            else:
                pass
        except TypeError:
            raise TypeError("The return value must be {}, not {}".format(sig.return_annotation, type(func(*args))
        return func(*args)
    return wrapper

@strict_return_type
def summa(a:int, b:int) -> int:
    return a + b

print(summa(2,2))