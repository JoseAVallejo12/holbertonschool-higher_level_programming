#!/usr/bin/python3

def read_file(filename=""):
    """read file funtions

    Args:
        filename (str): name file to open. Defaults to "".
    """

    with open(filename, mode='r', encoding="utf-8") as my_file:
        print(my_file.read())
