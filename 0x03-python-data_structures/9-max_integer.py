#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        n_max = my_list[0]
        for i in my_list:
            if i > n_max:
                n_max = i
        return n_max
    return None
