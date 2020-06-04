#!/usr/bin/python3
"""14-pascal_triangle.py module"""


def pascal_triangle(n):
    """[summary]

    Args:
        n ([type]): [description]
    """

    new_list = []
    for i in range(n):
        new_list.append([])
    for i in range(n):
        if i == 0:
            new_list[0].append(1)
            continue
        if i == 1:
            new_list[1].append(1)
            new_list[1].append(1)
            continue
        for j in range(i + 1):
            if j == 0 or j == i:
                new_list[i].append(new_list[i-1][j-1])
            else:
                res = new_list[i-1][j] + new_list[i-1][j-1]
                new_list[i].append(res)
    return(new_list)
