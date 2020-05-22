#!/usr/bin/python3
# jose vallejo <1545@holbertonschool.com>
"""
    create funtion that print swuare in # 
    @size must be only int
    Return: only print scuare by size*size in #
"""


def print_square(size):
    """
        print square with # character
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print(size * '#')
        i += 1
