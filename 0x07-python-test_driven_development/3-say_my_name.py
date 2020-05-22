#!/usr/bin/python3
# jose vallejo <1545@holbertonschool.com>
""" create funtion that say mi name """


def say_my_name(first_name, last_name=""):
    """ funtion for say name givend in parameters """
    if first_name:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        elif type(last_name) is not str:
            raise TypeError("last_name must be a string")
        else:
            print("My name is {} {}". format(first_name, last_name))
