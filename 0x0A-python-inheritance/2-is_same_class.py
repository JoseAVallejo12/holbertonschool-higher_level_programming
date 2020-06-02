#!/usr/bin/python3
""" funtion for validate if tow adject are equal """


def is_same_class(obj, a_class):
    """
        return true if a is type of a_class else fasle
    """
    if type(obj) is a_class:
        return True
    else:
        return False
