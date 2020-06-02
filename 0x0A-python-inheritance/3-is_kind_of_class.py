#!/usr/bin/python3
""" funtion for validate if tow adject are equal """


def is_kind_of_class(obj, a_class):
    """
        return true if a is intance de a_class else fasle
    """
    if isinstance(obj, a_class) or issubclass(a_class, type(obj)):
        return True
    else:
        return False
