#!/usr/bin/python3
""" create new funtion """
import json

def to_json_string(my_obj):

    if not isinstance(my_obj, (dict, list, tuple, str, int, float)):
        raise TypeError(my_obj)
    return json.dumps(my_obj, sort_keys=True)
