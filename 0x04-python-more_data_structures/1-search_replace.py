#!/usr/bin/phython3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    return (list(map(lambda x: replace if x == search else x, new)))
