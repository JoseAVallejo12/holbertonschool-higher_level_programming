#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    c_py = ""
    for c in str:
        if j != n:
            c_py = c_py + c
        j = j + 1
    return c_py
