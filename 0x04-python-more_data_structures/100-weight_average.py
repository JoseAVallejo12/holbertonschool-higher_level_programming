#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    sum2 = 0
    if my_list:
        for i in my_list:
            sum += i[0] * i[1]
            sum2 += i[1]
        return (sum /sum2)
    return 0
