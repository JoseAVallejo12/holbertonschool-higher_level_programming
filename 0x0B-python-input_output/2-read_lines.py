#!/usr/bin/python3
""" Create a new funtion """


def read_lines(filename="", nb_lines=0):
    """create funtion for print

    Args:
        filename (str): file to read. Defaults to "".
        nb_lines (int): number lines to read Defaults to 0.

    """

    count = 0
    with open(filename, mode='r', encoding="utf-8") as my_file:
        for lines in my_file:
            print(lines, end="")
            count += 1
            if count == nb_lines:
                break
