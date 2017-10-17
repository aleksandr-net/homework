#!/usr/bin/python3.5
def zero_check(x, y):
    if x == 0 or y == 0:
        raise ValueError
    else:
        pass


def get_quadrant_number(x, y):
    try:
        x = float(x)
        y = float(y)

        zero_check(x, y)

        if (x > 0) and (y > 0):
            return 1

        if (x < 0) and (y > 0):
            return 2

        if (x < 0) and (y > 0):
            return 3

        if (x > 0) and (y < 0):
            return 4

    except ValueError:
        """Возвращаем ничего"""
