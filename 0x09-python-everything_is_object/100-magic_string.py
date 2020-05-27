#!/usr/bin/python3
def magic_string(var=[0]):
    var[0] = var[0] + 1
    return ", ".join(["Holberton"] * var[0])
