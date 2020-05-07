#!/usr/bin/phython3
def search_replace(my_list, search, replace):
    if my_list:
        new = []
        new = list(map((lambda x: replace if x == search else x), my_list))
        return new
