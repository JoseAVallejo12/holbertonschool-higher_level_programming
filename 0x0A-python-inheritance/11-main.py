#!/usr/bin/python3
Square = __import__('11-square').Square
Rectangle = __import__('9-rectangle').Rectangle

s = Square(13)
a = Rectangle(13, 13)

print(s)
print(s.area())

print(a)
print(a.area())
