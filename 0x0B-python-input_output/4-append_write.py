#!/usr/bin/python3
""" define a new funtion """


def append_write(filename="", text=""):
    """create funtion for append inf in the file

    Args:
        filename (str): file to open or create. Defaults to "".
        text (str): string for append to file. Defaults to "".

    Returns:
        [int]: number of lines adds
    """

    with open(filename, mode="a", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)
