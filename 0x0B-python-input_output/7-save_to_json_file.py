#!/usr/bin/python3
""" create a new funtion """
import json


def save_to_json_file(my_obj, filename):
    """safe Json en file

    Args:
        my_obj ([any]): object python to convert Json
        filename ([str]): name of file
    """

    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
