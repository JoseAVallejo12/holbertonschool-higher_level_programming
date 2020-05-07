#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for str1 in set_1:
        for str2 in set_2:
            if str1 == str2:
                new.append(str1)
    return new
