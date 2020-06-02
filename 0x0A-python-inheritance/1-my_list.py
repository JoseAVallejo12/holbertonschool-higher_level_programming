#!/usr/bin/python3
""" new class inirent of class list """


class MyList(list):
    """ define a new class """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
