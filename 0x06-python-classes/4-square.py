#!/usr/bin/python3


class Square(object):
    """[summary]

        Arguments:
                object {object} -- for good practices
                __size {int} -- value private
        Raises:
                TypeError: rise error for type wrong
                ValueError: rise error for value negativ
        """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
