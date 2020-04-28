#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = int(repr(number)[-1])
less = "and is less than 6 and not 0"
greater = "and is grater than 5"
if number < 0:
    n = n * -1
if n > 5:
    print("Last digit of {} is {} {}".format(number, n, greater))
elif n == 0:
    print("Last digit of {} is {} and is 0".format(number, n))
elif n < 6:
    print("Last digit of {} is {} {}".format(number, n, less))

