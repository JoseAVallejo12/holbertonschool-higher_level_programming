#!/usr/bin/python3
# jose vallejo <1545@holbertonschool.com>
""" create funtion for add two number """


def add_integer(a, b=98):
    """ funtion for add number """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            return int(a) + b
        elif type(b) is float:
            return a + int(b)
        else:
            return a + b
