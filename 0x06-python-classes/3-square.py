#!/usr/bin/python3
# 3-square.py
# jose vallejo <1545@holbertonschool.com
"""Define a new class: """


class Square(object):
    """ new class defined """

    def __init__(self, size=0):
        """ inicialice size var """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method for Calculate area """
        return self.__size * self.__size
