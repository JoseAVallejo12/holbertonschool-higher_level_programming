#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = (0,0)
    res = tuple(map(sum, zip(tuple_a, tuple_b)))
    if (len(tuple_a) + len(tuple_b) != 4):
        res = tuple(map(sum, zip(tuple_a, t1)))

    return res