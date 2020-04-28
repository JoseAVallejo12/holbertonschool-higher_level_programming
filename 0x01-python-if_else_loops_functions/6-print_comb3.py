#!/usr/bin/python3
for n in range(10):
    for p in range(n + 1, 10):
        if n == 8 and p == 9:
            print("{}{}".format(n, p))
        else:
            print("{}{}, ".format(n, p), end="")
