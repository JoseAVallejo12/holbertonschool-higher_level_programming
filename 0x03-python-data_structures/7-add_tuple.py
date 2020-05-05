#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_t_a = list(tuple_a)
    list_t_b = list(tuple_b)

    if len(list_t_a) < 2:
        for i in range(len(list_t_a, 2)):
            list_t_a.append(0)

    if len(list_t_b) < 2:
        for i in range(len(list_t_b), 2):
            list_t_b.append(0)

    sum1 =list_t_a[0] + list_t_b[0]
    sum2 = list_t_a[1] + list_t_b[1]
    return sum1, sum2
