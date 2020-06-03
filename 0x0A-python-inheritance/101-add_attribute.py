#!/usr/bin/python3
""" createa a nuw funtion """

def add_attribute(obj, fiel_name, fiel_value):
    """ new funtion for add attribute an objetc """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    return setattr(obj, fiel_name, fiel_value)