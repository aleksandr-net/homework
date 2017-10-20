#!/usr/bin/python3.5
from inspect import signature, getcallargs
from functools import wraps


def strict_argument_types(func):
    # @wraps(func)
    global args

    def wrapper(*args):
        call_args = getcallargs(func, *args)
        result = func(*args)
        print(call_args)

        for key, val in call_args.items():
            print("key = {}, val = {}".format(key, val))
            sig = signature(func).parameters[key].annotation

            try:
                if sig != type(val):
                    raise TypeError
            except TypeError:
                raise TypeError("The argument {} must be {}, passed {}".format(key, sig, type(val)))

        return result

    return wrapper


def strict_return_type(func):
    # @wraps(func)
    global args

    def wrapper(*args):
        global result
        global sig
        result = func(*args)
        sig = signature(func)
        # print(sig)

        try:
            if sig.return_annotation != type(result):
                raise TypeError
            else:
                pass
        except TypeError:
            raise TypeError("The return value must be {}, not {}".format(sig.return_annotation, type(result)))

        return result

    return wrapper


result = 0
sig = signature(strict_return_type)


@strict_argument_types
@strict_return_type
def summa(a: int, b: int, c: int) -> int:
    return a + b + c


print(summa(2, 2, 2))
