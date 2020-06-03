#!/usr/bin/python3
""" create new funtion """
import json


def to_json_string(my_obj):
    """Convert python to JSON

    Args:
        my_obj ([dict]): object to convert

    Returns:
        [str-json]: object convert
    """

    return json.dumps(my_obj)
