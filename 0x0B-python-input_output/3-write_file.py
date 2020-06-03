#!/usr/bin/python3
""" define a new funtion """


def write_file(filename="", text=""):
    """create funtion for add inf the file

    Args:
        filename (str): file to open or create. Defaults to "".
        text (str): string for add to file. Defaults to "".

    Returns:
        [int]: number of lines adds
    """

    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)
