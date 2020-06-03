#!/usr/bin/python3
""" Create a new funtion """


def number_of_lines(filename=""):
    """Count number lines in my_file

    Args:
        filename (str): name of file. Defaults to "".

    Returns:
        [int]: count lines in file
    """
    count = 0
    with open(filename, mode='r', encoding="utf-8") as my_file:
        for lines in my_file:
            count += 1
    return count
