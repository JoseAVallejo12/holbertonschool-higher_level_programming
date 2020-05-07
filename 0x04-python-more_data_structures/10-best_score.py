#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n_max = max(list(sorted(a_dictionary.values())))
        for key in a_dictionary:
            if n_max == a_dictionary[key]:
                return (key)
    return None
