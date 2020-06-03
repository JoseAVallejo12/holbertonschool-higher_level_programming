#!/usr/bin/python3
""" create a new funtions """
import json


def load_from_json_file(filename):
    """load Json form file

    Args:
        filename ([str]): name of file Json

    Returns:
        [python-obj]:
    """

    with open(filename, mode='r', encoding="utf-8") as my_file:
        return json.loads(my_file.read())
