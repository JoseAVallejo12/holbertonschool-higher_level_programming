#!/usr/bin/python3
# 102-square.py
# jose vallejo <1545@holbertonschool.com
""" Define a new class """


class Square(object):
    """ create Square class """

    def __init__(self, size=0):
        """ inicialice size var """
        self.__size = size

    @property
    def size(self):
        """ getter method for private size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for private size """
        if type(value) is not int or float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Method for Calculate area """
        return self.__size * self.__size

    def __eq__(self, other):
        """ __eq__ represent a == b """
        return self.__size == other

    def __ne__(self, other):
        """ __ne__ represent a != b or a <> b """
        return self.__size != other

    def __gt__(self, other):
        """ __gt__ represent a > b """
        return self.__size > other

    def __ge__(self, other):
        """ __eq__ represent a==b """
        return self.__size >= other

    def __lt__(self, other):
        """ __lt__ represent a < b """
        return self.__size < other

    def __le__(self, other):
        """ __le__ represent a <= b """
        return self.__size <= other
