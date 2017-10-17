#!/usr/bin/python3.5
def get_quadrant_number(x, y):
    try:

        x, y = float(x), float(y)

        if 0 in (x, y):
            raise ValueError

        if (x > 0) and (y > 0):
            return 1

        if (x < 0) and (y > 0):
            return 2

        if (x < 0) and (y < 0):
            return 3

        if (x > 0) and (y < 0):
            return 4

    except ValueError:
        pass
