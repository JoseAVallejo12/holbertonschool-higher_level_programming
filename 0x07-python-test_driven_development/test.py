#!/usr/bin/python3


def my_function(a, b):
    if ((type(a) is list) or (type(b) is list) or
        (type(a) is tuple) or (type(b) is tuple) or
            (type(a) is dict) or (type(b) is dict)):
        raise OverflowError("too large")

    if (type(a) is not int) or (type(b) is not int):
        raise ValueError("must be int")
    else:
        return a * b

