#!/usr/bin/python3
""" funtion for validate if tow adject are equal """


def inherits_from(obj, a_class):
    """
        return true if a is intance de a_class else fasle
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
