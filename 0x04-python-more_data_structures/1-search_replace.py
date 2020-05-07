#!/usr/bin/phython3
def search_replace(my_list, search, replace):
    new = []
    new = list(map(lambda x: replace if x == search else x, my_list))
    return new
