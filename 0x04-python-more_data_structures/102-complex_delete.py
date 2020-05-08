#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    if value in a_dictionary.values():
        for key in a_dictionary.keys():
            if value == a_dictionary[key]:
                keys_to_del.append(key)
        for i in keys_to_del:
            del a_dictionary[i]

    return a_dictionary
