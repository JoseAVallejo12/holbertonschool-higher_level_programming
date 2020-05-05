#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_str = my_string
        return (new_str.translate({ord(i): None for i in 'Cc'}))
    new_str = my_string
    return new_str
