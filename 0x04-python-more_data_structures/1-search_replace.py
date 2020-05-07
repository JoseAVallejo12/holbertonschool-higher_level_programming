#!/usr/bin/phython3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        new_list = list(map((lambda x: x+87 if x == 2 else x), my_list))
        return new_list