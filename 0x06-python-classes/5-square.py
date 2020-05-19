#!/usr/bin/python3
# 5-square.py
# jose vallejo <1545@holbertonschool.com>
""" create a new class """


class Square(object):
    """ create Square class """

    def __init__(self, size=0):
        """ inicialice size var """
        self.__size = size

    @property
    def size(self):
        """ getter method for private value """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method for private val """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method for Calculate area """
        return self.__size * self.__size

    def my_print(self):
        """ Method for print square # in stdout """
        if self.__size == 0:
            print()
        else:
            x = self.__size
            while self.__size != 0:
                print(x * "#")
                self.__size -= 1
