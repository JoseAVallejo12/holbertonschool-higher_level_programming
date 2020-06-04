#!/usr/bin/python3
"""
Returns simple data structure type dict
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """new funtion

    Args:
        obj ([object]): is instance of an class

    Returns:
        [dict]: Json format
    """
    return (obj.__dict__)
