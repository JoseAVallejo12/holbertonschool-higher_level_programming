#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    for i in range(len(my_list)):
        if i == idx:
            print(my_list[idx])
            return my_list[idx]
    return