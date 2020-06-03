#!/usr/bin/python3
""" create new funtion """
import json


def from_json_string(my_str):
    """Convert python to JSON

    Args:
        my_obj ([dict]): object to convert

    Returns:
        [str-json]: object convert
    """

    return json.loads(my_str)
