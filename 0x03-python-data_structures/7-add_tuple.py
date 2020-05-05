#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_t_a = tuple_a + ('0', '0')
    list_t_b = tuple_b + ('0', '0')
    sum1 = int(list_t_a[0]) + int(list_t_b[0])
    sum2 = int(list_t_a[1]) + int(list_t_b[1])

    return sum1, sum2
