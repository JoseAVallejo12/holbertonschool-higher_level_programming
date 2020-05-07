#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in sorted(a_dictionary.keys()):
        new_dic = a_dictionary.copy()
        del new_dic[key]
        return new_dic
    return a_dictionary
